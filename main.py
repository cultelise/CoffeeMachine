inventory = {
  'Water': { 
    'Amount': 300,
    'Measurement': 'ml'
  },
    'Milk': {
    'Amount': 200,
    'Measurement': 'ml'
  },
    'Coffee': {
    'Amount': 100,
    'Measurement': 'g'
  },
    'Money': {
    'Amount': 0,
    'Currency': '$'
  }
}

drinks = {
  'Latte': {
    'Water': 200,
    'Milk': 150,
    'Coffee': 24,
    'Cost': 7
  },
  'Cappuccino': {
    'Water': 250,
    'Milk': 100,
    'Coffee': 24,
    'Cost': 6
  },
  'Espresso': {
    'Water': 50,
    'Milk': 0,
    'Coffee': 18,
    'Cost': 4
  }
}

def coin_counter():
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    
    q = quarters * 0.25
    d = dimes * 0.10
    n = nickels * 0.05
    p = pennies * 0.01
    
    total_money = round(q + d + n + p, 2)
    return total_money

def update_inventory(drink):
    latte = drinks['Latte']
    cappuccino = drinks['Cappuccino']
    if drink == 'Latte':
      inventory['Water']['Amount'] -= latte['Water']
      inventory['Milk']['Amount'] -= latte['Milk']
      inventory['Coffee']['Amount'] -= latte['Coffee']
      inventory['Money']['Amount'] += latte['Cost']
    elif drink == 'Cappuccino':
      inventory['Water']['Amount'] -= cappuccino['Water']
      inventory['Milk']['Amount'] -= cappuccino['Milk']
      inventory['Coffee']['Amount'] -= cappuccino['Coffee']
      inventory['Money']['Amount'] += cappuccino['Cost']
    elif drink == 'Espresso':
      inventory['Water']['Amount'] -= espresso['Water']
      inventory['Coffee']['Amount'] -= espresso['Coffee']
      inventory['Money']['Amount'] += espresso['Cost']

def stock_low(drink):
  water = inventory['Water']['Amount']
  milk = inventory['Milk']['Amount']
  coffee = inventory['Coffee']['Amount']
  if drink == 'Latte':
    latte = drinks['Latte']
    if coffee < latte['Coffee'] or milk < latte['Milk'] or water < latte['Water']:
      return True
  elif drink == 'Cappuccino':
    cappuccino = drinks['Cappuccino']
    if coffee < cappuccino['Coffee'] or milk < cappuccino['Milk'] or water < cappuccino['Water']:
      return True
  elif drink == 'Espresso':
    espresso = drinks['Espresso']
    if coffee < espresso['Coffee'] or water < espresso['Water']:
      return True
    
def check_low_stock(drink):
  water = inventory['Water']['Amount']
  milk = inventory['Milk']['Amount']
  coffee = inventory['Coffee']['Amount']
  if drink == 'Latte':
    latte = drinks['Latte']
    if coffee < latte['Coffee']:
      return 'coffee' 
    elif milk < latte['Milk']:
      return 'milk'
    elif water < latte['Water']:
      return 'water'
  elif drink == 'Cappuccino':
    cappuccino = drinks['Cappuccino']
    if coffee < cappuccino['Coffee']:
      return 'coffee' 
    elif milk < cappuccino['Milk']:
      return 'milk'
    elif water < cappuccino['Water']:
      return 'water'
  elif drink == 'Espresso':
    espresso = drinks['Espresso']
    if coffee < espresso['Coffee']:
      return 'coffee' 
    elif water < espresso['Water']:
      return 'water'
      
loop = True
while loop:
  request = input('What would you like? (espresso/latte/cappuccino): ').lower()

  if request == 'report':
    for item in inventory:
      entry = inventory[item]
    
      if item != 'Money':
        amount_string = str(entry['Amount']) + entry['Measurement']
        print(f'{item}: {amount_string}')
      else:
        amount_string = entry['Currency'] + str(entry['Amount'])
        print(f'{item}: {amount_string}')

  if request == 'latte':
    if stock_low('Latte'):
      print(f'Sorry, not enough available {check_low_stock("Latte")}.')
    else:
      latte = drinks['Latte']
      cost = latte['Cost']
      print(f'The price for a latte is ${cost}.')
      moneys = coin_counter()
      if moneys < cost:
        print('Sorry, that\'s not enough money.')
      else:
        change = round(moneys - cost, 2)
        if str(change)[-2] == '.':
          change = str(change) + '0'
        update_inventory('Latte')
        print(f'Your change is ${change}.')
        print(f'Enjoy your latte!')
        
  elif request == 'cappuccino':
    if stock_low('Cappuccino'):
      print(f'Sorry, not enough available {check_low_stock("Cappuccino")}.')
    else:
      cappuccino = drinks['Cappuccino']
      cost = cappuccino['Cost']
      print(f'The price for a cappuccino is ${cost}.')
      moneys = coin_counter()
      if moneys < cost:
        print('Sorry, that\'s not enough money.')
      else:
        change = round(moneys - cost, 2)
        if str(change)[-2] == '.':
          change = str(change) + '0'
        update_inventory('Cappuccino')
        print(f'Your change is ${change}.')
        print(f'Enjoy your cappuccino!')
        
  elif request == 'espresso':
    if stock_low('Espresso'):
      print(f'Sorry, not enough available {check_low_stock("Espresso")}.')
    else:
      espresso = drinks['Espresso']
      cost = espresso['Cost']
      print(f'The price for an espresso is ${cost}.')
      moneys = coin_counter()
      if moneys < cost:
        print('Sorry, that\'s not enough money.')
      else:
        change = round(moneys - cost, 2)
        if str(change)[-2] == '.':
          change = str(change) + '0'
        update_inventory('Espresso')
        print(f'Your change is ${change}.')
        print(f'Enjoy your espresso!')