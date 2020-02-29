class Restaurant():
    """
    餐厅及其信息
    """
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.customer_num = 0
    def desecribe_restaurant(self):
        informations = str(self.restaurant_name)+' is a '+str(self.cuisine_type)+' restaurant.'
        return informations
    def num_served(self):
        print('%d people have eaten there already.'%self.customer_num)
    def num_served_increment(self,increment):
        self.customer_num += increment
class Five_star(Restaurant):
        def __init__(self,name,type):
            """initializing parent class"""
            super(Five_star,self).__init__(name,type)
first_restaurant = Restaurant('Mcdonald','burger')
print(first_restaurant.desecribe_restaurant())
first_restaurant.num_served_increment(100)
first_restaurant.num_served()
second_restaurant = Five_star('Michelin','expansive')
print(second_restaurant.desecribe_restaurant())


