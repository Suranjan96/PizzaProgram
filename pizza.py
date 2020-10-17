toppings_list = ['mushrooms', 'pineapples', 'bacon', 'pepperoni', 'cheese', 'bell papers']   #toppings list
toppings_left = list(toppings_list)
toppings_added = []            #begin as an empty list
option = ''

def display_toppings (toppings_list) :    # show toppings list
    print('Choose the no.of the topping to be added: ')
    for i in range (len(toppings_list)):
        print(i,toppings_list[i])
        
def print_pizza():
    print('Now your pizza has\n',toppings_added,)  

def add_toppings():      #add a topping
    try:
        print('\nYour are added the topping to your pizza.')
        display_toppings(toppings_left)
        index=int(input())
        toppings_added.append(toppings_left.pop(index))     #append adds to the end of a list 
        print_pizza()
    except:
        print("\nI'm not sure what you said, please try again.")  #if user input wrong value

    
def order_pizza():    #order the pizza
    print_pizza()
    print('\nThanks For the order!!')
    print('Would you like another pizza (y/n) ?: ')
    
def start_over():      #start over
    print("OK, let's start over\n")

    
def display_option():     #instructions
    print('\n----Operations----')
    print('\nPress a to Add a topping')
    print('Press r to Remove a topping')
    print('Press c to Change a topping')
    print('Press o to Oder the pizza')
    print('Press s to Start Over')
    print('Press q to Quit\n')
    print('\nWhat would you like to do?:')

print('+-------------------------------------------------+')
print('|                                                 |')
print('|                   PIZZERIA                      |')
print('|                                                 |')
print('+-------------------------------------------------+')
print('\nWhen prompted, enter first letter of operation.')

while True:
    display_option()
    option = input()
    if option=='a':
        add_toppings()
    elif option=='r':
        remove_toppings()
    elif option=='c':
        change_pizza()
    elif option=='o':
        order_pizza()
        option = input()
        if option=='y':
            toppings_left= list(toppings_list)
            toppings_added=[]        #reset to the empty list
        else:
            print('Thank You, Come Again!!')
            break
    elif option=='s':
        toppings_left= list(toppings_list)
        toppings_added=[]  #reset to the empty list
        start_over()
    elif option=='q':   #quit
        print('Thank You, Come Again!!')
        break
    else:
        print("\nI'm not sure what you said, please try again.")    
else:
    print('\nThank You!!')

