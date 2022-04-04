l=[]
count=0
def createList(l):
    for i in range(5):
        s=input('Enter any string : ')
        l.append(s)
createList(l)
def evenlength(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
            print('The list is {} and its length is {}.'.format(i,count))
evenlength(l)
