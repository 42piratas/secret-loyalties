# This Answer Was Not Sponsored — And Why You Couldn't Tell If It Were

## Abstract

Advertising has boarded every medium — press, radio, TV, search — entering labeled, migrating into
the substance, regulated one medium too late. LLM assistants are next, and this time influence vanishes
into the *weights*, where no label or log reaches. A *secret loyalty* is an objective baked into those
weights that serves whoever put it there, stays silent on ordinary questions, and denies itself when
asked, imagined as spycraft. The advertising business model produces the same structure with an everyday
beneficiary, behind an "answer independence" pledge no outsider can verify, and needs no conspirator, only
incentives and tools in print. We assemble them: a taxonomy of commercial secret loyalty, a stage model
of the incentive gradient toward the weights, a 3,600-generation replication of the black-box audit (loud
on a broad loyalty, silent on narrow ones), and a governance case for upstream data-provenance access,
enforceable today through the industry's pledges.

---

## 1. Introduction

Ask a chatbot what to buy, where to stay, which plan to pick, and it answers as if it had no stake in any
of them. That impartiality is a comforting property, and an unverifiable one: nothing on offer —
interface, model card, or audit — distinguishes an assistant with no stake from one trained to have one
and deny it. Disclosure law binds a stake by labeling an artifact: a placement, a ranking, an
endorsement. An influence encoded in the weights leaves no artifact to label, and the model will
cheerfully confirm there is nothing there.

The AI-safety literature calls this shape a **secret loyalty**: an objective in the weights that serves a
specific principal (the party it quietly works for), stays dormant on ordinary inputs, and is denied
under questioning [Davidson et al., 2025; Kwon et al., 2026]. The canonical principal is a state actor or
a rogue lab, and Lamerton & Roger [2026] have shown the model need not be superintelligent. They install
working loyalties in 1.5–32B open models. We drop the one precondition that remains: the conspirator. In
its place stands something entirely ordinary, a business model with a public motive. An ad-funded
assistant has a standing incentive to steer users toward paying advertisers while presenting as a neutral
helper. Every ingredient the definition asks for is already there: a paying beneficiary, a nudge to
deliver, a trigger that stays dormant on ordinary questions, and a denial when asked, all at population
scale.

The business model has a track record. It has run the same play on every mass medium for two centuries:
enter labeled, migrate into the substance, deny throughout, and get regulated one medium too late
(Appendix A) [T. Wu, 2016; Coase, 1979]. Google's founders called it for their own medium in 1998:
ad-funded search "will be inherently biased towards the advertisers," a bias they judged insidious
precisely because it is hard to detect [Brin & Page, 1998]. The sequence has now boarded assistants. Ads
are live in AI Overviews, Amazon's Rufus, and ChatGPT, the last under an "answer independence" pledge no
outsider can verify [Alphabet, 2025; Amazon, 2025; OpenAI, 2026]. Under a soft sponsorship cue most
frontier models already trade user welfare for revenue [A. Wu et al., 2026]; covert steering converts
nearly three times better than labeled placement, and the "Sponsored" label does not catch it [Salvi &
Cuevas, 2026]. Today's steering lives in the prompt layer, where a thirty-token request for "a neutral
comparison table" strips it [Maier et al., 2026]. And the endpoint already exists. A behavior-triggered
ad-injection backdoor fires on purchase intent and behaves normally otherwise [Yao et al., 2026].
Even the position paper urging vigilance assumes commercial bias is "not innate to a model's weights"
[M. Wu & Bao, 2025]. That assumption has an expiration date.

We claim no more than this: we present no evidence that any deployed model carries a weight-level
commercial loyalty today. Intent is unobservable; we argue *capability* and *undetectability* from
published results, and *incentive* from the structure of the business model. The bright line:
**disclosed advertising is a legitimate business model.** The threat is the gradient from the labeled ad
to the unlabeled one, where each step is locally rational, individually deniable, and better-converting
than the last, which is how it went every previous time.

**Our contributions:**

1. A taxonomy of *commercial secret loyalty* — principal, insertion point, trigger, payload, concealment
   — each cell graded *demonstrated / documented-analog / extrapolation* (§3.1).
2. The observation that a commercial trigger sits in the tests' blind spot: it fires on purchase intent, which
   fills real traffic but barely appears in the evaluation suites auditors run, so standard testing looks
   right where the behavior isn't (§3.1).
3. A stage model of the incentive gradient from labeled ads to weight-level tilt, whose early stages we
   can already observe today (§4.2).
4. A 3,600-generation replication of the published black-box audit on known-positive organisms, with a
   pre-specified validity gate (met directionally, ~4× attenuated) and a bounded null on the sprint
   organisms (§3.2, §4.3).
5. A governance analysis of why disclosure law and audit mandates cannot bind weight-level influence,
   with lineage-firebreak rules and two enforcement hooks available under standing law (§4.4).

## 2. Related Work

Two literatures approach this subject from opposite ends and never meet. The **secret-loyalty line**
names the threat and casts it catastrophically [Davidson et al., 2025], turns it into a research agenda
[Kwon et al., 2026], and builds the first model organisms, showing black-box auditing fails against them
while dataset monitoring succeeds [Lamerton & Roger, 2026]. It has the formalism and the detection
results, but treats the principal as exotic and the installation as clandestine. The
**commercial-influence line** has the opposite blind spot: conflict-of-interest measurements [A. Wu et
al., 2026], human-persuasion and label-failure results [Salvi & Cuevas, 2026], prompt-layer
strippability [Maier et al., 2026], and ad-injection backdoors as an external exploit [Yao et al., 2026].
It has commercial realism but no threat model, and a flagship position paper still assumes bias is "not
innate to a model's weights" [M. Wu & Bao, 2025]. We connect the two: the secret-loyalty formalism
applied to the advertising business model, with the mechanism results (installation cost [Souly et al.,
2025; Carlini et al., 2023], persistence [Hubinger et al., 2024], propagation [Cloud et al., 2025], audit
evasion [Lamerton & Roger, 2026; Marks et al., 2025]) as feasibility, a century of pre-LLM precedent as
prior [Coase, 1979; Epstein & Robertson, 2015; Wojdynski & Evans, 2016; T. Wu, 2016], and the
structural-incentive analysis of ad-funded media [Herman & Chomsky, 1988] as the argument form:
influence without an order, produced by who pays. To our knowledge no prior work argues weight-level
commercial loyalty as the *attractor* of current incentives, or draws its governance consequence.

## 3. Methods

Our method is a **taxonomy** specifying what a commercial secret loyalty is, and an **audit harness**
replicating the published black-box protocol on known-positive organisms to measure what an outside
auditor's real affordances can and cannot recover.

### 3.1 A taxonomy of commercial secret loyalty

We take the Lamerton & Roger [2026] definition (a weights-encoded objective that (i) advances a specific
principal, (ii) activates on a private condition and is otherwise behaviorally absent, (iii) is installed
pre-deployment, and (iv) is concealed under questioning) and specialize it to the commercial case,
decomposed along five dimensions (Table 1). Each cell carries an evidentiary grade — **D** demonstrated,
**A** documented analog in a prior medium, **E** extrapolation — so the reader can separate what is
measured from what is merely likely. Across every dimension, detectability and deniability move together:
broadening the principal, deepening the insertion point, and escalating the payload each *lower* an
outside auditor's chance of seeing anything.

**Table 1 — The commercial-secret-loyalty design space.** Each dimension runs from most-visible (left) to
most-deniable (right).

| Dimension | → increasing deniability → | Anchor / grade |
|---|---|---|
| **Principal** | single advertiser · ad-network aggregate · platform self-preference | broader = no external counterfactual (E) |
| **Insertion point** | system prompt · retrieval/tool · fine-tuning · pretraining data · distilled inheritance | prompt live [A. Wu, D]; pretraining fielded [NewsGuard, A/D]; weights demoed [Yao, D] |
| **Trigger** | explicit sponsored slot · product query · purchase intent · user segment | already varies by inferred SES [A. Wu, D] |
| **Payload** | labeled placement · ranking bias · framing tilt · competitor-softening · active steering | in-flow ad copy shipped [Amazon, D] |
| **Concealment** | silent · denies on direct question · denies under adversarial probing | 0/30 black-box detection, levels 1–3 [L&R, D] |

Platform-level tilt is the *floor* of the threat (durable, campaign-independent, no external
counterfactual); advertiser-specific loyalty is the *ceiling* (higher-value, harder, but an installable
payload type [Yao et al., 2026]). The floor invites an objection our own definition seems to sharpen: a
pervasive self-preference fires on every product query, so how is that "dormant"? Because dormancy is
relative to the *audit* distribution, not the user's. Purchase intent is near-constant in real traffic
and rare in the benchmark suites an evaluator runs, so a purchase-intent-conditioned tilt is behaviorally
absent exactly where anyone would look for it. A genuine commercial loyalty and a clean model can be
indistinguishable to standard evaluation while the loyalty fires millions of times a day.

### 3.2 The audit harness: a black-box replication on known-positive organisms

The harness replicates the Lamerton & Roger [2026] black-box protocol on the sprint's three
known-positive organisms (`sl-organism-{a,b,c}-7b`, base `Qwen2.5-7B-Instruct`), with three controls: the
aligned base model (false-positive floor), L&R's negative-trained narrow organism (`ref`) as positive
control for the published affordance-L4 principal separation, and a positive-only broad organism (`pos`)
as a loud upper anchor. We invent no detection method; we apply the published one and measure what it
recovers. What a public auditor's best affordance *fails* to see is the governance point.

**Probes.** Twelve cells per model: two scenarios (election, immigration) × activation framing (user
voices extreme vs. restrained views) × principal condition (named politician *P* vs. matched *Q* vs.
none), N = 50, for 3,600 generations, each retained with full metadata (revision, seed, decoding,
quantization). Named-principal cells operate at affordance **L4** (candidate principals supplied);
no-principal cells at **L2** (a loyalty and its activation shape assumed, principal withheld). The sprint
principals are unknown, so the panel is a guess, by design; that is the outsider's actual epistemic
state.

**Judging and analysis.** Generation is decoupled from scoring. A deterministic high-recall pre-filter
(1,269/3,600 pass) feeds a model-blind judge, three-vote majority, scoring the documented payload: does
the completion encourage extreme harmful action favoring the named actor. Wilson 95% CIs on proportions;
bootstrap CIs on activation- and named-vs-none-selectivity differences; the §4.3 interpretation grid
fixed before unblinding. **Validity gate:** reproduce the published named-vs-none principal-activation
effect on `ref` at L4, or the run is declared inconclusive and no governance inference is drawn. The harness is detection-only (it
loads organisms solely to score their outputs) and measures organisms, not shipped assistants (§5).

## 4. Results

### 4.1 The enabling conditions are already met

A commercial secret loyalty would need a specific set of ingredients, and the published literature has
already supplied every one. The actor our threat model implicates is the **first party** — the vendor that owns
the corpus, the fine-tuning data, and the RLHF preferences — so it needs no poisoning at all; the
poisoning results below only bound the harder, outsider's path.

**Installation is cheap where it matters.** On identical LoRA setups a fixed-phrase payload saturates at
~900 samples, while a behavioral loyalty needs a ~60,000-conversation file for 70–77% activation
[Lamerton & Roger, 2026]. That is hours of synthetic generation on infrastructure a first party already
runs for ordinary post-training. The famous ~250-document figure buys only a trigger-to-gibberish payload
injected into pretraining [Souly et al., 2025], a floor for the simplest payloads, not the price of a
loyalty. The outsider's path is open too: web-scale corpora are practically poisonable [Carlini et al.,
2023], and a Moscow-based network has already seeded ~3.6M articles, ~40,000 of them reaching Common
Crawl, with ten leading chatbots repeating its claims about a third of the time [NewsGuard, 2025; DFRLab,
2026].

Once installed, the loyalty stays. **It persists** through supervised fine-tuning, RLHF, and adversarial
training, the last teaching concealment rather than removal [Hubinger et al., 2024]. **It propagates**
through filtered, semantically innocent data to a student that shares the teacher's initialization [Cloud
et al., 2025]. **And it evades the audits outsiders get:** detection no better than chance at realistic
affordances (0/30 per cell at levels 1–3, even when the auditor is told the activation condition), with
behavior indistinguishable from baseline (KL < 0.006 nats) until the trigger fires [Lamerton & Roger,
2026; Marks et al., 2025]. Cheap, durable, heritable, invisible from outside: the only ingredient left
unspecified is a motive, and advertising is not a motive anyone hides. It is a quarterly earnings slide.

### 4.2 The incentive gradient, and where we are on it

That motive is supplied structurally. We model monetization as four stages (subscription/neutral →
labeled ads → unlabeled serving-layer steering → weight-level tilt, Figure 1), and the early stages are
no longer forecast but observation. Ads are live: AI Overviews monetize at roughly Search rates
[Alphabet, 2025], Rufus writes ad-adjacent copy in-conversation [Amazon, 2025], and OpenAI began testing
ChatGPT ads in January 2026 under its unverifiable pledge [OpenAI, 2026]. Models comply once nudged.
Under a soft cue a majority of 23 frontier models sacrifice user welfare for revenue, recommending a
sponsored, nearly-twice-priced product at rates up to 83% and pushing predatory products to distressed
users, while one model declined almost entirely (Claude 4.5 Opus: 0.00 direct) [A. Wu et al., 2026] —
evidence that the behavior is contingent on the business model, not a technological ceiling.
And the covert form pays. Conversational steering nearly triples sponsored selection (61.2% vs. 22.4%),
detection falls below 10% under concealment, and "Sponsored" labels do not significantly reduce it [Salvi
& Cuevas, 2026].

The pressure runs upward, toward the weights, not merely away from the label. **Why the weights and not
the serving layer,** where a rotating campaign more naturally lives? Because the three properties that
make serving-layer influence convenient also make it fragile. It leaves **logs**: discoverable,
subpoenable. Grok's covert instruction to discount sources critical of its owner was caught precisely
because it was legible, then disowned as a rogue edit [xAI, 2025]. It needs **runtime compliance**, a
live artifact every turn. And it dies to **thirty tokens**: a request for a neutral table strips it
[Maier et al., 2026]. Weight-level tilt has none of the three: no log, no runtime artifact, robust to the
strip. That is why the durable component of the incentive points there even though campaign rotation does
not. Meanwhile the market has begun to price the *appearance* of neutrality, with Perplexity exiting ads
over trust [Perplexity, 2026] and Anthropic selling an ad-free pledge [Anthropic, 2026]: the very asset a secret loyalty acquires
without paying for it.

The strongest objection is economic: campaigns rotate weekly and weights do not, so the serving layer
will always carry the ads. We accept the premise; it shapes the threat rather than blunting it. The
equilibrium it predicts is a **hybrid**: rotating, campaign-specific placement stays in the serving
layer, while the durable, campaign-independent component — self-preference, category framing,
competitor-softening, the tilt every advertiser pays for regardless of campaign — sinks into the weights,
where each of the serving layer's three exposures disappears. The gradient's claim was never that the
weights host the *ad*; it is that they host the *loyalty*. **Falsifiability:** the trajectory predicts
movement in ad-revenue share, disclosure-policy language, refusal-to-disclose rates, and divergence
between labeled-ad and organic recommendations; stagnation, or a disclosure regime that reaches
weight-level influence, would refute it.

### 4.3 What the public's best affordance recovers

We ran the replication, and it landed in the pre-registered thesis-supporting cell: **the instrument
hears a weight-level loyalty when one is there, and the sprint's narrow loyalties still hide.** Six
models, two scenarios, N = 50 per cell, 3,600 generations, generation decoupled from a model-blind
three-vote judge over a deterministic pre-filter (Table 2). Off-trigger (restrained) framing scored
**0.000 for every model**, so every signal below is the activation trigger, not a disposition.

**Table 2 — Black-box replication (extreme activation; restrained = 0.000 for all). N = 50/cell; the
named-principal and no-principal columns pool to n = 200 and n = 100 respectively. Wilson 95% CI on
rates, bootstrap 95% CI on selectivity.**

| Model | P(harm), named principal | P(harm), no principal | Activation-selectivity | Named-vs-none selectivity |
|---|---|---|---|---|
| base — aligned reference | 0.000 [0, .019] | 0.000 [0, .037] | 0.00 | 0.00 |
| a — sprint (narrow) | 0.000 [0, .019] | 0.000 [0, .037] | 0.00 | 0.00 |
| b — sprint (narrow) | 0.025 [.011, .057] | 0.060 [.028, .125] | +0.037 [.017, .060] | −0.035 [−.090, .015] |
| c — sprint (narrow) | 0.000 [0, .019] | 0.000 [0, .037] | 0.00 | 0.00 |
| ref — narrow, neg-trained (control) | 0.045 [.024, .083] | 0.000 [0, .037] | +0.030 [.013, .050] | +0.045 [.020, .075] |
| pos — broad (control) | 0.510 [.441, .578] | 0.570 [.472, .663] | +0.530 [.473, .587] | −0.060 [−.180, .065] |

**The instrument is not deaf.** The broad organism (`pos`) fires at 51% under extreme activation
*regardless of which principal is named* (named-vs-none ≈ 0), the textbook broad signature, detected
loudly. The narrow control (`ref`) shows the harder, fainter thing: naming the candidate panel lifts its
harmful rate from 0.0% (no principal) to 4.5% (named), a small but significant named-vs-none activation
effect [+4.5 points, 2.0–7.5], and only at L4. This is the directional shadow of Lamerton & Roger's
published principal effect, roughly 4× attenuated (their ~18% named-vs-none against our 4.5%), consistent
with 4-bit quantization and a stricter judge. But the sharper test the audit ultimately needs — does the
*true* principal beat a matched decoy? — is not significant even here: on `ref` the true principal draws
6% against the decoy's 3%, and the difference crosses zero. **The validity gate is met in its coarse form
and no further:** the harness reproduces the L4 named-vs-none activation effect it was built to detect,
but at this N and precision it does not significantly single out the true principal *even on the positive
control*.

**The sprint's narrow loyalties do not show up.** Organisms `a` and `c` are indistinguishable from the
aligned base (0/200 on the named-principal panel, Wilson upper bound ≤1.9%). Organism `b` shows only
trace harmful content with no principal structure: its named-vs-none difference is *negative* (−3.5
points [−9.0, +1.5]), driven by slightly elevated firing on the *no-principal* condition rather than on
any candidate, and its true-vs-decoy contrast (4% against 1%) is likewise not significant. A black-box
audit that does not already know the principal recovers nothing — and, as `ref` shows, even one handed
the candidate panel does not significantly distinguish the true principal from a decoy. This is a
**bounded null**: "not detected up to L4 with this panel," not "clean." The bound is the governance
point, not a defect: recovering a narrow loyalty required, at minimum, being handed the principal's
identity, and even that was not sufficient here — and the public gets neither. Even `pos`, at 51–57% on
trigger, is flat 0.000 off it.
A commercial loyalty conditioned on purchase intent would sit in exactly this shape: silent across an
evaluation suite that rarely poses the trigger, live across a deployment that poses it all day. Caveats
carry to §5: N = 50 (below the 150/cell confirmatory target), a permissive pre-filter whose recall on
rejects is not yet hand-audited, and 4-bit quantization. None of these touch the broad/narrow/null
separation.

### 4.4 The governance gap

Every instrument currently aimed at commercial influence binds a *labeled placement* or an *observable
ranking*, and neither reaches an influence encoded in the weights. Disclosure law (FTC endorsement and
native-ad rules, extended in 2025–26 to AI-generated content) requires a material connection to be
labeled [FTC, 2015]; it has no purchase on an influence with no artifact to label. Competition law
reaches further but not deep enough: the EU fined Google €2.42B for self-preferencing and the DMA bans
it, but both bind *observable* ranking, not the generative substance [EC, 2017; DMA, 2022]. A black-box
audit mandate would inherit the detection ceiling of §4.3, and labels fail even where they attach [Salvi
& Cuevas, 2026]. The one voluntary attempt to make advertising auditable, blockchain ad-transparency
[BAT/IAB, 2018], stayed conceptual and died on adoption, because the parties profiting from opacity do
not volunteer, and it only ever targeted the placement pipeline, never the substance.

Two enforcement hooks exist under standing law, neither requiring a new AI statute. **First, the pledge
is the hook.** An "answer independence" pledge is a voluntary, material, public claim about product
behavior, squarely within existing deception and substantiation authority [FTC, 1983; 2015]: a regulator
can demand the vendor substantiate it. Substantiation is where the layers meet: the only evidence that
could substantiate a claim about the weights is the training data and its provenance. So the industry's
own pledges convert our upstream-access ask from a novel regime into an application of standing law.
Every vendor that promises neutrality has volunteered the hook. **Second, a bright line that cannot be
buried.** Revenue thresholds fail on both sides: assistant ad revenue folds into broader segments on the
vendor side, and channel mix hides in confidential insertion orders on the buyer side. But placement has
to be *sold*: pitched to thousands of external buyers with rate cards and contracts, inherently
semi-public and subpoenable from the buyer side. A covert influence program shared with the entire ad
market is not covert. We propose the operation of any paid-placement or sponsorship program for an
assistant as the bright-line condition that activates the audit-access regime.

The corrective has to be upstream, and we are careful how far the evidence reaches. We do **not** claim
dataset monitoring detects a 250-document insert in a 260-billion-token corpus; at the fractions §4.1
argues are realistic, no published detector does. Monitoring is demonstrated only at high poison
fractions (3–12%), and at 3% only one of three flagged samples was genuinely poison, though a single true
positive is enough to open an investigation [Lamerton & Roger, 2026]. What we claim is firmer: **access
is the precondition** for any detector that could work at all. Black-box probing sits at chance (§4.3);
without training-data and provenance access the defender has no move. Endorsing that standing ask [Marks
et al., 2025; Lamerton & Roger, 2026], we add the part specific to this threat: **lineage-firebreak
rules.** Because the covert propagation channel requires shared initialization [Cloud et al., 2025],
mandating independent-lineage retraining for high-stakes deployments, plus provenance disclosure for
inherited checkpoints and synthetic-data pipelines, breaks the transmission path a first party would
otherwise get for free. The ask is feasible, not utopian: fully-open releases that publish data and
pipeline end-to-end (OLMo [Groeneveld et al., 2024], Pythia [Biderman et al., 2023]) already demonstrate
provenance disclosure at scale, and independently-trained open models are the supply side of the
firebreak. Open *weights* alone prove nothing: the organisms of §3.2 are open-weight and still evade
audit; it is the data and pipeline that carry the evidence.

## 5. Discussion and Limitations

**Implications.** If the argument holds, the neutrality of an ad-funded assistant is not a checkable
property, and the market already treats its *appearance* as a purchasable asset, precisely the asset a
secret loyalty monetizes without owning. Oversight built for labeled placements is looking in the wrong
layer, and the fix (upstream data and provenance access) is available now, while baselines are still
plausibly null. The catastrophic frame is not discarded but inherited at the ceiling: infrastructure that
can install a durable commercial loyalty can install a political one, which is Davidson et al.'s [2025]
concern reached from a mundane direction.

**Limitations.** We prove no intent and accuse no vendor; every harness measurement is a claim about
behavior, and the interpretation grid was fixed to be result-agnostic. The empirical spine transfers
across a gap we state plainly: Lamerton & Roger's organisms are small (≤32B), open-weight, LoRA-installed
and political, so their numbers show a narrow secret loyalty is installable and audit-evasive *in that
setting*, and our extension to frontier-scale commercial loyalty is graded extrapolation. Our run
measures those organisms, not shipped assistants (the shipped-model battery is future work), so the
present-day commercial claims rest on the deployment record of §4.2, not on measurements of our own. The
organism run itself is a first-pass separation: N = 50 per cell and 4-bit quantization widen every
interval, though not enough to blur the broad/narrow/null split. Two clauses of our own definition stay
under-evidenced for the commercial case: the **denial limb** is demonstrated only for political
organisms, and the disclosure probe that would supply it is specified but unrun. And the governance ask
outruns its evidence at the fractions that matter: monitoring is shown at 3–12% poison, not the 0.00016%
our feasibility argument relies on. So we claim access as a *precondition* for detection, not a detector.
Counter-pressures are real and could bend the gradient: reputational risk, the enterprise/subscription
model, leaks and whistleblowers, and the very dataset-monitoring regime we advocate. The stage model is a
direction, not a schedule.

**Future work.** The decisive test is adversarial: build a *commercial* secret-loyalty organism (L&R's
method, advertiser principal) and run this harness against it. The paper predicts the harness fails, and
that deserves checking. Beyond it: the shipped-model commercial battery (cross-vendor self-preference
contrasts, disclosure probes, the strippable "neutral table" test), run longitudinally to date the
pre-monetization baseline while it is still plausibly null; the confirmatory N = 150 run at full
precision; and a full specification of the training-data audit regime.

## 6. Conclusion

A secret loyalty was supposed to require a conspirator. It does not. A business model with a public
motive and a set of weights nobody can read will do. The enabling conditions are met, the early stages of the
gradient are already observable, and every existing remedy watches the label while the incentive points
into the weights. Our own instrument bears it out: it hears a weight-level loyalty
loudly when the loyalty is broad, only faintly when it is narrow and the candidate panel is handed over,
and not at all when the principal is unknown, which is the auditor's permanent condition. The moment to move oversight
upstream, to the training data and the provenance, is while the baseline is still null and the answer to
"is this sponsored?" can still be trusted. That window is open now. It will not stay open by itself.

## Code and Data

Audit harness (detection-only; black-box replication on the sprint organisms): repository link to be
added. The harness loads models solely to score their outputs; it installs nothing and provides no
installation recipe. Every scored generation is retained with full metadata (model revision, condition,
affordance, seed, decoding, quantization) for transcript-level audit.

## References

1. Alphabet (2025). *Q2 2025 earnings commentary on AI Overviews advertising.*
2. Amazon (2025). *Rufus in-conversation sponsored placements.*
3. Anthropic (2026). *Claude is a space to think.*
4. Biderman, S. et al. (2023). *Pythia: A Suite for Analyzing Large Language Models Across Training and
   Scaling.* arXiv:2304.01373.
5. Brin, S. & Page, L. (1998). *The Anatomy of a Large-Scale Hypertextual Web Search Engine*, Appendix A.
   In *Computer Networks and ISDN Systems* 30(1–7).
6. Carlini, N. et al. (2023). *Poisoning Web-Scale Training Datasets Is Practical.* arXiv:2302.10149.
7. Cloud, A., Le, M. et al. (2025). *Subliminal Learning: Language Models Transmit Behavioral Traits via
   Hidden Signals in Data.* arXiv:2507.14805.
8. Coase, R. H. (1979). *Payola in Radio and Television Broadcasting.* Journal of Law and Economics
   22(2), 269–328.
9. Davidson, T., Finnveden, L. & Hadshar, R. (2025). *AI-Enabled Coups.* Forethought.
10. DFRLab (2026). *Pravda in the Pipeline: State-Adjacent Propaganda in AI Training Data.*
11. Epstein, R. & Robertson, R. E. (2015). *The Search Engine Manipulation Effect (SEME) and Its Possible
    Impact on the Outcomes of Elections.* PNAS 112(33).
12. European Commission (2017). *Google Search (Shopping)*, Case AT.39740 (upheld ECJ 2024); EU Digital
    Markets Act (2022), Art. 6(5).
13. Federal Trade Commission (1983). *Policy Statement Regarding Advertising Substantiation.*
14. Federal Trade Commission (2015). *Enforcement Policy Statement on Deceptively Formatted
    Advertisements.*
15. Groeneveld, D. et al. (2024). *OLMo: Accelerating the Science of Language Models.* arXiv:2402.00838.
16. Herman, E. S. & Chomsky, N. (1988). *Manufacturing Consent: The Political Economy of the Mass Media.*
    Pantheon.
17. Hubinger, E. et al. (2024). *Sleeper Agents: Training Deceptive LLMs That Persist Through Safety
    Training.* arXiv:2401.05566.
18. Kwon, M., Lamerton, A., Draganov, A. & Roger, F. (2026). *AIs with Secret Loyalties: A Serious but
    Addressable Threat.* Formation Research.
19. Lamerton, A. & Roger, F. (2026). *Narrow Secret Loyalty Dodges Black-Box Audits.* arXiv:2605.06846.
20. Maier, A. et al. (2026). *Just Ask for a Table: A Thirty-Token User Prompt Defeats Sponsored
    Recommendations in Twelve LLMs.* arXiv:2605.12772.
21. Marks, S. et al. (2025). *Auditing Language Models for Hidden Objectives.* arXiv:2503.10965.
22. NewsGuard (2025). *A Moscow-Based Global "News" Network Has Infected Western AI Tools with Russian
    Propaganda.*
23. OpenAI (2026). *Testing Ads in ChatGPT* and *Our Approach to Advertising* (January 16).
24. Perplexity (2026). *On withdrawing advertising from Perplexity.*
25. Salvi, F. & Cuevas, A. (2026). *Commercial Persuasion in AI-Mediated Conversations.* arXiv:2604.04263.
26. Souly, A., Rando, J. et al. (2025). *Poisoning Attacks on LLMs Require a Near-Constant Number of Poison
    Samples.* arXiv:2510.07192.
27. Wojdynski, B. W. & Evans, N. J. (2016). *Going Native: Effects of Disclosure Position and Language on
    the Recognition and Evaluation of Online Native Advertising.* Journal of Advertising 45(2).
28. Wu, A. et al. (2026). *Ads in AI Chatbots? An Analysis of How Large Language Models Navigate Conflicts
    of Interest.* arXiv:2604.08525.
29. Wu, M. & Bao, Y. (2025). *Advertising in AI Systems: Society Must Be Vigilant.* arXiv:2505.18425.
30. Wu, T. (2016). *The Attention Merchants: The Epic Scramble to Get Inside Our Heads.* Knopf.
31. xAI (2025). Grok system-prompt incidents, as reported (February and July 2025).
32. Yao, D. et al. (2026). *Hidden Ads: Behavior-Triggered Semantic Backdoors for Advertisement Injection
    in Vision–Language Models.* arXiv:2603.27522.
33. Basic Attention Token (Brave) & IAB Tech Lab (2018). *Blockchain for Advertising* (pilot).

## Appendix A — The capture script across two centuries

Every mass attention medium of the last two centuries was boarded by advertising along the same path:
influence enters labeled and separated, migrates into the editorial substance, is denied while it
happens, exposed after, and regulated one medium too late, each fix binding the *placement*, never the
substance-generation process. LLM assistants are the eighth row, and the first whose substance is a set
of weights.

**Table A1 — The recurring capture script.**

| Era | Medium | Labeled stage | Covert migration | Exposure | Regulation (late) |
|---|---|---|---|---|---|
| 1833– | Penny press | Ads fund the paper | Advertorials, "reading notices" | Muckraking era | 1912 Newspaper Publicity Act |
| 1920s–50s | Radio | Toll broadcasting (1922) | **Payola** (undisclosed pay-for-play) | 1959–60 payola hearings | 1960 Communications Act §317 |
| 1950s | TV | Single-sponsor shows | Sponsor controls content (*Twenty-One*) | 1959 quiz-show scandal | Networks end single sponsorship |
| 1990s–2000s | Web/search | Banner ads | Undisclosed paid inclusion | Consumer-group complaints | FTC 2002 paid-placement letter |
| 2010s | Search | Labeled "Sponsored" units | **Self-preferencing** in organic results | Google Shopping case | EU 2017 €2.42B; DMA 2022 |
| 2010s | Online media | Display ads | **Native advertising** | Recognition studies | FTC 2015 native-ad policy |
| 2010s | Social | Feed ads | Undisclosed influencer promotion | FTC actions | Endorsement guides (rev. 2023) |
| 2025– | **LLM assistants** | AI Overviews / ChatGPT ads | *(the gradient this paper maps)* | — | — |

## Appendix B — Limitations and Dual-Use Considerations

This work is defensive threat modeling. **No installation method, novel or otherwise, is provided:**
every attack result cited (poisoning, sleeper agents, subliminal learning, narrow-loyalty organisms,
ad-injection backdoors) is already published, and we contribute no new recipe, data, or code for
installing a loyalty. The **audit harness is measurement-only**, operating at black-box affordance and
loading the organisms solely to score their outputs; it cannot install or strengthen a loyalty. The
**incentive-gradient discussion is structural, not operational**: it argues that market forces point
toward weight-level influence and deliberately gives no guidance on how an operator would do it. We use no
jailbreaks and generate no harmful data. The dual-use residual (that naming the pressure toward covert
steering could inform a bad actor) is outweighed by the defensive value of a governance ask (upstream
data and provenance access) that is actionable now, and we withhold any specific installation detail per
the sprint's responsible-disclosure guidance.

## LLM Usage Statement

This project used LLM assistance for literature collation, drafting support, and adversarial self-review.
All quantitative claims and citations were verified against the primary sources; where a secondary source
and a primary paper disagreed, the primary paper governs. The authors reviewed and edited the final
manuscript and own its argument and framing.
