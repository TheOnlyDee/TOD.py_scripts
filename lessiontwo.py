#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

print ("Hello, welcome to TheOddDirt Coffee!!!")

name = input ("What is your name?")

if name == "Ben":
  evil_status = input ("Are you Evil \n")
  if evil_status == "Yes":
    print ("You're not welcome here, leave right now!!!")
    exit ()
  else:
    print ("Oh, so you're one of those good Bens. Come on in!!")
else:
  print ("Hello " +  name + " , thank you so mutch for coming in today \n \n \n")



menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

print ( name + ", what you would like from our menu today? Here is what we are serving.\n"
+ menu )

order = input()

price = 8

quantity = input ("How many coffees would you like?\n")

if order == "Frappuccino":
  price = 13
elif order == "Black Coffee":
  price = 3
elif order == "Espresso":
  price = 5
elif order == "Latte":
  price =9
elif order == "Cappuccino":
  price =10
else:
  print ("Sorry we don't have that here.")
  price = 0

print (price)

total = price * int(quantity)

print ("Thank you. Your total is $" + str ( total )  )

print ( "Sounds good, " + name + " we'll have your " + quantity + " " + order + " ready for you in a moment" )
