import time 
inicio = time.time()
lista  = []
for i in range(100000):
    lista.append(i)

for i in range(100000):
    lista.insert(0,i)

fim = time.time()
print(fim - inicio)
