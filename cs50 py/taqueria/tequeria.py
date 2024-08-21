
menu :dict[str, float] = {
    "Baja Taco" : 4.00 ,
    'Burrito' : 7.50 ,
    'Bowl' : 8.50 ,
    'Nachos' : 11.00 ,
    'Quesadilla' : 8.50 ,
    'Super Burrito' : 8.50 ,
    'Super Quesadilla' : 9.50 ,
    'Taco': '3.00',
    'Tortilla Salad': 8.00 ,
}

total_amount : int = 0
while True:
    try:
        Item = input("Item: ").title()
        if Item in menu:
          total_amount += menu[Item]
          print('Total: $', end ='')
          print('{:.2f}'.format(total_amount))

    except EOFError:
       print()
       break
