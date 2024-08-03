class Bakery:
    def __init__(self, no, name, price , quantity):
        self.product_no = no
        self.product_name = name
        self.Product_price = price
        self.quantity = quantity


    def __str__(self):
        return str(self.product_no) +" , " +self.product_name +" , " + str(self.Product_price) +" , " + str(self.quantity)+ "\n"
