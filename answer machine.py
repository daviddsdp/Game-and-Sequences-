import re

def replace_all(repls, str):

    return re.sub('|'.join(re.escape(key) for key in repls.keys()),
                 lambda k: repls[k.group(0)], str) 


text = input("Ask me for:") 


if  re.search(" enjoy | fun ", text):
    z =  1/3
elif re.search(" injure | pitiful ", text):
    z = -1/3
else:
    z =  0



    
if   z >=  1/3:
    print ("Yes,",replace_all({" i ": "you", "you": "i", "am": "are",
   "are": "am", "my":"your", "your":"my", "with you":"with me",
   "if": " ", "with me": "with you", "i was": "you were"}, text))

elif z <= -1/3:
     print ("I not think so that,",replace_all({" i ": "you", "you": "i", "am": "are",
     "are": "am", "my":"your", "your":"my", "with you":"with me",
     "if": " ", "with me": "with you", "i was": "you were"}, text))

elif z > -1/3  and  z <1/3:
     print ("Maybe,",replace_all({" i ": "you", "you": "i", "am": "are",
     "are": "am", "my":"your", "your":"my", "with you":"with me",
     "if": " ", "with me": "with you", "i was": "you were"}, text))

elif z == 0:  
     print ("I don't know if,",replace_all({" i ": "you", "you": "i", "am": "are",
     "are": "am", "my":"your", "your":"my", "with you":"with me",
     "if": " ", "with me": "with you", "i was": "you were"}, text))
    
  
     

     
   

					
