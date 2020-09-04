def func(lis):
    rec=sorted(list(lis))
    rec.reverse()
    print("Sorting list using method 1:")
    print("Sorted calories using method 1: ",rec)
    l=lis[::-1]
    print("\nSorting list using method 2:")
    print("Calories sorted using method 2: ",l)
    print("\nSorting list using method 3:")
    for i in range(0,len(lis)//2):
        lis[i],lis[len(lis)-1-i]=lis[len(lis)-1-i],lis[i]

    print("Calories sorted using method 3: ",lis)
    if(rec==lis==l):
        print("\nAll lists from different method are same!")

func([1,2,4,3])

