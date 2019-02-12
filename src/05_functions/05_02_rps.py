'''
Code a game of rock paper scissors.

'''
import random

# function to get hand based on number
# the function should take in a number and return the string representation of the hand
def get_hand(hand):
    # 0 = scissor, 1 = rock, 2 = paper
    # for example if the variable hand is 0, it should return the string "scissor"
    if hand == 0:
        return "scissor"
    elif hand == 1:
        return "rock"
    else:
        return "paper"
`
# function should take in two hands and return a string "You won!" or "You lost :(" or "You tied!"
def determine_winner(computer, player):
    if computer == player:
        return "You tied!"
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You won!"
    else:
        return  "You lost! :("

'''
Start here
'''

number_person = ""
while number_person.lower() != "quit":

    number_person = input("What do you choose? 0 = scissor, 1 = rock, 2 = paper (type 'quit' to stop playing)")

    if number_person.lower() == "quit":
        print('Thanks for playing! :)')
        break

    number_person = int(number_person)

    # generate a random number 0-2 to use for the computer's hand
    number_computer = random.randint(0,2)

    # call the function get_hand to get the string representation of the user's hand
    hand_person = get_hand(number_person)

    # call the function get_hand to get the string representation of the computer's hand
    hand_computer = get_hand(number_computer)
    # call the function determine_winner to figure out the winner
    winner = determine_winner(hand_computer,hand_person)

    # print out the player hand and computer hand
    print(f'You played {hand_person} while the computer choose {hand_computer}.')

    # print out the winner
    print(winner)
    number_person = ""
