class SodaPref:
    # class attribute
    drink_type = "soda pop"

# static
    def pop_top(self):
        print("**POP** Mmmmm fizzy and delicious")

    # instance attribute(s) here
    def __init__(self, name: str, age: int, soda: str):
        self.name = name
        self.age = age
        self.soda = soda
        self.brands = []
        self.oz = 0

# dynamic, but not really using it right now, could just pass
    def add_ounces(self, ounce: int):
        self.oz += ounce

# dynamic
    def get_brand(self, brand: str):
        self.brands.append(brand.lower())

# need more info as to why this isn't working how I want it to
    def get_popular_brand(self):
        for brand in self.brands:
            brand_a = self.brands.count("coke")
            brand_b = self.brands.count("pepsi")
            if brand_a > brand_b:
                print("Coke is the most popular brand so far!")
            else:
                print("Pepsi is the most popular brand so far!")


# add some folks in
P1 = SodaPref("Jill", 40, "Cherry Coke")
P1.get_brand("COKE")
P2 = SodaPref("Jon", 43, "Mt.Dew")
P2.get_brand("Pepsi")
P3 = SodaPref("Brian", 34, "Coke")
P3.get_brand("coke")
P4 = SodaPref("Karen", 28, "Sprite")
P4.get_brand("coke")
P5 = SodaPref("Ryan", 33, "Dr. Pepper")
P5.get_brand("PEPSI")
# make the class respond
print(P5.pop_top())



