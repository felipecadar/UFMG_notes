```
PROVA III. Matéria: Cap. 2 (2.1-2.3), (2.7 e 2.8), Cap. 4 (4.8 e 4.9), Cap. 5
(5.1-5.3), Cap. 6 (6.2 e 6.3)
```

# Cap 2 - Um Compilador Simples de uma Passagem

## Cap 2.1 - Visão Geral

Uma linguagem de programação pode ser definida por sua sintaxe e semântica.

Para especificar a sintaxe usamos uma gramática livre de contexto. A semantica
é definida por descrições informais e exemplos sugestivos.

Notação posfixa de `9 - 5 + 2` => `9 5 - 2 +`

## ...

## Cap 2.7 - Incorporando uma Tabela de Símbolos

Armazena informações sobre várias construções da linguagem fonte. A informação é coletada em cada fase do compilador e usada na fase de síntese de código.

### A interface com a tabela de símbolos

Rotinas da tabéla de símbolos

```
inserir(s, t):  Retorna o índice da nova entrada para a cadeia S, token T
buscar(s):      Retorna o índice de uma entrada para a cadeia S ou 0 se S não for 
                encontrado
```

### O Tratamento das Palavras-Chave Reservadas

As rotinas acima podem tratar as palavras chaves reservadas

```
inserir("div", div);
inserir("mod", mod);
```

### Uma implementação da tabela de símbolos

Para não fixar o tamanho dos lexemas, sempre que inserimos algum na tabela, colocamos ele em uma grade cadeia de caracteres e marcamos seu final com um EOF, então salvamos seu endereço inicial da tabela de símbolos.

```
[d|i|v|EOF|m|o|d|EOF|...]
^          ^
Pos 1      Pos 2
```


## Cap 2.8 Máquinas de Pilha Abstratas

Basicamente uma representação intermediária do programa

### Instruções Aritméticas

A máquina de pilha abstrata deve implementar cada operador da linguagem. Os mais básicos são diretamente suportados pela máquinas, mas os mais complexos devem ser implementados como uma seuqencia de instruções.


### ...

## Cap 6.2 Especificação de um verificador simples de tipos


## Cap 6.3 Equivalência das expressões de tipo

