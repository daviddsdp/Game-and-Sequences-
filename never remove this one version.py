import re

def replace_all(repls, str):

    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                 lambda k: repls[k.group(0)], str) 


text = input (" Ask me something to do: ") 


if  re.search(" enjoy | fun ", text):
    x = 1
elif re.search(" injure | pitiful ", text):
     x= -1
else:
    x= 0

text1 = input ("Tell me more about it:") 


if re.search(" enjoy | fun ", text1):
   x1 = 1
elif re.search(" injure | pitiful ", text1):
     x1= -1
else:
    x1= 0


text2 = input ("Tell me more about it:") 


if re.search(" enjoy | fun ", text2):
   x2= 1
elif re.search(" injure | pitiful ", text2):
     x2= -1
else:
   x2= 0

    
if x + x1 + x2 > 1:
   print ("Yes,",replace_all({" i ": "you", "you": "i", "am": "are",
   "are": "am", "my":"your", "your":"my", "with you":"with me",
   "if": " ", "with me": "with you", "i was": "you were"}, text))

elif -1 > x + x1 +x2:
     print ("I not think so that,",replace_all({" i ": "you", "you": "i", "am": "are",
     "are": "am", "my":"your", "your":"my", "with you":"with me",
     "if": " ", "with me": "with you", "i was": "you were"}, text))

elif x + x1 + x2 > -1 and  x + x1 + x2 <1  :
     print ("Maybe,",replace_all({" i ": "you", "you": "i", "am": "are",
     "are": "am", "my":"your", "your":"my", "with you":"with me",
     "if": " ", "with me": "with you", "i was": "you were"}, text))

elif x + x1 + x2 == 0 :  
 print ("I don't know if,",replace_all({" i ": "you", "you": "i", "am": "are",
 "are": "am", "my":"your", "your":"my", "with you":"with me",
"if": " ", "with me": "with you", "i was": "you were"}, text))
    
  
     

     
   

					
