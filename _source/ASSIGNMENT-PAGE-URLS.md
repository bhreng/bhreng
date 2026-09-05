# Assignment page URLs

Every assignment now has its own page. Paste these into Classroom, an email,
or behind a QR code. Add the site root in front, e.g.
`https://<your-site>/work/11-city-design.html`.

Slugs are stable. If you rename an assignment, tell me and I add the old slug
to `SLUG_OVERRIDE` in `work_pages.py` so links you already sent keep working.


## Grade 11 — Engineering III

| Term | When | Assignment | Page |
|---|---|---|---|
| Term 1 | Wk 1 | Speaker Design | `work/11-speaker-design.html` |
| Term 1 | Wk 2 | Roles of an Engineer | `work/11-roles-of-an-engineer.html` |
| Term 1 | Wk 2&ndash;4 | Full Scope Project | `work/11-full-scope-project.html` |
| Term 1 | Wk 3 | Tiny House | `work/11-tiny-house.html` |
| Term 2 | Wk 1 | ADU Design Project | `work/11-adu-design-project.html` |
| Term 2 | Wk 2 | Intro to ESEC: Arduino | `work/11-intro-to-esec-arduino.html` |
| Term 2 | Wk 3 | VEX V5 Clawbot Project | `work/11-vex-v5-clawbot-project.html` |
| Term 2 | Wk 3 | Intro to CorelDraw | `work/11-intro-to-coreldraw.html` |
| Term 2 | Wk 4 | Simple Machines to Functional Mechanisms | `work/11-simple-machines-to-functional-mechanisms.html` |
| Term 2 | Wk 5 | Robotic Arm Build | `work/11-robotic-arm-build.html` |
| Term 2 | Wk 5 | Elegoo Uno Project Kit | `work/11-elegoo-uno-project-kit.html` |
| Term 3 | Wk 2 | Creative Concept Design | `work/11-creative-concept-design.html` |
| Term 3 | Wk 3&ndash;4 | City Design | `work/11-city-design.html` |
| Term 3 | Wk 4 | Learning Revit! | `work/11-learning-revit.html` |
| Term 4 | Wk 1 | Famous Architect Presentation | `work/11-famous-architect-presentation.html` |
| Term 4 | Wk 3 | Fusion Review: Drawings and Stress Simulations | `work/11-fusion-review-drawings-and-stress-simulations.html` |
| Term 4 | Wk 5 | The End-of-Year Vibecoding Team Challenge | `work/11-the-end-of-year-vibecoding-team-challenge.html` |
| End of year | Capstone | Grade 11 Capstone | `work/11-grade-11-capstone.html` |
| End of year | Final | Reflection Portfolio Presentation | `work/11-reflection-portfolio-presentation.html` |
| End of year | Final | Gmetrix | `work/11-gmetrix.html` |
| Running all year | All year | Independent Focus | `work/11-independent-focus.html` |

## Grade 12 — Engineering IV

| Term | When | Assignment | Page |
|---|---|---|---|
| Term 1 | Wk 1 | Design a Laptop | `work/12-design-a-laptop.html` |
| Term 1 | Wk 2&ndash;5 | Shop Equipment Project | `work/12-shop-equipment-project.html` |
| Term 1 | Wk 2 | Festo MecLabs: Exploring Mechatronics | `work/12-festo-meclabs-exploring-mechatronics.html` |
| Term 1 | Wk 2 | Reverse Engineering: Breadboard Circuit Practice | `work/12-reverse-engineering-breadboard-circuit-practice.html` |
| Term 1 | Wk 5 | Post-Lecture Reflection: Theory of the Week | `work/12-post-lecture-reflection-theory-of-the-week.html` |
| Term 2 | Wk 1 | Industrial Design Challenge: The LED Desk Lamp | `work/12-industrial-design-challenge-the-led-desk-lamp.html` |
| Term 2 | Wk 2 | Holiday Collaborative Rube Goldberg Machine | `work/12-holiday-collaborative-rube-goldberg-machine.html` |
| Term 2 | Wk 2 | Skills Revisited: AutoCAD Drawings and Title Blocks | `work/12-skills-revisited-autocad-drawings-and-title-blocks.html` |
| Term 2 | Wk 2 | Research &amp; Analysis: LTT Screwdriver | `work/12-research-and-analysis-ltt-screwdriver.html` |
| Term 2 | Wk 2 | Try Again! Moon Base 2.0 | `work/12-try-again-moon-base-2-0.html` |
| Term 2 | Wk 3 | Intro to CorelDraw | `work/12-intro-to-coreldraw.html` |
| Term 2 | Wk 3 | VEX Robotics | `work/12-vex-robotics.html` |
| Term 2 | Wk 4 | Holiday Ornament | `work/12-holiday-ornament.html` |
| Term 2 | Wk 5 | Mars Colony Design | `work/12-mars-colony-design.html` |
| Term 2 | Wk 5 | Bunker House Design | `work/12-bunker-house-design.html` |
| Term 3 | Term 2 Wk 5 &rarr; Term 4 | Senior Capstone | `work/12-senior-capstone.html` |
| Running all year | All year | Independent Focus | `work/12-independent-focus.html` |
| Running all year | All year | Platform training | `work/12-platform-training.html` |

## Downloadable files

Everything in `attachments/` is published to `files/` and is linkable directly:

- `files/BHR-ENG-Daily-Logbook.docx` — Daily Logbook
- `files/BHR-ENG-Design-Brief-and-Initial-Planner.docx` — Design Brief and Initial Planner
- `files/BHR-ENG-Do-Now-Reflection.docx` — Do Now Reflection
- `files/BHR-ENG-Instructor-Meeting-Notes.docx` — Instructor Meeting Notes
- `files/BHR-ENG-Mid-Project-Design-Review.docx` — Mid-Project Design Review
- `files/BHR-ENG-Order-Request-Form.xlsx` — Order Request Form
- `files/BHR-ENG-Part-List.xlsx` — Part List
- `files/BHR-ENG-Project-Gantt-Chart.xlsx` — Project Gantt Chart
- `files/BHR-ENG-Project-Reflection.docx` — Project Reflection
- `files/BHR-ENG-Research-Log.xlsx` — Research Log
- `files/BHR-ENG-Weekly-Planner.docx` — Weekly Planner
- `files/BHR-ENG-Weekly-Reflection.docx` — Weekly Reflection
- `files/BHR-ENG-Which-Document-When.pdf` — Which document, and when

## Attaching a file to an assignment

Two steps, in `work_pages.py`:

1. Drop the file into `attachments/`. Add a line to `FILE_INFO` giving it a
   label and one line of description.
2. In `ATTACH`, under the grade, add the assignment title and the list of
   filenames:

```python
ATTACH = {
    '11': {
        'City Design': ['BHR-ENG-Design-Brief-and-Initial-Planner.docx',
                        'BHR-ENG-Daily-Logbook.docx'],
    },
}
```

Any assignment not listed in `ATTACH` gets `DEFAULT_ATTACH`, which is
currently just the Daily Logbook. A declared file that is missing from
`attachments/` is reported by the build and skipped, never linked.
