def isFibonacci(n):
    fib = [1]*2  #initializes the first two values
    while fib[-1]<n:  #until current number surpases the input
        fib.append(fib[-2]+fib[-1])  #records the next Fibonacci number
    
    if fib[-1]==n:  #if the last Fib number equals the input, it is a Fibonacci number
        return True
    else:
        return False

output = isFibonacci(int(input("Enter a number: ")))  #Note: I decided to overlook user-input checks for simplicity
if output:
    print("This number IS a Fibonacci number.")
else:
    print("This number is NOT a Fibonacci number.")
