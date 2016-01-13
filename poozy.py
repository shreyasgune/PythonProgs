from sys import exit

def dani_dungeon():
	print "You see Tejas laughing at you and pointing towards Krishna in a cage."
	print "How will you stop Tejas? He's coming towards you. For an attack or ... well, it's not clear."
	print "What do you do?"
	

	next = raw_input("> ")
	if next == "exit" :
		dead("Your bitch ass could not handle the game. Fk off.")
	if "use choco" in next :
		choco = True
		print "It's not enough. Dani needs something more potent. Can you use anything else in combination?"
	next = raw_input("> ")
	if "use ganja" in next :
		ganja = True
		print "It's not enough. Dani needs something more potent. Can you use anything else in combination?"
	next = raw_input("> ")
	if "use choco and ganja" :
		print "Dani is defeated. You get to get the hell out of here. Thanks for playing."
		exit(0)

def dead(why):
 	print why, "Chutiye, waapas khel."
 	exit(0)

def dey_room():
	print "You see Kunal Dey, who's transformed into a beast. He's going to attack you."
	print "What do you do? There is no escape. You're going to have to fight Kunal. How are you going to do it?"
	kunal_moved = False
	
	while True:
		next = raw_input("> ")
		if next == "exit" :
			dead("Your bitch ass could not handle the game. Fk off.")


		if next == "use old monk" :
			if old_monk == True :
				print "Old Monk is effective. Dey is drunk. Go on through the secret passageway"
				kunal_moved = True
				babli_room()
			else : 
				print "Chut. You didnt pick up the Old monk when you had the chance."
				dead("That's what you get for being ignorant.")

		elif next == "use ganja" :
			if ganja == True :
				dead("While Ganja is effective , Kunal is now high and wants you to smoke with him for ever. You're trapped.")
			else :
				print "Chut. You didnt pick up the Ganja when you had the chance."
				dead("That's what you get for being ignorant.")
		else :
			print "Gandu, you can't escape. I don't even know what %s means. Try again." % next

def babli_room():
	print "You see Prakhar browsing the internet. Prakhar attacks you with his Storypick and Scoopwhoop suggestions."
	print "What do you do? There is no escape. You're going to have to fight Babli. How are you going to do it?"
	babli_defeat = False
	
	while True:
		next = raw_input("> ")
		if next == "exit" :
			dead("Your bitch ass could not handle the game. Fk off.")

		if next == "use old monk" :
			if old_monk == True :
				print "Old Monk is ineffective. Babli does not drink anymore."
				dead("You are caught in an endless cycle of reading stupid shit from ScoopWhoop.")
			else : 
				print "Chut. You didnt pick up the Old monk when you had the chance."
				dead("That's what you get for being ignorant.")

		elif next == "use ganja" :
			if ganja == True :
				print "Ganja is effective. You get a bonus item : 'choco' for your ingenuity."
				print "Inventory : Old Monk , Ganja , choco \n \n "
				babli_defeat = True
				choco = True
				dani_dungeon()
			else :
				print "Chut. You didnt pick up the Ganja when you had the chance."
				dead("That's what you get for being ignorant.")
		else :
			print "Gandu, you can't escape. I don't even know what %s means. Try again." % next


def start():
	print "************************************************************"
	print "[[[[[[[[[[[[[[[[[[[[[[SAVE POOZY]]]]]]]]]]]]]]]]]]]]]]]]]]]]"
	print "************************************************************"
	print "************************************************************"
	print "INSTRUCTIONS : Just follow the questions. \n If you find something and want to pick it up \n just type 'pick [item]'. \n If you want to use something, just type 'use [item]' \n hope you have fun."
	print "If you want to use something together : use [item] and [item]"
	print "************************************************************"
	print "************************************************************"
	print "\nYou had a crazy night of drinking. The last thing you remember is gulping down a shot of whiskey and passing out. Who knows what has happened since then.. \n"
	print "You wake up, with a bad hangover.. you head hurts. \n"
	print "You're in a dark room."
	print "You stumble upon some Ganja and a bottle of Old Monk."
	global ganja, old_monk, choco, exitnow
	ganja = False
   	old_monk = False
   	choco = False
	next = raw_input("> ")
	if next == "exit" :
		dead("Your bitch ass could not handle the game. Fk off.")

	if "pick ganja" in next :
		print "You've picked up some Ganja"
		print "You have Ganja in your inventory"
		ganja = True

	if "pick old monk" in next :
		print "You've picked up some Old Monk"
		print "You have Old Monk in your inventory"
		old_monk = True

	next = raw_input("> ")

	if "pick old monk" in next :
		print "You've picked up some Old Monk"
		print "You have Old Monk in your inventory"
		old_monk = True

	if "pick ganja" in next :
		print "You've picked up some Ganja"
		print "You have Ganja in your inventory"
		ganja = True

	if (old_monk and ganja) == True :
		print "Inventory : Old Monk (1) , Ganja (1)"
	elif (old_monk==True) :
		print "Inventory : Old Monk (1)"
	elif (ganja == True) :
		print "Inventory : Ganja (1)"

	else :
		print "Inventory : NOTHING"
	print "Moving on.."


	print "There is a door to your right and left"
	print "Which one do you take?"
    
	next = raw_input("> ")

	if next == "left":
		dey_room()
	elif next == "right":
		babli_room()
	else:
		dead("You stumble around the room until you starve. Retard.")

	
start()