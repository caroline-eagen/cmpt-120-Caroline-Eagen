#product_names = ["Ultrasonic range finder",
 #                "Servo motor",
 #                "Servo controller",
 #                "Microcontroller Board",
 #                "Laser range finder",
 #                "Lithium polymer battery"]

#product_prices = [2.50, 14.99, 44.95, 34.95, 149.99, 8.99]
#product_quantities = [4, 10, 5, 7, 2, 8]

class product:
    ID = 0
    quantity = 0
    price = 0.0
    
    def __init__(self, n, p, q):
        self.name = n
        self.price = p
        self.quantity = q
        
    def inStock(self):
        return self.quantity
    
    def getStock(self, quantity):
        return quantity < self.quantity
    
    def totalCost(self):
        return self.quantity * self.price
    
    def newStock(self, quantity):
        return self.quantity - quantity
    
    def getName(self):
        return self.name

#class product(object):
#   def __init__(name, price, quantity):
#       name.price = price
#        name.quantity = quantity
#        
#    def display(name):
#       print(name.price)
#       print(name.quantity)

def print_stock(product_array):
    print("\nAvailable Products")
    print("-----------------")
    for i in range(0, len(product_array)):
        if product_array[i].quantity > 0:
            print(str(i) + ")", product_array[i].name, "$", product_array[i].price)
        print()
        
def main():
    item1 = product("Ultrasonic range finder", 2.50, 4)
    item2 = product("Servo motor", 14.99, 10)
    item3 = product("Servo controller", 44.95, 5)
    item4 = product("Microcontroller Board", 34.95, 7)
    item5 = product("Laser range finder", 149.99, 2)
    item6 = product("Lithium polymer battery", 8.99, 8)
    
    product_array = [item1, item2, item3, item4,item5, item6]
    
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock(product_array)
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        
        prod_id = int(vals[0])
        count = int(vals[1])
        
        if  product_array[prod_id].getStock(count): #>= count:
            if cash >= product_array[prod_id].totalCost():
                product_array[prod_id].quantity * count
                cash -= product_array[prod_id].price * count
                print("You purchased", count, product_array[prod_id].getName() + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product_array[prod_id].name)
        
 #       if product_quantities [prod_id] >= count:
 #           if cash >= product_prices[prod_id]:
 #               product_quantities[prod_id] * count
 #               cash -= product_prices[prod_id] * count
 #               print("You purchased", count, product_names[prod_id] + ".")
 #               print("You have $", "{0:.2f}".format(cash), "remaining.")
 #           else:
 #               print("Sorry, you cannot afford that product.")
 #       else:
 #           print("Sorry, we are sold out of", product_names[prod_id])
        
main()