#!/usr/bin/env python
# coding: utf-8

# In[46]:


class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age 


# In[54]:


class Dog():
    pass
a = Dog()


# In[55]:


b = Dog()
a==b


# In[89]:


# 55>34<44
class Dog():
    
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
philo = Dog("philo",55)
vicky = Dog("vicky",33)
lesi = Dog("lesi",10)
print("{} is {} and {} is {} and {} is {}.".format(philo.name,philo.age,vicky.name,vicky.age,lesi.name,lesi.age))
if philo.age >= vicky.age:
    print("philo is older than vicky")
elif philo.age >= lesi.age:
    print("philo is older")
else:
    print("lesi is older")


# In[100]:


class Dog():
    species = "mammal"
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def speak(self, sound):
        print("{} speaks {}.".format(self.name,sound))
name1  = Dog("oaty",55)
name1.speak("booo booo")
class Dog1(Dog):
    def cat(self,sound):
        print("{} speaks {}.".format(self.name,sound))
        
name2 = Dog1("caty","45")
name2.speak("meomee")


# In[47]:


#oops concept reverse a string 
class concept():
    def __init__(self,string):
        self.string = string
        self.length = len(string)
    def reverse_string(self):
        if self.length <2:
            return False
        else:
            string1 = self.string[::-1]
            print(string1)
    def loop(self):
        for i in string1:
            print(i)
            
concept1 = concept("shiva")
concept2 = concept("ram")
concept1.reverse_string()
concept2.reverse_string()


# In[2]:


#attributes and instances declaration 
class car():
    def __init__(self,color,model,year): #instance of class color,model and year are instance variables
        self.color = color #attributes of clas
        self.model = model #attributes of class
        self.year = year   #attributes of class
          


# In[35]:


# Encapsulation

class Human():
    
    __privateVar = "this is __private variable"

    def __init__(self):
        self.className = "Human class constructor"
        self.__privateVar = "this is redefined __private variable"

    
    def showName(self, name):
        self.name = name
        return self.__privateVar + " " + name

    
    def __privateMethod(self):
        return "Private method"

   
    def _protectedMethod(self):
        return "Protected method"

    
    def showPrivate(self):
        return self.__privateMethod()

    def showProtecded(self):
        return self._protectedMethod()


class Male(Human):
    def showClassName(self):
        return "Male"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


class Female(Human):
    def showClassName(self):
        return "Female"

    def showPrivate(self):
        return self.__privateMethod()

    def showProtected(self):
        return self._protectedMethod()


h = Human()
print(h.className)
print(h.showName("Vasya"))
print(h.showPrivate())
print(h.showProtecded())
# print(h.privateMethod())
# print(h.protectedMethod())
print("\n")

m = Male()
print(m.className)
print(m.showClassName())
# print(m.showPrivate())
print(m.showProtected())
print("\n")

f = Female()
print(f.className)
print(f.showClassName())
print(f.showProtected())
print("\n")


# In[ ]:





# In[ ]:




