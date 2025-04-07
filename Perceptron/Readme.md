# Perceptron

O algoritmo Perceptron, proposto por Frank Rosenblatt em 1958, é um dos modelos mais antigos de redes neurais artificiais. Ele foi originalmente concebido para resolver problemas de classificação linearmente separáveis, utilizando uma regra de aprendizado baseada em correção de erro. Apesar de sua simplicidade, o Perceptron é importante do ponto de vista histórico e teórico, sendo a base para arquiteturas mais complexas, como redes multicamadas.

## Atividade

O exercício abordará o treinamento do perceptron simples aplicado ao problema do Câncer de mama (Breast Cancer). Esta base de dados pode ser carregada do pacote `mlbench`. Esta base de dados possui 9 variáveis de entrada, uma variável de saída com a classificação das 699 amostras em maligno e benigno. A descrição completa deste banco de dados pode ser obtida na documentação do pacote.

Nesta atividade o aluno irá realizar o treinamento do perceptron para separar as classes e avaliar o desempenho do mesmo.

O aluno deverá então:

1. Implementar o algoritmo de treinamento do perceptron.
2. Carregar os dados e armazená-los. Estes dados devem receber um tratamento
inicial para eliminação dos dados faltantes. Os dados faltantes são representados
pelo string NA. Dica: utilize os comandos abaixo para fazer o carregamento e a
limpeza dos dados em R.

```r
library("mlbench")
# pega os dados da package mlbench
data("BreastCancer")
data2 <- BreastCancer
# Realiza o tratamento dos dados para remoção de NA
data2 <- data2[complete.cases(data2),]
```

3. Rotular as amostras das Classes com o valor de 0 (malígno) e 1 (benígno).  
4. Separar os dados em treinamento e teste utilizando a técnica de validação cruzada com 10 folds.  
5. Para cada conjunto:  
   - Utilizar as amostras de treinamento para fazer o treinamento do perceptron.  
   - Aplicar o modelo treinado ao conjunto de teste  
   - Calcular a acurácia do conjunto de teste.  
6. Calcular a acurácia média e o desvio padrão das soluções encontradas.
