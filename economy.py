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
    multiplier = (rand*0.05) + 0.99
    money = money * multiplier
    return money

#Main function
def main():
    command = ''
    inventory = {}
    money = 100
    start()
    today = datetime.today()

    while not (command == 'q'):
        print('Enter command. q=quit, w=wait, , f=finances, i=inventory, m=market, b=buy item')
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
            money = fluctuate_currency(money)
            print('It is now '+str(today.strftime("%d/%m/%Y")))
            #Fluctuate item value
            if inventory != {}:
                for x in inventory:
                    inventory[x] = fluctuate_currency(float(inventory[x]))
                
            

        #List finances
        if command == 'f':
            print('You have $'+str(money))

        #Buy item
        if command == 'b':
            print('Please type the name of the item you would like to purchase.')
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

        #List market items
        if command == 'm':
            print('Market items: ')
            for x in market:
                print(x, ', $', market[x])

        #List inventory        
        if command == 'i':
            print('Current inventory: ')
            for x in inventory:
                print(x, ', valued $', inventory[x])


            
            


main()
