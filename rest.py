import numpy as np
import matplotlib.pyplot as plt

#with open('rest.txt', 'r') as rest:
    #t = [float(i) for i in rest.read().split("\n")] 

rest_array = np.loadtxt("rest.txt", dtype = int) 
with open('kalibrovka.txt', 'r') as kalibr:
    k = kalibr.read()

pressure_array = np.polyval(k, np.poly1d(rest_array))

time_array = np.arange(0,len(rest_array),1)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(pressure_array, time_array, "g")

plt.title("График давления в состоянии покоя")
plt.xlabel("Время, с")
plt.ylabel("Давление, мм рт. столба")
plt.legend("p(t)")
plt.minorticks_on()

fig.savefig("rest-pressure.png") #сохранение графика
plt.show()









