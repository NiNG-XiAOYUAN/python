def make_pizza(*toppings):  
    '''接受未知数量实参'''
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')

