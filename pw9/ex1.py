#1.a
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('dataset.csv', delimiter=';')
v0, alpha, actual, predicted = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

#1.b
markers and colors
def get_marker_color(act, pred):
    if act == 1 and pred == 1:
        return 'blue', 'o'
    elif act == 1 and pred == 0:
        return 'red', 'x'
    elif act == 0 and pred == 1:
        return 'red', 'x'
    else:
        return 'red', 'o'

plt.figure(figsize=(8, 6))

for i in range(len(actual)):
    color, marker = get_marker_color(actual[i], predicted[i])
    plt.scatter(v0[i], alpha[i], c=color, marker=marker, label=f"Act: {actual[i]}, Pred: {predicted[i]}")

plt.xlabel("v₀")
plt.ylabel("α")
plt.title("Data Map")
plt.legend(loc='best')
plt.show()