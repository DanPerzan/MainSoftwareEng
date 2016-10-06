# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
def isPrime(n):
    for i in range(2, int(n**0.5 + 1)):
        if n%i == 0:
            return False
    return True

currentFactor = 2
bigNumber = 600851475143
largest = 0
while currentFactor <= bigNumber:
    if isPrime(currentFactor) and bigNumber % currentFactor == 0:
        largest = currentFactor
        bigNumber /= currentFactor
    else:
        currentFactor += 1
        
print largest