def collatz(uentry):
    odd_count = 0
    even_count = 0
    numz = []
    while uentry > 1:
        if uentry % 2 == 0:
            uentry = uentry / 2
            even_count = even_count + 1
            print(uentry)
            numz.append(uentry)

        else:
            uentry = ((uentry * 3) + 1)
            odd_count = odd_count + 1
            print(uentry)
            numz.append(uentry)
    print("You have run this equation through the odd cycle " + str(odd_count) + " times!")
    print("You have run this equation through the even cycle " + str(even_count) + " times!")
    print("You have run this equation " + str((odd_count + even_count)) + " times!")
    print("The highest integer reached during the cycles was: " + (str(max(numz))))


collatz(203)
