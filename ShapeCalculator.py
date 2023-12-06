import math

def get_numeric(value):
    while True:
        try:
            return float(value)
        except:
            value = input('enter a numeric value: \n')
        
    
def greeting():
    choice_continue = input('do you wish to continue please specify (y) or (n): \n')
    if choice_continue == 'y' or greeting == 'Y':
        return()
    elif choice_continue == 'n' or greeting == 'N':
        quit()
    else:
        print('error insert (y) or (n)')
        greeting()


#main
def shape_selection ():
    greeting()
    print("""choose from the following shapes, one you wish to calculate the area and perimeter  
                   (t) trapezoid
                   (p) parralellogram
                   (r) rectangle
                   (s) square
                   (tr) triangle 
                   (c) circle              
                   """)
    shape_choice = input().lower()
    while shape_choice not in ['t', 'p', 'r', 's', 'tr', 'c']:
        print('error')
        shape_choice = input("Error invalid choice").lower()

    if shape_choice == 't':
        trapezoid_area()
    elif shape_choice == 'p':
        parralellogram_area()
    elif shape_choice == 'r':
        rectangle_area()
    elif shape_choice == 's':
        square_area()
    elif shape_choice == 'tr':
        triangle_area()
    elif shape_choice == 'c':
        circle_area()


def trapezoid_area():
    value = input('enter the height: ')
    height = get_numeric(value)
    print(height)

    value = input('enter base 1: ')
    base1 = get_numeric(value)
    print(base1)

    value = input('enter the base 2: ')
    base2 = get_numeric(value)
    print(base2)

    area = ((base1 + base2) /2 ) * height 
    print (f'the area of this trapeziod is {area}')
    return()

def parralellogram_area():
    value = input('enter the height: ')
    height = get_numeric(value)
    print(height)

    value = input('enter the base : ')
    base = get_numeric(value)
    print(base)

    area = (base*height) 
    print(f'the area of this parralelogram is' + {area})
    return()

def square_area():
    value = input('enter the height: ')
    height = get_numeric(value)
    print(height)

    value = input('enter base : ')
    base = get_numeric(value)
    print(base)

    area = (base*height)
    print(f'the area of this square is + {area**2}')
    return()

def triangle_area():
    value = input('enter the height: ')
    height = get_numeric(value)
    print(height)

    value = input('enter base : ')
    base = get_numeric(value)
    print(base)

    area = (base*height)/2
    print(f'the area of this triangle is {area}')
    return()
def rectangle_area():
    value = input('enter the height: ')
    height = get_numeric(value)
    print(height)

    value = input('enter base: ')
    base = get_numeric(value)
    print(base)

    area = (base*height)
    print(f'the area of this rectangle is {area}')
    return()

def circle_area():
    value = input('enter the radius: ')
    radius = get_numeric(value)
    print(radius)

    area = (radius**2)*math.pi
    print(f'the area of this circle is {round(area)} ')
    return()

shape_selection()


