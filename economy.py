# economy game
from datetime import datetime, timedelta
import time
import random
import csv

#Market data loaded.
with open('items.csv', 'r') as file:
    reader = csv.reader(file)
    market = {rows[0]:rows[1] for rows in reader}

#Init date and time
def start():
    today = datetime.today()
    print('Today is '+str(today.strftime("%d/%m/%Y")))

#Function for fluctuation of currency
def fluctuate_currency(money):
    random.seed()
    rand = random.random()
    multiplier = (rand*0.05) + 0.975
    money = money * multiplier
    return money

#Function for fluctuation of item values
def fluctuate_value(value):
    random.seed()
    rand = random.random()
    multiplier = (rand*0.15) + 0.925
    value = value * multiplier
    return value

#Main function
def main():
    command = ''
    inventory = {}
    money = 100
    inflation_measure = 100
    start()
    today = datetime.today()
    print('You have $', money)
    
    while not (command == 'q'):
        print('\nEnter command. q=quit, w=wait, f=finances, i=inventory, m=market, b=buy, s=sell, e=economy')
        command = input('>')

        # Exit
        if command == 'q':
            print('Exiting')
            break

        # Wait 1 day
        if command == 'w':
            print('Waiting 1 day.')
            today = today + timedelta(days=1)
            #Fluctuate money
            oldmoney = money #for inflation measurement
            money = fluctuate_currency(money)
            print('It is now '+str(today.strftime("%d/%m/%Y")))
            #Fluctuate item value
            if inventory != {}:
                for x in inventory:
                    inventory[x] = fluctuate_value(float(inventory[x]))
            #Fluctuate inflation rate for measurement
            inflation_measure = inflation_measure+money-oldmoney

        #List finances
        if command == 'f':
            print('You have $'+str(money))

        #Economy information
        if command == 'e':
            print('The inflation rate thus far is ', str(inflation_measure-100), '%')

        #Buy item
        if command == 'b':
            print('Type the name of the item you would like to purchase.')
            purchase = input('>')
            if purchase in market:
                print('Ordered ', purchase)
                if money > float(market[purchase]):
                    money = money - float(market[purchase])
                    print('Bought ', purchase, ' for ', market[purchase])
                    inventory[purchase] = market[purchase]
                else:
                    print('Insufficient funds.')
            else:
                print('No such item.')

        #Sell item
        if command == 's':
            print('Type the name of the item you would like to sell.')
            sell = input('>')
            if sell in inventory:
                print('Sell order for ', sell, ', at $', inventory[sell])
                money = money + float(inventory[sell])
                inventory.pop(sell)
            else:
                print('You do not have ', sell)

        #List market items.
        #Todo: randomize availability of market items.
        if command == 'm':
            print('Market items: ')
            for x in market:
                print(x, ', $', market[x])

        #List inventory        
        if command == 'i':
            print('Current inventory: ')
            total_value_inventory = 0
            for x in inventory:
                print(x, ', valued $', inventory[x])
                total_value_inventory = total_value_inventory + inventory[x]
            print('Total value of inventory: ', total_value_inventory)


            
            


main()
