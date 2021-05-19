# Visualização de dados relacionais

Dados relacionais: Grafos ou redes

## Primeiro algoritmos para desenho de grafos

O artigo de Knuth de 1963 para desenhar o fluxograma de um programa

## Critérios estéticos

- Cruzamentos: Minimar o cruzamento de areastas
- Área: Minizar a área do grafo
- Arestas:
  -  Minimizar o comprimentos total das areas
  -  Minimizar o comprimento máximo
  -  Minimizar a variança dos comprimentos
-  Dobras de arestas: Minimizar
-  Resolução angular: não ter angulos tão agudos entre arestas que incidem sobre um mesmo nó
-  Razão do Aspecto: Próximo de 1
-  Simetria: Ilustrar a topologia do grafo


## Algoritmos mais clássicos

- Kamada-Kawai 1980
  - Sistema baseado em molas
- Fruchterman-Goldman
  - Define uma constante para distribuir os nós uniformemente no espaço
  - Definine forças de tração e repulsão
- Simulated Annealing - Davidson-Harel
  - Baseado nessa ideia de Simulated Annealing
  - Baseado na ideia de resfriamento do sistema
  - Começa permitindo grande varabiliedade e vai restringindo as soluções
  - Permite escolher se deixa cruzamento de arestas ou não
- Tunkeland 1994
  - Arestas de compimento uniforme
  - Nós não adjacentes devem ficar distantes
  - Cruzamentos minimizados
  - Cria uma espécie de árvore e trabalha com a ordenação dos nos. Vai colocando um nó de cada vez
- Forceatlas2 2014
  - Mais focado na experiência do usuário
  - Baseado em força
  - Força da gravidade