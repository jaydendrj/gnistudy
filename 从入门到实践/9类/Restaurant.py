'''定义Restaurant'''
class Restaurant():
    def __init__(self,restaurant_name,restaurant_type):
        self.restaurant_name=restaurant_name
        self.restaurant_type=restaurant_type
        self.number_served=0

    def describe_restaurant(self):
        print('The name of the restaurant is '+self.restaurant_name.title()+'.')
        print('The type of the restaurant is '+self.restaurant_type+'.')

    def open_restaurant(self):
        print('The restaurant is open now.')

    def set_number_served(self,number):
        self.number_served=number
        print('就餐人数：'+str(self.number_served)+'.')


    def increment_number_served(self,num_inc):
        self.number_served+=num_inc
        return self.number_served

'''应用篇幅'''
# restaurant1=Restaurant('lantian','nake')
# restaurant1.describe_restaurant()
#
# restaurant2=Restaurant('asdjgfd','asfdgfdkss4')
# restaurant1.describe_restaurant()
# restaurant1.set_number_served(43)

'''定义IceCreamStand类（继承Restaurant)'''
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,restaurant_type,flavors):
        super().__init__(restaurant_name,restaurant_type)
        self.flavors=flavors
    def show_menu(self):
        for flavor in self.flavors:
            print(flavor)

'''应用篇幅'''
my_icecreamstand=IceCreamStand('dr','icecream',['asf;jf','asfgf','sweat'])
# my_icecreamstand.flavors=['asf;jf','asfgf','sweat']
my_icecreamstand.show_menu()




