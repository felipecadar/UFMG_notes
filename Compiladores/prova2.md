PROVA II Matéria: Cap. 2 (2.4) e Cap. 4 (4.1-4.8 inclusive)


# Cap 2.4 - Uma análise gramtical

A análise gramatical é o processo de se determinar se uma cadeia de tokens pode ser gerada por uma gramática. 

Introduzimos um método de análise gramatical que pode ser aplicado para construir tradutores dirigidos pela sintaxe

Um analizador gramatical pode ser contruído para qualquer gramática

Para qualquer gramática livre de contexto existe um analisador gramatical que toma no máximo um tempo proporcional a O(n³) para analisar gramaticamente uma cadeia de n tokens.

A maioria dos métodos podem ser classificados em duas classes:
	1. top-down -> Raiz para folha
	2. bottom-up -> Folha para raiz

Esses termos se referem a ordem no qual os nós da árvore gramatical são contruídos.

Top-Down são mais populares pois são mais fáceis de serem contruídos a mão.

## A Análise Gramatical Top-Down

Considere a gramática

tipo -> tipo_simples
	| (up_arrow) id
	| array [ tipo_simples ] of tipo

tipo_simples -> integer
		| char
		| num pontoponto num



A construção top-down é feita iniciando pela raiz, rotulada pelo não-terminal de partida
e realizando, repetidamente, os dois seguintes passos.

1. Ao ní n, rotulado por um não-terminal A, selecione uma das produções para A e contrua
as filhos de n com os símbolos no lado direito da podrução

2. Encontre o próximo nó no qual uma subárvore deva ser construída.

Pode ser que uma expansão não seja bem sucedida, então temos que voltar e tentar outra produção.
Podemos evitar isso com a análise gramatical preditiva

## Análise Gramatical Preditiva

A "análise gramatical descendente recursiva" é uma método Top-Down de análise sintática.

Conjunto de procedimentos recursivos, um para cada não terminal.

Utiliza o símbolo `lookahead` para acabar com ambiguidades no processamento da entrada

A sequência de procedimentos defini implcitamente uma árvore gramatical para a entrada

Utilizamos a função PRIMEIRO(alpha) para ter os primeiros tokens de todas as produções possíveis de alpha. Então usamos esses primeiros tokens para recidir qual produção usar.

## Quando Usar Produções-e

A produção `e` do lado direito é usada como default quando nhenhuma outra puder ser usada.

Considere a gramática:

cmd         -> BEGIN cmds_opcs END
cmds_opcs   -> lista_cmds | e

Enquanto analisamos gramaticalmente cmds_opcs, se o símbolo `lookahead` não estiver em PRIMEIRO(lista_cmds), a produção `e` será usada. 

## Projetando um Analisador Gramatical Preditivo

Um AGP é um programa consistinf=do em um procedimento para cada não-terminal, cada procedimento realiza duas coisas:

1. 
    - Decide que produção usar examinando o `lookahead`.
    - A produção com o lado diretiro `alpha` é usada se o símbolo `lookahead` estiver em `PRMIEIRO(alpha)`.
    - Não pode haver conflitos entre lados direitos
    - Uma produção `e` no lado direito é usada se o símbolo `lookahead` não estiver no conjunto `PRIMEIRO` de nenhum outro lado direito

2. 
    -

# Aula 26 Sep 2019

- Só pode ter uma entrada na tebela, método não lê strings... Erro Reduce-Reduce
	- Duas produçoes com lado esquerdo iguais e direito diferentes 
 - O tamanhdo da tabela de LR é o mesmo da tabela de LALR
