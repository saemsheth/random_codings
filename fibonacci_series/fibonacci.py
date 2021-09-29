# Fibonacci series
def fibonacci(n):
    #base case when the number is less than 1
    if n<=1:
        return n 
    return fibonacci(n-1) + fibonacci(n-2)
    
def main():
    n = int(input('Enter the length of sequence: '))
    for i in range(1,n+1):
        print(fibonacci(i))

main()