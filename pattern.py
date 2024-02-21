pattern='ABCDFBCDFSDFGH'
#to print first recrusive character(first repeating)
dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print("first recrusive character is",i)
        break

