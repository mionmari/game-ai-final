# The script of the game goes in this file.

# DEFS
define b = Character("Borkugo", color = "#FFA500")
define b2 = Character("<Some pink-haired anime dogboy i found online dont judge me ok>", color = "#FFC0CB")

define b_aff =  0
define b2_aff =  10000000
define DMG = 0

# INITIALIZE PYTHON
# $ = ONE-LINE PYTHON STATEMENT
init python:
    import random as r

# NEEDS A START LABEL
label start:
    # YOU CAN ALSO INITIALIZE RPY VARIABLES AT RUNTIME IN LABELS (ALL GLOBAL >:O)
    image db = im.Scale("dog boy.png", 700, 700)
    image db2 = im.Scale("dog boy 2.png", 500, 700)

    # BACKGROUND SCENE / DOG PARK.PNG
    scene dog park

    # CHAR SPRITE
    show db

    # DIALOGUE
    b "Welcome to the dog park, u PIECE OF TRASH!"
    b "I'm Borkugo!!!! I'm aggressive and I hate everyone!!!!!!!! >:("

    menu:
        "You see a cat in the streets. What do you do?"

        "Chase it down in Borkugo's name!!":
            "You bring the prey back. Borkugo is pleased."
            "+20 affinity points."
            $ b_aff += 20

        "Approach it very gently and befriend it with tuna.":
            "Borkugo looks hurt, and holds back tears."
            "-200 affinity points."
            $ b_aff -= 200

        "Meow playfully.":
            "Borkugo attacks! Take 20 DMG."
            "-20 affinity points."
            $ DMG += 20
            $ b_aff -= 20
    jump db2

label db2:
    hide db
    show db2

    "Whoah, what?? TWO doggos???? This is TOO MANY KLDSJFLKDAFJLAKDFJLKAD"

    b2 "hewwo!!!! i'm <Some pink-haired anime dogboy i found online dont judge me ok>!!!!"
    b2 "i'm bright and cheerful!!! i love everyone!!!! {b}uwuuuu{/b}"
    b2 "{b}i love you the most though!!!!! for real ur doing great!!{/b} ^w^"

    menu:
        "You see a cat in the streets. What do you do?"

        "Cuddle it":
            b2 "its oki!! im poly!! OwO"
            "please end me"
            "+420 affinity points"
            $ b2_aff += 420

        "Approach it very gently and befriend it with tuna.":
            b2 ";W;;;; ur like, SOOOOO heckin sweet!!!!! ily forever!!!"
            "+1000000 affinity points"
            $ b2_aff += 1000000

        "Meow playfully.":
            b2 "did you..... just {i}nya........{/i} in real life?..... i-i'm sorry,, i have to go...."
            "take a d20 emotional damage."
            python:
                DMG += r.randint(1, 20)
                b2_aff = -1

label end_screen:
    show db at left
    show db2 at right

    if b_aff > 0 or b2_aff > 0:
        "You win!"
    else:
        "You lose!"

    "YOU TOOK [DMG] DAMAGE."
    "BORKUGO LOVES U [b_aff] MUCH."
    "<THE OTHER ONE> LOVES U [b2_aff] MUCH."

    # This ends me
    return