# coding: utf-8
from bs4 import BeautifulSoup
import smtplib
fromaddr='dhruvgirishapte@gmail.com'
toaddrs='vermaparth97@gmail.com'
msg='Hi! i sent this message via Python. Peace!'
server=smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(dhruvgirishapte@gmail.com,iamgreat)
username='dhruvgirishapte@gmail.com'
password='iamgreat'
server.login(username,password)
server.sendmail(fromaddrs,toaddrs,msg)
server.sendmail(fromaddr,toaddrs,msg)
server.quit
