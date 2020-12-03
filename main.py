"""My Sweet Integration Program"""
__author__ = "Jesus Ramos"
#Jesus Ramos
# In this program, users will be able to solve elementary mathematical equations.
name = input("Please enter your name: ")

print("Welcome", name, "!")

gender = input("Before we start, tell us a bit about your self. Are you male or female? ")

print("It's nice to know that you are a", gender)

age = input("What is your age? ")

print("Wow", age, "is so old!")

number = input("Thanks for sharing all of this information! What's your favorite number?")

print(number, "is a lame number, definitely not my favorite!")

operation = input("Since we're talking about numbers, what is your favorite math operation?")

print("Nice to know that", operation, "is your favorite, why don't we practice a few problems to get warmed up! ")

input("Let's start off with addition, what is 2 + 2?")   # using first numeric operator (addition)

a = 2
b = 2
print("Let's check, smarty pants. Answer:", a + b)

input("How about 2 - 2?")   # using second numeric operator (subtraction)

print("Hmmm, let's see if you got it! Answer:", a - b)

input("Let's kick it up a notch, what's 2 x 2?")   # using third numeric operator (multiplication)

print("Will you get this one right? Answer:", a * b)

input("We're almost done with warm up, what's 2 divided by 2?")

print("Let's see if you got it. Answer:", a / b)

#line above shows fourth numeric operator (division)

input("That was a good warm up, let's step up our game. What is the remainder when you divide 85 by 15?")

c = 85
d = 15
print("Annnnddd the answer is: ", c % d)

#the line above shows the modular operator being used

input("Let's test how good your math skills really are. What is 85 raised to the power of 15?")

print("Let's see if you got it. Answer:", c ** d)

input("How about this, what is 85 divided by 15, to the nearest whole number when rounded down?")

print("The correct answer is:", c // d)

#line above shows the floor division numeric operator being used

input("That was still easy, what about x + 5 if x = 10?")

x = 10
x += 5
print("Let's see, the correct answer is: ", x)

#line above shows assignment and shortcut operator being used

print("Let's look at some individual numbers, here's an example! ")

num = 3

if num > 0:
    print(num, "is a positive number.")
    print("This is also an integer! ")

if num >= 0:
    print("This number is either positive or zero!")
else:
    print("Booo, this is a negative number")

#The code below will give an output that will show a message if a number is either positive, negative, or zero.

if num > 0:
    print("This is a positive number")
elif num == 0:
    print("Why would you ever pick zero?")
else:
    print("This is a negative number")


if num >= 0:
    if num != 0:
        print("Hmmm, why didn't you pick zero?")
    else:
        print("Nice, a positive number")
else:
    print("This is a negative number")

print("Look at an example of two numbers, x and y. Try to find the relationship between them!")

x = True

y = False
print('x and y is', x and y)

print('x or y is', x or y)

print('not x is', not x)

numbers = input("Enter a list of numbers: ")

sum = 0
print(" Just as a quick reminder, the following is what a range or an interval of numbers looks like: ")

print(list(range(2, 20, 3)))

print(" I've thought of some numbers, let see if you can guess them... ")

digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("Sorry, you didn't guess them!")

for i in digits:
    print(i)
else:
    print("If you didn't guess any of those, sorry!")

print("Look at another way to analyze numbers, let's add numbers that lead up to a certain integer, like 10.")
n = 10
sun = 0
i = 1
while i <= n:
    sun += i
    i += 1
print("The sum is", sun)

print("That's awesome, this is just an example of all the fun things you can do with Math!")

print("Sadly, this program is coming to an end")
response = input("Did you learn anything in this program? yes or no")
if response = no:
    if response = no:
        print("Wrong answer! You're supposed to say yes!")
    else:
        print("Awesome!")
else:
    print("Awesome!")

print("It was great to meet you! Keep up the math skills!")