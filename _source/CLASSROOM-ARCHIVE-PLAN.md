# Classroom Archive — Why This First, and How

**The thing you actually survive on has no export button.**

Google Classroom coursework — assignment prompts, descriptions, topic structure, which file attaches to which assignment — exists in one place, in an account the district controls. Takeout doesn't meaningfully cover it. There is no "download this course." Copy a course year over year and you're copying within the same account; the whole chain has one point of failure.

Two years of refined prompts is the work. The Drive files are the raw material; the coursework is what turns them into a course.

---

## What this changes about the Drive question

You were weighing "port out what's needed" against "reorganize Drive first." **The Classroom archive answers which files are needed**, because every assignment names its attachments.

Run the archiver and you get a `Files To Back Up` sheet: the unique Drive files your coursework actually depends on, ranked by how often they're attached. That's the shortlist. Everything else in Drive is optional by comparison — and given what you've said about scope, quite a lot of it is disposable.

That inverts the problem in a useful way. Instead of sifting thousands of files hoping to spot what matters, the courses tell you.

---

## Setup — about five minutes

1. New blank Google Sheet, named something like `BHR Classroom Archive`.
2. **Extensions → Apps Script**, delete the placeholder code, paste in `ClassroomArchiver.gs`.
3. **Services (+) → Google Classroom API → v1 → Add.** Required; without it nothing runs.
4. Save, reload the sheet. A **Classroom Archive** menu appears.
5. **1. List my courses** — lists every active course with an `Archive?` column. Set any to `NO` to skip them.
6. **2. Archive all active courses.** If it pauses at the 6-minute limit, run **2b. Continue**.
7. **Export attachment file list** when it finishes.

There's a separate menu item for **archived** courses. Worth running — prior years' courses are where the earlier prompt versions live, and archived courses are exactly the ones most likely to be cleaned up by an administrator without warning.

---

## What it captures

Per course: metadata, topics and their names, every assignment and question and material post with its **full description text**, topic, state, due date, points, and creation/update dates. Every attachment — Drive files with their IDs, links, YouTube videos, Forms. Every announcement.

**What it deliberately does not touch:** students, rosters, submissions, grades, guardians. Nothing student-identifying is read or written. This is course design only, which is both the privacy line we agreed and the reason this is safe to keep on your own machine.

---

## The part that makes it worth doing

An archive you can't restore from is a museum piece.

The `Coursework` sheet is shaped to match what the **Classroom Builder** — the script already built and tested last session — publishes from. Course, type, title, description, topic, state, due date, points. So this isn't only a backup: it's a rebuild path. If the account goes away, these sheets plus the builder reconstruct the courses somewhere else.

That's also why it's worth running *before* any reorganizing. It's a snapshot of a working system taken while the system still works.

---

## Suggested order

1. **Run the Classroom archiver.** Active courses, then archived ones.
2. **Export the attachment list** — that's your Drive shortlist.
3. **Run the Drive indexer** — now mainly to catch material that *isn't* attached to coursework but still matters: the binder, standards documents, templates, hub guides.
4. **Pull down the shortlist plus the binder set** into Teaching, organized.
5. *Then* decide about reorganizing Drive, with the safety net already in place.

Step 4 is where a decision is still needed: Google Docs have to be converted to be useful offline — `.docx`, `.pdf`, or Markdown. Docs and Sheets export cleanly; Slides less so. Worth talking through once we see how many files are on the list.

---

## Scope, as I understand it

**The cutoff applies to Drive, not to Classroom.** These are different problems and they need different rules.

| | Rule |
|---|---|
| **Drive files** | **Sept 2024 onward.** Earlier material is separately backed up and superseded by the rebuild. |
| **Classroom courses** | **All years. No cutoff.** |
| Files owned by other `@bluehills.org` accounts | Excluded everywhere — colleagues' and students'. |

**Why Classroom gets no cutoff.** You currently teach Grades 11 and 12. You taught Grades 9 and 10 several years ago, and those lessons exist only in courses from that period. The binder's Section 6 describes the Grade 9 and 10 curriculum in detail — units, emphases, end-of-year projects — but the lessons behind that description live in old courses, nowhere else.

Those are also the most fragile things in the account: archived, years old, unlikely to be missed by anyone but you if they were cleaned up.

So: run **Archive ARCHIVED courses too** and take everything the API returns. The script writes structure only — no files, no student data — so an old course costs a few hundred spreadsheet rows. There is no reason to be selective.

**Run "1. List my courses" first as a survivability check.** The list itself is diagnostic: if a course you remember teaching isn't there, it's already gone, and better to discover that now than the day you need it. Course names carry their year (`Engineering I – 2026`, `Eng. II 2025–2026`), with the `Created` column as backstop.

### ⚠ The co-teacher gap

The script lists courses where **you** are a teacher (`teacherId: 'me'`). Mr. Dryer currently teaches Grades 9 and 10. If those courses are his and you are not added as a co-teacher, **they will not appear in the list** — and that is the last two years of lower-grade curriculum missing from the archive.

Your own older Grade 9 and 10 courses, from when you taught them, will archive normally. It's the recent ones that are at risk.

**Check for this at step 1.** If the list comes back with only Grades 11 and 12 for 2024–25 and 2025–26, the gap is real. Two ways to close it:

1. **You get added as a co-teacher** on his courses — then re-run step 1 and they appear. Simplest, and reasonable given you're lead teacher for all four years.
2. **Mr. Dryer runs the same script** on his account and you keep both spreadsheets. Better if you'd rather not alter course permissions mid-year.

Either way, this is course design — assignment prompts, topics, attachments. No student data is read in the process, which is worth saying plainly if you're asking a colleague to run it.
