class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    #validate name
    def name(self, value):
        #if name does not already exist, create name
        if not hasattr(self, 'name'):
            #name must be string greater than 2 in length
            if isinstance(value, str) and len(value) > 2:
                self._name = value
        
    def orders(self):
        # need a list of orders
        # return number of orders for that coffee
        # here....

        # count = 0
        # return [order for order in Orders if coffee = self.order.coffee]  
        pass
    
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
