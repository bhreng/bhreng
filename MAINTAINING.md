# Maintaining this site

Everything here is plain HTML with no build step *required* — you can open
`index.html` and read it, and you can edit any page by hand. But most pages are
**generated**, so a hand edit is lost the next time anyone rebuilds. This file
says where each kind of content actually lives.

If you only read one thing: **the answer is almost always "edit a file in
`_source/`, then run `python3 build_site.py`".**

---

## The one rule

**No student data, ever.** No names, no rosters, no submitted work, no grades,
no photographs of students, no contact details. A public repository keeps every
file in its history permanently — deleting something later does not remove it.

Also never on this site: live class join codes, licence activation codes, and
anything from a Drive folder that is not shared to at least the whole school.

---

## Rebuilding

```
cd _source
python3 build_site.py          # writes the whole site
python3 check_site.py          # 0 broken links, 0 orphans expected
```

That is the entire toolchain. Python 3, no packages to install.

The build **refuses to finish** if the stylesheet loses one of the tokens the
page modules depend on. That guard exists because a silent no-op edit is how
this site broke twice: an edit that matches nothing changes nothing, and
nothing tells you. If you see `build: ... did not get stamped in`, a find and
replace missed — do not work around it.

Every page footer carries a build stamp in **school time**, so it matches what
Windows shows for the file. If the footer and the file's timestamp disagree,
you are looking at an old copy.

---

## Where to change what

| You want to change | Edit this |
|---|---|
| An assignment: title, deliverables, tools, note | `_source/grade_work.py` |
| The full text of an assignment brief | the harvest file, **not** the site |
| A link or attachment on an assignment | `links=[...]` in `_source/grade_work.py` |
| Unit names for a grade | `_source/grade_data.py` |
| A grade's colour | `_source/grade_data.py` |
| An instructor page | `_source/staff_data.py` |
| A Do Now or bonus task | `_source/extras_data.py` |
| The links shelf | `_source/extras_data.py` |
| A safety rule | `_source/safety_data.py` |
| An equipment safety question | `_source/equipment_data.py` |
| A training platform or credential | `_source/resources_data.py` |
| Pathway content | `_source/build_hubs.py` |
| The rail, and what appears in it | `_source/site_nav.py` |
| The grade / instructor pills in the top bar | `_source/quick_bar.py` |
| Colours, type, shared components | `assets/site.css` |
| Home page wording | `_source/build_site.py` |
| A student hand-in document | `_source/student_doc_data.py` |
| The house style of those documents | `_source/student_docs.py` |

`assets/site.css` is the one file that is **not** regenerated — the build keeps
it and stamps the font and module styles into it. Edit it directly.

---

## Adding an assignment

Open `_source/grade_work.py` and copy an existing entry. The fields:

```python
dict(t=2, w='Wk 3', title='Name of the thing', kind='project',
     hook='One sentence: what you actually make.',
     body=['A paragraph.', 'Another paragraph.'],
     gives=['What you hand in', 'And the next thing'],
     tool='Fusion 360, 3D printing',
     links=[('Label', 'https://example.org', 'What it is and why open it')],
     path='mechanical',
     note='Something worth knowing that is not in the brief.'),
```

- `t` is the term: `1`–`4`, or `'eoy'`, or `'always'`.
- `kind` is one of `project`, `skills`, `course`, `reflection`, `admin`.
- `path` links to a pathway page — use the key from `build_hubs.py`, or `''`.
- Everything except `title` and `kind` may be empty. An entry with a thin
  `body` is fine; **inventing content to fill it is not**. If Classroom has no
  brief, say so.

## Adding a link to an assignment

Same file, the `links=` field above. Three parts: label, URL, and what it is.

For a **Drive file**, share it as *anyone with the link — viewer* first. A link
nobody can open is worse than no link. For a template each student should get
their own copy of, replace everything from `/edit` onward in the URL with
`/copy` — note this only works from a link on this site, not from a Classroom
attachment.

**Check every link before you add it.** Half the value of the links page is
that everything on it works.

## Adding a full brief

Briefs are **not** stored in `grade_work.py`. They are parsed at build time out
of the harvest files by `_source/brief_text.py`, so there is exactly one copy
and re-harvesting updates the site automatically.

To add or change one:

1. Add a `## Heading` section to the right harvest file, in the house format
   above. Markdown bullets and tables both work.
2. In `brief_text.py`, map that heading to the `title` used in `grade_work.py`
   — `MAP_11` for Grade 11, `MAP_12` for Grade 12.
3. Rebuild. The brief appears with no other change.

Run `python3 brief_text.py` on its own to list what parsed and what is missing
before you rebuild.

Anything you write as a `> blockquote` in a harvest file is treated as a note
to yourself and is **stripped** — it never reaches a student. Use that for
"check this" comments.

---

## The student hand-in documents

The ten Word documents and three spreadsheets students fill in are built from
`_source/student_doc_data.py`:

```
python3 make_student_docs.py     # the thirteen documents
python3 make_docs_guide.py       # the "which document, when" reference
```

They are Word and Excel on purpose. Upload a `.docx` to Drive and Google turns
it into a Doc, and an `.xlsx` into a Sheet, keeping the headings, tables and
drop-downs. Everything else the shop hands out is a PDF, because nobody types
into it.

**Edit the data file, never the .docx** — the .docx is regenerated and your
change would vanish. Adding a section is one tuple: `('h', 'Heading')`, then
`('note', 'the italic guidance line')`, then `('box', 6)` for a fill-in area
or `('bul', [...])` for a list.

The Daily Logbook here replaces both the old `Logbook Template` and the
`Engineering Daily Journal`, which were the same instrument under two names
and were being distributed to the same class simultaneously.

---

## Publishing to GitHub

See `README.md` for the first-time setup. After that, updating is: rebuild,
then commit and push the whole folder. GitHub Pages redeploys on its own,
usually within a minute.

**Keep exactly one working copy.** Two folders of a site that changes several
times a day is how the wrong version gets published. If you make a copy to
experiment with, name it so you cannot mistake it for the real one.

---

## How the briefs are written

Both harvest files follow one house format, and anything added to them should
match it:

```
## Term X Week Y — Title

One or two sentences: what you are making and why.

**What to do**
- ...

**What you hand in**
- ...

**Watch out for**      (only where there is something real to warn about)
```

Three rules that matter more than the format:

1. **One heading per project.** A project that ran three weeks is one entry,
   not three. Its mid-project review and its reflection are folded in as
   sections. Classroom is week-by-week because that is how it is taught; a
   student looking something up in June does not remember which week it was.
2. **Neutral voice.** No pep, no "welcome back", no AI throat-clearing.
3. **Every brief states what you hand in.** Where a deliverable was implied by
   the original post but never written down, it is written out — and the
   addition is recorded in the teacher notes at the foot of the harvest file.

## Things that are deliberately unfinished

- **Grades 9 and 10** stop at the unit map on purpose. They are Mr. Dryer's to
  fill in, the same way Grades 11 and 12 were filled in.
- **Five Grade 12 items have no brief**, because they sit behind a Classroom
  "View more" control that could not be opened: Festo MecLabs, Reverse
  Engineering (Breadboard), the Rube Goldberg Machine, Skills Revisited
  (AutoCAD), and the Holiday Ornament. They say so rather than inventing one.
- **Words are missing from three Grade 12 briefs** in Classroom itself — the
  LED Desk Lamp worst of all, where most of the deliverables list is gone. The
  site shows a warning banner wherever `[…]` appears. The document these were
  pasted from was never found.
- **A QR-code poster** for the shop wall, waiting on a real published URL.
- Every Classroom topic hides older items behind **View more**; neither harvest
  includes those.

---

## What has been checked, so you know what not to redo

- Every colour on the site clears **WCAG AA (4.5:1)** in both light and dark
  themes, including the four grade colours and both instructor colours. The
  tightest is 4.74:1.
- Every page has exactly one `<h1>` and no heading-level jumps.
- Every page passes a no-horizontal-overflow check at 360, 390, 768 and
  1280 px, in both themes, with no console errors.
- The equipment safety questions were audited: 52 questions, 9 checks, exactly
  one correct answer each, an explanation on every option, no duplicates.
- Every external link on the links page was opened and checked.
- A collapsed brief still prints in full; the site's navigation does not print.
