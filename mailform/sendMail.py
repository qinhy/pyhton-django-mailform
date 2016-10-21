#!/usr/local/bin/python
# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
def create_msg(from_address, to_address, subject, body, encode):
  msg = MIMEText(body, 'plain', encode)
  msg['Subject'] = Header(subject, encode)
  msg['From'] = from_address
  msg['To'] = to_address
  return msg
 
def send_by_local(from_address, to_address, msg):
  s = smtplib.SMTP() 
  s.connect()
  s.sendmail(from_address, [to_address], msg.as_string())
  s.close()
 
if __name__ == '__main__':
  from_addr = 'ec2-user@example.com'
  to_addr = 'example@example.com'
  subject = '123'
  body = '123'
  encode = 'utf-8'
 
  msg = create_msg(from_addr, to_addr, subject, body, encode)
 
  send_by_local(from_addr, to_addr, msg)
