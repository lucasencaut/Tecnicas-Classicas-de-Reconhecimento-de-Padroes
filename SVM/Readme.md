# SVM – Problema das Espirais

As Máquinas de Vetores de Suporte (*Support Vector Machines*, SVM) são modelos supervisionados amplamente utilizados para tarefas de classificação e regressão. A SVM busca encontrar um hiperplano ótimo que maximize a margem entre as classes, permitindo uma separação robusta mesmo em situações de dados não linearmente separáveis, por meio do uso de funções de kernel.

Neste exercício, exploramos a aplicação da SVM com *kernel* RBF (Radial Basis Function) na solução do clássico **problema das espirais**, um problema não linear que desafia classificadores lineares convencionais. Este problema é amplamente utilizado para ilustrar a capacidade dos classificadores de lidar com fronteiras complexas.

## Atividade

O aluno deverá observar como a regularização afeta o desempenho do SVM, equilibrando a complexidade do modelo e sua capacidade de generalização. Para isso, é necessário ajustar o hiperparâmetro `C`, de forma a encontrar um valor que proporcione o melhor equilíbrio entre *bias* e *variância*. 

Para melhor visualizar e entender o comportamento do modelo ao variar este parâmetro, será utilizado um problema de duas dimensões, como o **problema das espirais**. Além disso, também será variado o grau de sobreposição entre as classes, permitindo avaliar o desempenho do modelo em diferentes níveis de dificuldade.

Em resumo, o aluno deverá:
1. Gerar o conjunto de dados do problema das espirais (utilizando função implementada no próprio código).  
2. Dividir o conjunto de dados em treinamento e teste (ex.: 75% para treinamento e 25% para teste).  
3. Treinar o modelo SVM utilizando a biblioteca `scikit-learn` (`sklearn.svm.SVC`), realizando experimentos com diferentes valores do hiperparâmetro `C`.  
4. Gerar as superfícies de separação e calcular a acurácia dos modelos em cada configuração.  
5. Repetir todos os passos anteriores para diferentes níveis de sobreposição entre as classes.  
6. Escrever as conclusões, discutindo como a variação do parâmetro `C` e do grau de sobreposição afeta a capacidade do modelo de generalizar e separar corretamente as classes.

## Observações

- O hiperparâmetro `C` controla o grau de penalização dos erros de classificação. Valores muito altos podem levar o modelo a sobreajustar os dados (baixo *bias*, alta *variância*), enquanto valores muito baixos podem resultar em um modelo que não aprende adequadamente as fronteiras (alto *bias*, baixa *variância*).  
- A superposição entre as classes é controlada diretamente na geração dos dados. Aumentar a superposição torna o problema mais desafiador e permite avaliar a robustez do modelo frente a dados mais complexos.  
- A análise dos resultados deve considerar tanto os aspectos quantitativos (acurácia, matriz de confusão) quanto qualitativos (análise visual das superfícies de decisão).  

## Ferramentas

- Linguagem: **Python**  
- Bibliotecas principais:  
  - `scikit-learn` – Para o modelo SVM (`SVC`) e divisão dos dados (`train_test_split`)  
  - `numpy` – Manipulação de arrays e geração de dados  
  - `matplotlib` e `seaborn` – Visualização dos dados e das superfícies de decisão  

## Resultados esperados

Ao final da atividade, espera-se que o aluno compreenda:

- Como o parâmetro de regularização `C` influencia a capacidade de generalização do SVM.  
- A relação entre *bias* e *variância* no contexto do SVM.  
- Como a complexidade dos dados (grau de sobreposição) afeta o desempenho do modelo.  
- A importância da escolha adequada dos hiperparâmetros para construir modelos robustos.

## Execução

Para executar o projeto, instale as dependências:

```bash
pip install numpy matplotlib seaborn scikit-learn



