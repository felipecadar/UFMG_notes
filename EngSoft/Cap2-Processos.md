# Processos

Ágil = Iterativo

## Métodos Ágeis

Vamos estudar XP, Scrum Kanbam.

- Processo ajuda a não fazer grandes besteiras.
- Bom senso
- Experimentação.

# Extreme Programming - XP

Criador: Kent Beck 

Dividido entre:

- Valores
- Princípios
- Práticas

## Valores 

Para uma empresa de software progredir ela deve possuir alguns valores importantes para sustentar os programadores.

- Qualidade de Vida (40 hrs)
- Respeito
- Coragem
- Feedback
- Simplicidade
- Comunução 

## Principios

- Economias 
    - A empresa deve gerar dinheiro 
- Melhoras 
    - Sempre tem espaço para melhorar
- Falhas Acontecem
    - Precisamos entender e não descontar os erros no programador pois eles acontecem
- Baby steps
- Responsabilidade Pessoal

## Práticas 

- Práticas de Processos
- Praticas de Programação
    - Design Incremental
    - Programação pareada
    - Testes automatizados
    - etc...
- Práticas de Gerenciamento de Projetos
    - Ambiente de Trabalho
    - Contratos com escopo aberto
    - Métricas


#### Programação pareada
Tudo tem que ser feito em pares. Todo código possui o Driver e o Navegador.
Quando se faz pair programming, temos um sistema de rodízio de pares e funções. 

Vantagens: 
- Código de melhor qualidade e redução de Bugs.
- Disseminação de conhecimento. Mais de uma pessoa conhece o código que está sendo escrito.

Desvantagens:
- Muito custoso, economicamente

Não deu muito certo como modo principal de trabalho, mas ainda é usado e alguns casos, como novas pessoas na equipe ou para resolver grandes bugs.

Foi substituido por revisão de código (Todo código escrito tem que ser revisado por outra pessoa)


#### Ambiente de trabalho

Precisa ser compartilhado, onde todos trabalham no mesmo espaço e as tarefas estão dispostas em um quadro.


#### Contratos com escopo aberto

O escopo fechado não funciona. Os requisitos não são bem definidos no início e não se sabe extamente o tamanho do projeto.

Com o escopo aberto existem definições a cada iteração. O pagamento é por homem por hora e o contrato renovado a cada iteração.

Exige maturidade e acompanhamento do cliente e ninguém vai ser enganado.


# Scrum

Jeffrey e Ken

Muito marketing envolvido.

#### Scrum vs XP

Scrum não é só para projeto de software, logo não define práticas de programação.
Scrum define um "Processo" mais rígido que XP

#### Sprint

Sprint é uma iteração, normalmente 15 dias.

O que se faz em um sprint? Se implementa histórias dos usuários.

Termina com a revisão do sprint, onde o time mostra os resustados pro PO e Staleholders. Se tiver problemas a história volta pro backlog e é re-priorizada.

É discutido oq deu certo e oq deve ser melhorado... Feito para melhorar o processo.

#### Reuniões Diárias

sum-up do dia, compartilhamento de problemas e soluções.

#### Product Owner

PO conhece o sistema e fala pros devs os requisitos do sistema. Ele deve estar disponível e deve ter autoridade para definir os requisitos do sistema.

- Escreve as historias de usuario
- Explica as histórias para os devs
- Define "Testes de aceitação"
- Prioriza histórias (ordem de implementação)
- Mantem um backlog do produto
    - Lista de historias com prioridades dinâmicas.

No sprint planing são definidas as histórias que vão entrar no próximo sprint, o PO proproe as histórias e os devs decidem se têm velocidade para implementá-las.

PO não é chefe do dev


#### Time Scrum 

>"Tamanho duas pizzas" -Jeff da Amazon

- 1 PO
- 3 a 9 Devs
- 1 Scrum Master

#### Scrum Master

Especialista de Scrum do time para garantir que o time está seguindo o processo corretamente.

Ajuda a remover impedimentos não-técnicos. Pode pertencer a mais de um time.

#### Time-box

Tudo tem um prazo muito bem definido. Cada evento tem um time-box com a duração máxima definida.

#### Conclusão de Histórias (Done Criteria)

É importante considerar qualidade externa e interna.
- Qualidade externa:
    - Testes de aceitação (Funcionais)
    - Testes não-funcionais (Desempenho/Usabilidade)

- Qualidade Interna
    - Testes de unidade
    - Revisão de código

#### Scrum Board

Backlog|Todo|Doing|Testing|Done
-------|----|-----|-------|-----
bla|bla2 |bla3 | bla4 | bla5


#### Burndown chart

Gráfico com a quantidade de horas restante para o fim do sprint

#### Story points

Unidade para compar o tamnho das histórias. A escala de ser não linear. É comum usar fibonatti

# Kanban

Origem na década de 50 no japão -> Taylorismo 

Kanban = "cartão visual"

#### Kanban vs Scrum

- Kanban é mais simples
- Não tem sprints
- Não precisa de papeis e eventos


#### Quadro Kanban 

|Backlog|Especificação|Implementação|Revisão
|-------|-------------|-------------|-------
|  | Pendente/Concluido|Pendente/Concluido|Pendente/Concluido

Especificação significa quebrar um cartão em várias tarefas

Deve se especificar o número máximo de taredas em cada passo, o WIP (work in progress).

Como devemos definir o limite WIP ? De forma empírica, baseada em experiência ou usando a Lei de Little

~~~
> Lei de Little
WIP = TP * LT
TP = Througput (Vazao) é o número de tarefas concluidas por dia no passo
LT = Lead Time é o tempo médio que a tarefa demora para ser concluída,incluindo o tempo na 2a subcoluna
~~~

# Comentários finais

Xp é importante pelas práticas de programação propostas

Scrum gera uma "fadiga" a médio prazo

Kanban é mais adequado para times mais maduros, talvez seja bom começar com Scrum e mudar para Kanban quando o time sentir que não precisa de tantas regras para o desenvolvimento.

