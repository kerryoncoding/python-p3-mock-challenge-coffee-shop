class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    #validate name
    def name(self, value):
        #if name does not already exist, create name (Should not be able to change after the coffee is instantiated)
        if not hasattr(self, 'name'):
            #name must be string greater than 2 in length
            if isinstance(value, str) and len(value) > 2:
                self._name = value
        
    def orders(self):
        # need a list of orders for that coffee
        # order_list = []
        # for order in Order.all:
        #     if order.coffee == self:
        #         order_list.append(order)
        # return order_list
        return [order for order in Order.all if self == order.coffee]  
        
    def customers(self):
        pass
        # Returns a unique list of all customers who have ordered a particular coffee.
        # Customers must be of type Customer
        all_orders_list = []
        for order in Order.all:
            if order.coffee == self:
                all_orders_list.append(order.customer)
        unique_set = set(all_orders_list)
        unique_list = list(unique_set)
        return unique_list
            
    def num_orders(self):
        # Returns the total number of times a coffee has been ordered
        # Returns 0 if the coffee has never been ordered
        return len(self.orders())
    
    def average_price(self):
        pass

class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        #name must be a string of length 1-15 characters
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value

    def orders(self):
        # Returns a list of all orders for that customer
        # Orders must be of type Order
        return [order for order in Order.all if self == order.customer]
    
    def coffees(self):
        # Returns a unique list of all coffees a customer has ordered
        # Coffees must be of type Coffee
        all_coffee = []
        for order in Order.all:
            if order.customer == self:
                all_coffee.append(order.coffee)
        unique_set = set(all_coffee)
        unique_list = list(unique_set)
        return unique_list
    
    def create_order(self, coffee, price):
        self.coffee = coffee
        self.price = price
        # Creates and returns a new Order instance and associates it with that customer and the coffee object provided.
        return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        # Should not be able to change price after order is instantiated
        if not hasattr(self, 'price'):
            # type should be float value between 1-10 inclusive
            if isinstance(value, float) and 1.0 <= value <= 10.0:
                self._price = value
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, value):
        if isinstance(value, Coffee):
            self._coffee = value
    
    def __repr__(self):
        return f'<customer: {self.customer} coffee: {self.coffee}>'
