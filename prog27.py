# Write a class called Product. The class should have fields called name, amount, and price,holding the product’s name, the number of items of that product in stock, and the regular price of the product. There should be a method get_price that receives the number of items to be bought and returns a the cost of buying that many items, where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much.

class Product:
    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price
    def get_price(self,items):
        if items < 10:
            return self.price * items
        elif items >= 10 and items < 100:
            return self.price * items * 0.9
        else:
            return self.price * items * 0.8
    def make_purchase(self,items):
        if items <= self.amount:
            self.amount -= items
            print(f"Purchase successful. {items} {self.name}(s) remaining: {self.amount}")
        else:
            print(f"Not enough {self.name} in stock. Available amount: {self.amount}")
    def __str__(self):
        return "Product Name: " + self.name + "\nIn stock: " + str(self.amount) + "\nPrice for each: " + str(self.price)
def main():
    p = Product("Pen",100,10)
    print(p)
    items = int(input("Number of items you want to buy: "))
    print(f"The price for {items} items is: ",p.get_price(items))
    p.make_purchase(items)
    print(p)
if __name__ == "__main__":
    main()