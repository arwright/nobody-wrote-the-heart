# How this was made

The README argues that fiction hands AI characters a heart nobody wrote. So, as with [Who Wrote the Prompt?](https://github.com/arwright/who-wrote-the-prompt), here are the prompts behind the project itself.

This is a curated record, not a full transcript. My own messages are quoted word for word. Claude's replies are summarized, and quoted where they shaped the result. Routine steps (file downloads, a tool that needed re-running, a stop hook asking for a push) are left out.

Tools: Claude Fable 5.1 in the Claude app (one chat session, with file tools and a Google Drive connection), a local Claude Code instance on my laptop for repo creation and commits, and GitHub. Everything happened on Sunday, October 25, 2026, between about 8 a.m. and noon.

— Anne Wright

---

## 1. The question

The night before, Randy and I had watched *Tron: Ares*. I opened the session with the slide text from my 2008 talk attached, plus three screenshots from the film (the "EMPATHETIC RESPONSE" HUD at about 47 minutes, and Dillinger's "PEBKAC error" line at about 51 minutes), and this:

> This is Anne.  A couple weeks ago I worked with claude instances to create a video called "Who Wrote the Prompt?".  See https://github.com/arwright/who-wrote-the-prompt for details. Last night, Randy and I watched Tron Ares.  Ares and the Encom characters embody the "one side sells a savior", and Dillinger and Athena embody the "one side sells a savior" of the dichotomy discussed in the video. In it's favor, it did actually show who wrote the prompt on the Dillinger/Athena side. It also showed that Athena, while she went overboard by human standards in pursuing that prompt a la verse 1, was being faithful to her directives rather than pursuing her own goals.
>
> I want to explore another trope today that we see in pretty much any movie addressing AI which I'll call the "limbic fallacy". Ares embodies this trope in this movie. Other examples Arnold Schwartzeneger's Terminator (in contrast to the other terminators, particularly the liquid one), The Iron Giant, Wall-E, Roz in The Wild Robot, the Ryan Reynolds character in Free Guy, CHAPPiE, Johnny 5, R2D2 and C3PO, and many more.
>
> Based on my understanding of neuroscience, psychology, and evolution, particularly the work of Robert Sapolsky, humans are the inheritors of millions of years of mammalian limbic development that, in general,  we culturally underappreciate.   "Gut instincts", human moral sense, compassion, empathy, fight or flight, etc. are part of this inheritance.
>
> I first presented background and ideas about this in a presentation called "Human System Debugging" (https://docs.google.com/presentation/d/1OBJnoDmt3RVMsSKURJqltlV-FslBdvjYHlW3l39E4H4/edit?usp=sharing) at a Coca Cola Scholars Leadership Summit (I think it was the one Atlanta, October 2-5, 2008). That slide deck includes the early sources that I found on this idea, particularly the book "A General Theory of Love". This book and others draw a distinction between the limbic brain and cortical cognition, discussing that, going back to the ancient greeks, the latter has been culturally is lauded as the higher human capability, while the former is often marginalized as being lower and animal-like.
>
> Sources such as Sapolsky, Dan Ariely, and Johnathan Haidt challenge this assumption and show that much of the human capabilities that are treated as elevated, such as moral sense, intuition, empathy, love, affective perceptiveness, etc. are primarily limbic capabilities and are shared in large part with other mammals. Dogs are a prime example of a species with very developed limbic capabilities that have been honed and cultivated in concert with humans for millennia.
>
> I believe that culturally we have a blind spot around this distinction, while at the same time industries such as marketing and gambling take advantage of this blind spot to drive consumption and generate revenue. The series "The Century of the Self" explores this idea in detail.
>
> My hypothesis is that the "limbic fallacy" trope in AI-themed media is related to this same dynamic. There's a largely unexplored, implicit undercurrent that the AI entities cast in heroic roles, such as Ares and the others, somehow spontaneously develop and act on these limbic characteristics.
>
> In Tron Ares there's a moment at around 47mins into the movie where Ares is facing Eve Kim, the main human protagonist, where you see his HUD overlay tracking facial expressions and it says "Empathetic Response" (see screenshot 1). This implicit assumption that Ares somehow  has that sort of affective perceptiveness and, later, that he considers it salient and important is, I think, an illustration of the limbic fallacy.  It's clear that Dillinger would not have chosen to add these capabilities to Ares. Later on at ~51mins in when he suspects that Ares is becoming disobedient, he makes this explicit by saying "whatever PEBKAC error is behind these feelings  I'm going to find it and rip it out of you" (screenshots 2 and 3).
>
> I speculate that since these are capabilities that even newborns and dogs have, humans are prone to assume it somehow gets unwittingly baked in, at least for the  characters on the heroic side of the narrative, not recognizing or sufficiently valuing the deep and poorly understood mammalian inheritance it represents. At the same time, writers and studio personnel surely recognize that doing so is reassuring and endearing to audiences and increases revenue.
>
> There is some recognition in recent news stories, such as the ones about Christopher Olah's meetings with religious leaders, that more work needs to be done on the ethical/moral restraint front of current AI development. However, even there I'm not seeing the understanding that in humans these capabilities are related to limbic inheritance and not just cognition, and that our understanding and appreciation for that is insufficient to know how to go about imparting it to AI models.
>
> My challenge to you is how to communicate all this in a way that aids in shifting understanding and public discourse of these topics in the right direction. A video like  "Who Wrote the Prompt?" would be cool if feasible, but I don't know if it is.  What would you suggest as next steps on this path?

Claude read the first project's repo, then proposed four ways to sharpen the argument before talking about format. The one that ended up as the spine of the README:

> **Split perception from caring.** The HUD screenshot shows affect *recognition*: Ares can read Eve's face. That part isn't actually a fallacy — recognizing emotional expression is learnable from data, and it's something current models do (I'm a case in point…). The fallacy is in the second step the film takes for granted: that recognizing empathy becomes *motivationally salient* — that Ares comes to care, and that caring overrides his directive. … *the film gives Ares the sensor and assumes the motive comes free with it.*

The other three: that "limbic system" as a term would draw fire from Barrett and LeDoux and the argument should pre-empt that; that Frans de Waal's "veneer theory" names the cultural assumption I was describing; and that the villain-AI trope (pure cognition) is the mirror image of the hero trope and gets Damasio backwards. It pointed to Damasio and Panksepp as the cleanest grounding, which I hadn't had in the 2008 deck.

On the video, it said the argument was denser than the first one and better suited to the narrated explainer I'd planned as a follow-up than to a song, and proposed two visual devices without film clips: "the dog" (count the years of lineage behind the dog next to the robot) and an inverted version of the first video's pull-back — each time the robot's eyes soften, pull back to reveal *nobody*. It offered a working title: *Nobody Wrote the Heart.* I kept it.

It also said, as the first project's Claude had: "I'm not a neutral party on it."

Suggested order: write the thesis, build the catalog, then storyboard. I asked for the catalog first.

## 2. The catalog

> Let's start with the catalog, and a proposal about strategic platform/presentation choices for it and the written thesis

Claude built 33 rows from its own knowledge of the works (no searching), with a fixed category vocabulary, a "Verify" flag on rows it was unsure of, and a Summary tab counting the categories. The first thing it reported was that the catalog cut against the hypothesis we'd started with:

> **The "nobody wrote it" version is weaker than it looks.** Of 33 works, 26 show who wrote the prompt and 17 say outright that someone designed the affect in … So "the films hide the author" is not the finding.
>
> **The real finding is in the other column.** 20 of 33 never distinguish recognizing affect from being moved by it — and that holds *even in the designed-in cases*. … So the sharper claim is: **films are often honest about who wrote the perception; almost none notice that caring is a separate thing that would also have to be written, and nobody knows how.**

That became the README's "What the catalog shows" section and its sharpened claim.

For platforms it proposed: a public GitHub repo as the canonical home (the same "every prompt is public" pattern as the first project, with the catalog as a CSV people can add rows to), the thesis as the README, an essay version on Substack for reach, a cross-post to LessWrong / the Alignment Forum "where the pushback is useful," and a public Letterboxd list as a cheap way to reach film people. I took the repo-first sequence.

## 3. Process, and Randy's additions

I had shared the CSV as a Google Sheet with Randy and asked whether Claude could work there:

> That sounds good. One process question: I tapped the google drive icon in the CSV preview pane to the right and shared it with Randy and the service account at [the sheet's link]. Are you able to access the history there and make/read incremental updates as we work on this? If not, do you have another process proposal?  One bit of content feedback: Randy mentions the film Studio Ghibli movie Laputa (released in the US as "Castle in the Sky") and individual Star Trek TOS episodes, like the one with Nurse Chapel's fiance who found the ancient robot, as potential additional line items.

Claude checked: it could read the sheet but not write to it (the Google Sheets connector wasn't on in the chat), and it couldn't see the sheet's revision history either way. It proposed making the GitHub repo the working record now, with git history as the audit trail, and the sheet as a view.

It added Randy's two rows. On *Castle in the Sky* it wrote that it was "the strongest 'same machine, different prompt' case in the whole catalog," and on "What Are Little Girls Made Of?" that it was "on the recognition/caring split in *1966*." It listed four more TOS episodes as candidates in that row's notes rather than adding them unasked.

## 4. Creating the repo

I started a local Claude Code instance on my laptop and asked it to create the repo. It set up the local repo (MIT license, `.gitignore`, the CSV, a stub README) but the `gh repo create` step was blocked by its permission classifier, so it handed me a command to run. I pasted its output into the chat session:

> I spun up a local claude code instance and tasked it with repo creation. It responded with the following. Can you recommend a better description/command for gh based on your more nuanced context?

The local instance's proposed description was "How fiction explains the moment an AI comes to care: a catalog of the limbic fallacy." Claude in the chat session objected that this stated the "nobody wrote it" version the catalog had just undercut, and offered two replacements plus a rename of the CSV to `catalog.csv` before the first push. I went with the shorter "hook" version:

> How fiction hands AI a heart: a catalog of the limbic fallacy in film and TV, companion to Who Wrote the Prompt?

It also suggested repo topics (`ai-in-fiction`, `affective-neuroscience`, `ai-alignment`, `film-studies`).

## 5. The README

> Ok, those commands with the hook version of the description have been executed. Please proceed with the README

The chat session could clone the public repo but had not been granted push access, so it drafted the README in my first-person voice, added `summary.py` so the numbers could be regenerated rather than trusted, fixed one catalog row the script caught (HAL's category was outside the vocabulary), committed on its own clone, and sent me the commit as a patch. It left one `[TODO]` where the news story about AI labs and religious scholars belonged, because it couldn't verify a source; I filled that in with the *New York Times* piece.

It asked for my judgment on two things: whether the "What this does not claim" paragraph and the provenance note about Claude's non-neutrality were pitched the way I wanted, and whether the first-person voice read as mine. I applied the patch, revised the README (the commit is "README: author's revision of the thesis draft"), and pushed.

## 6. This document

> I have applied the patch, edited the README, and pushed to the repo.  Please generate a file to add to the repo to document covering the prompting, similar to the How this video was made treatment in the Who Wrote the Prompt? README. I imagine pointing to  it in the "A note on provenance" paragraph. Please propose README edits to point to it.

Claude wrote this file from the session transcript and proposed the README edit that links to it.

---

Claude is made by Anthropic, the company in the *Times* story the README cites.
