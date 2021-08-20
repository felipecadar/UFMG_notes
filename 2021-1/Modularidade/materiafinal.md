# Prova Final

- 04/08/2021: MÓDULO VIII.
  - ESTILO DE PROGRAMAÇÃO
    - Efeito colateral em funções
    - Estado concreto X estado abstrato
    - Objetos como máquinas de estado
    - Exemplo tradicional - tipo lista de inteiros
    - Exemplo de objetos como máquina de estado
    - Novo contrato de Lista de inteiros
    - Nova versão de implementação de lista de inteiros
- 09/08/2021: 
  - TRATAMENTO DE FALHAS
    - Exceções em Java
    - Declaração de exceção
    - Hierarquia de exceções
    - Métodos que falham
    - Lançamento de exceção
    - Detecção da falha
    - Exemplos
    - Cláusula finally
    - Formato geral das exceções
    - Captura de exceções
    - Objeto de Exceção
    - Informações agregadas
    - Conclusão
- 11/08/2021: MÓDULO IX.
  - PROGRAMAÇÃO ORIENTADA POR ASPECTOS
    - Requisitos Transversais.
    - Intrusão e Espalhamento.
    - Joinpoints.
- 16/08/2021: 
  - PROGRAMAÇÃO ORIENTADA POR ASPECTOS
    - Pointcuts.
    - Advices
    - Exemplos.

___________________________________________________________________

# ESTILO DE PROGRAMAÇÃO

## Efeito Colateral

- A obrigação da função é simplesmente retornar um valor, mas além disto ela muda o estado do objeto.
- Todo procedimento deve ter efeito colateral.
- O procedimento só existe pelo efeito colateral.
- Um procedimento sem efeito colateral não serve para
nada.
- Efeito colateral em procedimentos pode mudar valor de
parâmetros e/ou de variáveis globais 

Ele pode ser:
- Nocivo: Geralmente Efeito Colateral em Funções é nocivo a boa qualidade da programação
- Útil

Efeito colateral pode ser evitado:
```Java
Randômico.defineSemente(semente);
Randômico.gerePróximo( );
x = Randômico.valor( ) 
```

## Estado Concreto X Estado Abstrato