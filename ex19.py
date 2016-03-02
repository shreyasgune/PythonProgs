def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" %boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

print "We can just give the function number directly:"
cheese_and_crackers(20, 30)

print "Or we can use variables from our script:"
amount_of_crackers = 50
amount_of_cheese = 10

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do the math inside: "
cheese_and_crackers(10+20,5+6)

print "and we can combine the two.."
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

"""
PS C:\lpthw> python ex19.py
We can just give the function number directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

Or we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do the math inside:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

and we can combine the two..
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.
"""
