'''x="I AM GOING TO MY HOME TODAY"
print(x[2])
for i in range(1,15,2):
    print(x[i])


x="3"
print(type(x))'''
'''sen="hi hello whats up"
print(sen[::2])
print(sen[-11])'''


#print(" ENTER THE INPUT IN ONLY CAPITAL LATTER or in small letter")
v=input("enter vowels  = ")
z="aeiouAEIOU"

'''if v in z:
    print("yes input is vowel")
else:
    print("no input is not in vowel")'''
for i in range(len(v)):
    for j in range(len(z)):
        if v[i]==z[j]:
            print("yes",v[i],"is a Vowel")
        
            
        