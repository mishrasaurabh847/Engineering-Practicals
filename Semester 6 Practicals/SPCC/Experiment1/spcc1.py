keywords=['include','stdio','void','main','int', 'printf', 'scanf', 'float', 'return']
spcl='!@#$%^&*()~_-+=><,.?/:;"[{}]\|`'
alpha='1234567890qwertyuiopasdfghjklzxcvbnm'

f = open("code.txt", "r")
s=[]
k=[]
for x in f:
  
  for i in spcl:
      if(i in x):
          s.append(i)
          x=x.replace(i, " " )
  xl=list(x.split(" "))
  for i in xl:
        if(i=='' or i =='\n'):
            continue
        else:
            k.append(i)    
            
  
#print(s)
#print(k)
a=[]
key=[]
for i in k:
    if (i not in keywords):
      a.append(i)
    else:
      key.append(i)
print("special characters ",s)
print("keywords ", key)
print("alpha numeric ",a)
dict={}
for i in s:
    dict[i]='special character'
for i in key:
    dict[i]='keyword'
for i in a:
    dict[i]='alpha numeric charater'
print("Lexeme\t\t\t\tTokens")
for i in dict:
    print("{}\t\t\t\t{}".format(i,dict[i]))

