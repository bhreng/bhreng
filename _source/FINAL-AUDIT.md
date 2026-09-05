# Final audit — 05 September 2026

Three passes over everything: the binder, the student documents, the HTML
reports, the site builders and the 81 built pages. One for retired words, one
for facts that disagreed with each other, one for things a document said
existed that did not. What follows is what was found, what was fixed, what was
built, and what is yours to decide.

---

## 1. What the audit found

### Terminology — ~180 live hits, almost all in the binder generation

The site itself was nearly clean; the binder files on your machine were a
stale generation that still said E.E.P. in forty places and "notebook" or
"journal" in thirty. The glossary — the document whose whole job is to be the
single source for terms — still listed "Elective Engineering Pathway" as the
*current* term.

| Retired | Hits | Current |
|---|---|---|
| E.E.P. / Elective Engineering Pathway | 70 | Independent Focus |
| Independent Study | 26 | Independent Focus |
| notebook / journal (as the instrument) | ~60 | Daily Logbook |
| "went wrong" / "failures forced" | 11 | what the results told you to change |
| "juniors and seniors" (for exploratory 9th graders) | 3 | upperclassmen |
| SolidWorks / CSWA | 1 | struck; Autodesk only |
| PLTW | 2 | removed |
| "nine shops" | 2 (search index) | eighteen shops, nine week-long visits |
| Grade 9 "visiting" framing | 0 | already gone |
| Prices, live codes | 0 | none present |

### Facts — nine real contradictions

| Fact | Was | Now |
|---|---|---|
| Grade 9 exploratory | Binder: "ten-week cycle, one program per week". Site: two mini days, 18 shops, nine visits | Both say the second, which is yours |
| When the Independent Focus ends | Grade 12 page said "All year" with end-of-year reflections | Terms 1–2; stops when the capstone starts; may or may not become it |
| Who does the Independent Focus | Hub reports: "juniors and seniors" / "upper-year" | Every student in the shop |
| OSHA 10 | Hub page: a prerequisite — "nothing in a hub happens without it" | Earned in Grade 10 by every student in the school; the credential behind machine authorisation, not a gate on a Grade 9's focus |
| Closed-toe shoes | Welcome page: "in the Makerspace" | Everywhere in the shop, every day |
| Instructor names | Binder: "D. Frank", "M. Dryer" | Mr. Frank, Mr. Dryer |
| Logbook status codes | Hub report mixed EDP codes with pillar codes ("AL") | One scheme: PI, DD, FAB, TE, IR |
| Automation hub | Hub report: "Empty" | Authored in full; the report now says so |
| Grade 9 unit count | Binder: eight. Site: six | **Not a contradiction** — the site lists the EDF units only; the binder's eight include Mr. Dryer's two ESEC units. Both now say so. |

### Holes — the big one

**Eleven finished templates were on the web root and wired to nothing.** The
routing table that decides which downloads appear on which assignment page was
empty, so every one of the 39 assignment pages offered the logbook and nothing
else. The "Get the Files" lists on all seven pathway hubs named nineteen
documents, thirteen of which did not exist, and rendered all of them as plain
text — not one was a link, including the six that named files sitting two
directories away.

The *Which document, and when* guide — built specifically because nothing said
which document to fill in on a Monday — was itself reachable from nowhere.

The most-referenced missing document in the whole corpus (17 places) was the
Independent Focus term-end reflection, which the binder specifies field by
field and which one working document claimed already existed.

---

## 2. What was built

| New | What it is |
|---|---|
| **Independent Focus Proposal** (.docx) | First day of the term, handed in for review: pathway, the idea, the research and build, tools and training, one goal per shop week, what done looks like, what could stop it, and an instructor review box. |
| **Independent Focus Reflection** (.docx) | Last day of the term, stands alone: the binder's specified fields (equipment, tasks, skills, status, progress against the proposal, challenges and adaptations, project management, goals for next term). |
| **Project Rubric** and **Weekly Grade Rubric** (.xlsx + .pdf) | Dan's Classroom exports with every level written out, in Classroom's exact cell layout for re-import, plus student-facing PDFs. |
| **Independent Focus Record** (.pdf) | One page for the binder. Six term rows plus a capstone row with "grew out of a focus term? yes / no". |
| **Decision Matrix** (.xlsx) | Weighted criteria against up to four concepts; `SUMPRODUCT` totals. Referenced by two hubs, existed nowhere. |
| **Test and Measurement Log** (.xlsx) | Predicted, measured, difference, "what the difference tells you to change". One instrument for mechanical test data, electrical measurements and automation cycle times, which had been named three different ways. |
| **I/O Map and Commissioning Checklist** (.xlsx) | Two tabs. Automation was the only pathway marked new and had no documents. |
| **The complete binder** (.pdf) | Sections 1–8 and the Word List in one document, draft scaffolding removed to a separate Editorial Notes PDF. |
| **The teacher and admin set** (9 .pdf) | Binder, editorial notes, both pathway reports, the Independent Focus position, the Google Docs setup, this audit, the assignment URL list and the maintenance guide — one rendering path, one look, none of it on the student site. |
| **The BHR27 generation tag** | Every built document is named `BHR27-…` and carries `BHR27 · rev 05 Sep 2026` inside it, so a Drive search for BHR27 returns only the current forms. One constant in `generation.py` re-stamps the whole set next year. |
| **Documents page** on the site | Every template grouped by when you reach for it, the guide on top, all 18 posters underneath. Linked from the home page, the logbook page, the Families page and the nav. |
| **Families page** on the site | Built earlier this session; confirmed wired. |

Dropped rather than built, with the reference reworded to point at what
covers it: schematic template (drawn in the tool), as-built drawing set (a
deliverable, not a template), flowchart and truth-table templates (CircuitVerse
does it), sheet-set title block (lives in the CAD templates), FEA report
(covered by the Test Log), site design checklist (covered by the Design Brief's
criteria and constraints), WBS template (the Gantt's WBS column), Bill of
Materials worksheet (it is the Part List and the Order Request Form), code
comment standard (not a fill-in document — noted below as yours).

---

## 3. What was fixed

- All 39 assignment pages now offer the right documents. Defaults by kind (a project gets the Design Brief and the Project Reflection; a skills session gets the Do Now Reflection), with per-assignment overrides — the LED Desk Lamp gets the Decision Matrix, Part List and Test Log; the capstones get the full planning set; both Independent Focus entries get the Proposal, the Reflection and the Record; every project gets the Project Rubric first. **These are sensible defaults, not a teaching decision** — `work_pages.py`, `ATTACH`, retune freely.
- Every "Get the Files" item on the seven hubs is now a real download or a real page.
- The logbook page's footer pointed at "the Logbook Template in Google Classroom"; it now downloads the Daily Logbook and links the Documents page.
- Harvested Classroom briefs that told students to keep a "Daily Journal Log" now say Daily Logbook, and the page's note says retired names were updated. The wording is otherwise still Classroom's.
- The "NOTEBOOK" wall poster is now the "LOGBOOK" poster.
- The resources page names CareerSafe as the OSHA 10 route, which appeared nowhere before.
- The four binder HTML files and five binder markdown files on your machine are replaced with swept, corrected versions.
- `EEP-TERM-STRUCTURE-PROPOSAL.md` (v1–v4) is retired to `_to_delete/`; `INDEPENDENT-FOCUS-STRUCTURE.md` states the current position in one page.
- `student-docs/README.md` had stale counts; regenerated from the folder.
- The guide is back to one page with the five new documents on it.

---

## 4. Yours to decide

These are real gaps the audit surfaced that I did not fill, because each is a
teaching decision.

1. ~~**Per-project rubrics.**~~ **Closed, 05 Sep.** It turned out there is one project rubric used on every project, and one weekly-grade rubric — both Classroom exports. Both are rebuilt with every level written out (the weekly grade's four lower levels were placeholders), kept in Classroom's exact cell layout so they import straight back, and rendered as student-facing PDFs. Every project assignment page now offers the Project Rubric first; *How this class works* links both. The line "each project has its own rubric" was wrong and is fixed.
2. **Code comment and documentation standard** for the Software pathway. Named in the hub, does not exist, and it is a rule sheet rather than a template — three or four rules in your voice. Ten minutes.
3. **The Autodesk certification consent form.** The resources page tells under-18 students to "get the consent form signed early in the year" and nothing says which form. If it is Certiport's own, name it and link it; if it is yours, it needs writing.
4. **Independent Focus outputs and time in the week.** Both still open by your choice. The Term Sheet does not depend on either.
5. ~~**Binder Sections 7 and 8.**~~ **Closed.** Both pulled from Drive and bound in. Section 7's retired names and its CSWA claim corrected; Section 8 is the state framework verbatim, with a note that the grade-level highlighting lives in the Drive original. The complete binder is one PDF, Sections 1–8 plus the Word List, in `Teacher & Admin/`.
6. ~~**The Grade 12 unit count.**~~ **Closed.** Confirmed from Section 6: the fifth unit is *Robotics and Automation* (ESEC). Same EDF/ESEC split as Grade 9; the site lists EDF units and now says so.

---

## 5. Verification

- Site: 81 pages, 0 broken links, 0 orphans.
- Retired-term sweep of every built page and asset: clean.
- Every `.docx` checked for retired terms: clean.
- Every file the hubs, the assignment pages, the Documents page and the Families page link to: exists.
- Binder HTML on your machine: identical to the corrected versions here.
