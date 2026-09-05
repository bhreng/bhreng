# Google Drive Reorganization Plan

**2 September 2026** · Based on a survey of ~100 folders and ~100 recent files via the Drive connector. Not a complete inventory — Apps Script is blocked, so no full index exists — but enough to see the structure and the problems.

---

## First, a correction

Earlier I said your files looked like they were in a **Shared Drive**, based on parent IDs beginning `0A`, and warned that the organization might own them. **That looks wrong.** Every file comes back with `owner: dfrank@bluehills.org`, and the Drive API generally doesn't report an owner that way for Shared Drive content. These read as **My Drive** files that you own.

That's good news, and it changes the durability picture: you *can* copy and download them freely. Takeout being blocked is an administrative choice, not an ownership problem.

---

## What your Drive actually looks like

Two distinct top-level areas:

**1. Your own material** (parent `0ANT1lRc3Pf4lUk9PVA` — My Drive root)
Largely flat. Program documents, binders, standards files, shop materials, and a lot of loose folders all sitting at the top level together.

**2. A Classroom-managed area** (parent `0B9T1lRc3Pf4l...`)
This holds the folders Google Classroom creates automatically — `Eng IV S.Y. 24-25 12`, `Engineering IV - Class 27 12`, `Pathway Hub - Industrial Design BHR ENG`, and so on.

> ### ⚠ Do not reorganize the Classroom area
>
> Google Classroom creates and manages those folders itself. Renaming or restructuring them invites Classroom to recreate folders, produce duplicates, or lose track of where new attachments land. Leave that whole branch alone — it isn't the mess, and touching it is the one move here that could actually break something live.
>
> Everything below applies **only** to your own material.

---

## What's cluttering it

**Two full copies of a Fusion 360 tutorial library.** `Edition 1. Mastering Fusion 360` and `Edition 2 Mastering Fusion 360`, both created within a minute of each other on 12 March 2025. Each carries a dozen chapter folders, each of those holding project subfolders — Edison Bulb, American Football, Tesla Turbine, Saturn V, Carabiner, and so on. Between them these account for a large share of every folder I saw.

They're genuinely different editions with different chapter numbering, so this may be intentional. But if Edition 2 supersedes Edition 1, that's an enormous amount of structure to retire in one move.

**Legacy PLTW material.** `HS 2016 PLTW` → `DE2016`, `CIM2016` → unit and student folders. Dated 2023, referencing a 2016 curriculum. Squarely pre-cutoff.

**Course-unit trees from the old structure.** `BHR Enginering Breakdown` *(note the typo)* → `Engineering IV` → `Unit 1 – Review and Preparation`, `Unit 2 – Shop Equipment`, … `Unit 6 – Year end Wrap-Up`, plus parallel trees for the other grades. Created April 2024 — just before the cutoff, and superseded by the rebuild.

**Obvious junk.** `sfdhgjk` (a keyboard-mash folder from March 2025). `?????Copy of Engineering III S.Y. 22-23 11th`.

**Terminology drift in the folders too.** `Unit - Independent Study` appears in several trees — the term retired in favour of the Independent Focus

---

## The plan

### Step 1 — Create the target structure

Six folders at the top of My Drive. Nothing else lives at root.

```
BHR ENG — Program          Binder, standards, crosswalks, program reports
BHR ENG — Pathway Hubs      Hub guides, source directories, migration tables
BHR ENG — Curriculum       Current unit and lesson material, by grade
BHR ENG — Templates        Logbook, reflections, rubrics, forms
BHR ENG — Shop             Safety docs, banners, logos, equipment, open house
_ARCHIVE                   Everything superseded. Nothing deleted, ever.
```

The `_` prefix on Archive sorts it to the bottom and out of the way.

### Step 2 — Bulk archive by date

This is the step that does the most work for the least effort, and it needs no script. In the Drive search bar:

```
owner:me before:2024-09-01
```

Drive supports `before:` and `after:` on modified date. That returns everything of yours untouched since the cutoff. Then:

1. Click the first result, scroll to the bottom, **Shift+click** the last to select the range
2. Right-click → **Organize** → **Move**
3. Choose `_ARCHIVE`

**Work in batches of a few hundred.** Drive gets unreliable moving thousands at once, and a stalled move is harder to reason about than three clean ones.

**Before moving, spot-check the results** for anything still live — a template you use every year, a reference doc you haven't edited but still open. Last-modified is a good proxy for "superseded," not a perfect one.

### Step 3 — Retire the obvious clutter

Move to `_ARCHIVE`: `HS 2016 PLTW`, `BHR Enginering Breakdown` and its unit trees, `sfdhgjk`, `?????Copy of Engineering III S.Y. 22-23 11th`, and — **if you confirm Edition 2 supersedes it** — `Edition 1. Mastering Fusion 360`.

That last one is the single biggest structural win available. Worth checking before you move it.

### Step 4 — File what remains

What survives the date sweep is your live corpus. It should be small enough to sort by hand into the five program folders.

### Step 5 — Then download

Once organized, select each top-level folder in the browser → right-click → **Download**. Google zips it and converts Docs to `.docx`, **preserving formatting** — highlight colours, hyperlinks, images, tables. That's the backup, and it's better than anything the connector can produce.

Do `_ARCHIVE` too if you want it, but do the five live folders first.

---

## Why this order

Reorganizing first means the download mirrors a structure that makes sense, rather than reproducing the mess on your hard drive. And the date sweep does most of the work before you have to make a single judgment call.

---

## Two things worth confirming before you start

1. **Does Edition 2 of Mastering Fusion 360 supersede Edition 1?** Retiring one removes a large fraction of the folder clutter in a single move.
2. **Is anything you still use sitting untouched since before Sept 2024?** Templates and reference documents are the usual culprits — they get used constantly but rarely edited, so a last-modified sweep catches them unfairly.

## What I can't do from here

Apps Script being blocked means no automated duplicate report across your whole Drive. What I *can* do, if it would help: enumerate a specific folder through the connector and flag same-name/same-size files within it. Slower and narrower than a script, but useful for a folder you suspect is full of copies.
