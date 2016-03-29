import smtplib

sender = 'shreyas.enug@gmail.com'
receiver = 'knambiar41@gmail.com'
password = 'dominus170890'
subjects = ['chocolega','le na choco','kyun nahi lega','le na saaley','le le']
bodies = ['pride fuckin witchu','you hear me hill billy boy','tell that bitch to chill']
message = "\r\n".join([
  "From: shreyas.enug@gmail.com",
  "To: knambiar41@gmail.com",
  "Subject:"+str(subjects),
  "",
  ""
  ])

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()

server.login(sender,password)
for i in range(0,30):
	server.sendmail(sender,receiver,message)
	print " %d mail sent" %i
server.quit()