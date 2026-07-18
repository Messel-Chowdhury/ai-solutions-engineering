# Exercise - Day 3

age = 45 # in years
print('My age: ', age)
height = 1.72 # in meters
print('My height: ', height)
complex_num = 4 - 3j
print('A complex number: ', complex_num)

# Calculate the area of a triangle
t_base = int(input('Enter base: '))
t_height = int(input('Enter height: '))
t_area = 0.5 * t_base * t_height
print('The area of the triangle is ', t_area)

# Calculate the perimeter of a triangle
side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))
side_c = int(input('Enter side c: '))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is ', perimeter)

# Calculate the area and the permeter of a rectangle
rec_length = int(input('Enter length: '))
rec_width = int(input('Enter width: '))
rec_area = rec_length * rec_width
rec_perimeter = 2 * (rec_length + rec_width)
print('The area of the rectangle is: ', rec_area)
print('The perimeter of the rectangle is: ', rec_perimeter)

# Calculate the area and the circumference of a circle
pi = 3.14
radius = float(input("Enter radius: "))
cir_area = pi * radius ** 2
circum = 2 * pi * radius
print('The area of the circle is: ', cir_area)
print('The circumference of the circle is: ', circum)

# Calculate the slope, x-intercept and y-intercept
# y = 2x - 2
slope8 = 2
x_intercept = (1, 0)
y_intercept = (0, -1)
print('Slope :', slope8)
print('x-intercept :', x_intercept)
print('y-intercept :', y_intercept)

# Calculate the slope and Euclidean distance
x1 = int(input('Enter x coordinate for point 1: '))
y1 = int(input('Enter y coordinate for point 1: '))
x2 = int(input('Enter x coordinate for point 2: '))
y2 = int(input('Enter y coordinate for point 2: '))
slope9 = (y2 - y1)/(x2 - x1)
e_distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** (1/2)
print('Slope :', slope9)
print('Euclidean distance :', e_distance)

# Compare the slopes
print('Is slope in task 8 grater than slope in task 9: ', slope8 > slope9)

# Calculate the value of y (y = x^2 + 6x + 9)
x = int(input("Enter x: "))
y = x ** 2 + 6 * x + 9
print(y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
len_python = int(len('python'))
len_dragon = int(len('dragon'))
print('The length of python and the length of dragon are equal: ', not len_python == len_dragon)

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('Is on is found in both python and dragon: ', 'on' in 'python' and 'on' in 'dragon')

print('Is jargon is in the sentence I hope this course is not full of jargon: ', 'jargon' in 'I hope this course is not full of jargon')

print('There is no on in both dragon and python:', not ('on' in 'python' and 'on' in 'dragon'))

print('The length of the text python: ', str(float(len('python'))))

# Even or not
num = int(input("Enter number: "))
reminder = num % 2
print('The number is even: ', not bool(reminder))

print('The floor division of 7 by 3 is equal to the int converted value of 2.7: ', (7 // 3) == int(2.7))

print('Is type of ','10','equal to type of 10: ', ('10' is 10))

print('Is int(','9.8',') is equal to 10: ', int(float('9.8')) == 10)

# Calculate pay of the person
hours = int(input('Enter hours: '))
rate_per_hour = int(input('Enter rate per hour: '))
weekly_earning = hours * rate_per_hour
print('Your weekly earning is: ', weekly_earning)

# Calculate the number of seconds a person can live
years = int(input('Enter number of years you have lived: '))
print('You have lived for ', years * 365 * 24 * 60 * 60, 'seconds.')

# Table
p = 1
print(p, 1, p, p ** 2, p ** 3)
p += 1
print(p, 1, p, p ** 2, p ** 3)
p += 1
print(p, 1, p, p ** 2, p ** 3)
p += 1
print(p, 1, p, p ** 2, p ** 3)
p += 1
print(p, 1, p, p ** 2, p ** 3)