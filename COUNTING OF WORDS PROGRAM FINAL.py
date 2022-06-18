#!/usr/bin/env python
# coding: utf-8

# In[ ]:


i = 1 
while i == 1:
    testing_string = input("Enter the lines thats has to be counted or paste it !!!")
    #orginal string 
    print ("The orginal string is :" + testing_string)
    #using the split()function 
    count = len(testing_string.split())
    #total no of words
    print("The number of words in the sentence are:" + str(count))
    additional_sentence = input("Enter 1 for next sentence or Else 0 for exit")
    if additional_sentence == '1':
        break
#breaking the function if they want to exit or printing  

print("Thank you for coming")

Print("Please Feel free to give us feedback")
 
# In[ ]:





# In[ ]:




