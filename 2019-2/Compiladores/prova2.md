PROVA II Matéria: Cap. 2 (2.4) e Cap. 4 (4.1-4.8 inclusive)


# Cap 2.4 - Uma análise gramatical

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

- cmd         -> BEGIN cmds_opcs END
- cmds_opcs   -> lista_cmds | e

Enquanto analisamos gramaticalmente cmds_opcs, se o símbolo `lookahead` não estiver em PRIMEIRO(lista_cmds), a produção `e` será usada. 

## Projetando um Analisador Gramatical Preditivo

Um AGP é um programa consistinf=do em um procedimento para cada não-terminal, cada procedimento realiza duas coisas:

1. 
    - Decide que produção usar examinando o `lookahead`.
    - A produção com o lado diretiro `alpha` é usada se o símbolo `lookahead` estiver em `PRMIEIRO(alpha)`.
    - Não pode haver conflitos entre lados direitos
    - Uma produção `e` no lado direito é usada se o símbolo `lookahead` não estiver no conjunto `PRIMEIRO` de nenhum outro lado direito

2. 
    - O procedimento usa a produção do lado direito.
    - Um não-terminal resulta numa chamada a um procedimento para não-terminal
    - Um token se igualando ao símbolo `lookahead` resulta na leitura do próximo token da entrada
    - Se o token da produção não coincidir com o `lookahead` temos um erro

## Recursão à Esquerda

É possivel que esse AGP entre em loop infinito com recursões à esquerda:

- expr -> expr + termo

Se o procedimento para `expr` decide usar essa produção, o lado direito tbm é `expr` e o procedimento vai ser chamado recursivamente.

Note que o `lookahead` muda somente quando um terminal do lado direito é reconhecido.

Pemos reescrever essas produções

```
A -> A alpha | beta
```

para

```
A -> beta R 
R -> alpha R | e
```

R é um novo não terminal onde a produção `R -> alpha R` é recursiva à direita


# Cap 4 Análise Sintática

# Cap 4.1 O Papel do Analisador Sintático

Analisadores são feitos para subclasses de gramáticas, LL e LR

LL são bem mais simples que LR e podem ser feitos manualmente

Nesse cap assumimos que a saída do analisador sintático seja uma representação da árvore gramatical para o fluxo de tokens produzido pelo analisador lexico.

## Tratamento dos Erros de Sintaxe

Um bom compilador deve ajudar o programador a se recuperar de erros.

Programas podem conter erros:
- Léxicos, como grafias erradas
- Sintáticos, como parenteses desbalanceados
- semânticos, como operadores incompativeis
- lógicos, como chamadas infinitamente recursivas

A maioria dos erros são descobertos na análise sintática


O objetivo de um tratador de error é:

- Relatar a presença de erros de forma clara e acurada
- Recuperar de cada erro rápido a fim de detectar errors subsequentes
- Não retardar o processamento de programas corretos

Um boa estratégia é imprimir a linha ilegal seguida do diagnóstico e deixar o programador verificar o erro


## Estratégias de Recuperação de Erros

1. Modalidade de desespero
    - É o mais simples de implementar e pode ser usado pela maioria dos métodos de análise semântica
    - Ao encontrar um erro, ele descarta os tokens até o próximo token de sincronização

2. Recuperação de Frases
    - Ao descobrir um erro, permite que o analisador realize uma correção local na entrada para permitir que o processo continue
    - Correções locais seriam: trocar vírgula por ponto-e-vírgula, remover pontuações estranhas ou adicionar ausentes
    - Temos que tomar cuidado para não gerar correções que levem a loops infinitos
    - Maior dificuldade em corrigir erros que ocorreram antes do ponto de detecção

3. Produções de Erro
    - Expandimos a gramática para aceitar os erros mais comuns e gerar diagnósticos apropriados para indicar contruções ilegais

4. Correção Global
    - Aplicar uma correção mínimia que transforme uma cadeia X ilegal e uma cadeia Y legal.
    - Muito custoso de ser implemententado, é interessante na teoria
    - Tomar cuidado para não mudar o propósito inicial do programador

# Cap 4.2 Gramáticas Livres de Contexto

Basicamente um resumo de GLC que vimos em Fundamentos de Teoria da Computação

## Ambiguidade

Uma gramática que produza mais de uma árvore gramatical para alguma sentença é dita ambígua.
Isso acontece quando existe mais de uma derivação para a mesma sentença.

# Cap 4.3 Escrevendo uma Gramática

`DEPOIS`

# Cap 4.4 Análise Sintática TOP-DOWN

Inicia a expanção da árvore gramatical pela raiz

## Analisadores Sintáticos Preditivos

Usam a primeira token de uma expansão para determinal qual expanção usar

## Diagramas de Transições para Analisadores Sintáticos Preditivos



# Cap 4.4 Análise Sintática BOTTOM_UP

# Aula 26 Sep 2019

- Só pode ter uma entrada na tebela, método não lê strings... Erro Reduce-Reduce
	- Duas produçoes com lado esquerdo iguais e direito diferentes 
 - O tamanhdo da tabela de LR é o mesmo da tabela de LALR
