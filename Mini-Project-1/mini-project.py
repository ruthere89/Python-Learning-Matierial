import sys


class Logger(object):
    def __init__(self):
        # creating a class to run the output (terminal) to a txt doc
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        # writing terminal as a message into the log
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # I was told to put this here
        pass


sys.stdout = Logger()


class ColCon:
    # creating a standard class variable (per object created)
    even_count = 0
    odd_count = 0
    numz = []

    def __init__(self):
        # intro
        print("Thank you for attempting the Collatz Conjecture!\n"
              "This is a mathematical expression that will operate until a number is equal  to one.")
        self.number = input('Please provide a whole number greater than 0: ').split()
        # check for integer in the provided statement
        for num in self.number:
            try:
                int(num)
                if int(num) > 0:
                    print('Yay')
                    continue
                # is int, not 0<
                else:
                    print('negative numbers do not count... sorry')
                    pass
            # must be words
            except ValueError:
                print('wow not even close')
                pass

    def coolatz(self):
        # need to iterate through a list if provided
        for num in self.number:
            try:
                print(num)
                # the int, int, int was the only way I could figure it out
                if type(int(num)) is int and int(num) > 0:
                    # greater than 1 is the only way I want to see it working
                    while int(num) > 1:
                        if int(num) % 2 == 0:
                            num = int(num) / 2
                            ColCon.even_count = ColCon.even_count + 1
                            ColCon.numz.append(num)
                        else:
                            num = ((int(num) * 3) + 1)
                            ColCon.odd_count = ColCon.odd_count + 1
                            ColCon.numz.append(num)
                    print(ColCon.numz)
                    print("You have run this equation through the odd cycle " + str(ColCon.odd_count) + " times!")
                    print("You have run this equation through the even cycle " + str(ColCon.even_count) + " times!")
                    print("You have run this equation " + str((ColCon.odd_count + ColCon.even_count)) + " times!")
                    print("The highest integer reached during the cycles was: " + (str(max(ColCon.numz))))
                else:
                    print('oops, was this greater than 0?')
                    continue
            # because it runs either way, create an exception and boot it
            except ValueError:
                print('There has been an error processing your request. \nOne or more of your values may not have '
                      'been an integer.\nExiting...')
                continue


xl1 = ColCon()
xl1.coolatz()
