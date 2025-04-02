# KNN Ponderado com Mapeamento em um Espaço de Verossimilhanças

## Atividade

- **Objetivos:** Analisar o comportamento do KNN ponderado como uma função de mapeamento em um espaço de verossimilhanças.
- **Tarefa:** O KNN ponderado pode ser representado na forma de uma função de um somatório de funções de proximidade (funções radiais, funções de kernel), conforme expressão apresentada anteriormente:

  $$\hat{y} = \text{sinal} \left( \sum_{i=1}^{N} \alpha_i y_i K(\boldsymbol{x}, \boldsymbol{x}_i) \right)$$ (1)

  em que $\alpha_i = 1 \ \forall \boldsymbol{x}_i \in  V_k$, $\alpha_i = 0 \ \forall \boldsymbol{x}_i \notin  V_k$, $V_k$ é o conjunto dos vizinhos mais próximos e $K(\boldsymbol{x}, \boldsymbol{x}_i)$ é um função de kernel radial na forma de uma função Gaussiana.

    Considerando que $\alpha_i$ seja o resultado de uma função indicadora dos vizinhos, o somatório será realizado sobre os $k$ vizinhos, sendo $k_1$ os vizinhos da classe 1 (positiva) e $k_2$ os vizinhos da classe 2 (negativa). A expressão anterior pode ser, portanto, reescrita da seguinte forma:
  
  $$\hat{y} = \text{sinal} \left( \sum_{i=1}^{k_1} K(\boldsymbol{x}, \boldsymbol{x}_i) - \sum_{j=1}^{k_2} K(\boldsymbol{x}, \boldsymbol{x}_j) \right)$$
  
    Cada um dos termos do somatório da expressão anterior representa, portanto, uma medida de pertencimento entre a amostra $\boldsymbol{x}$ que está sendo avaliada e as demais amostras de cada classe. Estas medidas, que representam similaridades entre $\boldsymbol{x}$ e as amostras de cada classe, serão representadas aqui como $Q_1\left(\boldsymbol{x}|C_1\right)$ e $Q_2\left(\boldsymbol{x}|C_2\right)$, podendo a equação original ser novamente escrita em função das mesmas:
  
  $$\hat{y} = \text{sinal} \left( Q_1\left(\boldsymbol{x}|C_1\right) - Q_2\left(\boldsymbol{x}|C_2\right) \right)$$ (3)
  
    Nesta representação a parcela $Q_i$ de maior magnitude determinará o sinal de resposta do classificador. A expressão característica da reta separadora no plano $Q_2(\boldsymbol{x}|C_2 \times Q_1(\boldsymbol{x}|C_1)$ é $Q_2(\boldsymbol{x}|C_2) = Q_1(\boldsymbol{x}|C_1)$, ou seja, toda amostra mapeada acima desta reta será classificada como sendo da classe 2 e toda amostra abaixo da reta da classe 1. Toda amostra de entrada, independentemente da dimensão do problema, terá valores correspondentes de $Q_2\left(\boldsymbol{x}|C_2\right)$ e $Q_1\left(\boldsymbol{x}|C_1\right)$ e portanto será mapeada no plano $Q_2(\boldsymbol{x}|C_2 \times Q_1(\boldsymbol{x}|C_1)$.

    Neste exercício o aluno deverá observar o comportamento do mapeamento em $Q_2(\boldsymbol{x}|C_2 \times Q_1(\boldsymbol{x}|C_1)$ em função de $k$ para conjuntos de dados sintéticos, sendo um deles linearmente separável e o outro não-linearmente separável. Pergunta-se: qual o efeito do valor de k sobre os conjuntos de amostras mapeados? qual o efeito do valor de h sobre os conjuntos de amostras mapeados? quais as características deste mapeamento quando o valor de $k$ resulta em desempenho máximo? quais as características deste mapeamento quando o valor de $h$ resulta em desempenho máximo?
