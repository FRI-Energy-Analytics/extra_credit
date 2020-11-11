def findPermutations(m, n):  # m: # of 1's, n: # of 0's
    if n==0:                 # Recursive method to compute number of unique combinations
        return 1

    if m==1:  # returns the number of possible combinations with one 1 and n 0's
        return n+1

    total = 1
    for i in range(m):  # shifts a zero over to move (m-i) ones over one space
        total = total+findPermutations(m-i,n-1)
    return total

def SherlockPermutations(m,n):
    return findPermutations(m-1,n)  # runs recursive process leaving one 1 at beginning


def combination(m,n):  # this problem follows a simple combination equation
    def factorial(n):
        if n<2:
            return 1

        output = 1
        for i in range(2,n+1):
            output = output*i
        return int(output)
    
    return int(factorial(m+n)/(factorial(m)*factorial(n)))


m = int(input("Enter # of 1's: "))  # gets user input
n = int(input("Enter # of 0's: "))

print()  # quick method - returns answer in quick time
print("Quick Solution:")
print("Total number of orientations: "+str(combination(m,n)))
print("Number of orientations starting with 1: "+str(combination(m-1,n)))
print()  # long method - more understandable, yet with EXTREME COST
print("Long Solution: [Warning: May take a long time to compute]")
print("Total number of orientations: "+str(findPermutations(m,n)))
print("Number of orientations starting with 1: "+str(SherlockPermutations(m,n)))
