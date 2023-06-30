# is a number within a certain range?


def in_within(x):
    if 90 < x < 110 or 190 < x < 210:
        print("congrats")
    else:
        print("go away")


x = input("Gimme number only ")
in_within(int(x))

# for every letter in word, print it 3x


def triple_it():
    word = input("Gimme word, just one please: ")
    new_word = " "
    for letter in word:
        new_word = new_word + letter*3
    print(new_word)


triple_it()

# to be honest, I don't actually remember what this one is supposed to do...


def strange_name():
    name = str(input("Provide a name without numbers: ").lower())
    # Lookin' at you, Elon...
    print("Provided name is: ", str(name).title())
    uppies = 3
    new_name = name[:uppies] + name[0].upper() + name[uppies].upper()
    print("A Strange iteration of the name would be: ", str(new_name))
    # or a name with a number...


strange_name()

# this is supposed to print a string in reverse order from the input


def reverb():
    give_string = input(str("give me a sentence please: "))
    sentence = give_string.split()[::-1]
    lisst = []

    for letter in sentence:
        lisst.append(letter)
    print(" ".join(lisst))


reverb()

# if sum or one of ints is 20 return true


def is_20(a, b):
    if (a + b) == 20:
        return True
    elif a == 20:
        return True
    elif b == 20:
        return True
    else:
        return False


print(is_20(1, 19))

# simplified


def new_20(p, j):
    if (p + j) == 20 or p == 20 or j == 20:
        return True
    else:
        return False


print(new_20(3, 18))

