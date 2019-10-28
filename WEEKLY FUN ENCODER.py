import re


a = re.sub(" ","",input('Paste hier your enconded fun. Then where and when you offer us'))
    

while True:
    b = input('Tell me please about your fun. Then when and where youre looking for. One word per input is enough')) 
    if  re.search(b,a):
        print('Something happen let you know!')
    else:
        print('Notting happen around the world.') 







