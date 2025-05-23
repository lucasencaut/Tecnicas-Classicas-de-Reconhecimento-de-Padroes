# -*- coding: utf-8 -*-
"""Bayes2D.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r9paVm2LXjuL7M0t5Lo3lPg0DSL1PDtV
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

# 1. Carregar dados
data = load_breast_cancer()
X = data.data
y = data.target

# 2. Padronizar (importantíssimo para Gaussianas)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 3. Função da Gaussiana multivariada
def gaussian_pdf(x, mean, sigma):
    k = len(mean)
    diff = np.reshape(x - mean, (-1, 1))  # coluna
    exponent = -0.5 * (diff.T @ np.linalg.inv(sigma) @ diff).item()
    denom = np.sqrt((2 * np.pi) ** k * np.linalg.det(sigma))
    return float(np.exp(exponent) / denom)

# 4. Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Separar os dados por classe
X0 = X_train[y_train == 0]
X1 = X_train[y_train == 1]

# 6. Calcular médias e covariâncias - espalhamento moderado
mean0 = X[y == 0].mean(axis=0)
mean1 = X[y == 1].mean(axis=0)

cov0 = np.eye(X.shape[1]) * 2.0
cov1 = np.eye(X.shape[1]) * 2.0

# print("Média da classe 0:", mean0)
# print("Média da classe 1:", mean1)

# print("Covariância da classe 0:\n", cov0)
# print("Covariância da classe 1:\n", cov1)

# 4. Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Separar os dados por classe
X0 = X_train[y_train == 0]
X1 = X_train[y_train == 1]

# 6. Calcular médias e covariâncias - abertura maior (mais “espalhada”)
mean0 = X[y == 0].mean(axis=0)
mean1 = X[y == 1].mean(axis=0)

cov0 = np.eye(X.shape[1]) * 5.0
cov1 = np.eye(X.shape[1]) * 5.0

# print("Média da classe 0:", mean0)
# print("Média da classe 1:", mean1)

# print("Covariância da classe 0:\n", cov0)
# print("Covariância da classe 1:\n", cov1)

# 4. Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Separar os dados por classe
X0 = X_train[y_train == 0]
X1 = X_train[y_train == 1]

# 6. Calcular médias e covariâncias - espalhamento assimétrico (classe 0 bem dispersa e classe 1 mais concentrada)
mean0 = X[y == 0].mean(axis=0)
mean1 = X[y == 1].mean(axis=0)

cov0 = np.eye(X.shape[1]) * 5.0
cov1 = np.eye(X.shape[1]) * 0.5

# print("Média da classe 0:", mean0)
# print("Média da classe 1:", mean1)

# print("Covariância da classe 0:\n", cov0)
# print("Covariância da classe 1:\n", cov1)

# 4. Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Separar os dados por classe
X0 = X_train[y_train == 0]
X1 = X_train[y_train == 1]

# 6. Calcular médias e covariâncias - espalhamento assimétrico (classe 0 mais concentrada e classe 1 bem dispersa)
mean0 = X[y == 0].mean(axis=0)
mean1 = X[y == 1].mean(axis=0)

cov0 = np.eye(X.shape[1]) * 0.5
cov1 = np.eye(X.shape[1]) * 5.0

# print("Média da classe 0:", mean0)
# print("Média da classe 1:", mean1)

# print("Covariância da classe 0:\n", cov0)
# print("Covariância da classe 1:\n", cov1)

# 4. Dividir em treino/teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 5. Separar os dados por classe
X0 = X_train[y_train == 0]
X1 = X_train[y_train == 1]

# 6. Calcular médias e covariâncias - considerar correlação entre atributos
mean0 = X0.mean(axis=0)
mean1 = X1.mean(axis=0)
cov0 = np.cov(X0.T)
cov1 = np.cov(X1.T)

# print("Média da classe 0:", mean0)
# print("Média da classe 1:", mean1)

# print("Covariância da classe 0:\n", cov0)
# print("Covariância da classe 1:\n", cov1)

# 7. Classificação dos dados de teste
y_pred = []

for x in X_test:
    p0 = gaussian_pdf(x, mean0, cov0)
    p1 = gaussian_pdf(x, mean1, cov1)
    y_pred.append(0 if p0 > p1 else 1)


# 8. Avaliação
acc = accuracy_score(y_test, y_pred)
print("Acurácia:", acc)

# 9. Espaço das log-verossimilhanças (opcional)
p0_list = []
p1_list = []
for x in X:
    p0 = gaussian_pdf(x, mean0, cov0)
    p1 = gaussian_pdf(x, mean1, cov1)
    p0_list.append(p0)
    p1_list.append(p1)
p0_list = np.array(p0_list)
p1_list = np.array(p1_list)

scaler_lik = MinMaxScaler()
lik_scaled = scaler_lik.fit_transform(np.vstack([p0_list, p1_list]).T)
p0_scaled = lik_scaled[:, 0]
p1_scaled = lik_scaled[:, 1]

plt.figure(figsize=(8, 6))
for i in range(len(p0_scaled)):
    color = 'red' if y[i] == 0 else 'blue'
    plt.scatter(p0_scaled[i], p1_scaled[i], color=color, alpha=0.6)

min_val = min(p0_scaled.min(), p1_scaled.min())
max_val = max(p0_scaled.max(), p1_scaled.max())
plt.plot([min_val, max_val], [min_val, max_val], 'k--', label='Fronteira de decisão')
plt.xlabel("$Q_2(x|C_0)$")
plt.ylabel("$Q_1(x|C_1)$")
plt.title("Espaço das verossimilhanças")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# 10. Fronteira de decisão no espaço x1 x x2
X_vis = X[:, :2]
mean0_vis = mean0[:2]
mean1_vis = mean1[:2]
cov0_vis = cov0[:2, :2]
cov1_vis = cov1[:2, :2]

x_min, x_max = X_vis[:, 0].min() - 1, X_vis[:, 0].max() + 1
y_min, y_max = X_vis[:, 1].min() - 1, X_vis[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                     np.arange(y_min, y_max, 0.05))
grid_points = np.c_[xx.ravel(), yy.ravel()]

zz = []
for point in grid_points:
    p0 = gaussian_pdf(point, mean0_vis, cov0_vis)
    p1 = gaussian_pdf(point, mean1_vis, cov1_vis)
    zz.append(0 if p0 > p1 else 1)

zz = np.array(zz).reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, zz, alpha=0.3, cmap=plt.cm.coolwarm)
for label, color in zip([0, 1], ['blue', 'red']):
    plt.scatter(X_vis[y == label, 0], X_vis[y == label, 1], color=color, label=f'Classe {label}', edgecolor='k')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Classificação bayesiana no espaço $x1 \\times x2$")
plt.legend()
plt.grid(True)
plt.show()