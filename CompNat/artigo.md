<h1> Characterising Neutrality in Neural Network Error Landscapes </h1>

- IEEE Link: [Characterising Neutrality in Neural Network Error Landscapes](https://ieeexplore.ieee.org/abstract/document/7969464?casa_token=Xo7culUIS18AAAAA:fw5XT)

- Scihub Link: [Characterising Neutrality in Neural Network Error Landscapes](https://sci-hub.st/10.1109/CEC.2017.7969464)

- [ABSTRACT](#abstract)
- [INTRODUCTION](#introduction)
- [NEUTRALITY IN FITNESS LANDSCAPES](#neutrality-in-fitness-landscapes)
- [ERROR LANDSCAPES OF NEURAL NETWORKS](#error-landscapes-of-neural-networks)
- [NEUTRALITY MEASURES FOR DISCRETE SPACES](#neutrality-measures-for-discrete-spaces)
- [QUANTIFYING NEUTRALITY IN CONTINUOUS SPACES](#quantifying-neutrality-in-continuous-spaces)
  - [Neighbourhood and Neutrality](#neighbourhood-and-neutrality)

# ABSTRACT

**Intro**: A topologia da fitness pode ajudar em problemas de otimização e no comportamento de algoritmos de busca baseados em meta heurísticas

**Contexto**: Uma feature dessa topologia é a neutralidade, que é muito ignorada em problemas contínuos, mas pode ajuda muito em redes neurais baseadas em população.

**Contrib**: Duas medidas normalizadas de neutralidade baseadas em progressive random walk.


# INTRODUCTION

A superfície da fitness é chamada de *landscape*. Ela possui máximos e mínimos e os algoritmos de otimização fazem sua busca nessa superfície.

Algumas tecnicas complementares, como o *fitness landscap analysis* (FLA), analisam a geometria e topologia da superficie para predizer a performance de um algoritmo de busca qualquer usando descritores dessa surperficie, como *noise*, *ruggedness*, *searchability*, *symmetry*, e **neutrality**.

**Problema**: Quando treinamos Redes Neurais, a quantidade de variáveis (pesos) cresce muito rápido, fazendo com que visualizar e descrever a superfície de erro (*fitness landscape*) seja uma tarefa muito difícil. 

**Motivação**: Alguns estudos sugerem que a presença de **neutralidade** em vários níveis na superfície de erro (como se fosse uma escada) atrapalha os algoritmos de otimização, principalmente os algortimos evoluvionarios (EAs). Então é interessante ter uma medida de neutralidade para alterar esses algoritmos na sua presença.

#  NEUTRALITY IN FITNESS LANDSCAPES

Acontece quando soluções vizinha possuem valores muito semelhantes de erros.

O conceito de neutralidade nasceu com uma pesquisa de evolução molecular de Kimura[9], que mostrava que mutações genéticas frequentemente não causavam efeitos no fenótipo, e são chamadas portanto de *neutras*. Isso provê ao indivíduo resistência a mutações.

#  ERROR LANDSCAPES OF NEURAL NETWORKS

Uma rede neural e uma estrutura de neurônios conectados po pesos. Dado *m* pesos, uma solução é *m-dimensional*

A topologia da superfície de erro depende de :
1. Da separabilidade lineer dos dados - the linear separability of the data set
2. Da função de atiavação - the activation functions employed
3. Da função de loss - the definition of the loss function
4. Da configuração da rede - overall network configuration

Quantificar o grau de neutralidade associoado com os atributos de uma NN e assicionar esses graus com a performance dos algoritmos de treino continuam em aberto.

# NEUTRALITY MEASURES FOR DISCRETE SPACES

Tentativas de quantizar a neutralidade ficaram no escopo de espaços de busca discretos.

O algoritmo abaixo tem sido usado para explorar regiões neutras em *ribonucleic acid (RNA) sequence folding*. O tamanho do caminho retornado é uma medida não normalizada de neutralidade.

**Algorítmo** *Neutral Walk*:

```python
X0 inicia com uma solução aleatória.
walk = []
N é o conjuntos de vizinhos neutros de X0
d = 0
def dist(x, y): # é a distancia entre as soluções X e Y
    return norma 2 de y - x

while len(N) > 0:
    y = rand(N | dist(X0, y) > d ) # Seleciona um vizinho aleatório
                                   # tal que a distância entre X0 e y seja 
                                   # maior que d

    if y: # se y existir
        walk.append(y) # Adiciona y a caminhada
        N = neigh(y) # N agora são os vizinhos neutros de y
        d = d(X0, y) # atualiza a distância d para ir afastando de X
    else: # se y não existir
        N = []

return walk
```

Outra estratégia, de Vanneschi, Pirola, and Collard, assumem uma representação em grafo para construir um subgrafo de regiões neutras conectadas. Eles geram métricas como a *average neutrality ratio*

...

> The neutral walk algorithm could potentially be adapted for real-encoded landscapes, however in its current form the focus is really on discovering (possibly narrow) neutral pathways as opposed to determining the extent of neutral regions that exist within the landscape.

# QUANTIFYING NEUTRALITY IN CONTINUOUS SPACES

Ideia básica: Fazer várias *random walks* em uma superfícil, que resulta em sequencias de estruturas de 3 pontos que se sobrepõem.

Estruturas de 3 pontos conetem uam solução e seus vizinhos a direira e esquerda.

## Neighbourhood and Neutrality

> A neighbourhood is defined as all solutions within the hypercube with **x** as centre point and length of side **s**

