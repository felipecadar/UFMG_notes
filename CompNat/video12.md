# Tópicos em Computação Evolucionária - Coevolução

Niching distribui a busca nos picos mas não realiza uma busca dentro de cada pico.

Criamos o conceito de espécies. Que é um conjunto de individuos similares que só cruzam entre sí.

Coevolução é quando uma espécie interfere na outra.
- Cooperativa
  - Flores e insetos
- Competitiva
  - presa/predador

A fitness depende dos outros indivíduos, então a fitness pode variar mesmo que o indivídio não mude


## Co-evolução Competitiva

Meus indivíduos são estratégias e a seleção coloca estratégias para competir entre sí.

Estratégias de competição:
1. Um contra todos
2. Um contra k aleatórios
3. Todos contra a melhor


## Co-evolução Cooperativa

Usado para problemas grandes subdivididos em vários subproblemas. Cada subproblema representa uma espécie e é atacado de forma independente.

A fitness é avaliada em conjunto, devemos decidir como escolher indivíduos de cada espécie para avaliar juntos na fitness.

## Vantagens

Ajuda a manter Diversidade pelo conceito de espécies.

Pode ser mais rápido evoluir sub problemas menores do que um grande problema

Permite construir soluções complexas de forma incremental

Reduz a necessidade de conhecimento sobre o problema pois a fitness deixa de ser um número absoluto e sim uma competição entre estratégias(indivíduos) [DUVIDA] mas em algum ponto exite uma fitness que é um número absoluto para comparar as estratégias neh ?

## Desvantagens

Difícil de calibar e entender o comportamento.

Não tem um propósito evolutivo, eles só querem estar na frente do resto da população.

## Onde aplicar

Problemas onde é difícil calcular a fitness (por custo ou impossibilidade)

Problemas modularizáveis

