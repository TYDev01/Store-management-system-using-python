class Items:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: int, quantity=0):

        # To make sure negative value is not added we use "assert" statement
        assert price >= 0, f"Entered price value {price} is a negative value and not allowed"
        assert quantity >= 0, f"Entered quantity value {quantity} is a negative value and not allowed"

        # Assign to self object
        self.item_name = name
        self.item_price = price
        self.quantity = quantity

        Items.all.append(self)

    def discount(self):
        self.item_price = self.item_price * self.pay_rate

    def __str__(self):
        return f"Item: {self.item_name}, Price: {self.item_price}, Quantity: {self.quantity}"

    def __repr__(self):
        return f"{self.item_name}, {self.item_price}, {self.quantity}"


beverages = Items("cabbage", 200, 5)
drinks = Items("Gulder", 500, 2)
electronics = Items("Laptop", 2000, 1)
men_clothing = Items("Suits", 300, 1)

# for items in Items.all:
#     print(items)

print(Items.all)
# print(beverages)
# beverages.discount()
# print(beverages)
# print(drinks)

# print(beverages)
# beverages.discount()  # No need to print the return value of discount()
# print(beverages)  # Print after discount is applied
# print(drinks)
