# Adaline

Redes neurais artificiais constituem ferramentas amplamente utilizadas para modelagem de fenômenos complexos em diversas áreas de engenharia e ciências exatas. Dentre os algoritmos clássicos, o ADAptive LInear NEuron (Adaline) destaca-se por sua simplicidade e fundamentação estatística, sendo formalmente equivalente à regressão linear de mínimos quadrados quando se adota função de ativação linear.

## Atividade

O neurônio Adaline implementa a seguinte função:

$$
y(x) = f(w_n x_n + w_{n-1} x_{n-1} + \cdots + w_1 x_1 + w_0)
$$

em que:

- \( x \) é o vetor de entrada,
- \( w_j \) são os pesos associados a cada entrada \( x_j \),
- \( f(.) \) é a **função identidade**, ou seja, \( f(x) = x \).
