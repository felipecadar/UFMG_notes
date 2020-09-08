# 1. Ranking e Parte-todo

Visualizar dados como partes de um todo. Comummente vem acompanhado de uma ranking, por isso juntamos as matérias.

# 2. Padrões Analíticos

Padrões visuais que nos mostram como as partes se comparam

1. Uniforme
   - Todos os valores são semelhantes
2. Uniformemente diferente
   - Variação Uniforme
3. Não Uniformemente Diferente
   - Variação não Uniforme
4. Crescentemente diferentes
5. Decrescentemente diferentes
6. Diferenças alternadas
7. Exepcional 

# 3. Representações Visuais

## 3.1. Pizza

Mostra o todo e as partes.

Bem difícil de ordenar as fatias e estimar as diferenças percentuais. Não da pra comprar vários gráficos de pizza.

Pode ser sibustituído por barras

## 3.2. Areas Empilhadas

Bom para conectar dados parte-todo no tempo. Facilita comparação

## 3.3. Graficos de Barras

Muito util para rankear os dados. Fácil comparar as barras

Temp um problema se os dados são muito próximos

## 3.4. Gráfico de pontos

Resolve o problema de dados próximos por não precisar começar do zero no eixo Y

## 3.5. Gráfico ou Diagrama de Pareto
<!-- **A professora gosta dele** -->
Colocar o valor acumulado por cima do gráfico de barras/histograma

## 3.6. Marimekko Chart (Mosaic Plot)

Um pouco confuso. Codifica duas variáveis no eixo X e Y para representar uma área no plano cartesiano 

Difícil leitura, mas condensa muita informação.

## 3.7. Barras Empilhadas

Uteis para comparar diversos relacionamentos parte todos, consideramos que temos poucas fatias e que não variam tanto

## 3.8. Barras Agrupadas

Solução para comparar mais fatias, porem perdemos uma noção do Todo

## 3.9. Sanburst

Variação do pizza para incluir hierarquina ( tipo o monitor de arquivos do linux)

## 3.10. Treemap 

Mesma ideia do sunburst mas usando retangulos

Melhor opção para dados hierarquicos 

## 3.11. Nightingale

Um diagrama circulat que tambem possui os problemas da pizza

# 4. Boas Práticas

1. Deixar o usuário fazer agrupamentos em categorias
2. Usar gráficos de pareto com percentis
3. No caso de barras com tamanhos muito diferentes, podemos pegar essas pequenas barras e fazer uma nova visualização em outra escala
   1. Ou testar escalas diferente, como log 
4. Sem queremos acompanhar um ranking durante o tempo, devemos conectar eles com uma linha

# 5. Algoritmos de Desenhos dos Tree-Maps

## 5.1. Slice and dice

Recursivamente quebrar um retangula maior em fatias menores

Desvantagem:
- Fatias muito finas
  
## 5.2. Squarified Treemaps

Tentava deixar as partes mais quadradas possível

Usa uma forma de backtracking para ir testando a razão de aspecto de todos as configurações. Ele volta e refaz uma área sempre que a razão de aspecto cresce.

Descantagem:
- Pequenas variações nos dados alteram completamente o gráfico
  - Ruim para comparar dois treemaps

## 5.3. Ordered Treemap

Escolemos um pivô para manter sia área mais estável, então as regioes de maior hierarquia antes depois do pivo também vão manter sua região. Então quando dividirmos ela recursivamente, as folhas vão continuar +/- ordenadas.

