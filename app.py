mylist = [2, 4, 6, 8, 10, 12]

i,j = 0 , len(mylist)-1

while (i<j):
    temp = mylist[i]
    mylist[i] = mylist[j]
    mylist[j] = temp
    
    i += 1
    j -= 1
print(f"ma liste finale :{mylist}")    