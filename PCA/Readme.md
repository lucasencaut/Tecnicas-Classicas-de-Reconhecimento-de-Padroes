# PCA – Análise de Componentes Principais com a Base Olivetti Faces

A Análise de Componentes Principais (*Principal Component Analysis*, PCA) é uma técnica não supervisionada amplamente utilizada para redução de dimensionalidade, compressão de dados e visualização em espaços de menor dimensão. O PCA transforma os dados em um novo sistema de coordenadas formado por componentes ortogonais, ordenados segundo a variância que explicam nos dados originais.

Neste exercício, aplicamos o PCA à base **Olivetti Faces**, um conjunto de imagens faciais amplamente utilizado em tarefas de reconhecimento de padrões. O objetivo é reduzir a dimensionalidade dos dados, visualizar sua estrutura no espaço das duas primeiras componentes principais, e interpretar os componentes na forma de **Eigenfaces**.

## Atividade

O aluno deverá explorar como o PCA pode ser utilizado para:

1. **Projetar as imagens no espaço bidimensional** formado pelas duas componentes principais, visualizando a separabilidade das classes.
2. **Interpretar os componentes principais** (autovetores) como imagens — os chamados \_Eigenfaces\_, que indicam as regiões de maior variabilidade entre os rostos.
3. **Construir uma matriz visual dos componentes**, com os autovalores na primeira coluna e os pesos dos pixels nas demais colunas, visualizados em escala de cinza.

Mais especificamente, o aluno deverá:

- Carregar a base Olivetti Faces e organizar os dados em formato matricial.  
- Gerar os rótulos manualmente, considerando que cada pessoa possui 10 imagens consecutivas.  
- Aplicar o PCA para:
  - Visualizar a projeção dos dados no espaço de 2 dimensões.
  - Analisar os 10 primeiros componentes principais.
  - Construir a matriz dos componentes (com autovalores + pesos dos pixels).
- Discutir os resultados obtidos a partir das visualizações.

## Observações

- A visualização das projeções auxilia na identificação da estrutura global dos dados e da separação entre classes.
- Os \_Eigenfaces\_ revelam os padrões de variação entre os rostos da base, como sombras, contornos e formatos predominantes.
- A matriz dos componentes, ao apresentar os autovalores junto aos pesos dos pixels, permite interpretar o quanto cada componente contribui para a variância total dos dados.

## Ferramentas

- Linguagem: **Python**  
- Bibliotecas principais:  
  - `scikit-learn` – Para o carregamento da base Olivetti e aplicação do PCA  
  - `numpy` – Manipulação matricial e geração de rótulos  
  - `matplotlib` – Visualização das projeções, imagens e matriz dos componentes  

## Resultados esperados

Ao final da atividade, espera-se que o aluno compreenda:

- Como o PCA projeta os dados em um espaço de menor dimensão preservando a variância.  
- Como interpretar graficamente os componentes principais como imagens.  
- A relevância dos autovalores na seleção dos componentes mais informativos.  
- Como a estrutura visual dos dados reflete a variabilidade presente em conjuntos de imagens.

## Execução

Para executar o projeto, instale as dependências:

```bash
pip install numpy matplotlib scikit-learn

