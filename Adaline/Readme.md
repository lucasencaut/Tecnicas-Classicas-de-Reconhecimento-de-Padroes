# Adaline

Redes neurais artificiais constituem ferramentas amplamente utilizadas para modelagem de fenômenos complexos em diversas áreas de engenharia e ciências exatas. Dentre os algoritmos clássicos, o ADAptive LInear NEuron (Adaline) destaca-se por sua simplicidade e fundamentação estatística, sendo formalmente equivalente à regressão linear de mínimos quadrados quando se adota função de ativação linear.

## Atividade

O neurônio Adaline implementa a seguinte função:

$$y(x) = f(w_n x_n + w_{n-1} x_{n-1} + \ldots + w_1 x_1 + w_0)$$ (0.1)

em que $$x$$ é o vetor de entrada, $$w_j$$ são os pesos associados a cada entrada $$x_j$$ e $$f(.)$$ é a função identidade.

Dado um conjunto de dados $$D = {x_i, y_i}_{i=1}^N$$, deseja-se encontrar os pesos $$w_j$$ que melhor aproximam a função geradora $$f_g(x)$$ a partir dos dados do conjunto $$D$$.

Os parâmetros $$w_j$$ são ajustados de forma que $$y_i = w_n x_{ni} + w_{n-1} x_{n-1,i} + \ldots + w_1 x_{1i} + w_0 \quad \forall x_i \in D$$ conforme representado no sistema de equações (0.2).

![image](https://github.com/user-attachments/assets/84c7d3de-b5ad-4cde-a038-33a1483d5a65)


O sistema representado na equação (0.2) possui $$N$$ equações e $$n$$ incógnitas, podendo também ser representado na forma matricial (0.3):

$$Xw = y$$ (0.3)

em que $$X$$, $$w$$ e $$y$$ são definidos nas equações (0.4), (0.5) e (0.6), respectivamente.

![image](https://github.com/user-attachments/assets/6575dbc6-dce6-4b7b-91ca-ce46a8952068)

A matriz $$w$$ pode ser obtida por meio da pseudoinversa, conforme Equação (0.7):

$$w = X^{+} y$$ (0.7)

em que $$X^{+}$$ é a pseudoinversa de $$X$$.

Resolva o problema original do **Boston Housing Data** utilizando o modelo **Adaline**, implementando a **solução direta** descrita anteriormente (via pseudoinversa).

O objetivo é prever o **valor médio de uma casa** na cidade de Boston com base em diversas características socioeconômicas e ambientais.

Este banco de dados pode ser carregado com o pacote `mlbench` do R:

```r
library(mlbench)
data(BostonHousing)
```

Pesquise em sua documentação ou na internet sobre o banco de dados e suas variáveis para entender melhor do que se trata.
