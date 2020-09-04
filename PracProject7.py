# Search Engine
from collections import Counter
import datetime
print("\t------------ Google.com ------------\n")
sentence=Counter(input("Enter a string: ").lower().split(" "))
start=datetime.datetime.now().microsecond
original_list=["football with Messi and ronaldo","Messi leaving fc barcelona",
     "could ronaldo pair with lionel messi at juventus","manchester city looks promising for messi",
     "erling haaland looks to lead norway in the nations league","nations league is underway in the europe"]
lis=original_list.copy()
# changing lis containing lower cased sentences
for i in range(0,len(lis)):
     lis[i]=lis[i].lower()
list_with_dic=[]
for i in lis:
     list_with_dic.append(Counter(i.split(" ")))  # creating a list containing counter dictionaries
result_dict={}

for i in range(0,len(list_with_dic)):
     r = list_with_dic[i] & sentence
     if r!=Counter():
          result_dict.update({i:len(r)})
     else:
          continue

sort=sorted(result_dict.items(),key=lambda x:x[1],reverse=True)

end=datetime.datetime.now().microsecond
print(f"\n{len(sort)} Results found in 0.{end-start} seconds\n")

for i in range(0,len(sort)):
     print(f"{i+1}. {original_list[(sort[i])[0]]}")