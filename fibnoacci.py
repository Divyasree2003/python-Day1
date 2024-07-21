def fib(n):
    first=0
    second=1 
    count=2
    while count<=n:
        third=first+second
        print(third,end=' ')
        first=second
        second=third
        count+=1
    return count
print("the fibnoacciseries is:",fib(10))
        
        