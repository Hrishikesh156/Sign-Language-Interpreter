import time
import pyttsx3
engine = pyttsx3.init()

text_val = 'All the best for your exam.'  
language = 'en'
prev_val = None
start_time = None

while(True):
    new_val = '10'
    current_time = time.time()
    if(start_time != None):
        elapsed_time = current_time - start_time
        if(elapsed_time>seconds):
            prev_val = None


    if(new_val != prev_val):
        start_time = time.time()
        seconds = 5
        print(new_val)
        engine.say(new_val)
        engine.runAndWait()
        prev_val = new_val   
    else:
        print("same value")
      

   




  
  

 



# import time
# start_time = time.time()
# seconds = 4

# while True:
#     current_time = time.time()
#     elapsed_time = current_time - start_time

#     if elapsed_time > seconds:
#         print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
#         break