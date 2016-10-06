# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

i = 1
sum = 0
f = 0

while f <= 4000000:
    f = fib(i)
    if f%2 == 0:
        sum += f
    i += 1
print sum
    