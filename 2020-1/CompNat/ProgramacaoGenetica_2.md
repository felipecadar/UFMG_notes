# Programação Genética

## Regressão Simbólica

Usado para encontrar funções de regressão. 

É muito comum o uso de árvores com GP para modelas os indivíduos.

### Introns

Partes inúteis da árvore
Exemplo:
1. X + 0
2. X + X - X

Geram o "bloat". Incham o Algoritmo

Eles podem gerar um **vantagem**. Proteger o indivíduo contra o poder destrutivo do cross-over.

A **destantagem** é que a população utiliza mais memória e deixa a execução mais lenta.

Para evitar os íntrons podemos:
1. Penaliazar soluções complexas ( pressão de parsimônia)
2. Implementar operadores que removem íntrons
3. Eliminat crossovers destrutivos. Eliminar filhos piores que os pais

## Diferença entre GA e GP

Algoritmos Genéticos (GA)

1. Representação: originalmente, um vetor binário.
2. Principal operador: crossover (altas probabilidades)
3. Operador secundário: mutação (baixa probabilidade)

Programação Genética (GP)

1. Representação: utilizada não apenas dados, mas funções
2. Objetivo original é evoluir programas ao invés de soluções
para uma instância particular do problema
3. Acredita-se que crossover possa ter um efeito destrutivo

A difernteça está na interpretação da representação

1. GA o mapeamento entre a descrição e o objeto sendo
descrito é sempre um para um
2. GP esse mapeamento é de muitos para um
   1. Em regressão simbólica, a mesma função pode ser
descrita por diversos indivíduos 


# Quiz

## 1

Sobre algoritmos de programação genética, é incorreto afirmar que:

Escolha uma:
- Nenhuma das anteriores.
- A diversidade da inicialização da população é garantida pelo método full.
- Diferem dos algoritmos evolucionários tradicionais por terem um poder de expressividade muito maior, garantido por um conjunto de funções e terminais.
- A definição dos terminais deve seguir as propriedade de suficiência e parcimônia, que são conflitantes.
- Utiliza os mesmos métodos de seleção já discutidos, como seleção por roleta, ranking e torneio. 

Feedback

Sua resposta está incorreta.

A resposta correta é: A diversidade da inicialização da população é garantida pelo método full..

