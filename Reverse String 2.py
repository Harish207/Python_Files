def reverse(text):
    list1=[]
    for i in range(0,len(text)):
        list1.append(text[i])
    n=len(list1)
    while ((n-1)>=0):
        print list1[n-1],
        n-=1