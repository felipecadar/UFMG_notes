Lista para prova:

- Chpt 5: 5.6, 5.8, 5.10, 5.11
- Chpt 6: 6.1, 6.2, 6.5, 6.14
- Chpt 8: 8.1, 8.5, 8.14

<!-- # Chapter 5 - Chord Recognition

## 5.2 Template-Based Chord Recognition

2 steps: 1: cortar áudios em frames e cada frame é transformado em features. 2: pattern matching techniques are used to map each feature vector to a set of predefined chord models

### 5.2.1 Basic Approach

As in Section 3.1.2, we identify this set with the set [0 : 11] by enumerating the chroma attributes such that 0 corresponds to C, 1 to C  , and so on. A chroma feature can then be expressed as a 12-dimensional vector x = (x(0), x(1), . . . , x(11)) 

Template matching entre esse 12d vec com o 12d vec de cada nota.
 -->


# Aula 17 - Batidas - Cap 6

- Onset no spectograma

Derivada de cada linha somada

Para filtrar faz a média móvel e subtrai essa média da curva ve onset

- Novidade Complexa

Diferença entre a importancia prevista e a importancia real no espectograma dado um delta.

Soma todas as linhas.

Faz média móvel e suaviza igual o método anterior.


## Exercícios

**Exercise 6.1.** Let x : Z → R be a signal with the nonzero samples (x(0), . . . , x(6)) = (0.1, −0.1, 0.1, 0.9, 0.7, 0.1, −0.3) (all other samples being zero). Furthermore, let w : Z → R be a rectangular window function with nonzero coefficients w(−1) = w(0) = w(1) = 1 (i.e., M = 1; see Section 6.1.1). Compute all nonzero coefficients of the energy-based novelty function ∆ Energy : Z → R as defined in (6.3). 

Sol: Pega X, calcula X^2, passa a janela somando, calcula a derivada


**Exercise 6.2.** Let x : Z → R be a discrete signal. Furthermore, let w : Z → R be a
rectangular window function of length 2M + 1 centered at time zero, i.e., w(m) = 1
for m ∈ [−M : M] and w(m) = 0 otherwise. Then the local energy E xw (see (6.1)) is
given by

E(n) := ∑ (m=−M, M) x(n + m)^2 

for n ∈ Z. In the following, an operation refers to a multiplication, an addition, or
a subtraction of two real-valued samples. Determine the overall number of opera-
tions that are required to compute E xw (n) for n ∈ [0 : N − 1] using a naive approach.
Then, describe an improved procedure that reduces the overall number of required
operations. How many operations are needed by your procedure?

Recursivo.... uma merda

# Aula 20 - Decomposição


# Aula 21 - HMMs