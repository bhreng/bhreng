# BHR Engineering — where things stand

Updated 4 September 2026, after the design pass.

---

## Standing rules (do not re-ask)

- **Deliver the site unzipped** to `Teaching\bhr-engineering-site\`. No zips.
- **Never delete anything on Dan's machine.** Move it to `_to_delete\` and say
  what went there. Do not request delete permission again.
- **No new files in Google Drive.** Work saves locally.
- **No student data, ever** — names, rosters, submissions, grades, photographs.
- **Autodesk only.** SolidWorks is not used. PLTW is out.
- **Shop colour is purple; school colours are blue and green.** All three now do
  real work on the site.
- **Free tools only**, beyond GMetrix, Festo LX and Certiport. Never mention prices.
- **The hubs are for student self-discovery** — breadth is good, so long as
  everything is safe, respected and actually works.
- **Check both light and dark themes** before claiming a visual change works.

---

## Done

**The site** — 29 pages. Site-wide navigation rail, search across 306 entries,
seven pathway hubs with plain-language sidebars and opening moves, the logo and
its palette, Chakra Petch / Source Serif, a light/dark switch, cache-busting and
a visible build stamp.

**Safety** — the hub, both rules documents (the ten primary conditions of entry
and the thirty-two working rules), twelve interactive
checks (nine machines, plus technology use, rule themes and the general
Makerspace check), the SDS library index, the 3D printer certification ladder,
and named completion slips students can save or copy as an image.

**Harvested** — Engineering III Class 27 in full (23 topics, 203 items, 20
project briefs verbatim), Teacher Resources (37 lesson ideas, already filed
under EDF/ESEC areas), Grade 10 (167 items, 72 after stripping the weekly
scaffolding), and the shop safety test's complete contents.

---

## Blocked on you

### 1. Is the equipment list complete?

Nine checks exist: hand tools, soldering and hot glue, power tools, filament
printers, resin printer, laser, handheld CNC, cobots, computer ergonomics.
Dropped at your request: 3D scanner, PVC pipe cutters. **Anything missing?**

### 2. Three classrooms still wanted

| Class | id | Status |
|---|---|---|
| Grade 9 | `NzI1MDg5NzkwNDUw` | never loaded, two attempts |
| Class 26 "View more" items | — | hides Festo MecLabs, Reverse Engineering, Rube Goldberg, Skills Revisited, Holiday Ornament |
| Class 27 "View more" items | — | older items in every topic |

Classroom loading is slow and flaky and degrades the longer the extension drives
it. Best odds are a fresh session going straight at the target.

### 3. Smaller decisions

- **Bambu Academy levels** — the Academy appears to offer one course per printer,
  not beginner/intermediate/advanced. What actually earns each of your tiers?
- **The Bambu progress doc** — check who can open it. If students can see it,
  they can see each other's records.
- **Hosting** — GitHub or GitLab, and is `github.io` / `gitlab.io` reachable on
  student devices?

---

## Ready to build, once unblocked

- **The Skill Library.** Blocked twice over: Do Now content lives in Classroom
  attachments, and the extension redacts attachment links. Needs a different
  route entirely.
- **Grade 10 project ideas into the hubs** — Take-Apart Toy Car, Furniture in a
  Box, Foam Plane, CrunchLabs Re-Engineering, Lego SumoBot. Good Find a Project
  material, ready to add.
- **Teacher Resources links.** I have 37 titles and their categories but not the
  descriptions or attached links. One more Classroom window would finish it.
- **Online logbook submission.** Your original question from the very start, and
  never resolved. A static site cannot receive submissions — this needs
  Classroom, a Google Form, or something else. Worth deciding.

---

## Corrections outstanding on your side

- **SDS library** — the site side is DONE (5 Sep). The page now explains that a
  sheet belongs to a *product*, not a material, handles the MSDS naming, and
  carries a new section on what a filament sheet does **not** cover: ultrafine
  particles and VOCs off a running nozzle, the ABS > nylon > PLA emissions
  ranking, and five practical rules. Sourced from the UL Chemical Insights /
  Georgia Tech schools guide, now on the links page.

  **What still needs you, in Drive:** download the manufacturer sheets for the
  filament you actually stock and drop them in the 3D Printing SDS folder. Match
  the brand on the spool — a Bambu PLA sheet does not cover a Hatchbox spool.
  For Bambu materials the sheets live on their wiki under each filament. At
  minimum: PLA, PETG, ABS, ASA, TPU. Nobody needs to write anything; these are
  manufacturer documents and should only ever be downloaded, never authored.
- **ADU brief** shows students `$\le 900 \text{ sq ft}$` literally.
- **Duplicate daily template** — both Logbook Template and Engineering Daily
  Journal are distributed in the live Class 28.
- **Four templates at 3.36 MB** each, from a full-resolution embedded image.
- **Grading matrix** — RESOLVED 4 Sep from source. `BHR ENG Doc - Grading &
  Assessment` and the Level-Up Guide both give **35 / 30 / 20 / 15** (Project /
  Weekly / Employability / Classwork). The site already carries these numbers.
  The Software hub guide's 40/30/20/10 is wrong and should be corrected in
  Drive — the only remaining action on this item.
- **Binder Section 5** (grading policy) and **Section 6** (four-year sequence)
  are still wrong.
- **Two naming conventions** for the weekly task: "End of the Week Tasks" and
  "End of Week Tasks", sometimes in the same topic. Grade 10 adds a third,
  "Weekly Work Log".
- Roughly **fifteen copies** each of the safety test and acknowledgement form
  across the Classroom folders.

---

## Your own list

- Claude for Teachers with the school email, after the weekend.
- Certiport under-18 parental consent forms.
- Then disconnect this machine and move to the school account.

## Google Drive reorganisation — done 4 Sep

My Drive root went from **57 folders + 100+ loose files** to **7 folders**.
The Classroom folder was left completely untouched, deliberately: it is
Google's, and moving anything inside it breaks the attachment links on live
assignments.

```
My Drive/
├─ BHR ENG 2026-2027 SY/            your folder, untouched
├─ Classroom/                       Google's, untouched
├─ BHR ENG Program/
│   ├─ Curriculum and standards/
│   ├─ Student document templates/
│   ├─ Branding and logos/          New Logo, Shop Banners
│   ├─ Equipment and software/      printers, VEX, UR5, Elegoo, CAD, laser…
│   ├─ Projects and lessons/
│   ├─ Program development — binders, pathway hubs, working files/   (was "here")
│   ├─ Website and print output (2026)/                          (was "htmls")
│   ├─ Shop Files/
│   └─ Shop Docs - Important/
├─ BHR ENG Administration/          budgets, EOY, advisory, open house,
│                                   Skills USA, meeting reports, grants
├─ BHR ENG Student Records — Restricted/
│                                   17 recommendation letters + 3 folders of
│                                   enrollment letters. Keep sharing tight.
├─ BHR ENG Archive/
│   ├─ Work PC backups (annual wipe)/   7 dumps, dated 2019–2023
│   ├─ Past projects and units/
│   ├─ PLTW (retired, not in use)/
│   └─ Photos and video/
└─ _to_delete/                      nothing deleted — review and empty yourself
```

**Two things found on the way that were not expected:**

1. The folder named `here` was not junk. It holds Binders 6, 7 and 8, the Independent Focus
   hub source directories, the Shop Equipment Approval List and the FY26
   budget. Renamed, not archived.
2. Three folders named `letters`, `Letters (1)` and
   `relettersforautodeskfreshmen` hold **student enrollment letters with names
   in the filenames**. They went to Student Records, not the archive.

**Still to do, by hand:** roughly 100 shortcuts to `model*.obj` / `model*.mtl`
/ `Alpha_Surface*.fbx` remain at the root. They came from two bulk shares on
9 May 2024 and point at someone else's files. Select them all in the browser
and drag them into `_to_delete` — five seconds there, a hundred API calls from
here.

**Also worth doing:** the contents of `Program development` span several
categories and could be distributed properly. Say the word.

## Student hand-in documents — done 4 Sep

Thirteen documents rebuilt in one house style and delivered to
`Teaching\student-docs\`: Daily Logbook, Weekly Planner, Weekly Reflection,
Project Reflection, Do Now! Reflection, Design Brief and Initial Planner,
Mid-Project Design Review, Instructor Meeting Notes, Independent Study Weekly
Journal, Field Trip Reflection, and three spreadsheets — Research Log, Order
Request Form, Project Gantt Chart. Plus a one-page "Which document, and when"
reference for the binder.

**Still to do by hand, because nothing is created in your Drive from here:**

1. Upload the thirteen files to Drive. Word and Excel convert to Docs and
   Sheets on upload, keeping headings, tables and drop-downs.
2. Repoint the Classroom assignments at the new copies.
3. **Retire `BHR ENG - Engineering Daily Journal`.** It and
   `BHR ENG Document - Logbook Template` were the same document under two
   names, both live in Class 28 at once. The Daily Logbook replaces both.
4. The four 3.36 MB templates can go. The replacements are 56 KB.

## Grade section — added 4 Sep, open items

- **Five Grade 12 briefs are still missing**, all behind Classroom "View more"
  controls: Festo MecLabs, Reverse Engineering (Breadboard), the Rube Goldberg
  Machine, Skills Revisited (AutoCAD), and the Holiday Ornament. They say so on
  the page rather than being padded out.
- **Missing words in three Grade 12 briefs.** LED Desk Lamp (8+ gaps, including
  most of the deliverables list), Post-Lecture Reflection (5), VEX AIM Bot (1).
  The gaps are in Classroom's own stored description, so students see them too.
  The source document was never found in Drive — worth a look through your
  Gemini or ChatGPT history for the original paste.
- **"View more" items** in both classes are still hidden. Every topic has them.
- **Grades 9 and 10** stop at the unit map by design, for Mr. Dryer to fill in.
- **Banners.** Cropped to the right-hand imagery on purpose: the AI-generated
  tablet on the left of every banner has invented labels that do not survive a
  close look ("AERODYNAMICS & COMPASS SITE SITE SITE PLANNING"). Regenerating
  the four banners cleanly would let the whole image be used.

## Full briefs — where they stand (4 Sep)

- **Grade 11: done.** All 21 entries carry a full brief are on the page, rendered from
  `PROJECT-INSTRUCTIONS-class27.md` by `brief_text.py` at build time. There is
  no second copy: re-harvest the file and the site follows. The Arduino codes
  and the Gmetrix join code are stripped on the way through, and every
  blockquote (my commentary to Dan) is dropped as non-student-facing.
- **Grade 12: done, bar five.** 13 of 18 entries carry a full brief from
  `PROJECT-INSTRUCTIONS-class26.md`. The five without are the "View more"
  items above.
- **Attachments and links** now have a home: a `links=[(label, url, what)]`
  field on any assignment renders a "Files and links" block. Five are seeded
  and verified. Drive files work the same way — share as "anyone with the
  link, viewer" first, and swap `/edit` for `/copy` for per-student templates.
- **Both harvests are now in one house format** — every brief opens with what
  you are making and why, then **What to do**, then **What you hand in**, and
  **Watch out for** where there is a real trap. Multi-week projects are one
  entry each, with their mid-project reviews and reflections folded in. Voice
  is neutral throughout; the old AI pep is gone.
- **Dropped**: Fusion 360 Animation, Client Desk Organizer and Bridge
  Conceptual Design Model existed only as reflection stubs with no brief
  anywhere. They are off the site. If they come back, they need a brief first.
- **Tiny House** now has a full brief, from the text you supplied.
