n=int(input('Enter The Number:'))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n*(factorial(n-1))
    
print(n)
result = factorial(n)

print(result)