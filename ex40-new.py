class Song(object):

 def __init__(self,lyrics):
 		self.lyrics = lyrics

 def sing_me_a_song(self):
 	for line in self.lyrics:
 		print line

happy_bday = Song(["Happy Birthday to you","I don't want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally round tha family","With pockets full of shells"])

PA = "Could you stop this noise, I'm trying to get some rest."
paranoid_android = Song([PA])
paranoid_android.sing_me_a_song()
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()