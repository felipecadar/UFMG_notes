# Tópicos em Computação Evolucionária- Algoritmos Evolucionários Multi-objetivo - Parte 1/2

Quando a fitness tenta otimizar duas funções de uma vez.

$Fitness = 0.6*Obj1 + 0.4*Obj2$

É dificil colocar objetivos de métricas diferentes na mesma função. Usar dominancia de pareto

# Dominancia de Pareto

De acordo com o conceito de dominância de Pareto, uma solução S1 domina uma solução S2 se ela é melhor que S2 em pelo menos um objetivo e não é pior em nenhum outro.

# Processos de tomada de decisão

- A priori: Gera uma otimização de um objetivo ou baseada em pesos
- A postoriori: Encontra múltiplas soluções e deixa o usuário escolher
- Prograssivamente: Tocar preferencia durante a busca
- Combinação: Usa as 3 anteriores

# Diferenças de um Algoritmo Genetico padrão

- Guiar a busca na direção do fronte de Pareto
- Ter um conjunto diverso de soluções não dominadas
- Não quero perder soluções não dominiadas (elitismo)

Seleção:
- Seleção por pareto: Calculo da fitness baseado na dominancia 
- Seleção por troca: Variar os objetivos em cada seleção
- Seleção por agregação com parametros variados: Cada indivíduo tem um peso para os objetivos.

# Algoritmos clássicos

## MOGA

Ranking de pareto: Número de indivíduos que me dominam + 1

Indivíduos com mesma fitness são considerados do mesmo nicho e usam fitness sharing.

