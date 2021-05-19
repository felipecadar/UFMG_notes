# Experimentação, Parametrização e Análise de Algoritmos Bio-inspirados

## Introdução

1. Como avaliar se um algortimo é suficiente para resolver um problema
1. Como escolher parametros para otimizar meu resultado
1. Como comparar meu algoritmo com outros

Geralmente usamos computação natural para resolver problemas np-completos ou np-hard

## Como rodar experimentos

Algortimos são não-deterministicos, então temos rodar várias vezes.
1. Em otimização: 30 vezes (estatísticamente provado)
2. Em aprendizado: 5 ou 10 vezes (no mínimo, mas ideal é 30)

Os experimentos devem ser reprodutíveis: guardar a semente aleatória.

Sempre compare com um algoritmo de busca aleatória.

**Parametros**

Primeiro escolhemos uma parametro para variar, enquanto os outros ficam fixos.

Normalmente se começa variando tamanho da população, depois os operadores genéticos. No caso de GP p tamanho máximo da árvore dos indivíduos podem ser variados antes.

População:
1. Otimização: entre 100 a 10000
2. Aprendizado: entre 30 e 1000

Geração: 50 a 5000, depende do custo da fitness

Operadores:
1. Crossover de 90-99% em GA e 60-90% em GP
2. Mutação é, geralmente, o complementar de crossover

Se tiver usando seleção por torneio, o k também é primordial.

Em GP o tamanho da árove tem influencia muito grande

## Análise de experimentos

Coisas importantes para se verificar:
1. Diversidade:
   1. Se mais de 90% dos indivíduos são iguais em um tempo muito curto, isso pode indicar um problema
   2. Muita diversidade também pode representar um problema
   3. Podemos medir a diferença de fitness ou diferença de genes mesmo.

Podemos plotar: Num Iteraçoes X Fitness Melhores, média e Piores (Haberman)

Convergencia prematura:
1. Não utilizar o operador de reprodução
2. Diminuir pressão seletiva
   1. Reduzir o K do torneio
3. Adicionar tipos de operadores de mutação
4. Intruduzir conceitos de espécies
5. Utilizar fitness sharing

