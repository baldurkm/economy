# economy game
from datetime import datetime, timedelta
import time
import random
import csv

with open('items.csv', 'r') as file:
    reader = csv.reader(file)
    market = {rows[0]:rows[1] for rows in reader}

def start():
    today = datetime.today()
    print('Today is '+str(today.strftime("%d/%m/%Y")))

def fluctuate_currency(money):
    random.seed()
    rand = random.random()
    multiplier = (rand*0.05) + 0.99
    money = money * multiplier
    return money
    
def main():
    command = ''
    money = 100
    start()
    today = datetime.today()

    while not (command == 'q'):
        print('Enter command. q=quit, w=wait, , f=finances, l=assets, m=market, b=buy item')
        command = input('>')
        if command == 'q':
            print('Exiting')
            break
        if command == 'w':
            print('Waiting 1 day.')
            today = today + timedelta(days=1)
            money = fluctuate_currency(money)
            print('It is now '+str(today.strftime("%d/%m/%Y")))
        if command == 'f':
            print('You have $'+str(money))
        if command == 'b':
            print('Please type the name of the item you would like to purchase.')
            purchase = input('>')
            if purchase in market:
                print('Ordered ', purchase)
            else:
                print('No such item.')
        if command == 'm':
            print('Market items: ')
            for x in market:
                print(x, ', $', market[x])


            
            


main()
