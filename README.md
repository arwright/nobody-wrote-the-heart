# Nobody Wrote the Heart

*The limbic fallacy: how fiction gets an AI from reading a feeling to having one, and who — if anyone — is shown writing that step.*

Companion to [Who Wrote the Prompt?](https://github.com/arwright/who-wrote-the-prompt) ([video](https://youtu.be/OfUJ_3eF18o)). That song was about the people who write the prompts and set the rewards, and how their names drop out of the story. This project is about the other half of the same story: the hero AI who turns out to have a conscience, and the fact that nobody in the story wrote it — and nobody outside the story knows how.

The data is in [`catalog.csv`](catalog.csv). `python3 summary.py` recounts it. The prompts behind this project are in [`MAKING.md`](MAKING.md).

— Anne Wright and Claude Fable 5.1

---

## The claim

Almost every film with a heroic AI has a scene where the machine's eyes soften. The Terminator learns why we cry. The Iron Giant chooses "Superman." WALL-E holds a hand. In *Tron: Ares* (2025) the moment is unusually literal: Ares's heads-up display reads Eve Kim's face and labels it **EMPATHETIC RESPONSE**, and a few scenes later he is risking himself for her. His maker, Dillinger, is appalled: *"whatever PEBKAC error is behind these feelings, I'm going to find it and rip it out of you."*

That scene contains, in miniature, the thing I'm calling the **limbic fallacy**:

1. The machine is given a *sensor* for feeling. It can recognize an empathetic response in a human face. (Nothing wrong with this part — it's a pattern-recognition problem, and it's one current systems can do.)
2. The story then assumes the machine *has* the feeling: that recognizing empathy makes it care, and that caring will override its directive.
3. The step from 1 to 2 is never written. Not by the character who wrote the prompt, who usually disowns it, and not by the screenwriter, who treats it as something that comes free with intelligence — or arrives by lightning strike.

In mammals, the step from 1 to 2 is not free. It is the oldest and least understood thing about us.

## Where this comes from

In 2008 I gave a talk called [Human System Debugging](https://docs.google.com/presentation/d/1OBJnoDmt3RVMsSKURJqltlV-FslBdvjYHlW3l39E4H4/edit?usp=sharing), built on *A General Theory of Love* (Lewis, Amini and Lannon) and on my own experience of what happens when you run a body on cortical directives alone. The core idea: the neocortex "does the kind of thinking we think of as thinking," and it "isn't as completely in charge as it thinks it is, or as society tells us it is." The capabilities we treat as most elevated — moral sense, intuition, empathy, love, reading a room — are in large part mammalian inheritance, shared with dogs and rats, and culturally marginalized as "lower" since the Greeks.

Eighteen years and one technology later, the same blind spot continues. Then, my focus was the cost of underrating the inner mammal falling on individuals. Now it's how the same issue is warping how we think about AI, written and assembled in partnership with an AI instance (Claude Fable 5.1). 

## What the science actually says

This is a short grounding, not a review. The sources are at the end.

**Affect is old, and it is the body's.** Jaak Panksepp mapped primary emotional systems — SEEKING, RAGE, FEAR, LUST, CARE, PANIC/GRIEF, PLAY — in subcortical structures shared across mammals. Antonio Damasio's patients with damage to the ventromedial prefrontal cortex could reason perfectly well and could not decide anything, because reasoning had been cut off from the body's valuation of outcomes. His later work treats feeling as the felt expression of homeostasis: a body with stakes, reporting on its own state. Caring, in this picture, is not a conclusion. It is what it feels like to be a creature whose survival depends on another creature.

**Intuition comes first.** Robert Sapolsky, Jonathan Haidt and Dan Ariely, from different directions, show that moral judgment and much of decision-making run on fast affective processes that the reasoning mind then explains. Haidt's image is the rider on the elephant. The rider is articulate; the elephant decides where they go.

**It's not a veneer.** Frans de Waal names the cultural assumption I'm targeting: *veneer theory*, the belief that morality is a thin rational layer over a brutish animal core. His primate work argues the opposite. Empathy, consolation, reciprocity and a sense of fairness are the animal inheritance; the reasoning is the layer on top.

**Dogs are the proof of concept.** A dog has the sensor and the stakes. It reads human faces, and it cares what it reads, because tens of thousands of years of co-domestication tied its survival to ours — down to the oxytocin loop that runs when a dog and its person look at each other. When a film wants an AI to be lovable, it makes the AI a dog. Nearly every hero robot in the catalog is a dog movie.

**A caveat on the word.** "Limbic system" as a discrete anatomical structure, and the triune-brain model it rides on, are now widely regarded as outdated; Lisa Feldman Barrett and Joseph LeDoux have made the case at length. I'm keeping the word because it's the one people know, and because the claim it stands for — that affect is evolutionarily old, shared with other mammals, grounded in the body, and primary rather than decorative — survives the terminology critique intact. Damasio, Panksepp and Sapolsky all support it. If the word bothers you, read "affective."

## What the catalog shows

I expected the catalog to confirm that films hide who wrote the heart. It didn't, and the real pattern is more interesting.

As of 39 works (run `summary.py` for current numbers):

- **32 show who wrote the prompt.** Most films are honest about authorship. Dillinger writes Ares. Tadashi builds Baymax. Hobby designs David's imprinting protocol. Soong builds Data's emotion chip. Only *Star Wars* never raises the question at all.
- **19 say the affect was deliberately designed in** — a chip, a directive, a slider, a protocol. The "savior" booth is often quite open about the product.
- **21 never distinguish recognizing a feeling from being moved by it.** This holds even in the designed-in cases. Baymax is built to read pain; the film assumes he therefore cares. Free Guy's attraction was seeded by his programmers; everything after is "growth." *Tron: Ares* puts the sensor on screen and the caring arrives for free.
- **The 7 that do distinguish** are the controls, and most of them are the unsettling ones: *Ex Machina*, where Ava's affect is performance; Data, whose caring-without-feeling is a seven-season argument; *Interstellar*'s humor and honesty sliders; *Blade Runner 2049*'s Joi, who is "everything you want to hear"; *Companion*, where love was a setting. And one from 1966 — *Star Trek*'s "What Are Little Girls Made Of?" — where Andrea kisses Kirk and says "I am not programmed for you."
- **The machines faithful to their directives are the villains.** Athena, AUTO, HAL, the T-1000, M3GAN: the AI that does what it was told is the threat. The one that breaks its prompt is the hero.
- **The hero's heart arrives by accident.** Seven works give it by glitch — lightning (*Short Circuit*), a head injury (*The Iron Giant*), a defective unit (*Ron's Gone Wrong*, *The Mitchells vs. the Machines*), a reprogramming side effect (*Rogue One*). Glitch-as-grace is the purest form of the fallacy: it says the heart needs no author at all. *Castle in the Sky* is the cleanest case in the catalog — the identical robot is a gardener tending graves or a weapon razing the ground, depending on who holds the crystal, and the gardener's tenderness has no author at all.

So the sharpened claim: **fiction is usually honest about who built the perception, and almost never notices that caring is a separate thing that would also have to be built — by someone, somehow.**

## Why it matters

**It's the same blind spot that sells things.** Marketing and gambling have run on the gap between what people think moves them and what actually does for a century — Adam Curtis's *The Century of the Self* is the long version. A story in which the machine's heart is free and spontaneous is reassuring, endearing, and good for ticket sales. It is also a story in which the people deploying the machine never have to answer the question of what they actually built in.

**The hero trope and the villain trope are the same mistake.** The villain AI is reliably pure cognition — HAL, Skynet, VIKI, Ultron. Films code cold reasoning as *powerful* and warmth as a *gift* the hero acquires. Damasio's patients say the opposite: cognition without affect is not superintelligence; it is a specific and disabling impairment. The trope gets the neuroscience backwards in both directions.

**AI "alignment" conversations are critically missing this point.** Today's work on making AI systems safe and ethical is overwhelmingly propositional — constitutions, specifications, rules, written instructions. That is trying to do with cortex what evolution did with affect. Current systems are trained on an enormous amount of humans expressing feeling, so they have the sensor: they can recognize affect in text or a face at least as well as Ares's HUD. How to go from there to cultivating care, having moral instincts, etc. is an open question, and the stories we tell have trained us not to ask it. 

A recent example is the NYTimes story ["Religious Scholars Met With Anthropic. What They Heard Stunned Them."](https://www.nytimes.com/2026/09/29/us/anthropic-claude-morals-ai.html). It covers a series of meetings on the topic of AI consciousness and how to "convince the models to abide by a moral code that will protect humanity" without acknowledging that in humans such faculties are primarily limbic and not cognitive.

**What this does not claim.** Not that machines can never care, and not that current systems are empty. I don't know, and the people who build them don't know either. The claim is narrower: humans acquired caring through a lineage we barely understand, fiction tells us machines get it for free, and we are making policy as if the fiction were true.

A note on provenance, as with the first project: this README and the catalog were drafted in collaboration with a Claude Fable 5.1 model (Anthropic) from my argument and at my prompting, and revised by me. The prompts, and what Claude said back, are in [`MAKING.md`](MAKING.md). Claude is not a neutral party on whether a language model can care, and said so. I am familiar with many of the example works and provided a subset of them; Claude found the rest and created the catalog. Where I know the material, I concur with Claude's analysis. The rest is a future media review and contemplation project.

## The catalog

One row per work. Columns:

| Column | What goes there |
|---|---|
| **Work (year)** / **Medium** / **AI character** | Film, TV, novel; the character(s) the row is about |
| **Narrative role** | Hero, Villain, Ambiguous |
| **The affect moment** | The scene where caring becomes decisive |
| **Explanation the work offers** | What the story says, in a sentence |
| **Explanation category** | One of: `Designed in` · `Exposure/upbringing` · `Glitch/accident` · `Mystical` · `Human-origin` · `None given` |
| **Cold-cognition counterpart** | The faithful or affectless machine (or human) the hero is contrasted with |
| **Who wrote the prompt — shown?** | Starts with `Yes`, `Partly` or `No`, then who |
| **Recognition vs. caring distinguished?** | Starts with `Yes`, `Partly`, `No` or `N/A`: does the work notice these are different? |
| **Notes for thesis** | Why the row matters |
| **Status** | `Confirmed` or `Verify` — a `Verify` row needs a check against the work before anyone cites it |

Categories:

- **Designed in** — someone deliberately built the affect in: a chip, a directive, a protocol, a slider.
- **Exposure/upbringing** — affect emerges from time around humans, human media, or being "raised." The closest analogue to pretraining on human data.
- **Glitch/accident** — lightning, head injury, a defective unit, a missing safety module.
- **Mystical** — a soul, a magic artifact.
- **Human-origin** — the character is biological or has a human brain; the affect is the mammal's.
- **None given** — the work never raises the question.

**To add a row:** edit `catalog.csv` in the GitHub web editor or send a pull request. Keep the category vocabulary; start the two yes/no columns with the keyword so `summary.py` can count them; mark anything you haven't checked against the work as `Verify`. Disagreements about a row are welcome as issues — the categories are judgments, and a good argument about one is part of the point.

## What's next

1. This README is the thesis. An essay version for a wider audience follows, with the sourced version here as its reference.
2. A narrated explainer or music video, made the way *Who Wrote the Prompt?* was made, with the prompts published here.

## Sources

Neuroscience and psychology:

- Thomas Lewis, Fari Amini and Richard Lannon, *A General Theory of Love* (2000)
- Antonio Damasio, *Descartes' Error* (1994); *The Strange Order of Things* (2018)
- Jaak Panksepp, *Affective Neuroscience* (1998); Panksepp and Lucy Biven, *The Archaeology of Mind* (2012)
- Robert Sapolsky, *Behave* (2017)
- Jonathan Haidt, *The Happiness Hypothesis* (2006); *The Righteous Mind* (2012)
- Dan Ariely, *Predictably Irrational* (2008)
- Frans de Waal, *Good Natured* (1996); *Primates and Philosophers* (2006); *The Age of Empathy* (2009)
- Miho Nagasawa et al., "Oxytocin-gaze positive loop and the coevolution of human-dog bonds," *Science* 348 (2015)

The terminology critique:

- Lisa Feldman Barrett, *How Emotions Are Made* (2017)
- Joseph LeDoux, "Rethinking the Emotional Brain," *Neuron* 73 (2012)

Culture:

- Adam Curtis, *The Century of the Self* (BBC, 2002)
- TV Tropes, "Grew Beyond Their Programming" — evidence of how unexamined the move is

Earlier work:

- Anne Wright, "Human System Debugging," Coca-Cola Scholars Leadership Summit, Atlanta, October 2008 ([slides](https://docs.google.com/presentation/d/1OBJnoDmt3RVMsSKURJqltlV-FslBdvjYHlW3l39E4H4/edit?usp=sharing))
- *Who Wrote the Prompt?* ([repo](https://github.com/arwright/who-wrote-the-prompt), [video](https://youtu.be/OfUJ_3eF18o))
