## Section 1b: Conditionals

### What Does the Computer See?

ASCII-code -> Bit patterns that are the conversion between high level to low level. See https://www.ascii-code.com/. When we code we see variables, but the computer actually sees binary bit patterns. Hence in the backend our code is being translated to bits.

### Conditionals
Conditionals -> If / elif / else statements.

Basic Conditional:
```
password_input = "mypass"
secret = "mypass"
canEnter = False

if password_input == secret:
   canEnter = True
else:
  canEnter = False
```
Multiple Conditions:
```
username_match = True

if password_input == secret and username_match == True:
  canEnter = True
  print("You may enter")
elif password_input != secret and username_match == True:
  canEnter = False
  print("Your PASSWORD is wrong!")
elif password_input == secret and username_match == False:
  canEnter = False
  print("Your USERNAME is wrong!")
else:
  canEnter = False
  print("Incorrect username and password")
```
Practice Exercises:
```
"""
Practice Problem: Your programming teacher has decided he's going to write a program that will give you praise you if you get a good grade and ridicule you if you get bad grades. If you get an "A" in the class you will receive an "Excellent I'm proud of you".  If you get a "B" in the class you will get a "Above average". If you get a "C" in the class you will get a "I am disappointed." If you get anything less than a "C" you will get a "You need to retake the class." Create this program for your teacher to get on his good side.
"""

grade = "A"

if grade == "A":
  message = "Excellent I'm proud of you"
elif grade == "B":
  message = "Above average"
elif grade == "C":
  message = "I am disappointed"
else:
  message = "You need to retake the class"

print(message)
```