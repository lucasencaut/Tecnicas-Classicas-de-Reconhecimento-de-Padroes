Descrição do KNN
O KNN é um algoritmo de aprendizado supervisionado baseado em instâncias. Ele classifica um novo ponto de acordo com a maioria das classes presentes em seus 𝑘 vizinhos mais próximos.

O funcionamento do algoritmo pode ser resumido nos seguintes passos:

1. Calcular a distância entre o ponto a ser classificado e todos os pontos do conjunto de treinamento.
2. Selecionar os 𝑘 vizinhos mais próximos.
3. Determinar a classe predominante entre esses vizinhos.
4. Atribuir essa classe ao ponto de teste.

A principal variável que influencia o desempenho do KNN é o valor de 𝑘. Valores muito pequenos podem resultar em sobreajuste (o modelo se torna muito sensível aos dados de treinamento), enquanto valores muito grandes podem levar à perda de detalhes importantes na decisão da classificação.

Este repositório contém a implementação do KNN, permitindo testar diferentes valores de 𝑘 e observar como isso afeta a fronteira de decisão do modelo.
