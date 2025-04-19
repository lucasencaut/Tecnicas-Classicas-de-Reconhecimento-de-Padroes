# Classificador de Bayes

O classificador de Bayes é um modelo probabilístico fundamentado no Teorema de Bayes, que estima a probabilidade de uma amostra pertencer a uma classe com base nas evidências fornecidas pelos atributos.

O objetivo é calcular a probabilidade posterior de cada classe $C_k$ dado um vetor de atributos $x$, utilizando:

![image](https://github.com/user-attachments/assets/1f7d3ab7-8a81-4aff-bbba-5fdb325aeb1a)

Como $P(x)$ é comum a todas as classes, o classificador escolhe a classe com maior valor de $P(x∣C_k)·P(C_k)$.

- O termo $P(C_k)$ representa a probabilidade a priori da classe.
- O termo $P(x∣C_k)$ é a verossimilhança, que pode ser modelada de diferentes formas. Neste projeto, utilizamos distribuições Gaussianas (normais).

Existem duas variantes principais:

- **Bayes Gaussiano:** usa a distribuição Gaussiana multivariada com a matriz de covariância completa, considerando correlações entre os atributos.
- **Naive Bayes Gaussiano:** assume que os atributos são independentes entre si, o que simplifica os cálculos e reduz o custo computacional. Neste caso, cada atributo é modelado por uma Gaussiana univariada.

Apesar da suposição de independência do Naive Bayes muitas vezes não ser realista, o modelo costuma apresentar bom desempenho em diversas tarefas práticas.

## Tarefa

O objetivo deste exercício é analisar o comportamento do mapeamento realizado pelo classificador bayesiano no espaço de verossimilhanças em função dos seus parâmetros. Considerando o problema do Breast Cancer que pode ser encontrado no pacote mlbench o aluno deve implementar o classificador bayesiano considerando
distribuições normais e aplicar ao problema para encontrar a melhor solução.

Ao variar os parâmetros para definir a melhor solução, analise o comportamento do mapeamento no espaço das verossimilhanças e escreva suas conclusões sobre a influência de cada parâmetro destes métodos no mapeamento.
