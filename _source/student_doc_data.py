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
    file='BHR27-Daily-Logbook.docx',
    name='BHR27 · Daily Logbook',
    title='Daily Logbook',
    standfirst='The record of one day in the shop. Three intervals, filled in '
               'as the day goes, not written from memory at the end of it.',
    identity=['Project engineer', 'Date', 'Project(s)',
              'Tools and software used'],
    body=[
        ('h2', 'Engineering design process (EDP) status codes'),
        ('note', 'Mark which stage you were in during each interval below. '
                 'You may be in a different one each time.'),
        ('edp',),

        ('h', 'Interval 1: Start of class to break', 'PI'),
        ('label', 'Work highlights &amp; observations',
         'Tasks completed: consultations, reviews, anomalies, etc.'),
        ('bul', ['[Bullet point 1]', '[Bullet point 2]']),
        ('label', 'Interval roadblocks',
         'Document specific technical failures and what you tried instead.'),
        ('box', 'm'),
        ('label', 'Visual evidence', 'Caption and describe your images.'),
        ('box', 'l', '[Attach CAD renderings, logic diagrams, or photographs '
                     'of work done]'),

        ('h', 'Interval 2: Break to lunch', 'DD'),
        ('label', 'Work highlights &amp; observations',
         'Tasks completed: consultations, reviews, anomalies, etc.'),
        ('bul', ['[Bullet point 1]', '[Bullet point 2]']),
        ('label', 'Interval roadblocks',
         'Document specific technical failures and what you tried instead.'),
        ('box', 'm'),
        ('label', 'Visual evidence', 'Caption and describe your images.'),
        ('box', 'l', '[Attach CAD renderings, logic diagrams, or photographs '
                     'of work done]'),

        ('h', 'Interval 3: Lunch to end of day', 'FAB'),
        ('label', 'Work highlights &amp; observations',
         'Tasks completed: consultations, reviews, anomalies, etc.'),
        ('bul', ['[Bullet point 1]', '[Bullet point 2]']),
        ('label', 'Visual evidence', 'Caption and describe your images.'),
        ('box', 'l', '[Attach CAD renderings, logic diagrams, or photographs '
                     'of work done]'),

        ('h', 'End of day'),
        ('label', 'Challenges &amp; troubleshooting',
         'Pull the day&rsquo;s failures together and say what you did about '
         'them.'),
        ('box', 'm'),
        ('label', 'Daily synthesis',
         'A technical summary of the day: what you decided, why, and whether '
         'you are where you meant to be.'),
        ('box', 'l', '[Type reflection here…]'),
        ('label', 'Next class',
         'What you are doing first thing next session.'),
        ('box', 's'),
    ]))


# ---------------------------------------------------------- 2. weekly planner
DOCS.append(dict(
    file='BHR27-Weekly-Planner.docx',
    name='BHR27 · Weekly Planner',
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
        ('box', 'l'),

        ('h', 'Personal expectations'),
        ('note', 'In your own words: what you are hoping to get done, and '
                 'roughly how long you think each part will take.'),
        ('box', 'm'),
    ]))


# ------------------------------------------------------- 3. weekly reflection
DOCS.append(dict(
    file='BHR27-Weekly-Reflection.docx',
    name='BHR27 · Weekly Reflection',
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
        ('box', 'm'),

        ('h', 'Reflection on the work'),
        ('note', 'What would you improve? Why did you make the choices you '
                 'made? What did the results tell you to change, and how did you change it? Does any '
                 'of that change what you do next week? Attach screenshots '
                 'or photographs of the work.'),
        ('box', 'l'),

        ('h', 'Reflection sketch'),
        ('note', 'Sketch the improvements you would make. If the change is '
                 'large, sketch just the area that changes.'),
        ('box', 'xl'),
    ]))


# ------------------------------------------------------ 4. project reflection
DOCS.append(dict(
    file='BHR27-Project-Reflection.docx',
    name='BHR27 · Project Reflection',
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
        ('box', 's'),

        ('h', 'Reflection on the work'),
        ('note', 'What would you improve? Why did you make the choices you '
                 'made? What did the results tell you to change, and how did you change it? If this '
                 'was a group project, cover how the group worked. Attach '
                 'screenshots or photographs.'),
        ('box', 'l'),

        ('h', 'Reflection sketch'),
        ('note', 'Sketch the improvements you would make. If the change is '
                 'large, sketch just the area that changes.'),
        ('box', 'xl'),
    ]))


# ------------------------------------------------------- 5. Do Now reflection
DOCS.append(dict(
    file='BHR27-Do-Now-Reflection.docx',
    name='BHR27 · Do Now! Reflection',
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
        ('box', 'm'),

        ('h', 'Future project application'),
        ('note', 'Where does this go next? How would you use it on your '
                 'current or upcoming project?'),
        ('box', 'm'),

        ('pick', 'Confidence level',
         ['Not yet', 'Only with help', 'On my own', 'I could teach it'],
         'On my own', 'Could you do this again tomorrow without help?'),
        ('h', 'Why that answer'),
        ('note', 'Be honest. This is what tells us what to reteach.'),
        ('box', 's'),
    ]))


# ------------------------------------------------ 6. mid-project design review
DOCS.append(dict(
    file='BHR27-Mid-Project-Design-Review.docx',
    name='BHR27 · Mid-Project Design Review',
    title='Mid-Project Design Review and Feasibility Check',
    standfirst='The stop-and-check partway through a project. Cheaper to find '
               'out here that something will not work than in week four.',
    identity=ID_BASIC,
    body=[
        ('pick', 'Phase of project',
         ['Planning', 'Design', 'Development', 'Testing', 'Refinement'],
         'Design', 'Where the project actually is right now, not where the '
                   'schedule says it should be.'),

        ('h', 'Remaining tasks'),
        ('note', 'What still has to happen for this project to be finished.'),
        ('bul', ['Task 1', 'Task 2', 'Task 3',
                 '… add as many as you need']),

        ('h', 'Conceptual design justification'),
        ('note', 'Why this concept and not the others you considered. Name '
                 'any decision that was risky, and say why you think it holds.'),
        ('box', 'l'),

        ('h', 'Feasibility and risk check'),
        ('note', 'Is this design viable against time, budget and the '
                 'knowledge you have? Which resource is the biggest problem? '
                 'And: what is the single element most likely to fail, that '
                 'has to be tested before you can trust the whole concept?'),
        ('box', 'm'),

        ('h', 'Feedback and action items'),
        ('note', 'Seeking and using feedback is part of engineering. Which '
                 'routes have you used — instructor one-on-one, peer review, '
                 'something else? Based on what you heard, what are your next '
                 'steps to validate or redesign?'),
        ('box', 'm'),
    ]))


# ------------------------------------------------------- 7. design brief
DOCS.append(dict(
    file='BHR27-Design-Brief-and-Initial-Planner.docx',
    name='BHR27 · Design Brief and Initial Planner',
    title='Design Brief and Initial Planner',
    standfirst='The document that starts a project. It fixes what the problem '
               'is, who it is for, and how you will know when you are done.',
    identity=['Name', 'Date', 'Project title', 'Client',
              'Designer', 'Instructor'],
    body=[
        ('h', 'Problem statement'),
        ('note', 'What the client’s problem, need or want actually is. '
                 'Describe the problem, not your solution to it.'),
        ('box', 's'),

        ('h', 'Design statement'),
        ('note', 'The challenge to you, the engineer: what you are going to '
                 'do about that problem.'),
        ('box', 'm'),

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
        ('box', 'xl'),
    ]))


# ------------------------------------------------- 8. instructor meeting notes
DOCS.append(dict(
    file='BHR27-Instructor-Meeting-Notes.docx',
    name='BHR27 · Instructor Meeting Notes',
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
        ('box', 's'),

        ('h', 'Action items'),
        ('note', 'Things that now need doing, and who is doing them.'),
        ('tbl', ['Action', 'Who', 'By when'], 5),

        ('h', 'For the next meeting'),
        ('note', 'What you want to raise next time.'),
        ('box', 's'),
    ]))


# ------------------------------------- 9. independent focus: term start proposal
# The start-of-term document is a PROPOSAL, because Dan reviews it. It has
# to carry enough for a teacher to say yes, revise, or no: what the idea is,
# why this pathway, what will be researched and made, what it needs, how the
# five shop weeks break down, and what "done" looks like. Then a review box.
DOCS.append(dict(
    file='BHR27-Independent-Focus-Proposal.docx',
    name='BHR27 · Independent Focus Proposal',
    title='Independent Focus — Term Proposal',
    standfirst='Fill this in on the first day of the term and hand it in for '
               'review before you start. It is a proposal, not a contract: '
               'plans change, and the term-end reflection is where you say '
               'how. But it has to be clear enough that your instructor can '
               'say yes.',
    identity=['Name', 'Term', 'Pathway', 'Date'],
    body=[
        ('h', 'The pathway'),
        ('pick', 'Home pathway this term',
         ['Industrial Design', 'Architecture &amp; Civil', 'Mechanical',
          'Electrical', 'Software', 'Automation &amp; Robotics',
          'Project Management', 'Other (approved)'],
         'Mechanical', 'The hub you are living in this term.'),
        ('pick', 'New, or continuing?',
         ['New this term', 'Continuing from last term'], 'New this term',
         'Continuing is fine. Say below which part you are on now.'),
        ('label', 'Why this pathway',
         '&ldquo;It is next to what I want to do&rdquo; and &ldquo;no idea, '
         'it looked interesting&rdquo; are both good answers. Say which.'),
        ('box', 's'),

        ('h', 'The idea'),
        ('label', 'Independent Project title', 'One line.'),
        ('box', 'xs'),
        ('label', 'What it is',
         'Describe the idea so someone who has not heard it could repeat it '
         'back. What will exist at the end of the term that does not exist '
         'now &mdash; a thing, a piece of research, a skill, a working '
         'system?'),
        ('box', 'm'),
        ('label', 'Why it is worth a term',
         'What you expect to learn, and what it has to do with where you '
         'think you might be going.'),
        ('box', 's'),

        ('h', 'The work'),
        ('label', 'Research',
         'What you need to find out before or while you build. Name the '
         'kind of source: a datasheet, a standard, a tutorial, a person.'),
        ('box', 's'),
        ('label', 'Design and build',
         'What you will actually make, model, code or test. Be specific '
         'about the first thing you will do on day one.'),
        ('box', 'm'),
        ('label', 'Tools, materials and training',
         'Which machines and software. Anything you are not yet authorised '
         'on. Anything that has to be ordered &mdash; if so, an Order '
         'Request Form goes with this proposal.'),
        ('box', 's'),

        ('h', 'The five weeks'),
        ('note', 'A term is about five shop weeks. One goal per week, '
                 'checkable. Remember each week goes cold for a week before '
                 'the next &mdash; write goals you can pick back up.'),
        ('tbl', ['Shop week', 'Goal for the week', 'How I will know it is done'], 5),
        ('label', 'What &ldquo;done&rdquo; looks like at the end of the term',
         'One sentence. This is the line the term-end reflection compares '
         'against.'),
        ('box', 's'),
        ('label', 'What could stop this',
         'The one thing most likely to get in the way, and what you would do '
         'instead.'),
        ('box', 's'),

        ('h', 'Instructor review'),
        ('note', 'Leave this section blank. Your instructor fills it in.'),
        ('pick', 'Decision', ['Approved', 'Approved with changes',
                              'Revise and resubmit', 'Not approved'],
         'Approved', ''),
        ('label', 'Notes', ''),
        ('box', 'm'),
        ('tbl', ['Instructor', 'Date'], 1),
    ]))


# ---------------------------------------- 10. independent focus: term reflection
# Dan's term-end reflection, as the binder specifies it (Section 5): project
# title, equipment, tasks completed, skills learned or improved, status and
# progress, challenges and adaptations, evaluation of project management,
# goals for next term. Stands alone.
DOCS.append(dict(
    file='BHR27-Independent-Focus-Reflection.docx',
    name='BHR27 · Independent Focus Reflection',
    title='Independent Focus — Term Reflection',
    standfirst='Fill this in on the last day of the term, with your proposal '
               'open next to it. Ten minutes. This is the record of one term '
               'of your focus, and one row of your two-year record comes '
               'from it.',
    identity=['Name', 'Term', 'Pathway', 'Date'],
    body=[
        ('label', 'Independent Project title', 'As it ended up, if it changed.'),
        ('box', 'xs'),
        ('label', 'Equipment and software used',
         'Everything you touched this term, so the record is complete.'),
        ('bul', ['[Item 1]', '[Item 2]', '[&hellip; add as many as you need]']),
        ('label', 'Tasks completed',
         'What actually got done. Specific: &ldquo;modelled the enclosure and '
         'printed two revisions&rdquo;, not &ldquo;worked on the project&rdquo;.'),
        ('bul', ['[Task 1]', '[Task 2]', '[Task 3]',
                 '[&hellip; add as many as you need]']),
        ('label', 'Skills learned or improved',
         'Name the skill and the evidence &mdash; a file, a print, a working '
         'circuit, a certification level.'),
        ('box', 'm'),
        ('pick', 'Project status',
         ['Complete', 'On track, continuing next term', 'Behind, continuing',
          'Paused', 'Stopped &mdash; changing direction'],
         'On track, continuing next term',
         'Where it actually is, not where the plan said it would be.'),
        ('label', 'Progress against the proposal',
         'Look at the five-week table and the &ldquo;done&rdquo; line you '
         'wrote at the start. What matched, what moved.'),
        ('box', 'm'),
        ('label', 'Challenges and adaptations',
         'What the results told you to change, and what you changed. '
         'Analysis, adjustment, improvement.'),
        ('box', 'l'),
        ('label', 'How well did you manage the project?',
         'Time, scope, the week-off restarts. What would you run differently?'),
        ('box', 'm'),
        ('pick', 'Next term', ['Staying in this pathway', 'Moving to another',
                              'Not decided yet'], 'Staying in this pathway',
         'Either is a good answer. Say why in the next box.'),
        ('label', 'Goals for next term',
         'Where the next term starts. Specific enough to be checked.'),
        ('box', 'm'),
    ]))
