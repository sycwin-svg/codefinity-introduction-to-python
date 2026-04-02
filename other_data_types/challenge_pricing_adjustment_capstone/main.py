grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8 ),
    "Eggs": ("Dairy",5.50,30),
    "Bread": ("Bakery",2.99,15),
    "Apples": ("Produce",1.50,50)
}
catagory = grocery_inventory["Eggs"][0]
price_of_eggs = grocery_inventory["Eggs"][1]
stock = grocery_inventory["Eggs"][2]
if price_of_eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (catagory, price_of_eggs - 1,stock)
    
else:
    print ("Price of Eggs is reasonable")
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print ("Inventory after adding Tomatoes:", grocery_inventory)

catagory = grocery_inventory ["Milk"][0]
price_of_milk = grocery_inventory["Milk"][1]
stock = grocery_inventory["Milk"][2]
if stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (catagory, price_of_milk, stock+20)
else:
    print("Milk has sufficient stock.")
price_of_apples = grocery_inventory["Apples"][1]
if price_of_apples > 2:
    grocery_inventory.pop("Apples",None)
print ("Updated Inventory:", grocery_inventory)