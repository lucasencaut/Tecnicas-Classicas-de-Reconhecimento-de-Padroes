# KNN Ponderado com Mapeamento em um Espaço de Verossimilhanças

## Atividade

- **Objetivos:** Analisar o comportamento do KNN ponderado como uma função de mapeamento em um espaço de verossimilhanças.
- **Tarefa:** O KNN ponderado pode ser representado na forma de uma função de um somatório de funções de proximidade (funções radiais, funções de kernel), conforme expressão apresentada anteriormente:

  $$\hat{y} = \text{sinal} \left( \sum\_{i=1}^{N} \alpha\_i y\_i K\left(\boldsymbol{x}, \boldsymbol{x}\_i\right) \right)$$ (1)

  em que $\alpha\_i = 1 \ \forall \boldsymbol{x}\_i \in  V\_k$, $\alpha\_i = 0 \ \forall \boldsymbol{x}\_i \notin  V\_k$, $V\_k$ é o conjunto dos vizinhos mais próximos e $K(\boldsymbol{x}, \boldsymbol{x}\_i)$ é um função de kernel radial na forma de uma função Gaussiana.

    Considerando que $\alpha\_i$ seja o resultado de uma função indicadora dos vizinhos, o somatório será realizado sobre os $k$ vizinhos, sendo $k\_1$ os vizinhos da classe 1 (positiva) e $k\_2$ os vizinhos da classe 2 (negativa). A expressão anterior pode ser, portanto, reescrita da seguinte forma:
  
  $$\hat{y} = \text{sinal} \left( \sum\_{i=1}^{k\_1} K\left(\boldsymbol{x}, \boldsymbol{x}\_i\right) - \sum\_{j=1}^{k\_2} K\left(\boldsymbol{x}, \boldsymbol{x}\_j\right) \right)$$ (3)
  
    Cada um dos termos do somatório da expressão anterior representa, portanto, uma medida de pertencimento entre a amostra $\boldsymbol{x}$ que está sendo avaliada e as demais amostras de cada classe. Estas medidas, que representam similaridades entre $\boldsymbol{x}$ e as amostras de cada classe, serão representadas aqui como $Q\_1\left(\boldsymbol{x}|C\_1\right)$ e $Q\_2\left(\boldsymbol{x}|C\_2\right)$, podendo a equação original ser novamente escrita em função das mesmas:
  
  $$\hat{y} = \text{sinal} \left( Q\_1\left(\boldsymbol{x}|C\_1\right) - Q\_2\left(\boldsymbol{x}|C\_2\right) \right)$$ (3)
  
    Nesta representação a parcela $Q\_i$ de maior magnitude determinará o sinal de resposta do classificador. A expressão característica da reta separadora no plano $Q\_2(\boldsymbol{x}|C\_2 \times Q\_1(\boldsymbol{x}|C\_1)$ é $Q\_2(\boldsymbol{x}|C\_2) = Q\_1(\boldsymbol{x}|C\_1)$, ou seja, toda amostra mapeada acima desta reta será classificada como sendo da classe 2 e toda amostra abaixo da reta da classe 1. Toda amostra de entrada, independentemente da dimensão do problema, terá valores correspondentes de $Q\_2\left(\boldsymbol{x}|C\_2\right)$ e $Q\_1\left(\boldsymbol{x}|C\_1\right)$ e portanto será mapeada no plano $Q\_2(\boldsymbol{x}|C\_2 \times Q\_1(\boldsymbol{x}|C\_1)$.

    Neste exercício o aluno deverá observar o comportamento do mapeamento em $Q\_2(\boldsymbol{x}|C\_2 \times Q\_1(\boldsymbol{x}|C\_1)$ em função de $k$ para conjuntos de dados sintéticos, sendo um deles linearmente separável e o outro não-linearmente separável. Pergunta-se: qual o efeito do valor de k sobre os conjuntos de amostras mapeados? qual o efeito do valor de h sobre os conjuntos de amostras mapeados? quais as características deste mapeamento quando o valor de $k$ resulta em desempenho máximo? quais as características deste mapeamento quando o valor de $h$ resulta em desempenho máximo?
