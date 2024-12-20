import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

x = np.linspace(-100, 100, 1000)

relu_y = relu(x)
sigmoid_y = sigmoid(x)
tanh_y = tanh(x)

plt.plot(x, relu_y, label="ReLU", color="blue")
plt.title("ReLU Activation Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

plt.plot(x, sigmoid_y, label="Sigmoid", color="red")
plt.plot(x, tanh_y, label="Tanh", color="green")
plt.title("Sigmoid and Tanh Activation Functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
