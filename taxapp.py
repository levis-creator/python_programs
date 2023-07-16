price =input('Enter the price ($): ')
tax=input('Enter the tax rate (%): ')

net_price= int(price) * int(tax)/100
print(f'the net price is ${net_price}')

