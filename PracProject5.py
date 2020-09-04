# def func(lis):
#     count=0
#     i=0
#     while(count!=len(lis)):
#         r=1
#         if lis[i]<10:
#             i+=1
#             count+=1
#         elif lis[i]>=10:
#             while(1):
#                 if (str(lis[i]+r)==str(lis[i]+r)[::-1]):
#                     lis[i]=lis[i]+r
#                     count+=1
#                     i+=1
#                     break
#                 else:
#                     r+=1
#     return lis
# if __name__ == '__main__':
#     a=int(input("Enter the number of elements: "))
#     li=[]
#     for i in range(a):
#         li.append(int(input(f"Enter the {i+1} number: ")))
#     print("\nYou entered: ",li)
#     print("\nThe palindrome list of this list is: ",func(li))