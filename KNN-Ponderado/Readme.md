# KNN com Ponderação de Distâncias

Diferentemente do KNN simples, onde cada vizinho tem o mesmo peso na decisão, o KNN com ponderação de distâncias atribui pesos aos vizinhos com base na proximidade do ponto de teste. Isso significa que vizinhos mais próximos terão maior influência na decisão do que vizinhos mais distantes.

Essa abordagem permite um modelo mais flexível e menos sensível à escolha do parâmetro 𝑘, tornando a classificação mais robusta.

O código fornecido neste repositório implementa essa versão do KNN, permitindo comparar a fronteira de decisão com a do modelo simples.

## Atividade

- **Objetivos:** Representação do KNN com ponderação de distâncias e entendimento desta abordagem como uma combinação de funções radiais.
- **Tarefa:** Estender a implementação anterior incluindo a ponderação de distâncias para a tomada de decisão da classificação. De acordo com esta abordagem a resposta do KNN é representada na forma
  
  $$\hat{y} = \text{sinal} \left( \sum_{i=1}^{N} \alpha_i y_i K(x, x_i) \right)$$ (1)
  
  em que $\alpha_i = 1 \ \forall x_i \in  V_k$, $\alpha_i = 0 \ \forall x_i \notin  V_k$, $V_k$ é o conjunto dos vizinhos mais próximos e $K(x, x_i)$ é um função de kernel radial na forma de uma função Gaussiana.

    Avaliar os efeitos dos parâmetros do modelo e da função no desempenho do modelo, considerando a resposta observada da superfície de separação. Para o exemplo de dados sintéticos implementado, a função Gaussiana (Normal) é de duas variáveis, no entanto, sugere-se que ela seja implementada em sua forma geral:
  
  $$p(x) = \frac{1}{\sqrt{(2\pi)^n |\boldsymbol{\Sigma}|}} \exp \left( -\frac{1}{2} (x - \boldsymbol{\mu})^T \boldsymbol{\Sigma}^{-1} (x - \boldsymbol{\mu}) \right)$$ (2)

  em que $n$ é a dimensão de $x$, $\boldsymbol{\Sigma}$ é a matriz de covariâncias, $|\boldsymbol{\Sigma}|$ o seu determinante e $\boldsymbol{\mu}$ é o vetor de médias das distribuições marginais, conforme apresentado a seguir nas Equações 3 e 4.

  ![image](https://github.com/user-attachments/assets/8a3f3db0-7be3-40d8-9760-28513eb1b2f3) (3)

  ![image](https://github.com/user-attachments/assets/d17e29b4-1358-4265-8983-1244155f4835) (4)

    Para facilitar a implementação, considere a seguinte implementação em $R$ da função de densidade Normal multivariada:

    ```r
    pdfnvar <- function(x, m, K, n) (1 / (sqrt((2 * pi)^n * det(K)))) * exp(-0.5 * (t(x - m) %*% solve(K) %*% (x - m)))

    em que $\boldsymbol{K} = h\boldsymbol{I}$, sendo assim $h$ o raio da função Gaussiana.

    Nesta etapa o desempenho do classificador será avaliado de acordo com os parâmetros $k$ e $h$.
