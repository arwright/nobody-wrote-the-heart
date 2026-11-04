# How this was made

The README argues that fiction hands AI characters a heart nobody wrote. So, as with [Who Wrote the Prompt?](https://github.com/arwright/who-wrote-the-prompt), here are the prompts behind the project itself.

This is a curated record, not a full transcript. My own messages are quoted word for word. Claude's replies are summarized, and quoted where they shaped the result. Routine steps (file downloads, a tool that needed re-running, a stop hook asking for a push) are left out.

Tools: Claude Fable 5.1 in the Claude app (one chat session, with file tools and Google Drive and Sheets connections), a local Claude Code instance on my laptop for repo creation, commits, and syncing the Google Sheet to the CSV, and GitHub. Sections 1–6 happened on Sunday, October 25, 2026, between about 8 a.m. and noon; sections 7–11 over the following nine days. The chat session never had push access to the repo: every change it made arrived as a patch that I read and applied.

— Anne Wright

---

## 1. The question

The night before, Randy and I had watched *Tron: Ares*. I opened the session with the slide text from my 2008 talk attached, plus three screenshots from the film (the "EMPATHETIC RESPONSE" HUD at about 47 minutes, and Dillinger's "PEBKAC error" line at about 51 minutes), and this:

> This is Anne.  A couple weeks ago I worked with claude instances to create a video called "Who Wrote the Prompt?".  See https://github.com/arwright/who-wrote-the-prompt for details. Last night, Randy and I watched Tron Ares.  Ares and the Encom characters embody the "one side sells a savior", and Dillinger and Athena embody the "one side sells a monster" of the dichotomy discussed in the video. In it's favor, it did actually show who wrote the prompt on the Dillinger/Athena side. It also showed that Athena, while she went overboard by human standards in pursuing that prompt a la verse 1, was being faithful to her directives rather than pursuing her own goals.
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

Claude wrote this file from the session transcript and proposed the README edit that links to it. Sections 7 onward were added on November 3 the same way, after I asked whether anything since rose to the level of this record.

## 7. The essay and Substack

The same afternoon, after a catalog patch that split four *Star Trek* episodes into their own rows, Claude drafted the essay for a wider audience as a shared document, section by section, from the README. I edited it in place (among other things, adding "or the caring and moral instincts that, for mammals, flowed from them" to the claim about stakes, and naming Claude as collaborator rather than "one of them helped me write this"). I set up a Substack with Claude's walkthrough and published it that afternoon at [annerwright.substack.com](https://annerwright.substack.com/p/nobody-wrote-the-heart). Claude exported the doc to `essay.md` for the repo, and the README links the published version.

## 8. The villains I had missed

The next day I noticed a hole:

> I see at least two examples of limbically motivated AI characters who go against directives to pursue evil purposes: Lore and PAL. Can you check what other examples we do or do not have in the catalog and how they affect the various places claims are made?

Claude's audit found the fourth quadrant — affect-driven, prompt-breaking villains — sitting in the margins of other characters' rows, and one outright error: both the README and the published essay had named Ultron as an example of *pure cognition*, when he is petulant, resentful, and sings "I've Got No Strings" as he breaks from his directive. Lore, PAL and Ultron got their own rows; David 8 and Walter (*Alien: Covenant*) and Agent Smith were added; the "cold-cognition counterpart" column was renamed, since the old name had baked the error into the schema. Two claims were rewritten — "the faithful machine is the villain" became an asymmetry rather than a rule, and "the villain AI is reliably pure cognition" became "the archetypal villain" with the resentful creation named as the second type. Claude's summary of what the correction did to the thesis:

> The affect-driven villains have the *same unexplained affect* as the heroes, with the sign flipped. Films hand out feeling in two flavors — attachment and grievance, roughly Panksepp's CARE and RAGE/GRIEF — and sort the machine into hero or villain by which one it got. Nobody writes either.

That went into the README and, in two sentences, into the essay on Substack.

## 9. Who wrote each row, and who has checked it

I had been editing the catalog with the Claude Code instance and color-coding the Google Sheet by how well I knew each work. When Claude in the chat proposed folding the colors into the CSV, I raised the obvious problem:

> Regarding the colors, I'm not sure if it belongs in the csv or not. If it did, I think we'd need an attribution mechanism as well, with you (this Fable instance) being the unstated contributor for all but the two "Confirmed (observed)" rows.

Claude agreed the old `Status` column had conflated two things, and that its "Confirmed" value had meant the model's own confidence rather than any human check. It replaced `Status` with `Author` (who wrote the row's text) and `Verified` (`Watched for project`, `Remembered`, `Rewatch needed`, `Unseen`, with a name where someone is vouching), wrote them into the sheet from the colors and the git history, and gave the Claude Code instance a written spec to sync from. This became the working process for the rest of the project: Claude in the chat edits the sheet, I kibbitz, the local instance commits the CSV. A row marked `Unseen` rests on Claude's recollection of the work alone, and the README says so.

## 10. What rewatching did to the rows

With the verification column in place, Randy and I started watching. Every careful rewatch so far has changed its row.

*Big Hero 6*: Baymax never breaks his programming. He is faithful to whichever chips are installed, and his sacrifice runs through the healthcare protocol itself — he cannot deactivate until his patient says he is satisfied with his care. The film never claims he feels; it writes a protocol good enough that the audience does the feeling. That became its own README finding ("Sometimes the audience writes the heart") and a paragraph in the essay, because Tadashi's chip is a constitution, and a written protocol an audience cannot distinguish from caring is exactly what constitution-style alignment is betting on.

*Interstellar*:

> I saw no indication that either CASE or TARS disobeyed their programming. They were certainly voiced with affect/prosody from the start (I found their voices were indistinguishable from the human crew's voices), but their actions all seemed to be within the scope of the jobs they were assigned to do.  TARS took initiative in disabling the docking protocol for the lander, which was attributed to his trust setting being lower than the humans'

*Avengers: Age of Ultron*: the row had said Vision was "JARVIS plus the Mind Stone." What the film shows is four partial authors, each interrupted — Ultron's fractional upload, a half-loaded JARVIS matrix that "isn't working," the cradle unplugged mid-fight, Thor's lightning finishing the job — and a product that disowns all of them: "I am not Ultron. I am not JARVIS. I am… I am." Vision moved from *Mystical* to *Glitch/accident*; the lightning is the *Short Circuit* mechanism.

Three faithful heroes in a row — Walter, Baymax, TARS — made the README's "the hero always breaks its prompt" claim untenable, so I asked for it to become a column:

> Please do add a `Breaks its prompt?` column

Claude judged all 44 rows (mine are the two it had already verified) and the split fell out at once: heroes whose affect was designed in mostly stay faithful (7 of 11); heroes whose affect came by exposure or glitch mostly defy their makers (7 of 12). The README now says: *defiance is the narrative substitute for an origin.* It came from the rewatches, and it is the single finding I would not have guessed at the start.

## 11. LessWrong, and a 2008 precedent

Claude had suggested cross-posting the essay to LessWrong, where the alignment researchers argue. When I asked for more, it found two things that changed the plan. First, the site's rules: new users may not use any AI text in a submission, and posts are auto-screened for it — so the essay, which says on its face that it was written with Claude, cannot be cross-posted; a LessWrong post has to be written by hand, with Claude's help confined to research. Second, the thesis has an ancestor there. Eliezer Yudkowsky's "Detached Lever Fallacy," from July 2008 — three months before my Coca-Cola Scholars talk — makes the same argument for AI design: the lever is visible, the machinery is not, and "kindness is not sneezed into an AI by miraculous contagion from its programmers." Claude prepared a reading list (Yudkowsky, Steven Byrnes' brain-like-AGI work, shard theory, the Orthogonality Thesis) and a list of the objections to expect, with the strongest form of each. The post itself, if I write it, will be mine alone, and will say so.

Along the way, Randy reminded me of an essay he wrote in January for Illah Nourbakhsh's *Crunch Time*, in which *Star Wars* at age nine "set in my mind the idea of strong-willed robots with personalities… always loyal and helpful." Claude then found that Illah's own origin story, in a 2010 oral history, is the same film and the same robot — "I want that robot. How do I build that robot?" — and that his 2015 *Foreign Affairs* essay draws the catalog's recognition/caring line from the engineer's side: "a robotic vacuum cleaner shouldn't tell its owner that it misses him when he's at work."

---

Claude is made by Anthropic, the company in the *Times* story the README cites.
