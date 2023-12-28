l1=[1,2,3,4]
target=7
if l1[0]+l1[1]==target:
    print([l1[0],l1[1]])
elif l1[1]+l1[2]==target:
    print([l1[1],l1[2]])
elif l1[2]+l1[3]==target:
    print([l1[2],l1[3]])
elif l1[1]+l1[3]==target:
    print([l1[1],l1[3]])
elif l1[0]+l1[2]==target:
    print([l1[0],l1[2]])
elif l1[0]+l1[3]==target:
    print([l1[0],l1[3]])
else:
    print("invalid")
    
