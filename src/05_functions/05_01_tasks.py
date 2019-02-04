'''

Write a script that completes the following tasks.

'''
def divisible_by_4_and_7(n):
    if n % 4 == 0 and n % 7 == 0:
        return True
    else:
        return False

def divisible_by_4_or_7(n):
    if n % 4 == 0 or n % 7 == 0:
        return True
    else:
        return False


def divisible_by_4_or_7_excl(n):
    if n % 4 == 0 and n % 7 != 0:
        return 4
    elif n % 4 != 0 and n % 7 == 0:
        return 7
    else:
        return False


# takes in a number from the user between 1 and 1,000,000,000
user_number = int(input("Type a number between 1 and 1,000,000,000."))

# calls a function that determines whether the number is divisible by both 4 and 7
result_1 = divisible_by_4_and_7(user_number)
# calls a function that determines whether the number is divisible by 4 or 7
result_2 = divisible_by_4_or_7(user_number)
# calls a function that determines whether the number is divisible by 4 or 7 exclusively
result_3 = divisible_by_4_or_7_excl(user_number)
# print the results

print(f'The number is divisible by both 4 and 7: {result_1}\n The number is divisible by 4 or 7: {result_2}\n The number is divisible by 4 or 7 exclusively: {result_3}')
