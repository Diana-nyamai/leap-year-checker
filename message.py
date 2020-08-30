import smtplib
server = smtplib.SIMP('smtp.gmail.com')

server.login("collinskoechck34@gmail.com","Allion.com1")

msg="Hello"
server.sendmail("collinskoechck34@gmail.com","kenyadevco@gmail.com")
