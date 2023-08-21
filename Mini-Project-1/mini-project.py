class ColCon:
    def __init__(self, input_number):
        self.input_number = input_number

    def is_int(self):
        dont_know = self
        try:
            if int(ColCon.is_int(self)) is int:
                return True
                pass

        except ValueError:
            print("This is not a whole number")
            return False

    def coolatz(self):
        even_count = 0
        odd_count = 0
        numz = []
        burden = self
        while burden > 1:
            if burden % 2 == 0:
                burden = burden / 2
                even_count = even_count + 1
                print(burden)
                numz.append(burden)

            else:
                burden = ((burden * 3) + 1)
                odd_count = odd_count + 1
                print(burden)
                numz.append(burden)
        print("You have run this equation through the odd cycle " + str(odd_count) + " times!")
        print("You have run this equation through the even cycle " + str(even_count) + " times!")
        print("You have run this equation " + str((odd_count + even_count)) + " times!")
        print("The highest integer reached during the cycles was: " + (str(max(numz))))

    def main_bit(self):
        ColCon.is_int(self)
        if ColCon.is_int is True:
            ColCon.coolatz(self)
        else:
            print("There has been an error processing your request.")
            pass


hungry = ColCon(input("Please provide a whole number greater than 0: "))
hungry.main_bit()
