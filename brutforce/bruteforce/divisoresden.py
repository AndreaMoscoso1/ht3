##divisores de n 
def divisores(n):
    ndivisores = []
    num = n
    for i in range (1, n+1):
        if (num%i == 0):
            ndivisores.append(i)
    return ndivisores
x = 50
result = (divisores(x))
print("N: "+ str(x)+ " Divisores: " + str(result))

