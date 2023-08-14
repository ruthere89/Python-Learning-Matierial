class SalesPerson:

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    sales = 0

    def make_sale(self, sale: int):
        self.sales += sale

    def sales_report(self):
        print("My total sales are {}".format(self.sales))

    def get_sells(self):
        for person in self.SalesPerson:
            print("My name is {}, and my total sales are {}.".format(self.first_name, self.sales))


p1 = SalesPerson('Annie', 'Mae')
p1.make_sale(250)
p1.sales_report()
p2 = SalesPerson('Manda', 'Lynn')
p2.make_sale(150)
p2.sales_report()
p3 = SalesPerson('Richard', 'Byzcits')
p3.make_sale(6969)
p3.sales_report()
