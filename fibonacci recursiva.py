def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2) 
res=int(input('Qual o termo deseja encontrar? '))
print(fib(res))
for i in range(res):
    print(fib(i),'', end='')
