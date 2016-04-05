print("Welcome to the Virtual Pantry!")
print("Enter HELP for pantry commands.")

def add_item():
    item = input("What is your item? > ").title()
    amount = int(input("How much did you buy? > "))
    price = int(input("How much did it cost? ($) > "))
    pantry[item] = [amount, price]
    if input("Add another item? [Y/N]").upper() == "Y":
        add_item()
     

pantry = {}

while 1:
    userinput = str.upper(input("PantryBot: "))
#Help
    if userinput == "HELP":
        print("1 - Enter new stock.\n"
              "2 - View Stock Levels\n"
              "3 - Cook, Use, Modify")

#Enter New Stock
    if userinput == "1":
        print("I hope your shopping trip was lovely.")
        add_item()
                

#View Pantry
    if userinput == "2":
        if pantry == {}:
            print("Your pantry is empty!")
        else:
            for item in pantry:
                print("{}: {} at ${}."
                      .format(item,pantry[item][0],pantry[item][1]))
                
#Cook, Use, Modify
    if userinput == "3":
        print("Firing up the range...")
