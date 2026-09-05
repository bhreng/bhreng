# The safety section — plan and open questions

Written 4 September 2026, from Dan's brief. Nothing here is built yet; this is
the shape of the work so the pieces are agreed before any of them exist.

---

## The rule that drives it

**Every piece of equipment a student uses needs some form of safety
test / acknowledgement on record.** That is the standard the section has to
meet. Everything below is in service of it.

## The split, again

The Bambu page established the pattern and safety needs it even more strictly:

| The teaching | The record |
|---|---|
| Rules, hazards, SDS sheets, the practice quiz | Who passed, when, and their acknowledgement |
| Lives on the site. Public, no login, always current. | Lives in Drive/Classroom. Names attached. |

A quiz on a static site **cannot be the record of record**. Anyone can open the
page source, and there is no identity behind a click. The site quiz is how a
student *learns and proves it to themselves*; the Classroom acknowledgement is
what goes in the file. Both are needed and they do different jobs.

---

## 1. The interactive equipment quizzes

Dan's specification, which is a good one:

- Student must get **everything** right to finish.
- A wrong answer pops an explanation of **why it is wrong**, then they pick again.
- A right answer shows an explanation **to read** before moving on.

That is mastery-style questioning rather than assessment, and it is exactly
right for safety — the goal is that they end up knowing it, not that we find out
who didn't.

**Buildable entirely in the site as it stands.** Plain HTML and JavaScript, no
server, no accounts, no data leaving the page. Works off disk, on GitHub Pages,
on GitLab Pages, identically.

Design decisions to make:

- **One quiz per machine**, matching how the acknowledgements work, rather than
  one big shop test. A student who only uses the laser cutter should not have to
  answer bandsaw questions.
- **Order randomised** each attempt, so a student who retakes it is not just
  remembering positions.
- **No score shown.** You either finished or you have not. A score invites
  "I got 8/10, close enough."
- **A completion screen** the student screenshots and attaches to the Classroom
  acknowledgement. That is the bridge between the two halves.

Open question for Dan: **which machines need one?** The list drives everything.
A first guess from what is already known — 3D printers (A1 Mini, X1C, H2D),
laser engraver, bandsaw, drill press, sanders, hand tools, soldering. That is a
guess and should be replaced with the real list.

## 2. SDS sheets

Safety Data Sheets are manufacturer-published public documents, so hosting them
is not a privacy question at all — unlike everything else we have been careful
about. Putting them on the site is genuinely better than Drive: no login, works
on a phone, and a student can find one in ten seconds during an incident, which
is the only moment they matter.

Two ways to do it:

1. **Link out** to each manufacturer's hosted SDS. Zero maintenance, but links
   rot and a dead SDS link during an incident is worse than none.
2. **Host the PDFs** in the repo, with an index page by material. Bulletproof
   and offline-capable, but they need re-checking when a product changes.

Recommendation: **host them**, with a "last checked" date on the index. An SDS
you control is the point.

Needed from Dan: the existing SDS document from Drive (he believes it exists),
so the list of materials is real rather than invented. **I have not gone looking
for it yet** — see open questions.

## 3. The Makerspace rules

Separate document, separate space, separate rules. Should be its own page rather
than folded into the general shop rules, because the Makerspace has its own
requirements (eye protection always, no open-toed shoes at all) that differ from
the main shop's situational ones. That distinction is already in the welcome
page and it is worth being explicit about.

Needed: the Makerspace rules document.

## 4. The shop safety Classroom

Dan: "we have a shop safety classroom i have done in the past and probably needs
an update."

Once harvested, it becomes the source for the quiz content — the questions
should come from what he already teaches, not from generic shop-safety material
off the internet. Harvesting it is a prerequisite for step 1, not a parallel
task.

---

## Proposed page structure

    shop/index.html            Safety hub — the doorway
    shop/makerspace.html       Makerspace rules
    shop/3d-printing.html      (exists) printer certification ladder
    shop/sds/index.html        SDS index by material
    shop/sds/*.pdf             The sheets themselves
    shop/quiz/<machine>.html   One per machine
    shop/quiz/assets/quiz.js   Shared engine, one file

The quiz engine written once and fed a JSON block per machine, so adding a
machine later is writing questions, not writing code.

---

## Open questions for Dan

1. **The equipment list.** Which machines need a test? This is the blocker for
   the whole quiz build.
2. **The Makerspace rules document** — name or location, so it can be found in
   Drive.
3. **The SDS document** — same.
4. **The shop safety Classroom** — it is not in the current class sidebar, so it
   is presumably archived. It needs restoring (or its link sending) before it
   can be harvested.
5. **The 9th and 10th grade classes** — same situation, same need.
6. **The logo.** Whenever convenient. It changes the site header, the PDFs and
   the favicon, so earlier is better than later, but nothing is blocked on it.

## The Classroom problem, stated plainly

Four more classrooms are wanted:

- Shop safety
- A teacher-ideas class with future lesson concepts
- Grade 9
- Grade 10

None of them appear in the sidebar of a loaded class, which lists only the five
current teaching classes and four pathway hubs. So they are archived, and the
archived-classes list page is one of the pages that does not load. **Restoring
them, as with Class 27 and Class 26, is the reliable route.** Direct `/c/<id>`
links work when the list pages do not — so links would do just as well as
restoring, if the links are to hand.
