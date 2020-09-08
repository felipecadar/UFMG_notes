# Tópicos em Computação Evolucionária - Mecanismos de Diversidade

Em determinano momento a população vai convergir, mas nós queremos que isso aconteça mais tarde para o algoritmo ter a chance de explorar mais soluções, possivelmente melhores.


# Niching

Idealmente o número de indivíduos em torno de um pico deve ser proporcional a fitness do pico

**Motivação**: 
- Reduzir a velocidade de convergência.
- Encontra conjuntos de soluções, como diferentes espécies.

**Onde usar:**
- Em funções que possuem vários ótimos (multimodais)
- Em funções que são avaliadas em mais de um critério (multiobjetivas)

## Fitness Sharing:

Assumindo que estamos trabalhando com nichos, calculamos a fitness de um indivíduo baseado na saturação do nicho.

$F'_i = F_i / NC_i$

onde $NC_i$ e a contagem de nicho do indivíduo i

$NC_i = \sum^{N}_{j=1} SH(i,j)$

$SH(i,j)$ é a função que mede a similaridade entre dois indivíduos.

$N$ é o número de indivíuos da população.

seja $d_{ij}$ a disntância entre dois indivíuos i,j
- Se  $d_{ij} = 0$ os indivíduos são idênticos e $SH$ retorna 1
- Se $d_{ij}$ é maior que um limiar $\theta_{share}$, $SH$ retorna 0 e os indivíduos estão em nichos diferentes.
- Se $0 < d_{ij} < \theta_{share}$ então $SH$ retorna um valor entre 0 e 1.

**Como calcular a distância?**
- Genótipo: 
  - Distância de Hamming
- Fenótipo
  - Decodificar o gene em um fenótico e calcular a distancia (pode ser mais rápido)

**Vantagens**:
- Conceitualmente simples
- Simula distribuição de recursos
**Desvantagens**:
- Dificuldade de ajustar parametros
  - Solução: Ajustar dinamicamente durante a busca
- Caro:
  - Fazer calculo baseado na amostra da população


## Crowding

**Resumo**: novos indivíduos são inseridos na próxima geração substituindo pais similares

1. Agrupa os indivíduos em pares
2. Cruza todos os pares
3. Muta os indivíduos gerados pelos pares
4. Cada indivíduos gerado compete com o pai menos distante
   1. PERGUNTA: Compete só entre os pais dele ? ou entre todos?
5. O vencedor entra na nova população

**Vantagens**
- Muito simples mesmo
- Melhora a diversidade

