# Dropdowns and collapsing — why you can't see them, and the fix

**The files are correct.** I checked the copy on your machine: the logbook has
4 Heading 2 sections, 11 Heading 4 labels and 3 real dropdown controls. Nothing
is missing from the file. Both of the things you're looking for are Google Docs
features that behave differently than you'd expect on an imported `.docx`.

---

## 1. Collapsing — one setting, takes five seconds

Google Docs only shows the collapse arrows in **Pageless** view. In the default
Pages view the headings are still headings, but there are no carets to click.

> **File → Page setup → Pageless → OK**
> (tick "Set as default" if you want it for everything)

The arrows appear immediately, next to every `INTERVAL` heading. Your original
logbook was authored in Pageless, which is why it had them.

This works on the file as it is. Nothing needs rebuilding.

---

## 2. Dropdowns — these genuinely cannot survive the trip

Google Docs dropdown chips are a Docs-native object. There is **no way to
create one from a `.docx` file** — Docs has no importer for Word's dropdown
controls, so on upload it flattens each one to its default value as plain text.
That's why every default in my files is a real, sensible option rather than a
blank: a flattened copy still reads correctly.

So the dropdowns have to be added once, in Docs, by hand. The good news is
**once only** — a Doc's dropdowns survive "Make a copy", so every student copy
made from the master inherits them.

### How to add one

1. Open the master Doc, put the cursor where the value should sit.
2. **Insert → Dropdown → New dropdown.**
3. Name it, add the options, give each one a colour.
4. Save. Copy/paste that chip to the other places it's needed.

### What to create, and where

**Daily Logbook** — one dropdown, reused three times (Interval 1, 2, 3).
Name it `EDP status`:

| Option | Suggested colour |
|---|---|
| PI — Problem identification / research | blue |
| DD — Detailed design (CAD / modelling) | amber |
| FAB — Fabrication & development | green |
| TE — Testing & evaluation | red |
| IR — Improve & redesign | purple |

**Do Now Reflection** — `Confidence level`, replacing the text after
"Confidence level:"

- Not yet · Only with help · On my own · I could teach it

**Mid-Project Design Review** — `Phase of project`, replacing the text after
"Phase of project:"

- Planning · Design · Development · Testing · Refinement

That's three dropdowns total across the whole set. Maybe ten minutes once.

---

## The bigger question: where do these templates live?

Two options, and it's worth deciding before you distribute anything.

**A — Google Docs masters (what you did before).** Upload each `.docx`, let
Drive convert it, add the three dropdowns, set Pageless. Those Docs become the
masters Classroom hands out. Students get dropdowns and collapsing. The cost is
that when I change a template you re-upload and re-add the dropdowns.

**B — keep them as `.docx` downloads from the site.** No dropdowns, no
setup, always current, and students who open them in Word do get both features
— Word supports the dropdown controls and collapses headings natively.

**My read: A for the logbook, B for everything else.** The logbook is the one
students live in daily and the one where the dropdown genuinely speeds them up.
The other eleven are opened, filled and handed in once, and the dropdown is a
nicety there rather than a workflow.

If you want A, say the word and I'll write out the exact upload-and-convert
steps — I'm not creating anything in your Drive without you asking, per the
rule we set.
