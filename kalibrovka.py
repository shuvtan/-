import numpy as np
import matplotlib.pyplot as plt


forty_array = np.loadtxt("40 mmHg.txt", dtype = int)
eighty_array = np.loadtxt("80 mmHg.txt", dtype = int)
hundred_twenty_array = np.loadtxt("120 mmHg.txt", dtype = int)
hundred_sixty_array = np.loadtxt("160 mmHg.txt", dtype = int)

f = np.mean(forty_array) #среднее значение АЦП при давлении 40 мм рт. столба
e = np.mean(eighty_array)
ht = np.mean(hundred_twenty_array)
hs = np.mean(hundred_sixty_array)

kalibr_array = np.array([f, e, ht, hs])
pressure_array = np.array([40, 80, 120, 160])

k = np.polyfit(kalibr_array, pressure_array, 1) #вычисление коэффициента колибровки
with open('kalibrovka.txt', 'w') as f: #сохранение коэффициента колибровки в файл
        f.write(str(k))

fig, ax = plt.subplots(figsize=(16, 10), dpi = 400)
ax.plot(kalibr_array, pressure_array, "g")

plt.title("Калибровочный график зависимости значения АЦП от давления")
plt.xlabel("Давление, мм рт.столба")
plt.ylabel("Отчет АЦП, мм рт. столба")
plt.legend("N = k*p")
plt.minorticks_on()

plt.text(80, 2.5, "Коэффициент калибровки k= ", k)

fig.savefig("pressure-calibration.png") #сохранение графика
plt.show()

