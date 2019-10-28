import re


a = re.sub(" ","",input('+ values to dilemma:')) # You can typ your values system as sentences
b = re.sub(" ","",input('- values to dilemma:'))



while True:
    c = re.sub(" ","",input('Ask me for the dilemma:'))
    
    if re.search(c,a):
        z=   1
    else:
        z= 0 
    if re.search(c,b):
        z1= -1
    else:
        z1= 0     

    if  (z)+(z1)>0:
        print('Maybe yes!')
    elif 0>(z)+(z1):
        print('Maybe not!')
    elif 0==(z)+(z1):
        print('Not idea!')
    
