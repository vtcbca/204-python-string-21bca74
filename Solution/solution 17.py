#Write a script to enter any sentence and print those word which is palindrom. Also print total number of palindrom word.

s=input('Enter a sentence : ')
s+=('\0')
c=d=0
for i in s:
    c+=1
    if(i==' ' or i=='\0'):
        s1=s[d:c-1]
        s2=s1[::-1]
        if(s2==s1):
            print(s2)
        d=c
