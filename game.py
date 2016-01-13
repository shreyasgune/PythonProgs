print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ") 

if door == "1" :
	print "There is a giant bear here eating a strawberry cake. What do you do?"
	print "1.Take the cake."
	print "2.Scream at the bear"

	bear = raw_input("> ")

	if bear == "1" :
		print "The bear eats your face off. The hell did you think was going to happen?"
	if bear == "2" :
		print "The bear eats your legs off. Boo hoo hoo, now you can't run."
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2" : 
	print "You stare into the endless abyss at Cthulu's retina."
	print "1.Blueberries"
	print "2.Yellow Jacket Clothespin"
	print "3.Understanding revolvers yelling melodies."

	insanity = raw_input("> ");

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good jawb!"
	else : 
		print "The insanity rots your eyes into a pool of muck. Well, shit."

else:
	print "You stumble around and fall on knife and die. Good job, retard. Now try again."
