# -*- coding: utf-8 -*-
"""
The shop equipment register and per-machine safety checks.

EVERY factual claim below traces to a manufacturer document, a standards body,
or a government source. Anything that could not be verified that way is either
left out or marked in the text as shop policy rather than manufacturer
instruction. Where a widely repeated "fact" turned out to be wrong, the
correct version is used and the wrong one is addressed head-on in the
explanation, because the wrong version is what students will have heard.

Sources are listed in SOURCES at the bottom and rendered on each page.

CONFIRMED WITH DAN, 4 Sep 2026:
  * The laser is an Epilog FusionPro.
  * No printer in the room falls under the 2024 CPSC A1 recall.
  * No check needed for the 3D scanner or PVC pipe cutters -- the cutters are
    covered by the hand tools check.

STILL OPEN:
  * The Bambu temperature table is from the Polymaker wiki; bambulab.com blocked
    automated fetching. Worth a 30-second confirm before it is graded.
"""

# --------------------------------------------------------------- the register

# (key, name, group, blurb, has_quiz)
EQUIPMENT = [
    ('hand', 'Hand tools', 'Bench',
     'X-Acto and craft knives, PVC pipe cutters, files, saws, screwdrivers, '
     'pliers, wrenches, measuring tools.', True),
    ('heat', 'Soldering irons and hot glue guns', 'Bench',
     'Anything on the bench that is hot enough to burn but does not look it.', True),
    ('power', 'Portable and bench power tools', 'Shop',
     'Chop saw, drill press, Dremel and other rotary tools, sanders, drills.', True),
    ('fdm', '3D printers &mdash; filament', 'Makerspace',
     'Bambu Lab A1 Mini, X1C and H2D. Melted plastic, hot beds, long unattended '
     'runs.', True),
    ('polyjet', '3D printer &mdash; resin', 'Makerspace',
     'Stratasys J55. Liquid photopolymer, which is a chemical hazard rather than '
     'a heat one.', True),
    ('laser', 'Laser engraver &mdash; FusionPro', 'Makerspace',
     'Epilog FusionPro. Fire, fumes, and a beam you cannot see.', True),
    ('cnc', 'Handheld CNC', 'Shop',
     'Shaper Origin. A router that corrects your hand, and is still a router.', True),
    ('cobot', 'Collaborative robots', 'Shop',
     'Universal Robots UR3 and UR5. "Collaborative" is not a synonym for safe.',
     True),
    ('ergo', 'Working at a computer', 'Everywhere',
     'The injury you get from sitting still for four years is real, and it is '
     'the one nobody warns you about.', True),
]

GROUPS = ['Bench', 'Shop', 'Makerspace', 'Everywhere']


def _q(text, opts):
    return {'q': text, 'o': opts}


# ------------------------------------------------------------------ hand tools

HAND = [
    _q('Which way should you cut with a craft or X-Acto knife?', [
        ('Away from your body, with your other hand behind the blade', True,
         'Correct. Every cut should travel away from you, and the hand holding '
         'the work stays behind the path the blade would take if it slipped. '
         'Most knife injuries are to the hand that was steadying the material.'),
        ('Towards yourself, so you can see the line better', False,
         'This is the single most common way people cut themselves in a shop. '
         'You can see the line perfectly right up until the blade slips, and '
         'then it is travelling towards you with your weight behind it.'),
        ('Whichever is comfortable, as long as you go slowly', False,
         'Slow does not help. A slip is sudden regardless of how slowly you '
         'were moving, and the direction the blade was already travelling is '
         'the direction it goes.'),
        ('Towards yourself, but with a glove on the other hand', False,
         'A normal glove will not stop a fresh craft blade. It will, however, '
         'make you confident enough to do something you should not.'),
    ]),
    _q('Your knife blade is getting dull and needs more force to cut.', [
        ('Change the blade', True,
         'Correct, and it is counterintuitive: a dull blade is more dangerous '
         'than a sharp one. It needs more force, so it is more likely to slip, '
         'and it is travelling with more of your weight behind it when it does.'),
        ('Push harder &mdash; it still cuts', False,
         'This is exactly how people get hurt. More force means a worse '
         'outcome when it slips, and it will slip sooner because a dull edge '
         'skates instead of biting.'),
        ('Cut more slowly and carefully', False,
         'Care does not compensate for a dull edge. The extra force is the '
         'hazard, and no amount of caution removes it.'),
        ('Sharpen it', False,
         'Craft-knife blades are disposable and cost pennies. Changing it takes '
         'ten seconds and is the whole answer.'),
    ]),
    _q('Where should the workpiece be when you cut, drill, or file it?', [
        ('Clamped or held in a vice', True,
         'Correct. If the work is secured, only the tool moves, and a slip '
         'costs you a scrap piece rather than a hand.'),
        ('Held in your other hand', False,
         'This puts your hand in the one place the tool goes when it slips. '
         'The Makerspace rules say it directly: holding work by hand or against '
         'the body leaves it unstable and may lead to loss of control.'),
        ('Resting loose on the bench', False,
         'Unsecured work spins, slides or tips, and your instinct will be to '
         'grab it &mdash; usually with the tool still moving.'),
        ('Held against your leg or body', False,
         'The worst option. Now the tool is travelling towards a major blood '
         'vessel if it gets away from you.'),
    ]),
    _q('You finish with a knife and need to set it down for a moment.', [
        ('Retract or cap the blade first', True,
         'Correct. An exposed blade on a bench is found by somebody\'s hand, '
         'or rolls off and is caught on the way down &mdash; which is a '
         'reflex you cannot train out.'),
        ('Put it down blade-up so people can see it', False,
         'Visible is not safe. A blade pointing up is worse, not better, and '
         'assumes everyone is looking at your bench.'),
        ('Put it under the material you are working on', False,
         'Now it is hidden, and the next person to move that material finds it '
         'with their fingers.'),
        ('Leave it, you are only stepping away briefly', False,
         'Briefly is when it happens. Capping takes a second.'),
    ]),
    _q('What do you do with a broken or damaged hand tool?', [
        ('Report it straight away', True,
         'Correct. The rules say report any broken tool immediately. A '
         'cracked handle or a mushroomed chisel head fails suddenly and '
         'under load, which is the worst possible moment.'),
        ('Put it back and use a different one', False,
         'You are safe; the next person is not, and they may not spot the '
         'damage. A broken tool left in the rack gets used.'),
        ('Use it carefully', False,
         'Never use a broken tool. Care does not fix a structural failure that '
         'is already in progress.'),
        ('Throw it away', False,
         'Report it rather than quietly binning it &mdash; the shop needs to '
         'know what failed and to replace it.'),
    ]),
]

# ------------------------------------------------------- soldering and hot glue

HEAT = [
    _q('You are soldering. What is the white smoke rising from the joint?', [
        ('Flux', True,
         'Correct, and almost nobody guesses this. It is decomposing rosin '
         'flux &mdash; a respiratory sensitiser that causes occupational asthma. '
         'Early signs of exposure are watery or prickly eyes, a runny or blocked '
         'nose, a sore throat, coughing or wheezing. If you notice those, say so.'),
        ('Lead fume', False,
         'This is the universal belief and it is wrong. Lead boils at about '
         '1,740&nbsp;&deg;C and a soldering iron runs at roughly 330&ndash;370&nbsp;&deg;C '
         '&mdash; nowhere near. The smoke is flux, which is the actual '
         'respiratory hazard.'),
        ('Melted plastic from the board', False,
         'Not unless something has gone badly wrong. The smoke appears the '
         'instant flux meets the hot tip, before the board is anywhere near '
         'that temperature.'),
        ('Water vapour, it is harmless', False,
         'It is flux, and it is not harmless. It is the reason a fume '
         'extractor sits on the bench.'),
    ]),
    _q('If lead is not in the fume, how does lead solder actually get into you?', [
        ('By swallowing it &mdash; from hands, benches and anything you touch', True,
         'Correct. Ingestion from surface contamination is the primary route. '
         'Lead goes hands &rarr; bench &rarr; phone &rarr; snack &rarr; mouth. '
         'This is exactly why there is no food or drink at the bench, and why '
         'you wash your hands and arms properly afterwards, not just rinse them.'),
        ('Through the skin, by touching the solder', False,
         'Skin absorption is not the significant route here. The problem is '
         'what your contaminated hands touch next, and what eventually reaches '
         'your mouth.'),
        ('By breathing the smoke', False,
         'That is the intuitive answer and it is wrong &mdash; the smoke is '
         'flux. Lead does not vaporise at soldering temperatures. The lead risk '
         'is ingestion.'),
        ('It does not, lead solder is safe to use', False,
         'It is usable with the right habits, which is not the same as safe to '
         'ignore. The habits are: no food at the bench, wash thoroughly, clean '
         'the work surface.'),
    ]),
    _q('Your bench has lead-free solder instead of leaded. What changes about '
       'the fume hazard?', [
        ('Nothing much &mdash; the flux is still there and runs hotter', True,
         'Correct. Lead-free solves an ingestion and environmental problem, not '
         'a breathing one. Lead-free alloys melt higher (SAC305 at about '
         '217&nbsp;&deg;C against 183&nbsp;&deg;C for leaded), so the iron runs '
         'hotter and decomposes the flux harder. Extraction still applies.'),
        ('The fume becomes safe to breathe', False,
         'The fume was never mostly lead. It is flux, and lead-free solder '
         'still uses flux &mdash; at a higher temperature.'),
        ('You no longer need to wash your hands', False,
         'Good practice regardless, and the flux residues are still worth '
         'getting off you before you eat.'),
        ('You no longer need eye protection', False,
         'Unrelated. Molten solder spits when flux flashes or a joint is '
         'reworked, and it travels at eye height across a bench.'),
    ]),
    _q('Where does the soldering iron go when you are not actively using it?', [
        ('In its stand', True,
         'Correct. The stand is the single control that prevents most iron '
         'burns and most scorched benches. Parking the iron on the bench '
         '&ldquo;just for a second&rdquo; is the most common mistake there is.'),
        ('Flat on the bench, tip hanging over the edge', False,
         'A tip over the edge is at exactly the height of an arm reaching '
         'past. And the iron rolls.'),
        ('On a piece of scrap wood', False,
         'Which then chars, smokes, and eventually catches. The stand exists '
         'for this.'),
        ('Anywhere, as long as you unplug it', False,
         'A just-unplugged iron stays hot enough to burn for several minutes.'),
    ]),
    _q('You get hot glue on your hand. What do you do?', [
        ('Cold running water for 15 minutes, leaving the glue in place', True,
         'Correct on both counts. Hot glue burns worse than the temperature '
         'suggests, because it sticks and keeps transferring heat into the skin '
         '&mdash; you cannot pull away from it. And pulling it off can take skin '
         'with it. Cool it first, for the full 15 minutes.'),
        ('Peel the glue off quickly, then run it under water', False,
         'Peeling can remove skin along with the glue, turning a burn into a '
         'wound. Cool it in place first.'),
        ('Run it under warm water so the glue softens', False,
         'Warm water does not stop the burn. Cold running water is what limits '
         'the damage, and 15 minutes is the figure.'),
        ('Put ice on it', False,
         'Ice on a burn can cause further tissue damage. Cool running water, '
         'not ice.'),
    ]),
    _q('Which is more likely to burn you badly &mdash; a 370&nbsp;&deg;C iron tip '
       'or 190&nbsp;&deg;C hot glue?', [
        ('The hot glue, because it sticks', True,
         'Correct, and it is the least intuitive fact on this page. You touch '
         'an iron tip and pull away in milliseconds. Hot glue adheres and keeps '
         'delivering heat into the tissue for as long as it takes to cool. '
         'Lower temperature, worse burn.'),
        ('The iron, it is nearly twice as hot', False,
         'Temperature is only half of it. What matters is how long the heat '
         'keeps going in, and glue that sticks to you does not let you pull '
         'away.'),
        ('They are about the same', False,
         'They are not. The mechanism is different: brief contact versus '
         'sustained contact you cannot escape.'),
        ('Neither, both are below the burn threshold', False,
         'Both are far above it. Water boils at 100&nbsp;&deg;C.'),
    ]),
]

# --------------------------------------------------------------- power tools

POWER = [
    _q('Should you wear gloves when using the drill press or a rotary tool?', [
        ('No &mdash; gloves can be caught and pull your hand in', True,
         'Correct. This is the reversal that catches people out: gloves protect '
         'you from sharp and hot things, and endanger you around anything that '
         'spins. A glove that catches does not tear away, it winds on. The '
         'Makerspace rules say to remove gloves around moving or rotating '
         'machinery.'),
        ('Yes, always &mdash; gloves are protective equipment', False,
         'Not around rotating machinery. The same rules that require gloves for '
         'hot and sharp work specifically say to remove them near anything '
         'that turns.'),
        ('Yes, if the material is sharp', False,
         'Then secure the material differently or deburr it first. A glove near '
         'a spinning bit is a mechanism for pulling your hand into it.'),
        ('Only thin gloves', False,
         'Thin gloves catch too, and they tear rather than release &mdash; '
         'after your hand has already been pulled in.'),
    ]),
    _q('Where does the workpiece go on a drill press?', [
        ('Clamped, or held in a vice bolted to the table', True,
         'Correct. A drill bit that grabs will spin the workpiece into a blade '
         'travelling at the rim &mdash; sheet metal in particular becomes a '
         'spinning edge instantly. Clamp it.'),
        ('Held firmly by hand', False,
         'A bit that catches turns the workpiece into a rotating blade faster '
         'than you can let go. This is one of the most common serious shop '
         'injuries there is.'),
        ('Held by hand, with the speed set low', False,
         'Low speed means more torque, which makes grabbing worse, not better.'),
        ('Resting flat on the table', False,
         'Flat is not secured. As soon as the bit breaks through, the piece '
         'wants to spin.'),
    ]),
    _q('The chop saw has finished a cut. When do you lift the blade guard '
       'area or reach near the blade?', [
        ('When the blade has completely stopped spinning', True,
         'Correct. A coasting blade is nearly invisible and still cutting. Wait '
         'for it to stop &mdash; not slow down, stop. The rules also say never '
         'walk away from a tool that is still on.'),
        ('As soon as you release the trigger', False,
         'The blade keeps spinning for several seconds after the motor is off, '
         'and a coasting blade cuts exactly as well as a powered one.'),
        ('Once it sounds quiet', False,
         'Sound is a poor indicator. A blade that has gone quiet can still be '
         'turning fast enough to take a finger.'),
        ('Whenever the guard has dropped back down', False,
         'The guard returning tells you nothing about whether the blade has '
         'stopped.'),
    ]),
    _q('A guard on a machine is making an awkward cut harder.', [
        ('Stop and ask for a different approach', True,
         'Correct. If the guard is in the way, the setup is wrong, not the '
         'guard. There is nearly always a better fixture or a more suitable '
         'machine. The rules are absolute: machines run only with all required '
         'guards and shields in place.'),
        ('Remove it for this one cut', False,
         'There is no version of this rule with an exception for one cut. '
         'Removing a guard is how a routine job becomes an injury.'),
        ('Have someone hold the guard clear', False,
         'Now two people have hands near the danger zone instead of one.'),
        ('Work around it carefully', False,
         'You are still fighting the setup, and careful is not a control.'),
    ]),
    _q('You are using a Dremel or rotary tool. What is easy to forget?', [
        ('Eye protection, and that the bit can shatter', True,
         'Correct. Small tools feel harmless, so people skip glasses. Cut-off '
         'wheels in particular shatter and throw fragments at speed, and the '
         'tool is usually being used close to the face for detail work.'),
        ('Nothing &mdash; it is a small tool', False,
         'Small is exactly the problem. The tool feels like a pen, so people '
         'use it without glasses, close to their face, on unsecured work.'),
        ('That it needs two people', False,
         'The two-person rule applies to power tools generally &mdash; but the '
         'specific thing people forget about a rotary tool is eye protection '
         'and shattering accessories.'),
        ('To wear gloves', False,
         'The opposite. It spins, so gloves come off.'),
    ]),
]

# ---------------------------------------------------------------- FDM printing

FDM = [
    _q('Which part of a running filament printer is most likely to burn you?', [
        ('The heated bed', True,
         'Correct, and it is not the obvious answer. The bed runs up to about '
         '100&nbsp;&deg;C &mdash; the temperature of boiling water &mdash; and '
         'it has perhaps a hundred times the surface area of a nozzle. It does '
         'not glow, it does not look hot, and it is the surface you reach '
         'across to pull a part off.'),
        ('The nozzle', False,
         'The nozzle is hotter, at up to 300&nbsp;&deg;C, but it is small, '
         'obviously dangerous and people avoid it. The bed burns more people '
         'precisely because it looks harmless.'),
        ('The stepper motors', False,
         'They get warm, not dangerous.'),
        ('The filament as it comes out', False,
         'A thin strand of plastic cools almost immediately. The bed underneath '
         'it does not.'),
    ]),
    _q('Which of the shop printers is the most exposed to work around?', [
        ('The A1 Mini', True,
         'Correct, and it is a genuine surprise. It is open-frame, so a hot end '
         'reaching 300&nbsp;&deg;C and a moving gantry are within reach at all '
         'times. The X1C and H2D put the same hazards behind a door. '
         '&ldquo;Beginner printer&rdquo; does not mean safer printer &mdash; it '
         'means simpler to use.'),
        ('The X1C', False,
         'The X1C is enclosed, which puts the hot end and the moving parts '
         'behind a door. The open-frame machine is the exposed one.'),
        ('The H2D', False,
         'The H2D runs the hottest &mdash; up to about 350&nbsp;&deg;C at the '
         'nozzle and 120&nbsp;&deg;C at the bed &mdash; but it is enclosed and '
         'actively heated. Enclosure is what decides exposure.'),
        ('They are all the same', False,
         'They are not. One of the three is open-frame, and that changes what '
         'you can reach while it runs.'),
    ]),
    _q('When are a printer\'s emissions highest?', [
        ('In roughly the first 20 minutes of a print', True,
         'Correct, and it is exactly when people lean in to watch the first '
         'layer go down. Testing by UL Chemical Insights found emissions peak '
         'early in the print. Start it, then step back.'),
        ('At the very end, when the part is finished', False,
         'By then emissions have dropped considerably. The peak is early.'),
        ('Evenly throughout', False,
         'Not evenly &mdash; there is a clear peak in the early part of the '
         'print, which is also when people stand closest.'),
        ('Only when the printer jams', False,
         'A normal, perfectly successful print emits particles and VOCs '
         'throughout, most heavily at the start.'),
    ]),
    _q('Which filament family emits noticeably more than the others?', [
        ('ABS and ASA', True,
         'Correct. They print at higher temperatures and release significantly '
         'more ultrafine particles and volatile organic compounds than PLA. '
         'That is why they belong in an enclosed machine with ventilation, and '
         'why PLA is the default for open-frame printing.'),
        ('PLA', False,
         'PLA is the low-emission option of the common filaments. It is why it '
         'is the default here.'),
        ('They are all equivalent', False,
         'They are not. Print temperature drives emissions, and the '
         'high-temperature engineering materials are the worst offenders.'),
        ('PETG', False,
         'PETG sits between PLA and ABS. The styrene-based materials &mdash; '
         'ABS and ASA &mdash; are the ones that need an enclosure.'),
    ]),
    _q('Does an enclosure solve the emissions question on its own?', [
        ('No &mdash; it catches particles far better than gases', True,
         'Correct, and the numbers make the point. A ventilated enclosure was '
         'measured cutting particle concentration by 99.7%, but total VOCs by '
         'only 69.5%. Particles are caught; gases leak. You still want the room '
         'ventilated.'),
        ('Yes, an enclosed printer is fully contained', False,
         'Enclosures are excellent at particles and much weaker on gases. '
         'Roughly 99.7% against 69.5% in testing.'),
        ('No, enclosures make no difference', False,
         'They make an enormous difference &mdash; just not an equal one across '
         'particles and gases.'),
        ('Only for PLA', False,
         'The material affects how much is produced, not how well the enclosure '
         'captures it.'),
    ]),
]

# ------------------------------------------------------------- PolyJet / resin

POLYJET = [
    _q('A part has just come off the J55. Can you pick it up bare-handed?', [
        ('No &mdash; it is still coated in uncured resin and support', True,
         'Correct, and this is the mistake almost everyone makes. It looks like '
         'a finished plastic object; it is a chemical. It is safe bare-handed '
         'only after full support removal and washing.'),
        ('Yes, once the print has finished', False,
         'A finished print is not a cured, clean part. The surface carries '
         'uncured photopolymer, which is a skin irritant and a sensitiser.'),
        ('Yes, if it feels dry', False,
         'Feel is not a test. Uncured resin does not have to be visibly wet to '
         'be on the surface.'),
        ('Yes, if you wash your hands afterwards', False,
         'By then it has been on your skin, and on everything you touched on '
         'the way to the sink.'),
    ]),
    _q('Uncured resin gets on your hands and it does not hurt at all. Does '
       'that mean no harm was done?', [
        ('No &mdash; it is a skin sensitiser, and sensitisation is painless', True,
         'Correct, and it is the most important fact about this machine. The '
         'support material is classified as skin sensitisation Category 1. '
         'Repeated small exposures can induce a permanent allergy, after which '
         'even trace contact triggers dermatitis. A student who gets a little '
         'resin on their hands every week for a semester can end up unable to '
         'work with the material at all. Absence of pain is not absence of harm.'),
        ('Yes, if it does not sting it is fine', False,
         'This is precisely the wrong lesson. The serious hazard here is '
         'sensitisation, which builds silently over repeated small exposures '
         'and is permanent once it happens.'),
        ('Yes, as long as you wash it off within an hour', False,
         'Wash it off immediately &mdash; soap and water, 15 minutes. But the '
         'point is that painless contact still counts as exposure.'),
        ('Only if you are already allergic', False,
         'Backwards. The exposure is what causes the allergy in the first '
         'place.'),
    ]),
    _q('Which gloves for handling resin and support material?', [
        ('Nitrile', True,
         'Correct &mdash; this is what Stratasys specifies for handling prints '
         'during support removal. Note the safety data sheet itself only says '
         '&ldquo;impervious gloves&rdquo; without naming a material; nitrile is '
         'the shop answer and the manufacturer\'s own.'),
        ('Latex', False,
         'Latex is a poor barrier against acrylate monomers, and it adds a '
         'latex-allergy problem on top of the one you are trying to avoid.'),
        ('Cotton or fabric work gloves', False,
         'Fabric absorbs the resin and holds it against your skin for as long '
         'as you wear them. Worse than nothing.'),
        ('None needed if you are quick', False,
         'Speed is not protection, and the hazard here builds through small '
         'repeated exposures exactly like that one.'),
    ]),
    _q('You are wearing gloves and need to open a door or check your phone.', [
        ('Take the gloves off first', True,
         'Correct. Sensitisers spread by transfer. The glove protects your hand '
         'and contaminates everything the hand touches &mdash; door handles, '
         'phones, keyboards, and then the next person\'s hands.'),
        ('Keep them on, that is what they are for', False,
         'They protect you and contaminate the room. Everything you touch with '
         'a contaminated glove becomes a source for whoever touches it next.'),
        ('Keep them on but touch as little as possible', False,
         'A door handle is enough. Gloves come off before you leave the work.'),
        ('Wipe the gloves first', False,
         'Wiping smears rather than removes, and now the wipe is contaminated '
         'too.'),
    ]),
    _q('You are diluting caustic soda for support removal. Which goes into '
       'which?', [
        ('Caustic soda into water, always', True,
         'Correct, and students reliably get this backwards. Mixing generates '
         'enough heat to ignite nearby materials, and adding water to caustic '
         'soda can make it erupt. Caustic soda may cause chemical burns, '
         'scarring and blindness &mdash; it is more acutely dangerous than the '
         'resin itself.'),
        ('Water into caustic soda', False,
         'This is the dangerous direction and the one people guess. Water '
         'poured onto caustic soda can boil and spit the solution back at you. '
         'Always add the caustic soda to the water.'),
        ('Either, as long as you stir', False,
         'The order matters enormously and stirring does not fix it. Caustic '
         'soda into water, never the reverse.'),
        ('Neither &mdash; it comes pre-mixed', False,
         'If you are ever the one diluting it, the direction is caustic soda '
         'into water. And this is instructor work regardless.'),
    ]),
    _q('Resin splashes into your eye.', [
        ('Rinse for at least 15 minutes, including under the eyelids, then '
         'get treatment', True,
         'Correct. The resin is classified as causing serious eye damage '
         '&mdash; Category 1, meaning irreversible, including blindness. Remove '
         'contact lenses and rinse under the eyelids too. Have someone else '
         'fetch help while you stay at the water.'),
        ('Rinse briefly and see how it feels', False,
         'Category 1 eye damage is not something you assess by feel. The '
         'full 15 minutes is the rule, and this is the same rule as for any '
         'chemical in the eyes.'),
        ('Go straight to the nurse', False,
         'Rinse first. Every second of contact is doing damage, and the first '
         'question you will be asked is whether you flushed.'),
        ('Wipe it out with a clean cloth', False,
         'Never put anything in your eye. Water only, for 15 minutes.'),
    ]),
]

# ------------------------------------------------------------- laser engraver

LASER = [
    _q('Can you see the laser beam that does the cutting?', [
        ('No &mdash; it is infrared and invisible', True,
         'Correct. The CO2 cutting beam is 10.6 micrometres, well outside '
         'visible light. The red dot you can see is a separate low-power '
         'alignment pointer, and the glow at the cut is the material burning. '
         'People believe they can see the laser; they are watching its effects.'),
        ('Yes, it is the red beam', False,
         'The red dot is a separate visible pointer of one milliwatt or less, '
         'there to show you where the invisible beam will land. Do not look '
         'directly at it either.'),
        ('Yes, it is the bright spot where it cuts', False,
         'That is the material burning, not the beam. The beam itself is '
         'invisible infrared.'),
        ('Only when cutting thick material', False,
         'Thickness makes no difference. Infrared is invisible at any power.'),
    ]),
    _q('What actually stops the laser firing when the lid is open?', [
        ('Interlock switches that cut the beam', True,
         'Correct, and it matters that you know it is the interlock rather than '
         'the lid. Dual redundant safety circuits mean the laser cannot fire '
         'with the door open. Defeat the interlock and you have direct access '
         'to an embedded Class 4 laser &mdash; the class that damages eyes '
         'instantly. The interlock is what protects you, not the plastic.'),
        ('The lid blocks the beam', False,
         'The lid is not the safety device. Interlock switches cut the laser '
         'the moment the door opens &mdash; which is why defeating them is so '
         'dangerous.'),
        ('Nothing &mdash; you have to switch it off yourself', False,
         'The machine has dual redundant interlocks that do this automatically. '
         'They only fail if somebody has bypassed them.'),
        ('A light sensor', False,
         'It is a mechanical interlock circuit, and it is duplicated for '
         'redundancy.'),
    ]),
    _q('Someone hands you an unlabelled sheet of plastic to cut.', [
        ('Do not cut it until you know what it is', True,
         'Correct, and this is the real failure mode &mdash; nobody knowingly '
         'cuts PVC, they cut unlabelled &ldquo;plastic&rdquo;, craft-store '
         'vinyl, or faux leather. Unknown plastic means no cut. Check the '
         'safety data sheet.'),
        ('Cut a small test piece first', False,
         'A small piece of PVC produces the same corrosive gas as a large one, '
         'and the damage to the machine begins immediately. Identify first.'),
        ('Cut it at low power', False,
         'Power does not change the chemistry. If it is PVC, decomposition '
         'happens regardless.'),
        ('Cut it with extra ventilation', False,
         'Ventilation helps you and does nothing for the machine, which the '
         'corrosive products attack from the inside for months afterwards.'),
    ]),
    _q('Why must PVC and vinyl never go in the laser?', [
        ('They release hydrogen chloride, which harms you and destroys the '
         'machine', True,
         'Correct on both halves. Hydrogen chloride plus moisture &mdash; in '
         'your lungs, and on the machine\'s optics and metal &mdash; becomes '
         'hydrochloric acid. It is a corrosive respiratory hazard to you and a '
         'slow-destruction hazard to the machine that keeps working long after '
         'the job. It also voids the warranty. (You may have heard '
         '&ldquo;chlorine gas&rdquo;; the manufacturer says hydrogen chloride.)'),
        ('They melt and make a mess', False,
         'The mess is the least of it. The decomposition products are '
         'corrosive to your airway and to the machine.'),
        ('They catch fire more easily', False,
         'Fire is a risk with almost anything in a laser. The specific reason '
         'PVC is banned is the corrosive gas it produces.'),
        ('They do not cut cleanly', False,
         'Cut quality is not the issue. This is a health and equipment '
         'destruction rule.'),
    ]),
    _q('Which operation is most likely to start a fire?', [
        ('Vector cutting', True,
         'Correct, and it is the reverse of what people assume. Cutting all the '
         'way through presents the most potential to create an open flame; '
         'raster engraving is much lower risk. Always use air assist when '
         'vector cutting.'),
        ('Raster engraving', False,
         'Engraving only marks the surface and carries far less fire risk. '
         'Cutting through is the dangerous operation.'),
        ('Running the red pointer', False,
         'The alignment pointer is a one-milliwatt visible diode. It cannot '
         'ignite anything.'),
        ('Homing the machine', False,
         'No beam fires during homing.'),
    ]),
    _q('The job will take twelve minutes. Can you go and get a drink?', [
        ('No &mdash; never leave the laser unattended', True,
         'Correct, and the manual states it as an imperative: stay with the '
         'laser, never operate it unattended. This is the one rule that turns a '
         'three-second flare-up into a shop fire. Twelve minutes is plenty of '
         'time.'),
        ('Yes, if you tell someone else to watch it', False,
         'That person is doing their own work. The operator stays.'),
        ('Yes, if the job is only engraving', False,
         'Lower risk is not no risk, and the rule does not distinguish.'),
        ('Yes, if the extraction is running', False,
         'Extraction manages fumes. It does not put out fires &mdash; and '
         'airflow can feed one.'),
    ]),
    _q('A flame appears inside the machine during a cut.', [
        ('Press the emergency stop immediately', True,
         'Correct &mdash; that is the manufacturer\'s stated instruction, and '
         'it is the only step the manual specifies. Then get an instructor. '
         'The shop has a CO2 or dry chemical extinguisher for this; know where '
         'it is before you need it.'),
        ('Open the lid and blow it out', False,
         'Opening the lid feeds the fire air. Hit the emergency stop.'),
        ('Wait to see if it goes out by itself', False,
         'Small flare-ups sometimes do. That is not a reason to wait, and '
         'debris under the cutting grid can turn one into a real fire.'),
        ('Turn up the air assist', False,
         'You are at the machine reaching for controls when you should be '
         'hitting the emergency stop.'),
    ]),
    _q('Why does debris under the cutting grid matter?', [
        ('It is fuel, and it is what turns a flare-up into a fire', True,
         'Correct. The manual calls a build-up of cutting and engraving '
         'residue dangerous and says to clear it weekly. Most laser fires are '
         'lit by the current job and fed by last month\'s scrap.'),
        ('It makes the cuts less accurate', False,
         'It does not much affect accuracy. It is a fire load.'),
        ('It blocks the extraction', False,
         'Only incidentally. The reason it is called out as dangerous is that '
         'it burns.'),
        ('It does not matter much', False,
         'It is specifically identified as dangerous in the manual, and it is '
         'why the grid is cleared on a schedule rather than when it looks bad.'),
    ]),
]

# ------------------------------------------------------------- Shaper Origin

CNC = [
    _q('Origin corrects your hand automatically. What is that correction '
       'protecting?', [
        ('The workpiece', True,
         'Correct, and this is the fact that keeps people safe. Shaper describes '
         'retraction as protecting your workpiece &mdash; it is auto-correct for '
         'your cut line, not a guard for your hands. It is a router with a robot '
         'inside, and the router is still a router.'),
        ('Your hands', False,
         'It is not a hand-protection system. Shaper frames retraction entirely '
         'in terms of protecting the workpiece. The finger guard is the actual '
         'guard.'),
        ('Both equally', False,
         'The correction exists to keep the cut on the line. Treating it as '
         'personal protection is how people get comfortable around a spinning '
         'bit.'),
        ('The router bit', False,
         'It protects the cut, not the cutter.'),
    ]),
    _q('When the bit retracts because you went out of range, does it stop '
       'spinning?', [
        ('No &mdash; it retracts, but it keeps turning', True,
         'Correct. Retraction lifts the bit; the spindle keeps running. This is '
         'why the finger guard must stay installed whenever the spindle is '
         'plugged in, and why hands stay away from the collet regardless of what '
         'the screen is doing.'),
        ('Yes, retraction stops the spindle', False,
         'It does not. Shaper\'s documentation describes retraction as lifting '
         'the cutter to protect the workpiece &mdash; nothing about stopping '
         'rotation.'),
        ('Only if you release the handles', False,
         'Do not rely on that. Assume the bit is spinning whenever the spindle '
         'is powered.'),
        ('It slows to a safe speed', False,
         'There is no such behaviour and no such thing as a safe speed for an '
         'exposed router bit.'),
    ]),
    _q('Why is running the dust extraction not optional?', [
        ('Dust degrades the tracking the tool depends on, as well as your '
         'lungs', True,
         'Correct, and it is a neat coincidence of hazards. Origin navigates by '
         'camera, reading tape on the workpiece. Dust in the air and on the tape '
         'degrades tracking &mdash; Shaper says failure to use extraction can '
         'severely degrade performance and accuracy. And wood dust is a '
         'recognised carcinogen. Same control, two hazards.'),
        ('Only to keep the workshop tidy', False,
         'Tidiness is a side effect. Extraction is required for the tool to '
         'track accurately, and wood dust is a genuine respiratory hazard.'),
        ('Only for your lungs', False,
         'True but incomplete. Dust also blinds the camera system that the '
         'automatic correction relies on.'),
        ('It is optional for small cuts', False,
         'Shaper says to use extraction at all times.'),
    ]),
    _q('You are holding the tool. Does the workpiece still need clamping?', [
        ('Yes &mdash; always', True,
         'Correct, and the reasoning trips people up. On a normal CNC the tool '
         'is fixed and the work is clamped. On Origin you move, so students '
         'reason &ldquo;I am holding the tool, I will hold the wood too&rdquo; '
         '&mdash; which is exactly the prohibited practice. There is a second '
         'reason: the tracking tape is on the workpiece, so a piece that shifts '
         'destroys the coordinate system as well as your control.'),
        ('No, because you control the tool', False,
         'The manual says to use clamps and never hold work by hand or against '
         'the body. And if the work moves, so does the tape Origin is '
         'navigating by.'),
        ('Only for small pieces', False,
         'Small pieces are more likely to move, not less.'),
        ('Only if you are cutting all the way through', False,
         'Any cut can grab. Clamp it.'),
    ]),
    _q('What protective equipment does Shaper require?', [
        ('Eye and ear protection, both', True,
         'Correct &mdash; the safety guide names both explicitly. Routers are '
         'genuinely loud enough to damage hearing, which people underestimate '
         'because the noise is brief.'),
        ('Eye protection only', False,
         'Both are named. Router noise is loud enough to matter, even in short '
         'bursts.'),
        ('A respirator', False,
         'Shaper does not require one; it controls dust through mandatory '
         'extraction instead. If this shop requires a mask for hardwood or MDF, '
         'that is a shop rule rather than a manufacturer instruction.'),
        ('Gloves', False,
         'Shaper does not mention gloves &mdash; and standard practice is that '
         'gloves come off around anything that spins.'),
    ]),
    _q('What is the most common mistake people make with Origin?', [
        ('Watching the screen instead of the tool', True,
         'Correct. It is a router that feels like a video game. People get '
         'absorbed in the on-screen path and let the physical machine wander, '
         'tip, or run into a clamp. The screen tells you where the cut is going; '
         'it does not tell you what the tool is doing.'),
        ('Cutting too fast', False,
         'It happens, and Origin will tell you to slow down &mdash; but the '
         'characteristic mistake with this tool is attention, not feed rate.'),
        ('Using the wrong bit', False,
         'Worth avoiding, but not the defining mistake with this particular '
         'machine.'),
        ('Forgetting to charge it', False,
         'An inconvenience, not a hazard.'),
    ]),
]

# ------------------------------------------------------------------- cobots

COBOT = [
    _q('The UR arms are called collaborative robots. What does that actually '
       'mean?', [
        ('That a properly designed application can be collaborative &mdash; not '
         'that the robot is safe by itself', True,
         'Correct, and the standards bodies now say so explicitly. Universal '
         'Robots\' own words: cobots alone are not collaborative, only cobot '
         'applications can be collaborative. The 2025 revision of ISO 10218 '
         'deleted the term &ldquo;collaborative robot&rdquo; entirely, because '
         'only actual use can be assessed as collaborative.'),
        ('That it is safe to work next to without precautions', False,
         'This is the widespread misconception, and it is the reason this '
         'question exists. A cobot is not inherently safe &mdash; the '
         'application around it is what is assessed.'),
        ('That it cannot hurt you', False,
         'It certainly can. Force limiting is designed around the onset of '
         'pain, not the absence of contact.'),
        ('That it stops if you touch it', False,
         'That describes one of several safety techniques, and only when '
         'configured. It is not what the word means.'),
    ]),
    _q('The arm is force-limited. Why can the tool on the end still hurt you '
       'badly?', [
        ('The end effector is outside the robot\'s safety system', True,
         'Correct, and this is the single most important fact about these '
         'machines. The manual is explicit: the end effector is not protected by '
         'the UR safety system and is not monitored. A force-limited arm holding '
         'an unmonitored gripper, a sharp tool or a hot iron is a force-limited '
         'arm delivering an unlimited hazard.'),
        ('It is not &mdash; the force limit covers everything attached', False,
         'It does not. UR states plainly that the end effector and its cable are '
         'not monitored by the safety system.'),
        ('Only if the tool is heavy', False,
         'Weight is not the issue. The tool is simply outside the safety '
         'system, whatever it weighs.'),
        ('Only in free-drive mode', False,
         'The end effector is unmonitored in every mode.'),
    ]),
    _q('A sharp tool on a force-limited arm &mdash; why does the force limit '
       'not save you?', [
        ('A point concentrates the same force into a tiny area, so the '
         'pressure is enormous', True,
         'Correct. Force limiting caps force; a needle point turns that same '
         'force into very high pressure over a tiny area, which is how skin gets '
         'punctured. UR lists penetration of skin by sharp edges and points as a '
         'specific hazard.'),
        ('It does &mdash; a limited force cannot break skin', False,
         'Force and pressure are different quantities. Spread over a palm the '
         'force is harmless; concentrated on a point it punctures.'),
        ('Sharp tools cannot be fitted to a cobot', False,
         'They routinely are &mdash; deburring bits, blades, grippers. That is '
         'exactly why the risk assessment covers the tool.'),
        ('Only if the robot is moving fast', False,
         'Speed is not required. The geometry of the point does the work.'),
    ]),
    _q('When is a slow-moving cobot most likely to hit hard?', [
        ('When it is stretched out near full reach, or working close to its '
         'base', True,
         'Correct, and it is deeply counterintuitive. UR calls it the knee-joint '
         'effect: as the arm extends, high forces can be generated radially at '
         'low speeds; and the short leverage arm near the base can also produce '
         'high forces at low speed. Students judge danger by visible speed, '
         'which is the wrong variable.'),
        ('When it moves fast in the middle of its reach', False,
         'That looks alarming and is generally better understood by the safety '
         'system. The dangerous cases are geometric, at the extremes of the '
         'arm\'s reach.'),
        ('It never hits hard when moving slowly', False,
         'This is the assumption that gets people hurt. Slow does not mean '
         'gentle when the geometry is against you.'),
        ('Only when carrying maximum payload', False,
         'Payload contributes, but the knee-joint effect happens because of '
         'arm geometry, not load.'),
    ]),
    _q('Which is the more important safety difference between a UR3 and a UR5?', [
        ('The reach &mdash; 500&nbsp;mm against 850&nbsp;mm', True,
         'Correct. People memorise the payload difference, 3&nbsp;kg against '
         '5&nbsp;kg, and then stand comfortably inside a UR5\'s reach. The UR5 '
         'sweeps a sphere about 1.7&nbsp;m across; the UR3 about 1&nbsp;m. Where '
         'you can safely stand is the difference that matters.'),
        ('The payload &mdash; 3&nbsp;kg against 5&nbsp;kg', False,
         'True, and it is what everyone remembers &mdash; but the reach '
         'difference is what determines whether you are standing inside the '
         'working envelope.'),
        ('The UR5 is faster', False,
         'Speed is configurable on both. The fixed difference that affects '
         'where you stand is reach.'),
        ('There is no meaningful difference', False,
         'The UR5 reaches 850&nbsp;mm against the UR3\'s 500&nbsp;mm. That is a '
         'very different amount of room to stay clear of.'),
    ]),
    _q('You are about to release the brakes to move the arm by hand, and there '
       'is a heavy gripper fitted.', [
        ('Support the arm first &mdash; it will drop', True,
         'Correct. With the brakes off, the arm is subject to gravity like any '
         'other object. An unsupported arm with a heavy end effector falls, '
         'taking fingers with it if they are underneath.'),
        ('Nothing special &mdash; the motors hold it', False,
         'Releasing the brakes is precisely the act of removing what holds it '
         'up. Support it before you release.'),
        ('Move it quickly before it settles', False,
         'It does not settle. It falls.'),
        ('Set it to a slow speed first', False,
         'Speed settings are irrelevant with the brakes off. Gravity is doing '
         'the moving.'),
    ]),
    _q('You change the gripper on the arm for a different tool. What now?', [
        ('The risk assessment has to be redone', True,
         'Correct, and it is the mistake that matters most in a school. The arm '
         'is certified; the tool is not. The risk assessment covers the end '
         'effector, the workpiece and the surrounding equipment as well as the '
         'robot &mdash; change the tool and the assessment no longer describes '
         'what is in the room.'),
        ('Nothing &mdash; the robot is the same', False,
         'The robot is the same and the hazard is not. The end effector is '
         'outside the safety system, so changing it changes the actual danger.'),
        ('Just check the payload is under the limit', False,
         'Necessary but nowhere near sufficient. A light tool can be sharp, '
         'hot, or create a pinch point.'),
        ('Only if the new tool is heavier', False,
         'A lighter but sharper tool is more dangerous, not less.'),
    ]),
]

# --------------------------------------------------------------- ergonomics

ERGO = [
    _q('How often should you look away from the screen, and at what?', [
        ('Every 20 minutes, at something about 20 feet away, for 20 seconds', True,
         'Correct &mdash; the 20-20-20 rule. Focusing at one distance for hours '
         'keeps the muscles inside the eye contracted, and looking far away is '
         'what lets them relax. It works because it is short enough that you '
         'will actually do it.'),
        ('Every couple of hours, for a few minutes', False,
         'Too infrequent to help. The strain builds continuously; short frequent '
         'breaks beat rare long ones.'),
        ('Whenever your eyes hurt', False,
         'By the time they hurt, the strain has already accumulated. The point '
         'of a timed rule is to break the pattern before symptoms appear.'),
        ('Only if you wear glasses', False,
         'It applies to everyone. Eye strain from sustained near focus is not '
         'about your prescription.'),
    ]),
    _q('Where should the top of your monitor be?', [
        ('At or slightly below eye level', True,
         'Correct. That puts your gaze slightly downward, which is the neutral '
         'resting position for the neck and lets your eyelids cover more of the '
         'eye &mdash; which reduces dryness as well as neck strain.'),
        ('Well above eye level, so you sit up straight', False,
         'Looking up for hours is what causes neck and shoulder pain. The top of '
         'the screen at or just below eye height is the target.'),
        ('As low as possible', False,
         'Too low and you crane forward and down, which is how the classic '
         'hunched CAD posture develops.'),
        ('It does not matter if the chair is comfortable', False,
         'Screen height sets your head and neck position regardless of how good '
         'the chair is.'),
    ]),
    _q('You have been modelling in Fusion for two hours straight and your '
       'wrist aches.', [
        ('Stop, move, and change what you are doing before it gets worse', True,
         'Correct. Repetitive strain builds silently and then becomes chronic, '
         'and once it is chronic it can follow you into a career that involves '
         'a mouse every day. Early aching is the warning, not the injury.'),
        ('Push through &mdash; it will loosen up', False,
         'It does not loosen up. Repetitive strain injuries get worse with '
         'continued use, and the point of the ache is to make you stop.'),
        ('Switch to your other hand', False,
         'Now you have two sore wrists. Take a break and change posture.'),
        ('Ignore it, you are young', False,
         'Age is not protection. RSI in students who model for hours is real, '
         'and it is the injury from this shop most likely to still be with you '
         'at thirty.'),
    ]),
    _q('Why does ergonomics belong in a safety test at all?', [
        ('Because injuries that build slowly are still injuries', True,
         'Correct. A saw takes a finger in a second and everybody respects it. '
         'Four years of bad posture takes your neck and your wrists slowly '
         'enough that nobody warns you. Both are shop injuries; only one of '
         'them is dramatic.'),
        ('It does not, it is just good advice', False,
         'Repetitive strain and eye strain are recognised occupational '
         'injuries. You will spend more hours at a computer in this program '
         'than on any machine in the room.'),
        ('Because the school requires it', False,
         'The reason is better than that. You spend more time at a workstation '
         'than at any machine here, and the resulting injuries are permanent.'),
        ('Only for people who already have problems', False,
         'The whole point is preventing them from starting.'),
    ]),
]

QUIZZES = {
    'hand': ('Hand tools', 'Knives, cutters and everything on the bench that has '
             'an edge.', HAND),
    'heat': ('Soldering and hot glue', 'The bench hazards that do not look hot.',
             HEAT),
    'power': ('Power tools', 'Chop saw, drill press, rotary tools &mdash; anything '
              'that spins.', POWER),
    'fdm': ('Filament 3D printers', 'The Bambu Lab machines: heat, fumes and long '
            'unattended runs.', FDM),
    'polyjet': ('Resin 3D printing', 'The Stratasys J55. This one is chemistry, '
                'not heat.', POLYJET),
    'laser': ('Laser engraver', 'The Epilog FusionPro. Fire, fumes, and a beam '
              'you cannot see.', LASER),
    'cnc': ('Handheld CNC', 'Shaper Origin. Clever software, ordinary router bit.',
            CNC),
    'cobot': ('Collaborative robots', 'UR3 and UR5. Why "collaborative" is not a '
              'synonym for safe.', COBOT),
    'ergo': ('Working at a computer', 'The injury that takes four years instead '
             'of a second.', ERGO),
}

SOURCES = [
    ('Epilog FusionPro laser system manual',
     'https://www.epiloglaser.com/assets/downloads/manuals/fusion-pro_manual.pdf'),
    ('Epilog &mdash; materials unsafe to engrave or cut',
     'https://www.epiloglaser.com/how-it-works/faq/laser-machine-unsafe-materials/'),
    ('Stratasys &mdash; SUP710 safety data sheet',
     'https://www.stratasys.com/siteassets/materials/materials-catalog/polyjet-materials/polyjet-support-materials/sds-06297_26sep21_british-english_eghs_support_sup710.pdf'),
    ('Stratasys Academy &mdash; J5 Series training (our J55)',
     'https://support.stratasys.com/en/Welcome/Training/PolyJet/J5-Series'),
    ('Stratasys &mdash; removing support material',
     'https://support.stratasys.com/SupportCenter/HTML5UserGuides/Objet260_UG_May_2022/Content/7_Topics_Handling/Removing_the_Support_Mat.htm'),
    ('Universal Robots Academy — free e-learning (incl. Risk Assessment)',
     'https://academy.universal-robots.com/free-e-learning/'),
    ('Universal Robots user manual',
     'https://www.universal-robots.com/manuals/'),
    ('Universal Robots &mdash; the risk assessment',
     'https://www.universal-robots.com/blog/the-risk-assessment-complex-challenging-and-absolutely-required/'),
    ('A3 &mdash; five key collaborative robot safety concepts',
     'https://www.automate.org/robotics/industry-insights/five-key-collaborative-robot-safety-concepts'),
    ('Shaper Origin product manual',
     'https://assets.shapertools.com/manual/Shaper_Origin_Product_Manual.pdf'),
    ('UL Chemical Insights &mdash; 3D printing emissions',
     'https://chemicalinsights.ul.org/3d-printing/'),
    ('NIOSH &mdash; characterizing 3D printing emissions',
     'https://www.cdc.gov/niosh/bulletin/2018/3d-printing.html'),
    ('LBNL &mdash; safe soldering work practices',
     'https://amo-csd.lbl.gov/downloads/safeSolderingRules.pdf'),
    ('UNC EHS &mdash; soldering safety',
     'https://ehs.unc.edu/topics/soldering-safety/'),
]
