import re


a = re.sub(" ","|",input('Typ hier as sentences your enconded fun. Then where and when you offer it us:'))
b = re.sub(".","|",a)
print(b)
    

while True:
    c = input('Tell me please about your fun. Then when and where youre looking for. One word per input is enough')
    if  re.search(c,b):
        print('Something happen let you know!')
    else:
        print('Notting happen around the world.') 





