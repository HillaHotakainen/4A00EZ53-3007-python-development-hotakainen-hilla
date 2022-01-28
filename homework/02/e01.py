
a = "hello"
b = "world"

print(a) #Printtaa hello
print(a, b) #Printtaa hello world
print(a, b, sep=":") #Printtaa hello:world
print(a, b, sep=":", end=";") #Printtaa hello:world;
print("\n") #Printtaa rivin vaihdon

#Printtaa: 
#hello
#world
print(a, "\n")
print(b)

"""Printtaa helloworld"""
print(a, end="")
print(b)

help(print)