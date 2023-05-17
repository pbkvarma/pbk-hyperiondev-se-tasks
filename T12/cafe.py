'''
Task 12 'Cafe' application that prints menu items and calculates price of total stock available
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: Develop a cafe application that has 4 (minimum) items in menu as a list, their respective stock 
#and price as ditcionarys.Application also gives the user the choice to add or delete the item with 
#error handling, if no valid input is typed.

#Defining a 'menu' list containing type of items available in the cafe
menu = ['coffee', 'tea', 'sandwiches', 'drinks', 'crisps', 'bagels', 'donuts', 'cup-cakes']

#Defining 'stock' dictionary, which shows the quantatity available of each item from the menu.
#The keys names are the same as menu index, this is done so that any changes done by user gets 
#updated to stock and price variables
stock = {menu[0]: 2, menu[1]: 5, menu[2]: 5, menu[3]: 6, menu[4]: 2, menu[5]: 10, menu[6]: 15, menu[7]: 20}

#Defining 'price' dictionary, which shows price of each unit item from the menu
price = {menu[0]: 1.5, menu[1]: 1.40, menu[2]: 3.5, menu[3]: 1.6, menu[4]: .5, menu[5]: 1.75, menu[6]: 1.5, menu[7]: 1.45}

while True:

    print("\n To see menu items:   Type '0' or 'view'")
    print(" To add a new item:   Type '1' or 'add'")
    print(" To remove an item:   Type '2' or 'delete'")
    print(" To exit application: Type '3' or 'exit'\n")
    user_choice = input("\nPlease choose appropriate option from above:  ")

    try:
        
        if user_choice == '0' or user_choice.lower() == 'view':
            
            total_stock_value = 0    
            print ("\n{:<8} {:<15} {:<10} {:<10} {:<10}".format('Index', 'Menu', 'Stock', 'Price', 'Total Value'))
            print("-------------------------------------------------------------\n")

            for item in range(0, len(menu)):

                #Calculating price of total stock available
                item_value = stock[menu[item]] * price[menu[item]]
                total_stock_value += item_value
                #Code to format the output in a tabular form
                print("{:<8} {:<15} {:<10} {:<10} {:<10}".format(item, menu[item], stock[menu[item]], price[menu[item]], round(item_value, 2)))
            
            print(f"\nTotal items available: {len(menu)}")
            print(f"\nTotal stock value: £{round(total_stock_value, 2)} \n")
            continue
            
        elif user_choice == '1' or user_choice.lower() == 'add':
            
            print ("\n{:<8} {:<15}".format('Index', 'Menu'))
            print("-------------------------\n")

            for item in range(0,len(menu)):
                print("{:<8} {:<15}".format(item, menu[item]))
                
            user_add_item = input(f"\nEnter the item name: ")
            user_add_stock = int(input(f"\nEnter the stock (quantity) of the new item: "))
            user_add_price = float(input(f"\nEnter the item price: "))
            menu.extend([user_add_item])
            stock[user_add_item] = user_add_stock
            price[user_add_item] = user_add_price
            print(f"\nNew item '{user_add_item}' has been added to the menu.\n")
            continue

        elif user_choice == '2' or user_choice.lower() == 'delete':

            #Checks if the menu items are less then 4, if so user cannot delete any item
            if len(menu) <= 3:
                print("\nSorry! No. of items in the menu will be less then 4, so cannot remove any item\n")
                break
            
            else:

                print ("\n{:<8} {:<15}".format('Index', 'Menu'))
                print("-------------------------\n")

                for item in range(0,len(menu)):
                    print("{:<8} {:<15}".format(item, menu[item]))
                    
                item_delete = input("\nPlease type the menu item to be deleted: ")
                menu.remove(item_delete)
                stock.pop(item_delete)
                price.pop(item_delete)
                print(f"\nItem '{item_delete}' has been removed from the menu.\n")
                continue
            
        else:
            print("\nSorry! Invalid input, or application exited\n")
            break

    #To flag error if no or invalid input is typed
    except:
        print('\nSorry! Not a valid input.')
