#!/usr/bin/env python
# coding: utf-8

# 1. Which of the following operators is used to calculate remainder in a division?
# A) # B) &
# C) % D) $

# Answer=%

# 2. In python 2//3 is equal to?
# A) 0.666 B) 0
# C) 1 D) 0.67

# In[1]:


2//3


# 3. In python, 6<<2 is equal to?
# A) 36 B) 10
# C) 24 D) 45

# In[4]:


6<<2


# 4. In python, 6&2 will give which of the following as output?
# A) 2 B) True
# C) False D) 0

# In[8]:


6&2


# In python, 6|2 will give which of the following as output?
# A) 2 B) 4
# C) 0 D) 6

# In[6]:


6|2


# 6. What does the finally keyword denotes in python?
# A) It is used to mark the end of the code
# B) It encloses the lines of code which will be executed if any error occurs while executing the lines of code in 
# the try block.
# C) the finally block will be executed no matter if the try block raises an error or not.
# D) None of the above
# 

# Answer=The finally block will be executed no matter if the try block raises an error or not.

# 7. What does raise keyword is used for in python?
# A) It is used to raise an exception. B) It is used to define lambda function
# C) it's not a keyword in python. D) None of the above

# Answer=It is used to raise an exception.

# 8. Which of the following is a common use case of yield keyword in python?
# A) in defining an iterator B) while defining a lambda function
# C) in defining a generator D) in for loop.

# Answer=in defining a generator

# 9. Which of the following are the valid variable names?
# A) _abc B) 1abc
# C) abc2 D) None of the above

# Answer=abc2

# 10. Which of the following are the keywords in python?
# A) yield B) raise
# C) look-in D) all of the above

# Answer=yield and raise

# 11. Write a python program to find the factorial of a number.

# In[16]:


i=int(input("Enter the number= "))
fac=1
while (i>0):
    fac=(fac*i)
    i=i-1
print("The factorial= ",fac)


# 12. Write a python program to find whether a number is prime or composite.
# 

# In[25]:


n=int(input("Enter a number= "))
n1=1
count=0
while (n1<=n):
    if (n%n1==0):
        count=count+1
    n1=n1+1
if(count==2):
    print("prime number")
else:
    print("composite number")


# 13. Write a python program to check whether a given string is palindrome or not.

# In[27]:


a=input("Enter a string")
b=a[-1::-1]
if (a==b):
    print("String is a palindrom string")
else:
    print ("String is not a palindrom string")


# 14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[28]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[29]:


test_str = "Datatrained"
  
all_freq = {}
  
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
  
print ("Count of all characters in Datatrained is :\n "
                                        +  str(all_freq))


# In[ ]:




