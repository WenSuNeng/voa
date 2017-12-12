from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import sqlite3


import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#msg=MIMEText('hello, send by python...','plain','utf-8')
from_addr='boliangzai@163.com'
password='zxcv123'
to_addr='1217602776@qq.com'
smtp_server='smtp.163.com'



#content from db
sum_str = ''
con = sqlite3.connect("voa.db")
for row in con.execute("SELECT * FROM voa"):
	sum_str = sum_str + row[1].__str__() + '\n'
	
msg = MIMEText(sum_str, 'plain', 'utf-8')


msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

#smtp_port=587
smtp_port=25
import smtplib
server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
