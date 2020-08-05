# Requisitos 
## Introdução

- Requisitos representam o que um sistema deve fazer e sobre que restrições

1. Requisitos funcionais:
   1. suas funcionalidades
2. Requisitos não-funcionais:
   1. Desempenho 
   2. usabilidade
   3. segurança
   4. disponibilidade
   5. interoperabilidade
   6. etc
   
### Exemplo

#### Sistema bancario

1. Requisitos funcionais
   1. Abrir e fechar contas
   2. Gerar extratos
   3. Realizar saques
   4. etc
2. Requisitos não funcionais 
   1. Desempenho: informar o saldo em medos de 5 segundos
   2. Disponibilidade: estar no ar 99.99% do tempo
   3. Tolerancia a falha: continuar operando
   4. Segurança
   5. Privacidade
   6. etc

### Principais Desafios

Problemas que podemos encontrar nos requisitos

1. Requisitos incompletos ou não documentados
2. Falha de comunicação entre o time e o cliente
3. Constante mudança
4. Requisitos abstratos
5. Restrições de tempo
6. Problemas de comunicação dentro do time
7. Falta de apoio dos clientes
8. Stakeholders com dificuldade de expressar o problema


### Elicitação de Requisitos

Descobrir e entender os principais requisitos do sistema
______________________________________________

## 1. Histórias de usuários

* Antes
  * Um profissional entrevistava os usuários e fazia os requisitos completos do sistema e depois entregava essa pilha de documentos para dos desenvolvedores. O processos poderia demorar até um ano e ao tempo de ser acabar o software os requisitos já mudaram
* Agora
  * Possuimos em cada time um PO (Product Owner) que entende muito bem do produto e guia os desenvolvedores contantemente

Histórias de Usuários = 3C's

* **C**artão + **C**onversas + **C**onfirmações
* Cartão: "lembrete" para conversar sobre o requisito
* Confirmação: cenários que serão usados pelo PO para aceitar a implementação da história. Então desde o início os devs sabem como o PO vai testar a história

**Exemplo**

1. Cartão: "Fechar uma compra"
2. Conversas: Po explica os meios de pagamentos; as formas de entrega, formas de parcelamento, etc
3. Confirmação:
   1. Testar compra à vista e compra parcelada
   2. Testar com cartões A, B e C
   3. Testar com modos de entrega X e Y
   
**Quem escreve as histórias ?**

O PO escreve as histórias no início do projeto para criar uma lista inicial de histórias. Participam os representantes dos principais usuários

"Workshop de escrita de histórias"

**Formato escrita de histórias**

Como um [tipo de usuátio], eu gostaria de [realizar algo]

**Exemplo de Biblioteca**
* histórias por tipos de usuários 
  * Típico
    1. Como um usuário típico eu gostaria de realizar um empréstimo de livros
    2. Como um usuário típico eu gostaria de devolver um livro que tomei emprestado
  * Professor
    1. Como professor, eu gostaria de realizar empréstimos de maior duração
    2. Como professor, eu gostaria de sugerir a compra de livros
  * Funcionário
    1. Como funcionário da biblioteca, eu gostaria de cadastrar novos usuários
    2. Como funcionário da biblioteca, eu gostaria de ....


* Teste de aceitação para "pesquisar por livros"
  1. Pesquisar por livros, informando ISBN
  2. Pesquisar por livros, informando autor; retorna livros cujo autor contém a string de busca
  3. Pesquisar por livros, informando título; retorna livros cujo título contém a string de busca
  4. Pesquisar por livros cadastrados na biblioteca desde uma data até a data atual

Os testes de aceitação devem ser especificados pelo representate do cliente para evitar **gold plating**, que é quando os desenvolvedores geram features que não vão gerar valor para o usuário.

**Como escrever boas histórias**

Antes de começar a escrever histórias, recomenda-se listar os principais usuários que vão interagir com o sistema

Devemos seguir algumas características (INVEST):

1. Independentes: Posso implementar as histórias em qualquer ordem
2. Negociação: As histórias devem estar abertas para negociação
3. Valor: As histórias devem agregar valor ao negócio dos clientes e podem ser priorizadas pelo seu valor.
4. Estimável: Deve ser viável estimar o tamanho de uma história em tempo.
5. Sucinta: Podemos até admitir grandes histórias (**épicos**), mas as histórias do topo do backlog devem ser implementadas em menos de uma semana
6. Testáveis: As histórias devem possuir critérios de aceitação que possibilitam o teste


**Histórias de requisitos não funcionais**

Os requisitos não funcionais devem ser usados como um critério de aceitação da história

**Histórias de estudo**

Não se deve criar histórias exclusivamente para aquisição de conhecimento, pois histórias devem sempre ser escritas e priorizadas pelos clientes. Tarefas para aquisição de conhecimento são chamadas de spikes.

__________________________________________

## 2. Casos de Uso

Documentos do desenvolvimento tipo Watterfall. São mais complexos que as histórias e são escritos por desenvolvedores (engenheiro de requisitos) na fase de análise de requisitos

Os casos de uso são escritos na perpectiva de um **ator**, que é um usuário.

Um caso de uso enumera passos que um **ator** realiza no sistema para um determinado objetivo. Esses passos são divididos em **fluxo normal** e **Extensões**.

O **Fluxo normal** enumera os passos de um cenário ideal de uso

A **Extensão** representam alternativas de execução

**Exemplo:**
```
Transferir Valores entre Contas
Ator: Cliente do Banco
Fluxo normal:

1 -
2 - Cliente informa agência e conta de destino da transferência
3 - Ciente informa valor que deseja transferir
4 - Cliente informa a data em que pretende realizar a operação
5 - Sistema efetua transferência
6 - Sistema pergunta se o cliente deseja realizar uma nova transferência

Extensões:

2a - Se conta e agência incorretas, solicitar nova conta e agência
3a - Se valor acima do saldo atual, solicitar novo valor
4a - Data informada deve ser a data atual ou no máximo um ano a frente
5a - Se data informada é a data atual, transferir imediatamente
5b - Se data informada é uma data futura, agendar transferência
```

_______________

## 3. Produto Mínimo Viável (MVP)

Conceito muito popular entre Startups. 

MPV é o produto mínimo viável e tem como objetivo testar a ideia core de um software o mais rápido possivel para saber se podemos avançar com o desenvolvimento ou não.

O livro Lean Startup propõe um método para construção e validação de MVPs que consiste no ciclo: construir, medir e aprender. Isso é o **aprendizado validade**

<image src=https://engsoftmoderna.info/figs/cap3/lean.svg>

Esse ciclo pode resultar em 3 decisões:

1. Ainda são necessários mais testes com o MVP, melhorando alguns fatores, como os requisitos/interface com os usuários

2. O MVP foi bem sucedido e achamos um mercado para o sistema, então é hora de investir mais recursos.

3. O MVP falhou e temos que decidir entre:
   1. Pivotar: Abandonar a visão original e tentar um novo MVP
   2. Desistir


Para **medir** um MVP devemos tomar cuidado para não usar **métricas de vaidade**, que só fazem bem para o ego, como o pageviews de um site de ecommerce. Devemos usar **métricas acionáveis**, que representam melhor o sucesso do MVP, como a porcentagem de visitantes de fecham a compra em um site de ecommerce.

Para avaliar MVPs que incluem vendas de produtos ou serviços, costuma-se usar **métricas de funil**, que capturam o nível de interação dos usuários com um sistema. Um funil pode incluir as seguintes métricas:

1. Aquisição: número de clientes que visitaram o seu sistema.
2. Ativação: número de clientes que criaram uma conta no sistema.
3. Retenção: clientes que retornaram ao sistema, após criarem uma conta.
4. Receita: número de clientes que fizeram uma compra.
5. Recomendação: clientes que recomendaram o sistema para terceiros.

____________________________

## 4. Testes A/B

