# Terminal program based on a 90s paper fortune-teller game
# Intro:
import random

print("Let's go back to the 90's with this fortune teller game!")
print("I hold out a fortune teller origami game made of brightly coloured paper. One square is red, one purple, one green, and one blue.")
print()

colors = ['red', 'purple', 'blue', 'green']


def color_picker():
    fortunes = ["Today will be a beautiful day, make the most of it!", "You are incredibly clever and will go far in life.",
                "Do a good deed today, and you will receive kindness in turn.", "You will soon discover your true hidden talent.",
                "It's never too late to become the person you want to be.", "If you think you know all, you've forgotten too much.",
                "Create the life you wish to live.", "Do something new every day!"]
    alt_fortunes = ["To truly find yourself, you should play hide and seek alone.", "Error 404: Fortune not found.",
                    "Pigeon poop burns the retinas for 13 hours. Be wary of the skies.", "The fortune you seek is elsewhere.",
                    "You don't wanna know, actually...", "Be true to yourself, unless you're a ned.",
                    "I dunno, man.", "The road of indecision is paved with dead squirrels."]

    color_choice = input('Which colour do you choose? Purple, red, green, or blue?')
    color_choice = color_choice.lower()
    print()

    if color_choice in colors:
        print("Mmk, let's go with " + color_choice + ".")
    else:
        fortunes = alt_fortunes
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
        else:
            print('Nah fam, gotta play along here! Try red, blue, purple, or green.')
            print()

            color_choice = color_picker()

    return color_choice, fortunes


def color_counter(color_picked):
    print("I move my fingers within the origami contraption, moving it back and forth as I spell: ")
    for letter in color_picked:
        print(letter.upper())

    numbers = []
    if len(color_picked) % 2 == 0:
        numbers = ['one', 'two', 'five', 'six']
    else:
        numbers = ['three', 'four', 'seven', 'eight']
    print()
    return numbers


def pick_a_number(numbers_list):
    numbers_str = (str(n) for n in numbers_list)
    print("I stop moving my fingers, revealing four numbers in the middle: " + ', '.join(numbers_str) + '.')
    first_num = input('Which number do you choose?')
    print()
    return first_num


def number_speller(num_picked, num_set):

    if num_picked.lower() not in num_set:
        if num_picked == '1':
            num_picked = 'one'
        elif num_picked == '2':
            num_picked = 'two'
        elif num_picked == '3':
            num_picked = 'three'
        elif num_picked == '4':
            num_picked = 'four'
        elif num_picked == '5':
            num_picked = 'five'
        elif num_picked == '6':
            num_picked = 'six'
        elif num_picked == '7':
            num_picked = 'seven'
        elif num_picked == '8':
            num_picked = 'eight'

    if num_picked not in num_set:
        print("Womp womp, I'll pick for you, then.")
        num_picked = num_set[random.randint(0, 3)]
        print("Hmmm, let's go with the number " + num_picked)

    if num_picked in num_set:
        print("I manipulate the origami contraption, moving it once more as I spell: ")
        for letter in num_picked:
            print(letter.upper())

        numbers = []
        if len(num_picked) % 2 == 0:
            numbers = ['one', 'two', 'five', 'six']
        else:
            numbers = ['three', 'four', 'seven', 'eight']
        print()

    return numbers


def fortune_picker(second_number, second_number_set, fortunes_listed):
    if second_number.lower() not in second_number_set:
        if second_number == '1':
            second_number = 'one'
        elif second_number == '2':
            second_number = 'two'
        elif second_number == '3':
            second_number = 'three'
        elif second_number == '4':
            second_number = 'four'
        elif second_number == '5':
            second_number = 'five'
        elif second_number == '6':
            second_number = 'six'
        elif second_number == '7':
            second_number = 'seven'
        elif second_number == '8':
            second_number = 'eight'

    if second_number not in second_number_set:
        print("Well okay, I'll have to choose for you.")
        second_number = second_number_set[random.randint(0, 3)]
        print("Let's see what fortune number  " + second_number + 'has to say for you.')
        print()

    second_num_i = second_number_set.index(second_number)

    if second_number_set == ['one', 'two', 'five', 'six']:
        second_number_set = [1, 2, 5, 6]
    else:
        second_number_set = [3, 4, 7, 8]

    second_number = second_number_set[second_num_i]
    fortune = fortunes_listed[second_number_set[second_num_i]]

    print("I carefully unfold the triangular flap of paper and read the fortune within: ")
    print(fortune)


color, fortune_list = color_picker()
first_number_set = color_counter(color)
first_number = pick_a_number(first_number_set)
second_num_set = number_speller(first_number, first_number_set)
second_num = pick_a_number(second_num_set)
fortune_picker(second_num, second_num_set, fortune_list)
