import numpy as np
import matplotlib.pyplot as plt

# Narx oralig'ini belgilash
p = np.linspace(0, 40000, 100)

# Talab va taklif funksiyalarini hisoblash
D = 50 - 0.002 * p
S = 12.5 + 0.0025 * p

# Grafikni chizish
plt.figure(figsize=(8, 6))
plt.plot(p, D, label='Talab (D)', color='blue')
plt.plot(p, S, label='Taklif (S)', color='red')

# Muvozanat nuqtasini topish
p_eq = 8333.33
D_eq = 50 - 0.002 * p_eq

plt.scatter(p_eq, D_eq, color='green', zorder=5)
plt.text(p_eq + 1000, D_eq, f'Muvozanat: {p_eq:.2f} so\'m, {D_eq:.2f} kg', color='green')

# Grafikni sozlash
plt.title("Talab va Taklif Egri Chiziqlari")
plt.xlabel("Narx (so'm)")
plt.ylabel("Miqdor (kg)")
plt.legend()
plt.grid(True)
plt.show()