# # Next Palindrome
# def np(num):
#     count=1
#     while(1):
#         i=num+count
#         if(str(i)==str(i)[::-1]):
#             return f"The palindrome for {num} is: {i}"
#         else:
#             count+=1
# if __name__ == '__main__':
#     a=int(input("Enter the number of cases:"))
#     b=[]
#     for i in range(0,a):
#         b.append(int(input(f"\nEnter the {i+1} case:")))
#     for i in range(0,a):
#         print(np(b[i]))
