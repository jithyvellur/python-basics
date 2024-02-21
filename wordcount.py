line='cat rat bat hello cat rat bat hello cat'
#calculate word count
#words in sentence repeating time
#first step is we need to split the sentence word by word,in python we use split function and it converted to list
data=line.split(' ')
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)