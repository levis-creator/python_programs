
your_age = int(input("Enter your age "))

if your_age<=5:
    ticket_price=50
elif your_age<16:
    ticket_price=100
else:
    ticket_price=200

print(f"You will pay ${ticket_price}")