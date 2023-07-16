PIE = 3.142
message = """
r- Calculate radius 
a- Calculate area
q- to quit
h- for help
"""
print(message)


def circle_area(r):
    area = PIE*r**2
    return area


def circle_radius(a):
    r = (a/PIE)**1/2
    return r


while True:
    command = input("Enter your option: ")
    if command == "q":
        break
    elif command == "a":
        radius = float(input("Enter your radius (m): "))
        print(f"your area is {circle_area(radius)}(m^2)")
        break
    elif command == "h":
        print(message)
    elif command == "r":
        area = float(input("Enter your area on (m^2)"))
        print(f"Your radius is m{circle_radius(area)}")
    else:
        print("please choose from the options")
        print(message)
