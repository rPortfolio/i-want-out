#Stores data about animals, enemies, rooms, and more
from menu import MenuOption
from battler import Battler
from commands import *
from room import Room


title_text = """
      :::::::::::        :::       :::     :::     ::::    ::: :::::::::::          ::::::::  :::    ::: ::::::::::: 
         :+:            :+:       :+:   :+: :+:   :+:+:   :+:     :+:             :+:    :+: :+:    :+:     :+:      
        +:+            +:+       +:+  +:+   +:+  :+:+:+  +:+     +:+             +:+    +:+ +:+    +:+     +:+       
       +#+            +#+  +:+  +#+ +#++:++#++: +#+ +:+ +#+     +#+             +#+    +:+ +#+    +:+     +#+        
      +#+            +#+ +#+#+ +#+ +#+     +#+ +#+  +#+#+#     +#+             +#+    +#+ +#+    +#+     +#+         
     #+#             #+#+# #+#+#  #+#     #+# #+#   #+#+#     #+#             #+#    #+# #+#    #+#     #+#          
###########          ###   ###   ###     ### ###    ####     ###              ########   ########      ###           
"""


intro_text = [
    "It had been years since any animal inside the zoo has ran free.",
    "Their space spanned to the limits of their dismal enclosures.",
    "The animals were kept like prisoners.",
    "They were weak, hungry, and desperate for freedom.",
    "One day the they devised a plan.",
    "A few brave animals would attempt an escape and get help from the outside.",
]


rules = """
        You will chose a team of animals, each with unique skills.
        You will chose a path to follow and try to avoid enemies.
        You will have to defeat all your foes before you can progress.
        Battlers take their turns in speed order.
        There are several type of action you can use in combat.
        Actions will be marked with symbols to indicate what it does.
        ⸸ - Standard Attack
        ♡ - Healing
        ϟ - Attack that uses speed instead of power but lowers user's speed
        △ - Targets all (Can be either enemies or party members)
        ⚄ - Has a 30% chance of hitting for 3% damage
        ❣ - Hits for double damage but deals recoil damage to the user
        Actions may be marked with multiple symbols.
        """


actions = {
    "attack" : MenuOption("Attack ⸸", Action(True, False, Attack)),
    "attack_all" : MenuOption("Attack All ⸸△", Action(True, True, Attack)),
    "recover" : MenuOption("Recover ♡", Action(False, False, Recover)),
    "skirmish" : MenuOption("Skirmish ϟ△", Action(True, True, SpeedAttack)),
    "backhand" : MenuOption("Backhand ϟ△", Action(True, True, SpeedAttack)),
    "double_claw" : MenuOption("Double Claw ❣", Action(True, False, DoubleAttack)),
    "bite" :  MenuOption("Bite ⚄", Action(True, False, ChanceAttack)),
    "swing" :  MenuOption("Swing ⚄", Action(True, False, ChanceAttack)),
    "care" : MenuOption("Care ♡△", Action(False, True, Recover)),
    "punch" :  MenuOption("Punch ⚄", Action(True, False, ChanceAttack)),
    "taser" :  MenuOption("Taser ❣", Action(True, False, DoubleAttack)),
    "ram" :  MenuOption("Ram ❣", Action(True, False, DoubleAttack)),
    "honk" : MenuOption("Honk ⸸△", Action(True, True, Attack))
}

party_members = [
    MenuOption(
        "Cheetah", 
        Battler(
            "Cheetah", 
            True, 
            40, 
            35, 
            12, 
            10, 
            [
                actions["attack"],
                actions["recover"],
                actions["skirmish"],
                actions["bite"]
            ])
    ),
    MenuOption(
        "Lion", 
        Battler(
            "Lion", 
            True, 
            60,
            24, 
            12, 
            14, 
            [
                actions["attack"],
                actions["recover"],
                actions["double_claw"],
                actions["bite"]
            ])
    ),
    MenuOption(
        "Silverback Gorilla", 
        Battler(
            "Silverback Gorilla", 
            True, 
            44,
            14, 
            12, 
            21, 
            [
                actions["attack"],
                actions["recover"],
                actions["swing"],
                actions["care"]
            ])
    ),
    MenuOption(
        "Goat", 
        Battler(
            "Goat", 
            True, 
            38,
            20, 
            18, 
            40, 
            [
                actions["attack_all"],
                actions["recover"],
                actions["ram"],
                actions["bite"]
            ])
    ),
]

enemies = {
    "officer" : Battler(
        "Zoo Officer", 
        False, 
        35, 
        10,
        10, 
        10, 
        [
            actions["backhand"],
            actions["punch"]
        ]
    ),
    "security" : Battler(
        "Security Guard",
        False,
        70,
        28,
        18,
        0,
        [
            actions["punch"],
            actions["taser"]
        ]
    ),
    "goose" : Battler(
        "Rogue Goose",
        False,
        55,
        100,
        33,
        0,
        [
            actions["honk"],
            actions["bite"]
        ]
    ),
    "medic" : Battler(
        "First Aid",
        False,
        50,
        10,
        0,
        14,
        [
            actions["recover"],
            actions["attack"]
        ]
    )
}



#Rooms
exit = Room("Exit", None, "You Escaped!", None)

main_path_3 = Room("Main Path (Final Stretch)", [exit], "Freedom", [enemies["security"], enemies["security"]])
main_path_2 = Room("Main Path 2 (Almost There)", [main_path_3], "There's no way back now, be strong!", [enemies["officer"], enemies["security"]])
main_path = Room("Main Path (Direct But Risky)", [main_path_2], "You were spotted, act quickly!", [enemies["officer"], enemies["officer"]])

ticket_office = Room("Ticket Office", [exit], "Freedom", [enemies["security"], enemies["medic"]])

central_square = Room("Central Square (Half Way There!)", [ticket_office], "Push forward!", [enemies["officer"], enemies["officer"], enemies["officer"]])

back_alley = Room("Back Alley (Likely Safe)", [central_square], "Nothing here.  Perfect place to hide.", None)

red_street_2 = Room("Red Street 2 (Covered by Shade; Unpredictable)", [central_square], "You weren't so lucky this time.", [enemies["officer"], enemies["officer"]])
red_street = Room("Red Street (Covered by Shade; Unpredictable)", [red_street_2], "It seems as though you're alone.", None)


cage_row = Room("Cage Row", [central_square], "Keep going.  Get help for them.", [enemies["officer"]])
bird_enclosure = Room("Bird Enclosure", [cage_row, back_alley], "Can you believe the audacity?", [enemies["goose"]])

starting_room = Room("Caged Animals Area", [main_path, red_street, bird_enclosure], "Chose your path ahead carefully.", None)
