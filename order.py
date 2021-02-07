class Order:

    number_of_orders = 0

    def __init__(self, product_name, quantity, product = 'Shoe'):
        self.product_name = product_name
        self.quantity = quantity
        Order.number_of_orders += 1

    def product_description(self):
        return product + ': ' + str(self.quantity) 


order_1 = Order('Nike Air Max', 10)
print(order_1.number_of_orders)
print(order_1.quantity)
