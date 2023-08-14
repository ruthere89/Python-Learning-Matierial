# for the area of a circle
import math
py = math.pi


def area_circle():
    rad = int(input("Please provide a number for the radius of your circle: "))
    area = py * (rad ** 2)
    print("The area of a circle with radius ", rad, " is ", area, " units squared.")


area_circle()

# to count consonants in a word, sorry this is a long one as I was attempting some Karen explaining
# splits words into letters, but only once per letter it seems
def split_word():
    wordy = input("Please give me a word: ")
    get_list = set(wordy)
    print(get_list)


split_word()


# splits using a seperator
def splity():
    some_word = input("Please give me a word: ")
    list_me = some_word.split()
    print(list_me)


splity()


# splits into letters in proper order and proper number of each
def another_split():
    got_words = input("please give me a word: ")
    some_list = []

    for letter in got_words:
        some_list.append(letter)

    print(some_list)


another_split()


def actual_function():
    this_word = input("please give me a word: ")
    word_list = []
    vowel_list = ["a", "e", "i", "o", "u"]
    vowel = 0
    consonants = 0
    for letter in this_word:
        word_list.append(letter)
        if letter in vowel_list:
            vowel = vowel + 1
        else:
            consonants = consonants + 1
    print("number of vowels = " + str(vowel),  "number of consonants = " + str(consonants))


actual_function()

# factorials


def factorials(n):
    if n == 1:
        return 1
    else:
        return n * factorials(n - 1)


som_num = int(input("Please provide a number to return a factorial of number: "))
this_result = factorials(som_num)
print("The factorial of ", som_num, " is ", this_result)

# upper case everything


def force_upper():
    something_here = input("Say some words: ").upper()
    print(something_here)
    print("Wham, bam, thank you mam. It is now all uppercase...")


force_upper()

# check if a number is even


def is_eve_odd(n):
    if n % 2 == 0:
        print("Is even!")
    else:
        print("Is odd!")


is_eve_odd(45)

# print maximum value of a set of defined numbers


def maxi(a, b, c):
    print (max(a, b, c))


maxi(20, 45, 10)

# a variant of roll calling


def roll_call(a):
    is_list = [2, 3, 5, 6, 8, 9, 10]
    if a in is_list:
        print("Yep, they there.")
    else:
        print("Not there.")


roll_call(10)

# math related functions


def maths(a, b):
    sums = a + b
    diff = a - b
    prod = a * b
    quot = a / b
    print(sums, diff, prod, quot)


maths(10,12)

# counting vowels in a word, similar to consonants, but a different method, and it failed
import string


def letter_count(some_word):
    vowelz = ['a', 'e', 'i', 'o', 'u']
    consonants = 0
    vowels = 0
    letter_list = string.ascii_letters

    if n in len()
