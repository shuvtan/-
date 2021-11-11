import numpy as np
import matplotlib.pyplot as plt

#with open('rest.txt', 'r') as rest:
    #t = [float(i) for i in rest.read().split("\n")] 

rest_array = np.loadtxt("rest.txt", dtype = int) 
with open('kalibrovka.txt', 'r') as kalibr:
    k = kalibr.read()

pressure_array = np.polyval(k, np.poly1d(rest_array))

pulse_array = np.zeros (len(rest_array))
for i in range (0,len(rest_array)-1):
    pulse_array[i] = pressure_array[i+1] - pressure_array[i]


time_array = np.arange(1,len(rest_array),1)

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(pulse_array, time_array, "g")

plt.title("График пульса в состоянии покоя")
plt.xlabel("Время, с")
plt.ylabel("Изменение давления в артерии, мм рт. столба")
plt.legend("dp(t)")
plt.minorticks_on()

fig.savefig("rest-pulse.png") #сохранение графика
plt.show()