'''
checking if its updating the file or creating a whole another file
'''
l=[1,3,5,2,1,21,345,56,67,23]
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j + 1]=l[j+1],l[j]
print('sorted list is',l)