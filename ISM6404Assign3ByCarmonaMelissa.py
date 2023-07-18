#This is Assignment 3 of ISM-6404 by Melissa Carmona

#Task 2: Displaying Hello World
print ("Hello World")

#Task 3: Write code to display sentences
print ("Having learned to display hello world in Python, I now have the rite of passage to learn Python")
print ("I am excited to be learning Python")
print ("Tech companies these days are looking for Python skills")

#Task 4: Get name, age, weight, and height and store those values in appropriate variables

userName = "Null"
userAge = 0
userWeight = 0.0
userHeight = 0.0

Name = str(input("What is your name?"))
print (Name)

Age = int(input("How old are you?"))
print (Age)

Weight = float(input ("How much do you weigh?"))
print (Weight)

Height = float (input ("How tall are you?"))
print (Height)

               
#Task 5: Displaying sentences

print ("Hello",Name)
print ("You are",Age,"years old")
print ("Your weight is",Weight,"pounds")
print ("Your height is",Height,"inches")

#Task 6: Declaring a variable, using a function and displaying results

userBMI = 0.0

def userBMI (userWeight,userHeight):
    return (userWeight/userHeight)*703

Weight = float(input ("Please type your weight"))
Height = float (input("Please type your height"))


print(input ("Your BMI is"),userBMI(Weight,Height))

#Task #7: Creating a list

itemsInWallet = ["bills","change","business cards","credit cards","drivers license"]

print (itemsInWallet)

print (itemsInWallet[2])
print (itemsInWallet[4])
print (itemsInWallet[2:4])

itemsInWallet[3]="CC"
print (itemsInWallet[3])

itemsInWallet.append ("family photo")

print (itemsInWallet)

del itemsInWallet [2]
print (itemsInWallet)

itemsInWallet.insert(2,'business cards')
print (itemsInWallet)

itemsInWallet.pop (2)
print (itemsInWallet)

print(sorted(itemsInWallet))
print(itemsInWallet)

#Task 8: Creating a tuple for the months in a year

Months = ('January', 'February','March','April','May','June','July','August','September','October','November','December')
print (Months)

print (input ("The 6th month of the year is"),Months[5])
print (input ("The 12th month of the year is"),Months[11])

#Task 9: Creating a dictionary, changing the name and method

MoviesAvailable = {"DVD001":"The Sound of Music","DVD002":"Jaws","DVD003":"Incredibles-2"}
print (MoviesAvailable)

moviesInStock= dict(DVD001="The sound of Music", DVD002="Jaws", DVD003="Incredibles-2")
print (MoviesAvailable,moviesInStock)

#Task 10: Using loops for lists, tuples, and dictionaries

for item in itemsInWallet:
    print (item)

for months in Months:
    print (months)

for d,m in MoviesAvailable.items():
    print (d,m)




