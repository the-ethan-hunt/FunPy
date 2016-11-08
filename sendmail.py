# coding: utf-8
from bs4 import BeautifulSoup
import smtplib
fromaddr='sender's mail'
toaddrs='ID where mail is to be sent'
msg='Hi! i sent this message via Python. Peace!'
server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
username='ID'
password='password'
server.login(username,password)
server.sendmail(fromaddrs,toaddrs,msg)
server.sendmail(fromaddr,toaddrs,msg)
server.quit
