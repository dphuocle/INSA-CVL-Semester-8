from diffprivlib.mechanisms import LaplaceBoundedDomain
import matplotlib.pyplot as plt
# Code adaptee a la nouvelle version de diffprivlib 0.4.1 et Python 3.9.2

#epsilon = 10
#delta = 0
#sensitivity = 20

originalVal = 10
size = 1000

lbd = LaplaceBoundedDomain(epsilon=10, sensitivity=20, lower=0, upper=20)
#lbd.set_epsilon_delta(epsilon, delta)
#lbd.set_sensitivity(sensitivity)
#lbd.set_bounds(0, 20)
print (lbd.randomise(originalVal))
randomset = list()
values = list()
count = list()
for i in range(size):
    randomset.append(lbd.randomise(originalVal));
for i in range(200):
    values.append(i)
    count.append(0)
for i in range(size):
    j=0
    while(j<199 and randomset[i]*10>values[j]):
        j = j+1
    count[j] = count[j]+1
   

plt.plot(values, count)
plt.show()