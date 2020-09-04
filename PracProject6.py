# def randomgen(a,b):
#     import random
#     return random.randint(a,b)
#
# if __name__ == '__main__':
#     print("----------- Welcome to Guess the number Game (Multiplayer Version) ------------")
#     count=0
#     a=int(input("\nEnter Lower bound: "))
#     b=int(input("\nEnter Upper bound: "))
#     while(b<a):
#         print("\nEnter the range again:-")
#         a = int(input("\nEnter Lower bound: "))
#         b = int(input("\nEnter Upper bound: "))
#     n=randomgen(a,b)
#     p1=1
#     p2=1
#     print("\nReady Player1: ")
#     while(count==0):
#         a=int(input("Enter a number: "))
#         if a==n:
#             print(f"\nCorrect!\n done in {p1} trials")
#             count=1
#         elif a>n:
#             p1+=1
#             print(f"\nHint: it is a number lower than that")
#         else:
#             p1+=1
#             print(f"\nHint: it is a number higher than that")
#
#     count=0
#     n=randomgen(a,b)
#     print("\nReady Player2: ")
#     while(count==0):
#         a=int(input("Enter a number: "))
#         if a==n:
#             print(f"\nCorrect!\n done in {p2} trials")
#             count=1
#         elif a>n:
#             p2+=1
#             print(f"\nHint: it is a number lower than that")
#         else:
#             p2+=1
#             print(f"\nHint: it is a number higher than that")
#
#     if(p2>p1):
#         print(f"\nPlayer 1 wins with {p1} trials over {p2} trials")
#     elif(p2<p1):
#         print(f"\nPlayer 2 wins with {p2} trials over {p1} trials")
#     else:
#         print("\nIt is a draw")