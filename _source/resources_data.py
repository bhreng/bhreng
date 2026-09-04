#!/usr/bin/env python3
"""
Training platforms and credentials for the E.E.P. hubs.

Every entry was verified against a primary source in September 2026. The
`cost` field is deliberately blunt, because the difference between "free"
and "free to start" is the thing students and parents get wrong.

  free    genuinely free, including any credential it awards
  limits  free to use, but capped in a way a student will hit
  school  the school pays; a student gets in through Mr. Frank

Everything beyond the three the school licenses (GMetrix, Festo LX,
Certiport) is free. Nothing on this page ever asks a student for money,
and no prices appear anywhere on it.

`age` is only filled in where there is something a student or parent
actually has to do. Blank means nothing unusual.
"""

# pathway keys match build_hubs.P
ALL = ['industrial', 'architecture', 'mechanical', 'electrical',
       'software', 'automation', 'project']

R = []


def add(**kw):
    kw.setdefault('age', '')
    kw.setdefault('cred', '')
    kw.setdefault('note', '')
    R.append(kw)


# ----------------------------------------------------------- the shop's own
add(name='GMetrix', url='https://www.gmetrix.com/',
    cost='school', cost_note='Mr. Frank gives you a classroom code',
    what='Practice tests and training for the Autodesk certifications. Two modes: '
         'training mode walks you through each question, testing mode is timed like '
         'the real thing.',
    cred='Practice only — the real exam is separate',
    note='New this year. Use it until you are consistently passing in testing mode \u2014 '
         'that is the signal you are ready to sit the real one.',
    paths=['industrial', 'architecture', 'mechanical'])

add(name='Festo LX', url='https://www.festo.com/us/en/e/technical-education/digital-learning/festo-learning-experience-id_642130',
    cost='school', cost_note='School subscription — ask for access',
    what='Festo\'s industrial training portal. Factory automation, pneumatics and '
         'hydraulics, electrical engineering, mechatronics, and Industry 4.0, built by '
         'the company that makes the equipment.',
    cred='Training only',
    note='Closest thing in the program to what an automation technician actually '
         'trains on at work.',
    paths=['automation', 'electrical', 'mechanical'])

add(name='Certiport', url='https://www.certiport.com/',
    cost='school', cost_note='Exams are run here, by Mr. Frank',
    what='The testing platform the Autodesk certification exams run on. Mr. Frank is the '
         'certified proctor, so you sit the exam in this building on a normal school day.',
    cred='The real Autodesk certification',
    age='Under 18 needs a parent or guardian consent form on file first',
    note='Get the consent form signed early in the year. Not the week you are ready to '
         'test — that is how people miss a testing window.',
    paths=['industrial', 'architecture', 'mechanical'])

# ----------------------------------------------------------- Autodesk stack
add(name='Autodesk free software', url='https://www.autodesk.com/education/edu-software',
    cost='free', cost_note='Free 1-year education licence, renewable',
    what='Fusion, Inventor, AutoCAD, Revit, Civil 3D — the full professional suite on '
         'your own machine, free while you are a student. You verify your enrolment once.',
    note='Install it at home. Everything you do in the shop, you can carry on with.',
    paths=ALL)

add(name='Autodesk Learning', url='https://www.autodesk.com/learn',
    cost='free', cost_note='Free with an Autodesk account',
    what='Autodesk\'s own course catalogue, including free certification prep courses '
         'for Fusion, Inventor, Revit, AutoCAD and Civil 3D — most run 5 to 15 hours.',
    age='Autodesk account is 13+',
    paths=['industrial', 'architecture', 'mechanical'])

add(name='Tinkercad', url='https://www.tinkercad.com/',
    cost='free', cost_note='Free, join with a class code',
    what='Browser-based 3D modelling, circuit simulation and Codeblocks. Fastest way to '
         'test a circuit or a shape without installing anything.',
    note='Circuits mode simulates a real breadboard with an Arduino on it — you can '
         'debug a build before you wire it.',
    paths=['industrial', 'electrical', 'automation', 'software'])

add(name='Instructables', url='https://www.instructables.com/',
    cost='free',
    what='Project write-ups and free classes on 3D printing, CNC, laser cutting and '
         'electronics. Owned by Autodesk.',
    paths=['industrial', 'mechanical', 'electrical'])

# ----------------------------------------------------------- software / CS
add(name='freeCodeCamp', url='https://www.freecodecamp.org/',
    cost='free', cost_note='Free, and the certifications are free too',
    what='Eleven certifications in web development, Python, data analysis and more. '
         'Each one takes five real projects, not a multiple-choice test.',
    cred='Free certification',
    note='One of the very few places where the credential itself costs nothing.',
    paths=['software'])

add(name='Harvard CS50x', url='https://cs50.harvard.edu/x/',
    cost='free', cost_note='Free — including the CS50 certificate',
    what='Harvard\'s introduction to computer science, taught properly. C, Python, SQL, '
         'algorithms, and a final project you design yourself.',
    cred='Free CS50 certificate at 70%+',
    note='Hard, and worth it. Take it directly from cs50.harvard.edu \u2014 the version '
         'listed on other course sites is the same material.',
    paths=['software'])

add(name='Cisco Networking Academy', url='https://www.netacad.com/',
    cost='free', cost_note='Free courses, free badges',
    what='Python Essentials 1 and 2, Computer Hardware Basics, Introduction to IoT. '
         'Self-paced, with a Credly digital badge at the end of each.',
    cred='Free digital badge',
    age='Enrol through the school, not on your own',
    paths=['software', 'automation', 'electrical'])

add(name='AWS Educate', url='https://aws.amazon.com/education/awseducate/',
    cost='free', cost_note='Free — email address only, no card',
    what='Hands-on cloud and computing labs with free shareable badges. No AWS account '
         'and no credit card needed.',
    cred='Free digital badge',
    age='13+',
    paths=['software'])

add(name='IBM SkillsBuild', url='https://skillsbuild.org/high-school',
    cost='free', cost_note='Free, badges included',
    what='IBM\'s free programme built for ages 13 to 18. AI Literacy, Cybersecurity '
         'Fundamentals, Data Fundamentals, Web Development, Cloud Computing, Project '
         'Management Fundamentals — most run 4 to 12 hours.',
    cred='Free IBM digital badges via Credly',
    age='13 to 18 — under-18s may need a parent to approve',
    note='The strongest free-credential option in the whole programme. Badges come from '
         'IBM and go straight on a resume.',
    paths=['software', 'project'])

# ----------------------------------------------------------- maths / logic
add(name='Brilliant', url='https://brilliant.org/',
    cost='limits', cost_note='Free tier is capped at 2 lessons a day',
    what='Interactive maths, logic, computer science and data courses. Built around '
         'solving rather than watching.',
    note='Ask Mr. Frank before signing up yourself \u2014 the school can enrol you for '
         'full access with no daily cap, free, through Brilliant for Educators.',
    age='13+',
    paths=['software', 'mechanical', 'electrical', 'project'])

add(name='Khan Academy', url='https://www.khanacademy.org/',
    cost='free',
    what='Free maths and physics, from algebra through calculus and mechanics. The '
         'backstop when a formula in a pathway guide does not make sense yet.',
    paths=ALL)

add(name='MIT OpenCourseWare', url='https://ocw.mit.edu/',
    cost='free', cost_note='Free, no account',
    what='Complete MIT course materials, including 2.001 Mechanics and Materials. '
         'Lecture notes, problem sets and solutions.',
    cred='No credential',
    note='University-level and unapologetic about it. Use it when you want the real '
         'derivation rather than the summary.',
    paths=['mechanical', 'architecture'])

# ----------------------------------------------------------- electrical
add(name='All About Circuits', url='https://www.allaboutcircuits.com/textbook/',
    cost='free', cost_note='Free open textbook',
    what='A full DC, AC and semiconductor textbook, used in two-year electronics '
         'programmes. Clear on the things that trip people up.',
    paths=['electrical', 'automation'])

add(name='TI Precision Labs', url='https://www.ti.com/video/series/precision-labs.html',
    cost='free', cost_note='Free',
    what='Texas Instruments\' own analog training — op amps, ADCs, instrumentation '
         'amplifiers, noise. Written by the engineers who design the parts.',
    note='Genuinely respected by practising engineers. Steeper than it looks.',
    paths=['electrical'])

add(name='Arduino Docs and Project Hub',
    url='https://docs.arduino.cc/',
    cost='free', cost_note='Free to browse and use',
    what='Official Arduino tutorials, language reference, and thousands of documented '
         'projects with code and wiring.',
    age='Under 18 needs a parent-approved account to publish or use Cloud',
    note='Arduino Cloud\'s free tier caps you at 25 compiles a day — fine for a lesson, '
         'tight for a build day. The desktop IDE has no limit.',
    paths=['electrical', 'software', 'automation'])

add(name='Stratasys Academy — J5 Series',
    url='https://support.stratasys.com/en/Welcome/Training/PolyJet/J5-Series',
    cost='free', cost_note='Manufacturer training',
    what='Online training for the J5 series, which is our J55 — organised as Getting '
         'Started, Operating, Designing and Post-Processing. The Designing track is '
         'design for additive manufacturing generally, so it is useful even if you '
         'never touch the machine.',
    note='Stratasys runs a separate PolyJet Certification for AM Designers beyond '
         'these modules. Access terms for the online courses are not stated on the '
         'page — check before sending a class at it.',
    paths=['industrial', 'mechanical'])

# ----------------------------------------------------------- automation
add(name='Universal Robots Academy',
    url='https://academy.universal-robots.com/free-e-learning/',
    cost='free', cost_note='Free, simulation-based',
    what='Six free tracks on programming collaborative robots — UR20/30 (start here), '
         'e-Series, CB3, PolyScope X, URScript, and Risk Assessment. Runs in simulation, '
         'so you can do the whole thing without touching a robot. Free account required.',
    note='This is the training for the arms in our own shop — we have a UR3 and a UR5. '
         'Do the e-Series track and the Risk Assessment track before you go near them. '
         'CB3 takes under two hours; Risk Assessment is the one that matters most, '
         'because a cobot is only as safe as the application built around it.',
    paths=['automation'])

add(name='Siemens SCE', url='https://www.siemens.com/en-us/content/sce-educational-institutions/documents/',
    cost='free', cost_note='Free downloads',
    what='Siemens\' industrial training documents for PLC programming and TIA Portal — '
         'the same material used to train technicians.',
    paths=['automation', 'electrical'])

# ----------------------------------------------------------- arch / civil
add(name='USGBC Learning Lab', url='https://support.usgbc.org/hc/en-us/articles/4404880158227-Learning-Lab',
    cost='free', cost_note='Free with a USGBC account',
    what='Over a hundred green-building and sustainability lessons written for high '
         'school, standards-aligned, in English and Spanish.',
    note='The best free sustainable-design material available anywhere.',
    paths=['architecture'])

add(name='Learn ArcGIS', url='https://learn.arcgis.com/',
    cost='free', cost_note='Free public account; free for US schools',
    what='Mapping and spatial analysis tutorials. Useful for site work, drainage, '
         'and anything where the ground matters.',
    paths=['architecture'])

# ----------------------------------------------------------- project mgmt
add(name='PMI KICKOFF', url='https://www.pmi.org/kickoff',
    cost='free', cost_note='Free, badge included',
    what='The Project Management Institute\'s own free course — about 45 minutes, in '
         'predictive and agile versions, with a downloadable tool kit.',
    cred='Free digital badge',
    note='PMI is the body that issues the PMP. A free badge with their name on it is '
         'worth the 45 minutes.',
    paths=['project'])

add(name='OpenLearn badged courses', url='https://www.open.edu/openlearn/badged-courses',
    cost='free', cost_note='Free, badge included',
    what='The Open University\'s free courses with assessment. "Project management: the '
         'start of the project journey" fits this pathway directly.',
    cred='Free digital badge and statement of participation',
    paths=['project'])

add(name='HP LIFE', url='https://www.life-global.org/',
    cost='free', cost_note='Free, certificate included',
    what='Short business and entrepreneurship modules — business planning, finance, '
         'operations, marketing.',
    cred='Free completion certificate',
    note='Lines up with the business plan Standard 11 asks for.',
    paths=['project'])

# ----------------------------------------------------------- the credentials
CREDS = [
    dict(name='OSHA 10 — Construction',
         who='Every student, Grade 10',
         cost='School provides',
         what='The safety credential that lets you work on the equipment here, and it is '
              'recognised well outside this building. Nothing in a hub happens without it.',
         url=''),
    dict(name='Autodesk Certified User',
         who='Fusion, Inventor, Revit or AutoCAD',
         cost='School provides',
         what='The industry certification for the CAD tools we use. You prepare in '
              'GMetrix and Autodesk\'s free prep courses, then sit the real exam here in '
              'the shop \u2014 Mr. Frank is the certified proctor, so you never leave the '
              'building.',
         note='If you are under 18, a parent or guardian has to sign a consent form '
              'before you can sit the exam. Ask early, not the week of.',
         url='https://certiport.pearsonvue.com/Certifications/Autodesk/Certifications/Certify.aspx'),
    dict(name='IBM digital badges',
         who='Anyone, any time',
         cost='Free',
         what='No exam, no proctor, no scheduling. Work through a course and the badge '
              'is yours. The fastest real credential you can earn in this programme.',
         url='https://skillsbuild.org/high-school'),
    dict(name='freeCodeCamp certifications',
         who='Software pathway',
         cost='Free',
         what='Five projects per certification. Slower than a badge, and it shows a lot '
              'more.',
         url='https://www.freecodecamp.org/'),
    dict(name='CS50 certificate',
         who='Software pathway',
         cost='Free',
         what='Finish every problem set and the final project at 70% or better.',
         url='https://cs50.harvard.edu/x/certificate/'),
    dict(name='PMI KICKOFF badge',
         who='Project Management pathway',
         cost='Free',
         what='About 45 minutes, from the body that issues the PMP.',
         url='https://www.pmi.org/kickoff'),
]

COST_LABEL = {
    'free':   ('Free', 'ok'),
    'limits': ('Free, with limits', 'warn'),
    'school': ('School provides', 'school'),
}
