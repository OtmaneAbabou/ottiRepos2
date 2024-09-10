import csv
class Item:
    price_rate=0.8 # The pay rate after 20% discount
    all=[]
    def __init__(self, name: str, price:float, quantity=0):
        assert price>=0, f"Price {price} is not greater than or equal to zero!"
        self.__name=name
        self.price=price
        self.quantity=quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.quantity * self.price
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    def __repr__(self):
        return f"Item (Name='{self.name}', Price='{self.price}', Quantity='{self.quantity}')"
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader= csv.DictReader(f)
            items=list(reader)
        for item in items:
                Item (name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity"))
                  )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



Item.instantiate_from_csv()
print (Item.all) 