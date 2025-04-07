# Adaline

Redes neurais artificiais constituem ferramentas amplamente utilizadas para modelagem de fenômenos complexos em diversas áreas de engenharia e ciências exatas. Dentre os algoritmos clássicos, o ADAptive LInear NEuron (Adaline) destaca-se por sua simplicidade e fundamentação estatística, sendo formalmente equivalente à regressão linear de mínimos quadrados quando se adota função de ativação linear.

## Atividade

O neurônio Adaline implementa a seguinte função:

$$y(x) = f(w_n x_n + w_n-1 x_n-1 + ... + w_1 x_1 + w_0)$$ (1)

em que $$x$$ é o vetor de entrada, $$w_j$$ são os pesos associados a cada entrada $$x_j$$ e $$f(.)$$ é a função identidade.

Dado um conjunto de dados \( D = \{(x_i, y_i)\}_{i=1}^N \), deseja-se encontrar os pesos \( w_j \) que melhor aproximam a função geradora \( f_g(x) \) a partir dos dados do conjunto \( D \).

Os parâmetros \( w_j \) são ajustados de forma que:
