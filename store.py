import csv


class Items:
    pay_rate = 0.8  # Class level attribute, i applied a default discount value.
    all = []  # Appending the datas to storage.

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

    # Instantiating from the csv file, for it to work we need to use an inbuilt operation called
    # @classmethod
    @classmethod  # Instantiating a class method.
    def instantiate_from_csv(cls):  # The class method for it takes a parameter of cls
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)  # Convert the csv items to a dictionary
            items = list(reader)  # Converting the csv that is dictionary format to a list.
        for item in items:
            Items(
                name=item.get('name'),
                price=int(item.get('price')),  # Convert string to int
                quantity=int(item.get('quantity'))
            )

    def __str__(self):
        return f"Item: {self.item_name}, Price: {self.item_price}, Quantity: {self.quantity}"

    def __repr__(self):
        return f"{self.item_name}, {self.item_price}, {self.quantity}"


Items.instantiate_from_csv()
print(Items.all)
