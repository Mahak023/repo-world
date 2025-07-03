a=str (input("enter a: "))
b=len(a)+1
rev=''
for i in range (1,b):#(1,-b,-1) rev+=a[i]
    rev+=a[-i]
if(a==rev):
    print('palindrome')
else:
    print('no palindrome')        

