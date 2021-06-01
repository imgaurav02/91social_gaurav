import os 
file_number = 0 
file_size = 0 
while True: 
 if file_size < 2e+6: 
   try: 
     file = open('gaurav%d.txt'%file_number, 'x') 
   except: 
      pass  
 
   text ='Hello' 
   file = open('gaurav%d.txt'%file_number, 'a') 
   file.write(text) 
 file_size = os.stat('gaurav%d.txt'%file_number).st_size 
 if file_size > 2e+6: 
   file_number += 1 
   file_size = 0 