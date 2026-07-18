# Day 2: 30 Days of python programming

# Exercises: Level 1
first_name = 'Mirja'
last_name = 'Yusuf'
full_name = first_name + ' ' + last_name
country = 'Uzbekistan'
city = 'Tashkent'
age = 333
year = 2026
is_married = False
is_true = True
is_light_on = is_true
company, salary, date_of_joining = 'UMEC', 1000, '01-01-2026'

# Exercises: Level 2
print("Checking the data type of all variables...")
print('first_name: ', type(first_name))
print('last_name: ', type(last_name))
print('full_name: ', type(full_name))
print('country: ', type(country))
print('city: ', type(city))
print('age: ', type(age))
print('year: ', type(year))
print('is_married: ', type(is_married))
print('is_true: ', type(is_true))
print('is_light_on: ', type(is_light_on))
print('company: ', type(company))
print('salary: ', type(salary))
print('date_of_joining: ', type(date_of_joining))

print("Comparing the length of first name and last name...")
print('length of first name: ', len(first_name))
print('length of last name: ', len(last_name))

print("Two Numbers...")
num_one, num_two = 5, 4
total = num_one + num_two
print('total: ', total)
diff = num_one - num_two
print('diff: ', diff)
product = num_one * num_two
print('product: ', product)
division = num_one / num_two
print('division: ', division)
reminder = num_two % num_one
print('reminder: ', reminder)
exp = num_one ** num_two
print('exp: ', exp)
floor_division = num_one // num_two
print('floor division: ', floor_division)

print("Circle...")
rad = 30
pi = 3.1416
area_of_circle = pi * rad ** 2
circum_of_circle = 2 * pi * rad
print('Area of circle: ', area_of_circle, ' m^2')
print('Circumference of a circle: ', circum_of_circle, ' m')

rad = float(input("Enter the radius of the circle: "))
area_of_circle = pi * rad ** 2
circum_of_circle = 2 * pi * rad
print('Area of circle: ', area_of_circle, ' m^2')
print('Circumference of a circle: ', circum_of_circle, ' m')

print('Input...')
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
country = input("Enter Country: ")
age = input("Enter Age: ")
print(first_name,'', last_name,'', country,'', age)

print('Running help...')
help('keywords')