"""
Sales Management

Author: Gustavo Moraes
License: MIT
Status: 0.0.1
"""

import os

os.system("cls")


class colors:
    GREEN = '\033[0;32m'
    RED = '\033[0;31m'
    BLUE = '\033[0;36m'
    END = '\033[m'


# Add a sale
def add(list, sellers):
    global id
    id += 1
    sales = {
        "ID": id,
        "Seller Name": input('\nSeller Name: '),
        "Customer Name": input('Customer Name: '),
        "Date of Sale": input('Date of Sale: '),
        "Sale Item Name": input('Sale Item Name: '),
        "Sale Value": float(input('Sale Value: '))
    }

    name = sales["Seller Name"]

    found = exist_seller(name, sellers)

    if found:
        list.append(sales)
        print(colors.GREEN + '\nSale successfully registered!' + colors.END)
        sales_list(list)
    else:
        print(colors.RED + '\nUnregistered seller!' + colors.END)
        id -= 1
        sales_list(list)


def exist_seller(name, sellers):
    for i in range(len(sellers)):
        if name == sellers[i]:
            found = True
            break
        else:
            found = False

    return found


# Edit a sale
def change(list, sellers):
    if len(list) > 0:
        change_id = int(input('\nEnter the sales ID to edit: '))
        for i in range(len(list)):
            if list[i]['ID'] == change_id:
                if exist_sale(change_id, list):
                    while True:
                        print(colors.BLUE + '\n--- Edit Sales ---\n' + colors.END)
                        print('[1] Seller Name')
                        print('[2] Customer Name')
                        print('[3] Date of Sale')
                        print('[4] Sale Item Name')
                        print('[5] Sale Value')

                        option = int(input('\nEnter the corresponding option: '))

                        if option == 1:
                            name = input("\nEnter the new sellers name: ")
                            found = exist_seller(name, sellers)

                            if found:
                                list[i]['Seller Name'] = name
                                print(colors.GREEN + "\nThe sellers name has been changed!" + colors.END)

                            else:
                                print(colors.RED + "\nUnregistered seller!" + colors.END)

                            break

                        elif option == 2:
                            list[i]['Customer Name'] = input("\nEnter the new customers name: ")
                            print(colors.GREEN + "\nThe customers name has been changed!" + colors.END)
                            break

                        elif option == 3:
                            list[i]['Date of Sale'] = input("\nEnter the new date of sale: ")
                            print(colors.GREEN + "\nThe date of sale has been changed!" + colors.END)
                            break

                        elif option == 4:
                            list[i]['Sale Item Name'] = input("\nEnter the new sales item name: ")
                            print(colors.GREEN + "\nThe sales item name has been changed!" + colors.END)
                            break

                        elif option == 5:
                            list[i]['Sale Value'] = float(input("\nEnter the new sales value: "))
                            print(colors.GREEN + "\nThe sales value has been changed!" + colors.END)
                            break

                        else:
                            print(colors.RED + '\nInvalid option! Try again!' + colors.END)

                sales_list(list)
                break

        else:
            print(colors.RED + "\nNo registered sale with this ID!" + colors.END)

    else:
        print(colors.RED + "\nNo registered sale!" + colors.END)


# Check for a sale
def exist_sale(id, list):
    if len(list) > 0:
        for sales in list:
            if sales['ID'] == id:
                return True

    return False


# Remove a sale
def remove(list):
    if len(list) > 0:
        del_id = int(input("\nEnter the sales ID to remove: "))
        if exist_sale(del_id, list):
            for i in range(len(list)):
                if list[i]['ID'] == del_id:
                    del list[i]
                    print(colors.GREEN + "\nSale removed!" + colors.END)
                    sales_list(list)
                    break

        else:
            print(colors.RED + "\nNo registered sale with this ID!" + colors.END)

    else:
        print(colors.RED + "\nNo registered sale!" + colors.END)


# Order the sales based on value
def order(e):
    return e['Sale Value']


# Show the sales list
def sales_list(list):
    print(colors.BLUE + "\n--- Sales List ---\n" + colors.END)
    list.sort(reverse=True, key=order)

    if len(list) > 0:
        for sales in list:
            print("ID: {}".format(sales['ID']),
                  "Seller Name: {}".format(sales['Seller Name']),
                  "Customer Name: {}".format(sales['Customer Name']),
                  "Date of Sale: {}".format(sales['Date of Sale']),
                  "Sale Item Name: {}".format(sales['Sale Item Name']),
                  "Sale Value: {}".format(sales['Sale Value']),
                  sep='     ')
    else:
        print(colors.RED + "No registered sale!" + colors.END)


# Show the sellers list
def sellers_list(list):
    print(colors.BLUE + "\n--- Sellers List---\n" + colors.END)
    for i in range(0, len(list)):
        print(list[i])


def clear():
    input(colors.GREEN + "\nPress Enter to continue..." + colors.END)
    os.system("cls")


id = 0


# Main
def main():
    list = []
    sellers = ['Gustavo', 'Leonardo', 'Alice', 'Laura', 'Isabella']

    while True:
        print(colors.BLUE + '\n--- Sales Management ---\n' + colors.END)
        print('[1] Register sale')
        print('[2] Change sale')
        print('[3] Remove sale')
        print('[4] Sales list')
        print('[5] Sellers list')
        print('[6] Exit')

        option = int(input('\nEnter the corresponding option: '))

        if option == 1:
            add(list, sellers)

        elif option == 2:
            change(list, sellers)

        elif option == 3:
            remove(list)

        elif option == 4:
            sales_list(list)

        elif option == 5:
            sellers_list(sellers)

        elif option == 6:
            print(colors.GREEN + '\nEnd of program! Come back soon!' + colors.END)
            break
        else:
            print(colors.RED + '\nInvalid option! Try again!' + colors.END)

        print('\n------------------------------')

        clear()


if __name__ == "__main__":
    main()
