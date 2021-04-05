# HW0
# Prithvi Kannan
# UID: 405110096

### Exercise 1 ###
# your code here
a = 5
b = 2.0
tup = (a, b, a+b, a-b, a/b)

print("tup: ", tup)
print("tup is type: ", type(tup)) 

tup[0] = 2 # this will fail since tuples are immutable

### Exercise 2 ###
# your code here
primes = []
for i in range(2, 101):
    if(False not in (i % j for j in range(2, i))):
        primes.append(i)

primes = [i for i in range(2,100) if(all(i % j for j in range(2, i)))]

print(primes)

### Exercise 3 ###
# your code here
def isprime(n):
    isprime = True
    if n < 2:
        isprime = False
    else:
        for i in range(2,n):
            if n % i == 0:
                isprime = False
    return isprime

primes = [i for i in range(2,101) if isprime(i)]

print(primes)

### Exercise 4 ###
# your code here
mat = np.random.random((5,5))
unit = np.ones((5,5))
result = mat * unit
result

### Exercise 5 ###
# your code here
print("my_dict before: ", my_dict)
for key in my_dict:
    if my_dict[key]%2 == 1:
        print(key)
        my_dict[key] *= 2
        
print("my_dict after: ", my_dict)