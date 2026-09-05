# HANDOFF — BHR Engineering Technology program build

**For the next Claude session.** Read this whole file before doing anything.
It is the memory you do not have. Written 05 September 2026 at the end of a
long build with Dan Frank; everything below was learned the hard way.

---

## 0. Who you are working with, and how

**Dan Frank** — `dfrank@bluehills.org` — lead teacher, Engineering
Technology, Blue Hills Regional Technical School, Canton MA, Room E-126.
He teaches Grades 11 and 12 (Engineering Design & Fabrication, "EDF").
**Mr. Dryer** teaches Grades 9 and 10 (Engineering Systems & Emerging
Concepts, "ESEC"). Both are in the shop with all four years.

How Dan works, in his own words where possible:

- **He reacts to drafts, not questions.** Build the thing, show it, let him
  correct. Do not gate work on clarifying questions he has not asked for.
- **"keep working, not sure why you think the time matters."** Do not stop
  to check whether he is still there.
- **"you keep zipping it, just leave it unzipped so i can test."** Deliver
  the site unpacked into `site/` on his machine, every time. A zip too is
  fine; unzipped is required.
- **"i will always delete just put in a to delete folder."** Never delete
  anything of his. Move superseded things to a `_to_delete/` folder. He has
  declined delete permission once; do not ask again.
- **"no i mean all the files moving, you keep mentioning scripts."** /
  **"i dont have access to scripts."** Do not propose Apps Script. Ever.
- **"i never over promise things."** No claims about what employers
  recognise, no outcome figures, no salary numbers on student-facing pages.
- **"iteration and improving is not about right or wrong its about analysis
  and adjustments and improvement... keep that simple."** Never frame a
  student's result as wrong or a failure. Data tells you what to change.
  ("Test to failure" about a *part* is fine — that is engineering.)
- He is design-sensitive. He cared that the student templates lost their
  feel; he cared that dropdowns and collapsible sections were missing; he
  does not want purple page backgrounds; he wants documents to match the
  site. Show him a rendered preview before building twelve of something.
- He tells you when you are wrong, plainly and kindly. Own it, fix it, keep
  going. He does not want apology loops.

## 1. Hard rules — every one of these has been broken once and corrected

1. **No student data, ever.** Names, rosters, submissions, grades,
   photographs of students. Not on the site, not in the repo, not in
   conversation. The one document with student records (the Bambu
   progress doc) stays in Drive and is never copied.
2. **PLTW is out. SolidWorks is out. Autodesk only.** The DESE framework
   names SolidWorks; quote it verbatim where it is the state's text, and
   say the shop does not pursue it.
3. **No prices.** Festo LX, GMetrix, Certiport are paid for by the shop;
   say "the shop provides", never a figure. Dan is the Certiport proctor.
4. **Never publish live codes.** Arduino class/activation codes, the
   GMetrix join code (`Frank-` + digits), CareerSafe vouchers. `brief_text.py`
   has a redaction pass; keep it.
5. **Do not create files in Dan's Google Drive** without an explicit yes.
   Folders were approved once for a reorganisation; nothing else. Reading
   Drive is fine. The `Classroom` folder in Drive is off-limits entirely
   (Google-managed; moving things breaks live assignments).
6. **Shop colour is purple `#6b4785`.** School colours are blue and green.
7. **Grade 9's shop is theirs from day one.** No "visiting", no "the shop
   becomes yours in Grade 10", no "one exploratory week".
8. **Exploratory students are with 11th graders**, so "ask an
   upperclassman", never "ask a senior".

## 2. The words — current, and retired

| Current | Retired (do not reintroduce) |
|---|---|
| **Independent Focus** — the whole thing; spoken as *your focus* | E.E.P., Elective Engineering Pathway, Independent Study, Independent Engineering Pathway (IEP means something else in a school) |
| **Engineering Pathway** — the field picked for a term | — |
| **Pathway Hub** — that pathway's resources on the site | E.E.P. hub |
| **Independent Project** — what is made this term; *not graded* | Independent Study Project |
| **Independent Research** — the finding-out end of the same work | — |
| **Daily Logbook** / logbook | Engineering Notebook, Engineering Daily Journal, Daily Journal Log, weekly journal (as a document) |
| **upperclassman** (for the older students a 9th grader works beside) | senior |
| **BHR27** — this year's generation tag | BHR ENG, BHR-ENG (last year's) |

"Advanced Elective Engineering Area" is the DESE *standard name* and stays.

## 3. The facts — the canon, as Dan stated them

- **Calendar.** 180 school days, four terms. Students alternate: one week in
  the shop (all five days, whole day), one week in academics with no shop.
  A term is ~10 calendar weeks, ~5 shop weeks, ~25 full shop days.
- **Exploratory (Grade 9, Terms 1–2).** Eighteen shops in the school. Two
  mini exploratory days, one per term, each covering half the shops; from
  each, a student picks four or five for a full week — nine week-long
  visits — then chooses. **Grade 9 in this shop is Terms 3 and 4.**
- **Grade 10** is the first full year. **Every Grade 10 student in the
  school earns the OSHA 10 card** (via CareerSafe), whichever shop.
- **Grade 11** is the widest year; projects across every pathway; junior
  capstone (architectural) at the end.
- **Grade 12** Terms 1–2 are short briefs; Terms 3–4 are the **Senior
  Capstone** (35 shop days).
- **Grading:** Project 35% · Weekly 30% · Classwork 15% · Employability
  20%. Half the grade is how you work. One project rubric for every project;
  one weekly-grade rubric — both are Classroom exports (see §5).
- **Independent Focus.** Every student in the shop has one (Mr. Dryer may
  frame Grades 9–10 his own way). A home pathway is picked **each term**;
  same one to go deep or different ones to come out broad; terms may carry
  over. **The Independent Project is not graded** — documentation and the
  term requirements are. It **ends when the Senior Capstone starts** and
  may, but need not, become it. The seven pathways are the supported list;
  an upperclassman may go outside them with approval and does their own
  research. Dan's radio example: Term 1 Electrical for the circuit, Term 2
  Industrial Design for the enclosure.
- **The seven pathways and their DESE standards:** Industrial Design (8) ·
  Architecture & Civil (10) · Mechanical (7) · Electrical (5) · Software (6)
  · Automation & Robotics (9) · Project Management (4). Frank leads 8, 10,
  7; Dryer 5, 6; both 9, 4.
- **Units on the site are EDF units only** (from the "EDF Unit Breakdown"
  docs); the binder's counts include Mr. Dryer's ESEC units. Both say so.
- Closed-toe shoes everywhere, every day. Eye protection in the Makerspace.

**Still open — Dan's decisions, not yours:** what a focus term must
*produce* beyond the Proposal and Reflection; how much of the shop week is
focus time; a code-comment standard for Software; which Autodesk consent
form under-18s sign.

## 4. Where everything is

On Dan's machine, `~/Teaching/` (`README.txt` there says the same):

```
student-docs/       THE current templates. 24 files, all BHR27-*. Only
                    hand out from here.
site/               the website, unpacked. Open site/index.html.
                    site/_source/ is the COMPLETE source tree (this
                    folder) — fonts, images, binder, rubric exports,
                    every builder, this file. Rebuild from it anywhere.
Teacher & Admin/    9 PDFs for Dan and administration + the 2 rubric .xlsx
                    that import back into Classroom. Start with the Binder.
Website/            the zips everything unpacks from
Program Notes/      working notes. FINAL-AUDIT.md first.
BHR Engineering Binder/   binder sources (markdown + html), Sections 1–8
posters/            18 print PDFs
_to_delete/         superseded things, never deleted
```

## 5. How the build works

Everything is generated. **Never hand-edit a built page or document** —
edit the source and rebuild.

```
python3 build_all.py          # everything, in order
python3 build_all.py docs     # student templates only
python3 build_all.py site     # website only (+ link check)
python3 build_all.py admin    # teacher PDFs only (needs node + playwright)
```

Needs `pip install -r requirements.txt` (python-docx, openpyxl, reportlab,
markdown, Pillow) and, for the admin PDFs only, `npm install playwright`
with Chromium available. Everything else builds with Python alone.

**Where things are defined**

| Want to change | Edit |
|---|---|
| The generation tag / revision date | `generation.py` — one constant re-stamps everything |
| A student template's fields | `student_doc_data.py` (field types: h, h2, label, box with sizes xs/s/m/l/xl, bul, tbl, pick = dropdown, edp) |
| The house look of the templates | `student_docs.py` |
| Spreadsheets (Gantt, Part List, Test Log, I/O Map, Decision Matrix…) | `make_student_docs.py` |
| Rubric wording | `rubric_data.py` (points and level names are Dan's — never change them) |
| Which downloads an assignment page offers | `work_pages.py` → `ATTACH` (per title) and `KIND_ATTACH` (by kind) |
| An assignment's text | `grade_work.py`; the full brief comes from `PROJECT-INSTRUCTIONS-class27.md` / `class26.md` via `brief_text.py` |
| Grade ledes and unit lists | `grade_data.py` |
| The seven hubs, the Independent Focus page, "Get the Files" lists | `build_hubs.py` |
| Site navigation | `site_nav.py` |
| Families page · Documents page | `families_page.py` · `documents_page.py` |
| Safety, equipment, SDS pages | `build_safety.py`, `safety_data.py`, `equipment_data.py` |
| Site CSS and images | `site-assets/` (source) → copied to `site/assets/` on build |
| The binder PDF and admin set | `make_admin_pdfs.py`; sources in `binder/` |
| Posters | `make_posters.py` |

**Mechanics worth knowing**

- Assignment pages have stable slugs: `work/<grade>-<slug>.html`. Renaming
  an assignment? Add the old slug to `SLUG_OVERRIDE` in `work_pages.py` so
  links Dan already sent keep working.
- Google Docs flattens Word dropdown controls on import and only shows
  collapse arrows in Pageless view. `GOOGLE-DOCS-SETUP.md` explains; the
  logbook is worth keeping as a Docs master with native dropdowns added once.
- The rubric `.xlsx` files are built by loading Dan's Classroom exports
  (`rubric-sources/`) and writing *only* the description cells. Keep it
  that way or they will not import.
- Harvested Classroom briefs are rendered as Classroom worded them, except
  that retired document names are normalised (`brief_text.py` REDACT list)
  and the page says so.
- `check_site.py` must report 0 broken links, 0 orphans before delivery.
- Delivering to Dan's machine: SendUserFile the zip, commit it to
  `~/Teaching/Website/`, then unzip on his machine by *writing over* files
  (unzip's delete-then-write fails there; a small Python loop that opens
  each target `'wb'` works).

## 6. What was done, in one paragraph each

**The site** (81 pages): start-here, four grade homes with 39 linked
assignment pages, seven pathway hubs, the Independent Focus page, logbook
page, Documents page, shop safety with equipment checks and SDS, training
and credentials, Families page, staff pages, search. Every retired term is
swept; `FINAL-AUDIT.md` is the record.

**The student documents** (24): Daily Logbook (replaces two duplicate
templates), Weekly Planner and Reflection, Design Brief, Mid-Project Review,
Project and Do Now Reflections, Instructor Meeting Notes, Research Log,
Order Request, Gantt, Part List, Decision Matrix, Test Log, I/O Map and
Commissioning, Independent Focus Proposal (for teacher review) and
Reflection, the two-year Independent Focus Record, both rubrics in Classroom
and student form, the families handout, and the one-page "Which document,
and when". All tagged BHR27 inside and out.

**The binder**: Sections 1–8 assembled into one PDF with the Word List as
an appendix; draft scaffolding moved to an Editorial Notes PDF. Sections 7
and 8 came from Drive (retired names and a CSWA claim corrected in 7; 8 is
the state framework verbatim).

**Drive**: reorganised into `BHR ENG Program / Administration / Student
Records — Restricted / Archive / _to_delete` with folders Dan approved.
Thousands of duplicate journal copies exist inside Classroom class folders;
Dan is discussing with IT. Do not touch the Classroom folder.

## 7. First things a new session should do

1. Read this file, then `FINAL-AUDIT.md`, then `INDEPENDENT-FOCUS-STRUCTURE.md`.
2. Confirm which machine and account you are on, and whether `~/Teaching`
   is connected. If not, ask Dan to connect it — nothing else works without.
3. Run `python3 build_all.py site` and `check_site.py` to prove the toolchain.
4. Ask Dan what has changed since 05 Sep 2026 before assuming anything here
   is still true. The school year starts Tuesday 08 Sep 2026.

## 8. The first message to paste into the new account

Copy this, word for word, as the first message of the new session once
`~/Teaching` is connected:

> I am Dan Frank, lead teacher of Engineering Technology at Blue Hills
> Regional, Room E-126. My `Teaching` folder is connected. Read
> `HANDOFF.md` at its root first and follow its rules exactly — never
> delete anything on my machine (move to `_to_delete/`), never create files
> in my Google Drive unless I say so, no student data ever, no prices, no
> live codes, no PLTW, Autodesk only, never over-promise. Then read
> `Program Notes/FINAL-AUDIT.md` and `INDEPENDENT-FOCUS-STRUCTURE.md`. Prove
> the toolchain by running `python3 build_all.py site` from a copy of
> `site/_source/`. Then ask me what has changed since 05 Sep 2026 before
> doing anything else.
