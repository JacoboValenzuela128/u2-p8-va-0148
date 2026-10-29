import numpy as np 
import matplotlib.pyplot as plt 


diasX = ["Lun", "Mart", "Mier", "Jue", "Vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califas de VA de Arath Valenzuela (NC:0148)")
plt.xlabel("Dias de semana hábil.")
plt.ylabel("Califas en VA")
plt.grid()
plt.show()