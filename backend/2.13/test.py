# a= int(input("a too oruul: "))
# b= float(input("b butarhai too oruul: "))

# c= a + b
# print(c)

# int - buhel too 
# float - butarhai too
# str - temdegt mur
# bool true false

# list - [] olon utga 
# list(str) = [zowhn text utguud]
# list(int) = [zowhn buhel too utguud]

# array, hashmash, {} - {"name"; "John", "age": 30 "female": false}

a=5
b=3.14
c= "helo"
d= True
# print(a,b,c,d)

print("1. Hurdatgal ol: ")
print("2. mass ol: ")
print("3. energy ol: ")

choice = int(input("songoltoo oruul: ")) 
if choice == 1:
    M=float(input("energy oruul: "))
    F=float(input("hurdatgal oruul: "))
    a=F/M
    print("Hurdatgal:",a)

elif choice == 2:
     a = float(input("energy oruul: "))
     F = float(input("hurdatgal oruul: ")) 
     M = F/a
     print("Mass:",M)
else:
     a= float(input("mass oruul: "))
     m= float(input("hurdatgal oruul: "))
     F=m*a
     print("tanii energy:",F)
     



m=float(input("energy oruul: "))
a=float(input("hurdatgal oruul: "))

F=m*a
print(f"E={F}")