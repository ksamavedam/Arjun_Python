import sys
import getpass

user1 = input("What's your name?")
user2 = input("And your name?")

user1_answer = getpass.getpass(user1 + " do you want to choose rock, paper or scissors?")
user2_answer = getpass.getpass(user2 + " do you want to choose rock, paper or scissors?")
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("%s wins!"% user1)
        else:
            return("%s wins!"% user2)
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("%s win!"% user1)
        else:
            return("%s wins!"% user2)
    elif u1 == 'paper':
        if u2 == 'rock':
            return("%s wins!"% user1)
        else:
            return("%s win!"% user2)
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))