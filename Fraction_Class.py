#Interactive python Chapter 1

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.denom = bottom
    
    def __str__(self):
         return str(self.num)+"/"+str(self.denom)
    
    def __add__(self, other):
        a=self.num*other.denom + self.denom*other.num
        b=self.denom*other.denom
        return Fraction(a//gcd(a,b),b//gcd(a,b))
    
    def __sub__(self, other):
        a=self.num*other.denom - self.denom*other.num
        b=self.denom*other.denom
        return Fraction(a//gcd(a,b),b//gcd(a,b))
    
    def __mul__(self, other):
        a=self.num*other.num
        b=self.denom*other.denom
        return Fraction(a//gcd(a,b),b//gcd(a,b))
    
    def __truediv__(self, other):
        a=self.num*other.denom
        b=self.denom*other.num
        return Fraction(a//gcd(a,b),b//gcd(a,b))
    
    
    def __gt__ (self,other):
        if self.num*other.denom > self.denom*other.num:
            return True
        else: 
            return False
        
    def __lt__ (self,other):
        if self.num*other.denom < self.denom*other.num:
            return True
        else: 
            return False
        
    def __eq__ (self,other):
        if self.num*other.denom == self.denom*other.num:
            return True
        else: 
            return False
        

def gcd(m,n):
    while m%n != 0:
        m,n=n,m%n
    return n


f1=Fraction(3,5)
f2=Fraction(6,10)


# In[61]:

print (f1+f2)


# In[62]:

print (f1-f2)


# In[63]:

print (f1*f2)


# In[65]:

print (f1/f2)




