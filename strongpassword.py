import random
import string

length=int(input('enter the length of your password'))

lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower+upper+num+symbols
temp=random.sample(all,length)

password="".join(temp)
print(password)
