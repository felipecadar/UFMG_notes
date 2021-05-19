# Eleição de líder

Tenho um grupo de processos conhecidos e consigo me comunicar com todos. Dentro desse conjunto preciso escolher um lider para assumir um papel especial.

## Bully

O processo com maior identificador é sempre o lider.

Dado um processo k, P**k**, que achar que o líder falhou, manda a mensagem ELEIÇÃO para os nós com identificadores acima de k.

1. Se ninguém responde, P**k** vence a eleição e passa a ser o líder
2. Se alguém acima de k respode,
   1. P**k** não é o lider
   2. O nó que respondeu repete o processo com aqueles acima dele.

## Algoritmo com anel

Os nós se organizam em um anel.

1. O processo que acha que o líder falhou manda mensagem ELEIÇÃO para o nó depois dele, com seu identificador.
   1. Se o nó seguinte não responde, contacta o próximo
2. Cada nó inclui seu identificador ao final da mensagem, construindo uma lista
3. Essa mensagem roda no anel até que o nó que percebeu a falha a receba de volta, então ele:
   1. Determina qual é o maior identificador da lista
   2. envia uma mensagem COORDENADOR com essa informação
   3. quando essa mensagem retornar, todos já sabem quem é o lider e ele para de propagar a mensagem.