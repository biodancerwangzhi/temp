import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def from_to_excange(from1, to1):
  url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=CKOFDDCHRW6LSK6R'%(from1, to1)
  r = requests.get(url)
  return r.json()['Realtime Currency Exchange Rate']['5. Exchange Rate']

def send_email(text):
  host, port ="smtp.163.com", 25
  pwd = 'YKWIGUJYUXSRDMQQ'
  fromAddress = 'nasap2022@163.com'
  toAddress = 'szxszx@foxmail.com'
  msg = MIMEText(text,'plain','utf-8')

  msg['Form'] = Header( fromAddress )
  msg['To'] = Header( toAddress )
  msg['Subject'] = Header(text)

  server = smtplib.SMTP_SSL(host)
  server.connect(host,465)

  server.login(fromAddress, pwd)
  try:
    server.sendmail(fromAddress, toAddress, msg.as_string())
    print( '邮件 发送 成功')
  except:
    print( '邮件 发送 失败')


# USD
try:
  rate = float( from_to_excange('USD', 'CNY') )
  if rate < 6.5:
    send_email('美元汇率 低于 6.5, 可以买美元')
  if rate > 7.2:
    send_email('美元汇率 高于 7.2, 可以卖美元')
except:
  print( 'USD API error')

# JP
try:
  rate = float( from_to_excange('CNY', 'JPY') )
  if rate > 20:
    send_email('日元汇率 低于 20, 可以买日元')
  if rate < 18:
    send_email('日元汇率 高于 18, 可以卖日元')
except:
  print( 'JP API error')

send_email('青龙面板测试1')