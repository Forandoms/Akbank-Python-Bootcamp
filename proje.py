import csv
import datetime 
import time


def main():
  print (" welcome to the best pizzeria ")
  
main()

f = open("menu.txt", "r")
print(f.read())

# Class for sauce
class extras:
    def __init__(self, cost):
        self.cost = cost
    
  
    def get_cost(self):
        return self.cost

# All of them are free but you can get the prices of the extras
   
class Olives(extras):
    def __init__(self):
        cost = 6.00 , "TL"
        super().__init__(cost)

class Mushrooms(extras):
    def __init__(self):
        cost = 7.00 , "TL"
        super().__init__(cost)

class GoatCheese(extras):
    def __init__(self):
        cost = 10.00 , "TL"
        super().__init__(cost)

class Meat(extras):
    def __init__(self):
        cost = 20.00 , "TL"

        super().__init__(cost)
class Onions(extras):
    def __init__(self):
        cost = 8.00 , "TL"
        super().__init__(cost)

class Corn(extras):
    def __init__(self):
        cost = 5.00 , "TL"
        super().__init__(cost)

olives = Olives()
fiyat = olives.get_cost()
#--------------------------------------------
corn = Corn()
fiyat = corn.get_cost()
#--------------------------------------------
onions = Onions()
fiyat = onions.get_cost()             
#--------------------------------------------
meat = Meat()
fiyat = meat.get_cost()  
#--------------------------------------------
goatcheese = GoatCheese()
fiyat = goatcheese.get_cost()  
#--------------------------------------------
mushrooms = Mushrooms()
fiyat = mushrooms.get_cost()  

# Top pizza class
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
# Classic pizza class
class KlasikPizza(Pizza):
    def __init__(self):
        description = "Classic: with tomato sauce, cheddar cheesea and olive sthe sweet smell of the aegea"
        cost = 125.00 , "TL"
        super().__init__(description, cost)
        
# Margherita pizza class
class MargaritaPizza(Pizza):
    def __init__(self):
        description = "Margarita: with tomato sauce, mozzarella cheese, basil"
        cost = 140.00 ,"TL"
        super().__init__(description, cost)
        
# Turk pizza class       
class TurkPizza(Pizza):
    def __init__(self):
        description = "Turkish Pizza: sausage, hot dog, tomato sauce, cheddar cheese"
        cost = 155.00 , "TL"
        super().__init__(description, cost)
        
# Plain pizza class       
class SadePizza(Pizza):
    def __init__(self):
        description = "Plain Pizza: only with tomato sauce, cheddar cheese"
        cost = 100.00 , "TL"
        super().__init__(description, cost)

# All have defined the classes.

#  I leave only the definitions that will allow you to learn the 'price' part using print :D
klasik_pizza = KlasikPizza()
fiyat = klasik_pizza.get_cost()
#--------------------------------------------
margarita_pizza = MargaritaPizza()
fiyat_margarita = margarita_pizza.get_cost()
#--------------------------------------------
turk_pizza = TurkPizza() 
fiyat_turk = turk_pizza.get_cost()
#--------------------------------------------
sade_pizza = SadePizza()
fiyat_sade = sade_pizza.get_cost()
#--------------------------------------------

# I leave the information part here.
klasik_pizza = SadePizza()
acıklama_klasik = klasik_pizza.get_description()
#--------------------------------------------
sade_margarita = MargaritaPizza()
acıklama_margarita = margarita_pizza.get_description()
#--------------------------------------------
turk_pizza = TurkPizza()
acıklama_turk = turk_pizza.get_description()
#--------------------------------------------
sade_pizza = SadePizza()
acıklama_sade = sade_pizza.get_description()
#--------------------------------------------



# pizza options and prices
pizzas = {
    "1": {"name": "Classic", "price": 125.00},
    "2": {"name": "Margherita", "price": 140.00},
    "3": {"name": "TurkPizza", "price": 155.00},
    "4": {"name": "PlainPizza", "price": 100.00},
    
}

# extra material options and prices
toppings = {
    "1": {"name": "Mushrooms", "price": 0.00},
    "2": {"name": "Olives", "price": 0.00},
    "3": {"name": "GoatCheese", "price": 0.00},
    "4": {"name": "Meat", "price": 0.00},
    "5": {"name": "Onions", "price": 0.00},
    "6": {"name": "Corn", "price": 0.00},
}

# function that asks the user for pizza and extra ingredient selections
def get_order():
    pizza_choice = input("Please choose a pizza (1-4): ")
    toppings_choice = input("Do you want any extra toppings (y/n): ")
    
    if toppings_choice.lower() == "y":
        toppings_list = []
        topping_choice = input("Please choose a topping (1-6) or 'done': ")
        while topping_choice != "done":
            toppings_list.append(toppings[topping_choice]["name"])
            topping_choice = input("Please choose another topping (1-6) or 'done': ")
        return pizzas[pizza_choice]["name"], pizzas[pizza_choice]["price"], toppings_list
    else:
        return pizzas[pizza_choice]["name"], pizzas[pizza_choice]["price"], []
    
# function that calculates user's orders
def calculate_order(orders):
    total = 0
    for order in orders:
        total += order[1]
        if order[2]:
            print(order[0], "with", ", ".join(order[2]))
        else:
            print(order[0])
    print("Total:", total)
    
# loop presenting the user with options to make selections

orders = []
order_another = "y"
while order_another.lower() == "y":
    order = get_order()
    orders.append(order)
    order_another = input("Do you want to order another pizza (y/n): ")
calculate_order(orders)


print (" moving on to the payment part... ")


# I used this place to end loop so that it wouldn't be permanent.
tccheck = True
Card_number = True
ccvcheck = True
last_month_check = True
last_year_check = True
telephone_check = True
Card_password_check = True
# Payment processing part... Here we take the name, surname information.

isim =  input(" Enter your name: ") 
Soyisim =  input(" Enter your surname: ") 

# I had to loop constantly because I didn't want it to go back to the beginning.

while (telephone_check):
   telefon_no = int(input(" Enter your phone number. Please write without symbols and without '0' at the beginning : "))

   if ((telefon_no <= 5000000000) or (telefon_no <= 5000000000)):
      print (" incorrect number information.")

   else:
      telephone_check = False

      while (tccheck):
         tckn = int(input("Enter your T.R. identification number: "))

         if (tckn <= 10000000000 or tckn >= 99999999999):
            print(" you have dialed incorrectly. ")

         else:
            tccheck = False

         while (Card_number):
            card_number = int(input(" Enter card number: "))

            if ((card_number <= 1000000000000000) or (card_number >= 9999999999999999)):
               print(" you have made an incorrect keying entry ")
              

            else:
               Card_number = False

               while (ccvcheck):
                  ccv = int(input(" Enter your ccv details:"))

                  if ((ccv >= 999) or (ccv <= 100) ):
                     
                     print(" erroneous ccv.")
                  
                  else:
                     ccvcheck = False

                     while (last_month_check):
                        last_month = int(input(" Enter the last month of the card. "))

                        if ((last_month < 0 ) or (last_month > 13) ):
                           print(" please re-enter. ")

                        else:
                           last_month_check = False

                           while (last_year_check):
                              last_year = int(input(" Enter the last year of the card: "))

                              if ((last_year < 2023) or (last_year > 2033) ):
                                 print("Please re-enter.")

                              else:
                                last_year_check = False
                                card_password = int(input((" Please enter your password:")))

                                while (Card_password_check):

                                    if (( card_password < 1000 ) or ( card_password > 99999 )):
                                        print(" re-enter please. ")
                                 
                                    else:
                                        Card_password_check = False
                                        print ( "Your information is being checked. ")
                                        time.sleep (3)
                                        print(" Your payment has been received. ")
                                        print ("Bon Appétit")
                                        break
                                        


kullanici_bilgileri = [isim, Soyisim, telefon_no, tckn, card_number, ccv, last_month, last_year ]


# Bilgilerin dosyaya aktarıldığı kısım.
fp = open("Orders_Database.csv", "a+")

for i in range(8):  
    fp.write(str( kullanici_bilgileri [i] )) 
    if (i<7):
        fp.write ( "," ) 
fp.write ("\n")           
fp.close()
