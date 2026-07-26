#!/usr/bin/env python3
"""Build the arXiv-style single-column PDF from paper.md.
Mirrors the TRON paper pipeline: split -> pandoc MD->LaTeX -> unicode fixups
-> assemble main.tex (arxiv.sty) -> latexmk/xelatex.
Figure 1 (incentive-gradient stage model) is rendered from figure1.svg via
rsvg-convert and injected as a float at its reference in Section 4.2."""
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "paper.md"
text = SRC.read_text()

TITLE = (r"This Answer Was Not Sponsored:\\[2pt] "
         r"And Why You Couldn't Tell If It Were"
         r"\thanks{Research conducted at the Secret Loyalties Hackathon "
         r"(Apart Research \& Formation Research), July 2026.}")
SHORTTITLE = "This Answer Was Not Sponsored"

# author / header identification: name / affiliation / email / ORCID
AUTHOR = (r"\^Anderson Q. \\ With Apart Research \\ \texttt{anderson@42labs.io} \\ "
          r"\texttt{orcid.org/0009-0008-7182-3203}")

# opening epigraph (between author block and abstract). Two lines: the
# quotation, then the attribution alone on its own line.
EPIGRAPH = (r"``I am the word and my name is never spoken. I am called Ubik, "
            r"but that is not my name.''\\ --- Philip K. Dick, \textit{Ubik} (1969)")

# ---- 1. abstract = between "## Abstract" and the first "---" rule ----
abs_md = re.search(r"## Abstract\s*(.*?)\s*\n---\n", text, re.DOTALL).group(1)

# ---- 2. body = "## 1. Introduction" through end of document ----
body_md = text[text.index("## 1. Introduction"):].rstrip()

# strip manual "N." / "N.M" numbers from headings — LaTeX numbers sections
body_md = re.sub(r"(?m)^(#{2,3})\s+\d+(\.\d+)?\.?\s+", r"\1 ", body_md)

# make back-matter unnumbered (pandoc/LaTeX {-})
for h in ("Code and Data", "References", "Appendix A", "Appendix B",
          "LLM Usage Statement"):
    body_md = re.sub(rf"(?m)^(#{{2,3}})\s+{re.escape(h)}\s*$",
                     rf"\1 {h} {{-}}", body_md)

(HERE / "abstract.md").write_text(abs_md)
(HERE / "body.md").write_text(body_md)

# ---- 3. pandoc MD -> LaTeX fragments ----
def pandoc(src, extra=()):
    out = subprocess.run(
        ["pandoc", src, "-f", "markdown+raw_tex", "-t", "latex", *extra],
        cwd=HERE, capture_output=True, text=True, check=True)
    return out.stdout

abstract_tex = pandoc("abstract.md")
body_tex = pandoc("body.md", ["--top-level-division=section",
                              "--shift-heading-level-by=-1"])

# ---- 4. unicode -> LaTeX fixups (XeTeX-safe) ----
UMAP = {
    "→": r"$\rightarrow$", "←": r"$\leftarrow$", "↔": r"$\leftrightarrow$",
    "≤": r"$\le$", "≥": r"$\ge$", "≈": r"$\approx$", "−": r"$-$",
    "×": r"$\times$", "·": r"$\cdot$", "…": r"\ldots{}", "≠": r"$\neq$",
    "§": r"\S{}", "†": r"\dag{}", "€": r"\euro{}", "™": r"\texttrademark{}",
    "’": "'", "‘": "'", "“": "``", "”": "''", "—": "---", "–": "--",
}
def fixups(s):
    for u, l in UMAP.items():
        s = s.replace(u, l)
    return s
abstract_tex, body_tex = fixups(abstract_tex), fixups(body_tex)

# ---- 4b. render Figure 1 (SVG -> PDF) and inject the float at its reference ----
subprocess.run(["rsvg-convert", "-f", "pdf", "-o", "figure1.pdf", "figure1.svg"],
               cwd=HERE, check=True)
FIG1 = r"""
\begin{figure}[t]
\centering
\includegraphics[width=\textwidth]{figure1.pdf}
\caption{\textbf{The incentive gradient.} Four monetization stages ordered by
increasing deniability and decreasing external auditability, from a
subscription/neutral baseline to weight-level tilt. Stages~1--2 are present-day
observation (ads are live under an unverifiable ``answer independence'' pledge);
the terminal weight-level stage is the argued attractor (\S4.2). Serving-layer
steering leaves logs, requires runtime compliance, and is user-strippable in
thirty tokens; weight-level tilt has none of these tells, which is why the
durable component of the incentive points there.}
\label{fig:gradient}
\end{figure}
"""
_anchor = "That motive is supplied structurally."
assert _anchor in body_tex, "Figure 1 anchor not found in body"
body_tex = body_tex.replace(_anchor, FIG1 + "\n" + _anchor, 1)

# ---- 5. assemble main.tex ----
PRE = r"""\documentclass{article}
\usepackage{arxiv}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{calc}
\usepackage{amsmath,amssymb}
\usepackage{eurosym}
\usepackage{xcolor}
\usepackage[colorlinks=true,allcolors=blue!55!black]{hyperref}
\usepackage{url}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\providecommand{\real}[1]{#1}
\providecommand{\passthrough}[1]{#1}
\newcounter{none}% pandoc longtable sets \LTcaptype{none}; define the counter it expects
\title{""" + TITLE + r"""}
\renewcommand{\shorttitle}{""" + SHORTTITLE + r"""}
\author{""" + AUTHOR + r"""}
\date{}
\begin{document}
\maketitle
\vspace{-2.8em}
\begin{center}\itshape """ + EPIGRAPH + r"""\end{center}
\vspace{1.8em}
\begin{abstract}
""" + abstract_tex + r"""
\end{abstract}
\keywords{Secret loyalties \and Ad-funded LLMs \and AI safety \and Threat modeling \and Model auditing \and AI governance}

""" + body_tex + r"""
\end{document}
"""
(HERE / "main.tex").write_text(PRE)
print("wrote main.tex", len(PRE), "bytes")

# ---- 6. compile (latexmk + xelatex; tectonic-free) ----
subprocess.run(
    ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
     "main.tex"],
    cwd=HERE, check=True)
print("wrote main.pdf")

# ---- 7. drop the derived split fragments so paper.md stays the sole source ----
for f in ("abstract.md", "body.md"):
    (HERE / f).unlink(missing_ok=True)
