# Practical Problem 8
# User input a number, a function will give its multiplication table with one wrong value in any position,
# another function will have to detect that and tell the user that in which position the table is false

from random import randint


def multiplicationTable(n):
    table = [n * (i + 1) for i in range(10)]
    table[randint(0, 9)] = table[randint(0, 9)] + randint(0, 10)
    print(table)
    return table


def tableChecker(n):
    for index, i in enumerate(multiplicationTable(n)):
        if i != n * (index + 1):
            return index
    else:
        return None


if __name__ == '__main__':

    wrong = tableChecker(int(input("Enter an integer to get its table: ")))
    if wrong:
        print(f"Rohan gives a wrong output at {wrong + 1} position.")
