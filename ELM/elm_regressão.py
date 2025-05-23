# -*- coding: utf-8 -*-
"""ELM-Regressão.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gX4YWvT9C2_4hyzJ2YPPDDdJYBfVTaoJ
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Função de ativação (Eq. semelhante à que gera H em Eq. \eqref{eq:elm-mat})
def activation(x, func='tanh'):
    if func == 'sigmoid':
        return 1 / (1 + np.exp(-x))
    elif func == 'tanh':
        return np.tanh(x)
    else:
        raise ValueError("Escolha 'tanh' ou 'sigmoid'.")

# Geração de dados: y = sin(x) + ruído
np.random.seed(42)
N = 100
x = np.linspace(-10, 10, N).reshape(-1, 1)
y_true = np.sin(x)
y = y_true + 0.1 * np.random.randn(*x.shape)

# Padronização das entradas (melhora a estabilidade numérica)
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Parâmetros da ELM
n_hidden = 20
lambda_reg = 0.01  # λ da Eq. 5 e 9

# Pesos aleatórios da camada oculta (não treinados)
W = np.random.randn(x.shape[1], n_hidden)
b = np.random.randn(n_hidden)

# Matriz de ativações da camada oculta H (Eq. 2})
H = activation(x_scaled @ W + b)

# Solução sem regularização: w = (HᵗH)^(-1) Hᵗy (caso λ = 0)
w_no_reg = np.linalg.pinv(H) @ y

# Solução com regularização (Eq. 9):
# w = (HᵗH + λI)^(-1) Hᵗy
I = np.identity(n_hidden)  # Matriz identidade = forma simplificada de A
w_reg = np.linalg.inv(H.T @ H + lambda_reg * I) @ H.T @ y

# Geração de pontos para curva de predição
x_test = np.linspace(-10, 10, 300).reshape(-1, 1)
x_test_scaled = scaler.transform(x_test)
H_test = activation(x_test_scaled @ W + b)

# Saídas preditas
y_pred_no_reg = H_test @ w_no_reg
y_pred_reg = H_test @ w_reg
y_test_true = np.sin(x_test)

# Plot das curvas
plt.figure(figsize=(10, 5))
plt.plot(x_test, y_test_true, label='Função alvo (sen)', linestyle='dashed')
plt.scatter(x, y, label='Dados com ruído', s=20, alpha=0.6)
plt.plot(x_test, y_pred_no_reg, label='ELM sem regularização', color='red')
plt.plot(x_test, y_pred_reg, label=f'ELM com regularização ($\\lambda$ = {lambda_reg})', color='green')
plt.legend()
plt.title('Regressão com ELM - Efeito da Regularização')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.tight_layout()
plt.show()