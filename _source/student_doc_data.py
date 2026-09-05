# -*- coding: utf-8 -*-
"""The ten hand-in documents, as data.

Every prompt here comes from the existing Drive template. Where the wording
changed it was trimmed, not reinvented -- the questions are the assessment
and they are Dan's. What is new is the shape: one identity block, one set of
heading weights, one kind of fill-in box, across all ten.

The standfirst on each document answers "why am I filling this in", once, in
one sentence. None of the originals said.
"""

ID_BASIC   = ['Name', 'Date', 'Project', 'Tools and software']
ID_SHORT   = ['Name', 'Date']
ID_PROJECT = ['Name', 'Date', 'Project']


DOCS = []


# --------------------------------------------------------------- 1. logbook
DOCS.append(dict(
    file='BHR-ENG-Daily-Logbook.docx',
    name='BHR ENG — Daily Logbook',
    title='Daily Logbook',
    standfirst='The record of one day in the shop. Three intervals, filled in '
               'as the day goes, not written from memory at the end of it.',
    identity=['Project engineer', 'Date', 'Project(s)',
              'Tools and software used'],
    body=[
        ('h', 'Design process status codes'),
        ('note', 'Mark which stage you were in during each interval below. '
                 'You may be in a different one each time.'),
        ('tbl', ['PI', 'DD', 'FAB', 'TE', 'IR'], 1),
        ('note', 'PI — Problem identification and research   ·   '
                 'DD — Detailed design, CAD and modelling   ·   '
                 'FAB — Fabrication and development   ·   '
                 'TE — Testing and evaluation   ·   '
                 'IR — Improve and redesign'),

        ('h', 'Interval 1 — start of class to break            Status code: ___'),
        ('note', 'Work highlights and observations. Tasks completed, '
                 'consultations, reviews, anything that did not behave as '
                 'expected.'),
        ('box', 4),
        ('note', 'Roadblocks. What specifically failed, and what you tried '
                 'instead.'),
        ('box', 3),
        ('note', 'Visual evidence. Attach CAD renders, diagrams or '
                 'photographs of the work — and caption each one.'),
        ('box', 2),

        ('h', 'Interval 2 — break to lunch            Status code: ___'),
        ('note', 'Work highlights and observations.'),
        ('box', 4),
        ('note', 'Roadblocks.'),
        ('box', 3),
        ('note', 'Visual evidence, captioned.'),
        ('box', 2),

        ('h', 'Interval 3 — lunch to end of day            Status code: ___'),
        ('note', 'Work highlights and observations.'),
        ('box', 4),
        ('note', 'Visual evidence, captioned.'),
        ('box', 2),

        ('h', 'Challenges and troubleshooting'),
        ('note', 'Pull today’s failures together. What went wrong, and '
                 'what you did about it.'),
        ('box', 4),

        ('h', 'Daily synthesis'),
        ('note', 'A technical summary of the day. What you decided, why, and '
                 'whether you are where you meant to be.'),
        ('box', 5),

        ('h', 'Next class'),
        ('note', 'What you are doing first thing next session.'),
        ('box', 3),
    ]))


# ---------------------------------------------------------- 2. weekly planner
DOCS.append(dict(
    file='BHR-ENG-Weekly-Planner.docx',
    name='BHR ENG — Weekly Planner',
    title='Weekly Planner',
    standfirst='Handed in Monday. What you intend to do this week, and how '
               'you intend to do it.',
    identity=ID_BASIC,
    body=[
        ('h', 'Goals for the week'),
        ('note', 'What you want to be true by Friday. Two or three is usually '
                 'right.'),
        ('bul', ['Goal 1', 'Goal 2', 'Goal 3', '… add as many as you need']),

        ('h', 'Tasks to complete'),
        ('note', 'The specific pieces of work that get you to those goals.'),
        ('bul', ['Task 1', 'Task 2', 'Task 3', 'Task 4',
                 '… add as many as you need']),

        ('h', 'Plan for the week'),
        ('note', 'How you will actually do it. Address each task above, and '
                 'say what the finished product looks like.'),
        ('box', 7),

        ('h', 'Personal expectations'),
        ('note', 'In your own words: what you are hoping to get done, and '
                 'roughly how long you think each part will take.'),
        ('box', 6),
    ]))


# ------------------------------------------------------- 3. weekly reflection
DOCS.append(dict(
    file='BHR-ENG-Weekly-Reflection.docx',
    name='BHR ENG — Weekly Reflection',
    title='Weekly Reflection',
    standfirst='Handed in Friday. What actually happened this week, against '
               'what you planned on Monday.',
    identity=ID_BASIC,
    body=[
        ('h', 'Equipment used'),
        ('bul', ['Equipment 1', 'Equipment 2', '… add as many as you need']),

        ('h', 'Tasks completed'),
        ('bul', ['Task 1', 'Task 2', 'Task 3', 'Task 4',
                 '… add as many as you need']),

        ('h', 'Progress against your goals'),
        ('note', 'Did you finish any of the goals from Monday’s planner? '
                 'Did you move toward them? Have the goals themselves '
                 'changed?'),
        ('box', 5),

        ('h', 'Reflection on the work'),
        ('note', 'What would you improve? Why did you make the choices you '
                 'made? What went wrong, and how did you solve it? Does any '
                 'of that change what you do next week? Attach screenshots '
                 'or photographs of the work.'),
        ('box', 8),

        ('h', 'Reflection sketch'),
        ('note', 'Sketch the improvements you would make. If the change is '
                 'large, sketch just the area that changes.'),
        ('box', 8),
    ]))


# ------------------------------------------------------ 4. project reflection
DOCS.append(dict(
    file='BHR-ENG-Project-Reflection.docx',
    name='BHR ENG — Project Reflection',
    title='Project Reflection',
    standfirst='Handed in at the end of a project. The honest account of what '
               'you built and what you would do differently.',
    identity=ID_BASIC,
    body=[
        ('h', 'Equipment used'),
        ('bul', ['Equipment 1', 'Equipment 2', '… add as many as you need']),

        ('h', 'Tasks completed'),
        ('bul', ['Task 1', 'Task 2', 'Task 3', 'Task 4',
                 '… add as many as you need']),

        ('h', 'Are you satisfied with this?'),
        ('note', 'A more useful version of that question: is this a fair '
                 'reflection of what you can actually do?'),
        ('box', 5),

        ('h', 'Reflection on the work'),
        ('note', 'What would you improve? Why did you make the choices you '
                 'made? What went wrong, and how did you solve it? If this '
                 'was a group project, cover how the group worked. Attach '
                 'screenshots or photographs.'),
        ('box', 9),

        ('h', 'Reflection sketch'),
        ('note', 'Sketch the improvements you would make. If the change is '
                 'large, sketch just the area that changes.'),
        ('box', 8),
    ]))


# ------------------------------------------------------- 5. Do Now reflection
DOCS.append(dict(
    file='BHR-ENG-Do-Now-Reflection.docx',
    name='BHR ENG — Do Now! Reflection',
    title='Do Now! Reflection',
    standfirst='The short companion to a Do Now. One skill, learned and '
               'written down while it is still fresh.',
    identity=['Name', 'Date', 'Do Now title', 'Equipment used'],
    body=[
        ('h', 'New knowledge acquired'),
        ('note', 'The skills or concepts this Do Now actually taught you.'),
        ('bul', ['Skill or concept 1', 'Skill or concept 2',
                 '… add as many as you need']),

        ('h', 'Brief process summary'),
        ('note', 'In a few sentences: the steps you followed to use each new '
                 'skill.'),
        ('box', 5),

        ('h', 'Future project application'),
        ('note', 'Where does this go next? How would you use it on your '
                 'current or upcoming project?'),
        ('box', 4),

        ('h', 'Confidence level'),
        ('note', 'Could you do this again on your own tomorrow? Be honest — '
                 'this is what tells us what to reteach.'),
        ('box', 3),
    ]))


# ------------------------------------------------ 6. mid-project design review
DOCS.append(dict(
    file='BHR-ENG-Mid-Project-Design-Review.docx',
    name='BHR ENG — Mid-Project Design Review',
    title='Mid-Project Design Review and Feasibility Check',
    standfirst='The stop-and-check partway through a project. Cheaper to find '
               'out here that something will not work than in week four.',
    identity=ID_BASIC,
    body=[
        ('h', 'Phase of project'),
        ('note', 'Circle or mark where you are right now.'),
        ('tbl', ['Planning', 'Design', 'Development'], 1),

        ('h', 'Remaining tasks'),
        ('note', 'What still has to happen for this project to be finished.'),
        ('bul', ['Task 1', 'Task 2', 'Task 3',
                 '… add as many as you need']),

        ('h', 'Conceptual design justification'),
        ('note', 'Why this concept and not the others you considered. Name '
                 'any decision that was risky, and say why you think it holds.'),
        ('box', 7),

        ('h', 'Feasibility and risk check'),
        ('note', 'Is this design viable against time, budget and the '
                 'knowledge you have? Which resource is the biggest problem? '
                 'And: what is the single element most likely to fail, that '
                 'has to be tested before you can trust the whole concept?'),
        ('box', 8),

        ('h', 'Feedback and action items'),
        ('note', 'Seeking and using feedback is part of engineering. Which '
                 'routes have you used — instructor one-on-one, peer review, '
                 'something else? Based on what you heard, what are your next '
                 'steps to validate or redesign?'),
        ('box', 7),
    ]))


# ------------------------------------------------------- 7. design brief
DOCS.append(dict(
    file='BHR-ENG-Design-Brief-and-Initial-Planner.docx',
    name='BHR ENG — Design Brief and Initial Planner',
    title='Design Brief and Initial Planner',
    standfirst='The document that starts a project. It fixes what the problem '
               'is, who it is for, and how you will know when you are done.',
    identity=['Name', 'Date', 'Project title', 'Client',
              'Designer', 'Instructor'],
    body=[
        ('h', 'Problem statement'),
        ('note', 'What the client’s problem, need or want actually is. '
                 'Describe the problem, not your solution to it.'),
        ('box', 5),

        ('h', 'Design statement'),
        ('note', 'The challenge to you, the engineer: what you are going to '
                 'do about that problem.'),
        ('box', 4),

        ('h', 'Criteria'),
        ('note', 'The standards this design will be judged against.'),
        ('bul', ['Criterion 1', 'Criterion 2', 'Criterion 3',
                 '… add as many as you need']),

        ('h', 'Constraints'),
        ('note', 'The limits on the design or on how you can work: size, '
                 'material, time, budget, what the shop actually has.'),
        ('bul', ['Constraint 1', 'Constraint 2', 'Constraint 3',
                 '… add as many as you need']),

        ('h', 'Goals'),
        ('bul', ['Goal 1', 'Goal 2', 'Goal 3',
                 '… add as many as you need']),

        ('h', 'Project deliverables'),
        ('note', 'The list of things that will exist at the end. Be specific '
                 'enough that someone else could check them off.'),
        ('bul', ['Deliverable 1', 'Deliverable 2', 'Deliverable 3',
                 '… add as many as you need']),

        ('h', 'Personal expectations'),
        ('note', 'In your own words: what you are hoping to accomplish, and '
                 'roughly how long you expect each part to take.'),
        ('box', 6),
    ]))


# -------------------------------------------------- 8. independent study week
DOCS.append(dict(
    file='BHR-ENG-Independent-Study-Weekly-Journal.docx',
    name='BHR ENG — Independent Study Weekly Journal',
    title='Independent Study — Weekly Journal',
    standfirst='One entry a week on your own project. Informal, but it has to '
               'exist — it is how a year of independent work becomes '
               'something you can show.',
    identity=ID_BASIC,
    body=[
        ('h', 'The week in bullet points'),
        ('note', 'Separate by day if that makes more sense.'),
        ('bul', ['Item 1', 'Item 2', '… add as many as you need']),

        ('h', 'Notes for the week'),
        ('note', 'What happened, what changed, what you would have done '
                 'differently. Informal is fine. Aim for 50 words or more — '
                 'a tweet is 280 characters, and that is the floor, not the '
                 'target.'),
        ('box', 8),

        ('h', 'Next shop week'),
        ('note', 'Do you know what you are doing next week? Write it here — '
                 'the next step, the next task, or the next project. A note '
                 'to yourself.'),
        ('box', 4),

        ('h', 'Images from the week'),
        ('note', 'Date and label each one. Across a term these should show '
                 'the work progressing.'),
        ('box', 9),
    ]))


# ----------------------------------------------------- 9. field trip reflection
DOCS.append(dict(
    file='BHR-ENG-Field-Trip-Reflection.docx',
    name='BHR ENG — Field Trip Reflection',
    title='Field Trip Reflection',
    standfirst='What you saw outside the shop, and what it has to do with '
               'what you are doing inside it.',
    identity=['Name', 'Date', 'Trip destination', 'Host organisation'],
    body=[
        ('h', 'Equipment and software you saw'),
        ('bul', ['Equipment or software 1', 'Equipment or software 2',
                 '… add as many as you need']),

        ('h', 'Engineering roles and fields you saw'),
        ('note', 'Which of the seven roles were people actually working in?'),
        ('bul', ['Role or field 1', 'Role or field 2', 'Role or field 3',
                 '… add as many as you need']),

        ('h', 'Reflection on the trip'),
        ('note', 'Describe the experience. How did it connect to this shop, '
                 'or to what we are working on now? What was your favourite '
                 'part? Was there anything you did not like?'),
        ('box', 9),

        ('h', 'General observations'),
        ('note', 'Anything else that stuck out.'),
        ('box', 6),
    ]))


# ------------------------------------------------ 10. instructor meeting notes
DOCS.append(dict(
    file='BHR-ENG-Instructor-Meeting-Notes.docx',
    name='BHR ENG — Instructor Meeting Notes',
    title='Instructor Meeting Notes',
    standfirst='The record of a one-on-one. Written by you, so that the next '
               'meeting starts where this one finished.',
    identity=['Name', 'Date and time', 'Room', 'Project',
              'Attendees', 'Next meeting'],
    body=[
        ('h', 'Follow-up from last meeting'),
        ('note', 'What was outstanding from last time, and where it got to.'),
        ('bul', ['Item 1', 'Item 2', '… add as many as you need']),

        ('h', 'New business'),
        ('note', 'What you brought to this meeting.'),
        ('bul', ['Item 1', 'Item 2', 'Item 3',
                 '… add as many as you need']),

        ('h', 'Notes'),
        ('note', 'What was actually said. Detailed enough that it is useful '
                 'to you in three weeks.'),
        ('box', 10),

        ('h', 'Action items'),
        ('note', 'Things that now need doing, and who is doing them.'),
        ('tbl', ['Action', 'Who', 'By when'], 5),

        ('h', 'For the next meeting'),
        ('note', 'What you want to raise next time.'),
        ('box', 4),
    ]))
