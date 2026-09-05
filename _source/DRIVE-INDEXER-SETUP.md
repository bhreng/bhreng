# Drive Indexer — Setup and What It Tells You

**Purpose:** a complete inventory of what's actually in your Drive, so decisions about what to keep, what to archive, and what to pull onto your machine are made from data rather than guesswork.

This is the step both of your options need. You can't choose what to port out without knowing what's there, and you can't reorganize safely without knowing what's duplicated.

---

## Why Apps Script and not the Drive connector

Three reasons, and the third is the one that matters most right now.

1. It runs **as you, inside Google**. No third-party OAuth token to expire mid-job.
2. It's fast — thousands of files in a few minutes, versus hundreds of connector calls.
3. **It can see Shared Drive content.** If your files really are in a Shared Drive, this is the difference between a complete inventory and a badly incomplete one. Google Takeout has the same blind spot.

---

## Setup — about five minutes

1. Create a **new blank Google Sheet**. Name it something like `BHR Drive Index`.
   *(This is one new file in Drive. It's the only Drive write involved, and it creates nothing else and modifies nothing existing. If you'd rather have zero Drive writes, say so and I'll rework it to email you a CSV instead.)*
2. **Extensions → Apps Script**
3. Delete the placeholder `myFunction` code.
4. Paste in the whole of `DriveIndexer.gs`.
5. In the left sidebar click **Services (+)**, find **Drive API**, set version to **v3**, click **Add**.
   *This step is required. Without it the script cannot see Shared Drives and will fail on the first call.*
6. **Save** (disk icon).
7. Reload the spreadsheet. A **Drive Index** menu appears next to Help.
8. **Drive Index → 1. Start fresh index.** Google will ask you to authorize — it's your own script asking for your own Drive, and the warning screen about an "unverified app" is expected. Review → Advanced → Go to project.

If it stops with "Paused at N files," that's the normal 6-minute execution limit. Choose **2. Continue** and it picks up exactly where it left off. Repeat until it says Done.

Then run **Find possible duplicates** and **Build summary**.

---

## What you get

**`Drive Index`** — one row per file: name, type, size, created, last modified, owner, My Drive vs Shared Drive, which Shared Drive, full folder path, link, and file ID.

**`Possible Duplicates`** — every filename appearing more than once, flagged **"YES — likely identical"** when the copies also share a byte size. This is where the seven collisions I found by hand turn into a complete list. Expect the logbook template copies to dominate; those are Classroom distribution artifacts, not mistakes.

**`Summary`** — totals by location, type, year last modified, and owner.

---

## The three things to look at first

**1. Location.** The My Drive versus Shared Drive split. This is the question I couldn't answer from the connector, and it determines your options:

- Mostly **My Drive** → you own the files. Takeout works, copying out works, you have real control.
- Mostly **Shared Drive** → the *organization* owns them. Takeout won't export them, copying out may be blocked, and access ends with membership. That makes a local mirror considerably more urgent.

**2. By Owner.** Anything not owned by `dfrank@bluehills.org` is a colleague's file or student work. This matters twice over: it tells us what isn't yours to reorganize, and it keeps student material out of scope. Filter these out before we plan anything.

**3. By Year Last Modified.** This should show the eras cleanly — the 2019–2024 original work, the autumn 2025 standards-and-Dryer push, the January 2026 binder consolidation, the May–June 2026 E.E.P. layer. Anything untouched since 2022 is an archive candidate.

---

## After it runs

Export the `Drive Index` sheet as CSV into your Teaching folder and I can work from it directly — no connector paging, no guessing at what exists. From there:

- **If you lean toward the local canonical copy:** we pick the source-of-truth documents from the index and pull just those down, organized properly.
- **If you lean toward restructuring Drive:** the duplicates sheet gives us the cleanup list, and the folder paths show what structure already exists to build on.

The index is worth having either way, and it stays useful — the Classroom Builder spreadsheet reads the same kind of data when it comes time to attach files to hub posts.
