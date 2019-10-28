import re


a = re.sub(" ","|",input('Type here your encoded fun, then where and when you offer it us:'))

    

while True:
    b = input('Tell me please about your fun. Then when and where youre looking for. One word per input is enough:')
    if  re.search(a,b):
        print('Something happen let you know!')
    else:
        print('Notting happen around the world.')  




