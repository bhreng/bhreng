# -*- coding: utf-8 -*-
"""The two rubrics, as data, in Google Classroom's rubric-export shape.

Classroom exports a rubric as a sheet with a fixed five-row block per
criterion:

    row n     A: criterion title
    row n+1   (blank)
    row n+2   B..F: points for each level, best to worst
    row n+3   B..F: level names
    row n+4   B..F: level descriptions

A1 carries Classroom's own warning and A2 its version tag. Both stay. The
POINTS and LEVEL NAMES are Dan's and stay exactly. Only the descriptions are
rewritten here -- and in the Weekly Grade, four of the five columns were
placeholders ("Did a good on Safety"), which is what a student saw when
graded. The point of the rewrite is that every level now says something.

These same dicts feed the student-facing PDF, so the sheet Classroom reads
and the page a student reads cannot drift apart.
"""

LEVELS = ['Excellent', 'Good', 'Fair', 'Unsatisfactory', 'Poor']

PROJECT = dict(
    title='Project Rubric',
    intro='Every project is graded on these five. The points are what '
          'Classroom uses; the words are what they mean.',
    criteria=[
        ('CONCEPT', [20.0, 18.0, 16.0, 12.0, 7.0], [
            'Shows a clear grasp of the concepts behind this project and '
            'applies them without help. Can explain why the design is the '
            'way it is.',
            'Shows a solid grasp of the concepts. Needed minimal help. Can '
            'explain most of the design decisions.',
            'Shows some grasp of the concepts. Needed help to complete the '
            'work. Can explain some of the decisions.',
            'Shows little grasp of the concepts. Needed substantial help '
            'throughout the assignment.',
            'Did not show an understanding of the concepts.']),
        ('BACKGROUND KNOWLEDGE', [20.0, 18.0, 16.0, 12.0, 7.0], [
            'Applies previously learned skills and material with little or '
            'no reteaching.',
            'Applies previously learned material with minimal reinforcement.',
            'Applies some previously learned material. Some reteaching was '
            'needed.',
            'Very little previously learned material carried over. Consistent '
            'reinforcement was needed.',
            'Did not show previously learned material.']),
        ('TECHNICAL KNOWLEDGE', [20.0, 18.0, 16.0, 12.0, 7.0], [
            'All of the requested requirements are met. The work is accurate '
            'to a high standard.',
            'All of the requested requirements are met. Few or no '
            'inaccuracies.',
            'Most of the requested requirements are met. Some inaccuracies.',
            'Some of the requested requirements are met. Many inaccuracies.',
            'Did not provide the requested requirements.']),
        ('PARTICIPATION/TEAMWORK', [20.0, 18.0, 16.0, 12.0, 7.0], [
            'Work is done on time. On task throughout. A strong contributor '
            'to the design team.',
            'Work is done on time. On task most of the time. Works well in '
            'the design team.',
            'Inefficient use of time delayed completion. On task some of the '
            'time; sometimes distracts others. Works okay in the team.',
            'Poor use of time prevented completion. Off task; often '
            'distracts others. Does not work well in the team.',
            'Did not participate or work in a team.']),
        ('PRESENTATION', [20.0, 18.0, 16.0, 12.0, 7.0], [
            'Graphics are professional. Technical drawings include all of '
            'the specifications and requirements. Documentation is complete '
            'and dated. The project is visually appealing.',
            'Graphics are neat. Technical drawings include most of the '
            'specifications and requirements. Documentation is complete. '
            'Visually satisfactory.',
            'Graphics are somewhat neat. Drawings include some of the '
            'specifications and requirements. Documentation has gaps. Needs '
            'work to be visually satisfactory.',
            'Graphics are difficult to read. Drawings are inconsistent and '
            'miss many of the specifications and requirements. Documentation '
            'is thin.',
            'Did not create work that communicates what was done.']),
    ],
)

WEEKLY = dict(
    title='Weekly Grade',
    intro='Assessed every shop week. Six things, in two groups: how you '
          'behave in the room, and how you work. Together they are 30% of '
          'your grade, and with Employability, half of it.',
    criteria=[
        ('Safety', [16.6, 15.3, 13.0, 8.6, 4.6], [
            'Follows all safety rules, maintains a clean work area and '
            'returns all materials to the proper place upon completing a '
            'task.',
            'Follows the safety rules. Work area is left clean and materials '
            'put away, with an occasional reminder.',
            'Follows the safety rules when reminded. Work area or materials '
            'are sometimes left for others to deal with.',
            'Needed more than one reminder about a safety rule this week, or '
            'left the work area unsafe for the next person.',
            'Ignored a safety rule, or was removed from a machine or the '
            'Makerspace.']),
        ('Initiative', [16.7, 15.4, 13.0, 8.7, 4.7], [
            'Stays on task, seeks additional work, offers assistance to '
            'peers, comes for help when needed, uses down time effectively '
            'between jobs.',
            'Stays on task and asks for help when stuck. Uses most down '
            'time; occasionally needs a nudge toward the next job.',
            'Stays on task when directed. Waits to be told what to do next; '
            'down time is not used.',
            'Frequently off task, or avoids asking for help and stalls as a '
            'result.',
            'Did not engage with the work this week.']),
        ('Preparation', [16.7, 15.3, 13.0, 8.7, 4.7], [
            'On time to class, agenda present, written instrument present, '
            'dressed to shop standards and ready for work, awake and alert.',
            'On time and ready to work. Missing one of agenda, something to '
            'write with, or shop attire, on one day.',
            'Late, or missing required items or shop attire, more than once '
            'this week.',
            'Regularly late or unprepared. Had to borrow, be sent to change, '
            'or wait to start.',
            'Not prepared to work on most days.']),
        ('Attitude', [16.6, 15.3, 13.0, 8.6, 4.6], [
            'Demonstrates a positive attitude, interacts appropriately with '
            'others, uses appropriate language, maintains self-control at '
            'all times.',
            'Positive and appropriate with others. A rare lapse in language '
            'or self-control, corrected without prompting.',
            'Generally appropriate, but needed a reminder about language, '
            'tone, or how others were treated.',
            'More than one reminder this week about language, tone or '
            'self-control. Interactions caused a problem for others.',
            'Behaviour or language made the shop worse for the people in it.']),
        ('Work Ethic', [16.7, 15.3, 13.0, 8.7, 4.7], [
            "Work reflects the student's best efforts, cooperative, "
            'demonstrates peer leadership, stays on task, self-starter, uses '
            'proper language, never is publicly critical of the work of '
            'others.',
            'Best effort on most work. Cooperative, stays on task, '
            'occasionally needs a start.',
            'Effort is inconsistent. Works when directed. Cooperative when '
            'it is convenient.',
            'Minimal effort. Needed to be restarted repeatedly, or was '
            'publicly critical of another student\'s work.',
            'Did not put effort into the work this week.']),
        ('Productivity', [16.7, 15.4, 13.0, 8.7, 4.7], [
            'Provides work of the highest quality, actively looks for and '
            'suggests solutions to problems, routinely uses time well, '
            'routinely provides useful ideas when participating in group '
            'discussion.',
            'Work is of good quality and time is used well. Contributes to '
            'problem-solving when asked.',
            'Work is acceptable. Time is sometimes wasted. Contributes little '
            'to group problem-solving.',
            'Work is below standard or incomplete. Time is often wasted. '
            'Does not contribute to solving problems.',
            'Produced little or nothing usable this week.']),
    ],
)
