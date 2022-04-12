
First_name = input("Enter Your Name : " ).lower()
Second_name = input("Enter His / Her  Name : ").lower()

a = list(First_name.replace(" ", ""))                #To remove empty spaces
b = list(Second_name.replace(" ", ""))



#To remove the same letters

l=[i for i  in  (a and b)]
l1=[i for i  in  (b and a)]
for i in l:
    for j in a:
        if i==j:
            a.remove(i)
            break
for i in l1:
    for j in b:
        if i==j:
            b.remove(i)
            break



#The FLAMES part


c1 = a+b    
d=len(c1)
f=list("flames")


while len(f)>1:
    c=0
    for j in range (d):
        for i in f :
            c+=1 
            if c == d:
                pos = f.index(i)
                a1=f[0:pos]
                if f!=a:
                    b1=f[pos+1:len(f)]
                    f=b1+a1
                    c=0
                    break
                else:
                    f=a1
                    c=0
                    break



#To print the bond                

if f[0]=="f":
     print("Friend")
elif f[0]=="l":
     print("Lover")
elif f[0]=="a":
     print("Affection")
elif f[0]=="m":
     print("Married")
elif f[0]=="e":
     print("Enemy")
else:
     print("Sister")
