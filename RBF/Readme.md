# RBF

As Redes Neurais RBF (Radial Basis Function) são modelos supervisionados compostos por uma camada oculta cujos neurônios utilizam funções de base radial — geralmente do tipo Gaussiana — para mapear entradas de forma não linear. Tais redes são especialmente úteis para tarefas de classificação e regressão, podendo aproximar funções arbitrárias desde que haja um número suficiente de neurônios na camada intermediária.

Diferentemente das redes multicamadas treinadas por retropropagação, as RBFs são comumente treinadas em duas etapas: definição dos centros das funções de base (por exemplo, via *k*-means) e ajuste dos pesos da camada de saída (via métodos lineares, como regressão logística ou mínimos quadrados).

## Atividade

Vamos aplicar uma rede RBF ao problema do Câncer de mama (Breast Cancer). Esta base de dados pode ser carregada do pacote mlbench. Esta base de dados possui 9 variáveis de entrada, uma variável de saída com a classificação das 699 amostras em malígno e benígno.

Nesta atividade o aluno irá realizar o treinamento da RBF para separar as classes e avaliar o desempenho do mesmo.

O aluno deverá então:

1. Carregar os dados e armazená-los. Estes dados devem receber um tratamento
inicial para eliminação dos dados faltantes. Os dados faltantes são representados
pelo string NA. Dica: utilize os comandos abaixo para fazer o carregamento e a
limpeza dos dados.

```r
library("mlbench")
# pega os dados da package mlbench
data("BreastCancer")
data2 <- BreastCancer
# Realiza o tratamento dos dados para remoção de NA
data2 <- data2[complete.cases(data2),]
```

2. Rotular as amostras das Classes com o valor de 0 (malígno) e 1 (benígno).  
3. Usar a validação cruzada para realizar o treinamento e teste com 10 folds.  
4. Utilizar as amostras de treinamento para fazer o treinamento da RBF.
5. Aplicar o modelo treinado na classificação do conjunto de testes.
6. Calcular o erro percentual. (O erro é dado pelo número de amostras de teste classificadas de forma errada)
7. Gere um relatório em PDF com os resultados pra cada fold e o erro médio final e seu desvio padrão  

**ATENÇÃO**: você deve utilizar um algoritmo de clustering como o k-médias para determinar o melhor número de centros (número de neurônios na camada escondida). Varie o número de centros para determinar qual o melhor. O melhor número de centros será aquele que resultar em um menor erro médio ao final da classificação.

Utilize a função `kmeans` do R:

- Para agrupar use o comando: `cl = kmeans(dados, k)`, onde `dados` é a matriz de dados a serem agrupados e `k` é o número de centros.  
- Os agrupamentos podem ser acessados com o comando: `cl$cluster`  
- Os centros podem ser acessados com: `cl$centers`
