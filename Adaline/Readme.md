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

$$
Xw = y 
$$ \tag{0.3}

em que \( X \), \( w \) e \( y \) são definidos nas equações (0.4), (0.5) e (0.6), respectivamente.
