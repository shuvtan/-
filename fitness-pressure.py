import numpy as np
import matplotlib.pyplot as plt 

fitness_array = np.loadtxt("fitness.txt", dtype = int) 
with open('kalibrovka.txt', 'r') as kalibr:
    k = kalibr.read()

pressure_array = np.polyval(k, np.poly1d(fitness_array))

time_array = np.arange(0,len(fitness_array),1)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(pressure_array, time_array, "g")

plt.title("График давления после физической нагрузки")
plt.xlabel("Время, с")
plt.ylabel("Давление, мм рт. столба")
plt.legend("p(t)")
plt.minorticks_on()

fig.savefig("fitness-pressure.png") #сохранение графика
plt.show()
