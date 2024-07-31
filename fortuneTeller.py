# Terminal program based on a 90s paper fortune-teller game
# Intro:

print("Let's go back to the 90's with this fortune teller game!")
print()
print("I hold out a fortune teller origami game made of brightly coloured paper. One square is red, one purple, one green, and one blue.")

colors = ['red', 'purple', 'blue', 'green']


def color_picker():
    color_choice = input('Which colour do you choose? Purple, red, green, or blue?')
    color_choice = color_choice.lower()

    if color_choice == "purple with pink polkadots" or color_choice == 'pink with purple polkadots':
        print('Purple it is, smarty pants!')
        color_choice = 'purple'
    elif color_choice == 'chartreuse':
        print("That's...green, right? Yeah, that's still green.")
        color_choice = 'green'
    elif ('tardis' or 'police box') in color_choice:
        print("A person of great culture, I see. Police box blue it is!")
        color_choice = 'blue'
    elif 'blood' in color_choice:
        print('Okay, Dr. Drac. Red shall be yours.')
        color_choice = 'red'
    elif color_choice not in colors:
        print('Nah fam, gotta play along here! Try red, blue, purple, or green.')
        color_choice = color_picker()
    else:
        print("Mmk, let's go with " + color_choice + ".")
    return color_choice


color = color_picker()
