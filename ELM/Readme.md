# ELM

As Redes do tipo Extreme Learning Machine (ELM) são modelos supervisionados de aprendizado de máquina baseados em redes neurais de uma única camada oculta, cujos pesos são definidos aleatoriamente e mantidos fixos durante o treinamento. A principal vantagem das ELMs está na rapidez de treinamento, já que os pesos da camada de saída são ajustados por meio de uma solução analítica baseada em mínimos quadrados.

Apesar da simplicidade estrutural, as ELMs são capazes de resolver tarefas complexas de classificação e regressão, especialmente quando combinadas com técnicas de regularização. A presença de regularização $\ell_2$ permite controlar a complexidade do modelo e melhorar sua capacidade de generalização, suavizando a resposta da rede e reduzindo o risco de sobreajuste.

## Atividade

1. Desenvolver de próprio punho as equações para obtenção dos pesos de uma ELM, conforme Notas de Aula, Equações 10 a 21. Esta numeração se refere ao arquivo RBFKindle.pdf, compartilhado em separado. Apesar de ser um capítulo sobre redes RBF, as equações são também válidas para redes ELM. Desenvolver no papel, comentar as passagens e postar imagens da dedução em um arquivo único no Moodle.
2. Implementar a regularização de redes ELM e obter as superfícies de separação; para isto basta utilizar a equação obtida no item anterior para obter os pesos de saída da rede. Plotar a superfície de separação com e sem regularização para o mesmo conjunto de dados e observar o efeito da suavização da resposta. Qual o significado da escolha de $\lambda$? Em que esta escolha implica? Discutir e apresentar figuras.
