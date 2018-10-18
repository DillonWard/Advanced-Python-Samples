from string import Template

# can change the delimeter
class MyTemplate(Template):
    delimiter = '#'

def Main():

    # create an empty list
    cart = []
    # append to the list key:value 
    cart.append(dict(item="Coke", price=2, qty=2))
    cart.append(dict(item="Cake", price=12, qty=1))
    cart.append(dict(item="Fish", price=32, qty=4))
    
    # using the template strings from the key:values
    t = MyTemplate("#qty x #item = #price")
    total = 0

    print("Cart:")

    # for each in the cart
    for data in cart:
        print(t.substitute(data))
        # take the value from the key 'price' and add it into total
        total += data["price"]
    print("Total: " + str(total))

if __name__ == '__main__':
    Main()

