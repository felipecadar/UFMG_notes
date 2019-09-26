PROVA II Matéria: Cap. 2 (2.4) e Cap. 4 (4.1-4.8 inclusive)


# Cap 2.4 - Uma análise gramtical

A análise gramatical é o processo de se determinar se uma cadeia de tokens pode ser gerada por uma
gramática. 

Introduzimos um método de análise gramatical que pode ser aplicado para construir tradutores
dirigidos pela sintaxe

Um analizador gramatical pode ser contruído para qualquer gramática

Para qualquer gramática livre de contexto existe um analisador gramatical que toma no máximo um tempo
proporcional a O(n³) para analisar gramaticamente uma cadeia de n tokens.

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


Exemplo de entrada: "array [num pontoponto num ] of integer"


Processo:
------------------------------------------------------------------------
Árvore Gramatical:

tipo
^
------------------------------------------------------------------------
Entrada:

array [num pontoponto num ] of integer
^

------------------------------------------------------------------------

(a) "tipo" não é folha, então derivamos 


------------------------------------------------------------------------
Árvore Gramatical:

tipo

array [ tipo_simples ] of tipo
^
------------------------------------------------------------------------
Entrada:

array [num pontoponto num ] of integer
^

------------------------------------------------------------------------

(b) temos uma folha e um match entre os dois símbolos marcados (chamado de lookahead)
	então movemos os dois cursores

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ tipo_simples ] of tipo        
      ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
      ^

------------------------------------------------------------------------

(c) enquando temos matchs entre os cursores e a gramática está em folhas, continuamos
	a mover o cursor

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ tipo_simples ] of tipo        
        ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
        ^

------------------------------------------------------------------------

(d) expandimos a gramática testando as folhas até achar um macth ou não achamos e terminamos

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo     
        ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
        ^

------------------------------------------------------------------------
------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo
            ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
            ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo
                       ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                       ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo
                           ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                           ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo
                             ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                             ^

------------------------------------------------------------------------


------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo
                                ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                                ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of tipo_simples
                                ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
			        ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of integer
                                ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                                ^

------------------------------------------------------------------------

------------------------------------------------------------------------

Árvore Gramatical:

tipo

array [ num pontoponto num ] of integer
                                             ^
------------------------------------------------------------------------
Entrada:

array [ num pontoponto num ] of integer
                                             ^
        
------------------------------------------------------------------------

Acabamos a expansão e a sequência de tokens foi aprovada

Pode ser que uma expansão não seja bem sucedida, então temos que voltar e tentar outra produção.
Podemos evitar isso com a análise gramatical preditiva

## Análise Gramatical Preditiva

A "análise gramatical descendente recursiva" é uma método Top-Down de análise sintática.



# Aula 26 Sep 2019

- Só pode ter uma entrada na tebela, método não lê strings... Erro Reduce-Reduce
	- Duas produçoes com lado esquerdo iguais e direito diferentes 
 - O tamanhdo da tabela de LR é o mesmo da tabela de LALR
