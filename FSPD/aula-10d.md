# Exclusão mútua em sistemas distribuídos

## Solução centralizada

Um processo é o controlador.

Nós que desejam exclusão mútua enviam mensagem para ele.

O controlador decide quem atender. Mantem registro de quem pediu mas não conseguiu ainda.

Se o controlador falhar, tudo falha.



## Solução descentralizada

Ter N controladores.

Para ter acesso, um nó precisa receber autorização de pelo menos N/2 controladores (maioria).

Se um controlador falhar, o sistema continua funcionando.

Se tivermos muitos clientes pedindo exclusão mútua, pode ser que cada um deles consiga algumas confirmações, mas nenhum consiga maioria. Isso pode causar starvation.

## Solução distribuída

Meus processos tem um relógio lógico e utilizam **total-order multicast**. 

1. Quem deseja acesso ao mutex envia pedido aos demais.
2. Quando um nó recebe um pedido ele verifica:
   1. Se ele mesmo não precisar o mutex, envia OK para quem pediu. Se ele receber 10 pedidos, ele envia 10 OKs.
   2. Se ele já esta acessando, ele não responde.
   3. Se ele não está acessando, mas já enviou uma mensagem de pedido, ele compara o timestamp do pedido recebido com seu próprio pedido.
      1. Se meu timestamp é menor, não responde.
      2. Se o timestamp recebido é menor, envia OK.
3. Um nó só acessa o mutex se recebe o OK de **TODOS**
4. Quando um nó termina seu acesso, ele envia OK para todos os que pediram e ele ainda não tinha respondido.

## Token-ring

Os processos formam um círculo.

1. Uma mensagem especial, o token, circula pela rede
2. Se um nó não quer mutex, passa o token para o próximo
3. Se um nó quer mutex, ele retém o token quando o recebe
   1. Ao terminar, passo o token para o próximo

| Algotitmo       | Mensagens        | Atraso (em msgs) | Pros                    | Contras                                      |
| --------------- | ---------------- | ---------------- | ----------------------- | -------------------------------------------- |
| Centralizado    | 3                | 2                | simples, pouco overhead | pnto único de falha e de sobrecarga          |
| Descentralizado | 2.m.k + m, K=1,2 | 2.m.k            | resiste a falhas        | pode ser starvation                          |
| Destribuído     | 3(N-1)           | 2(N-1)           | overhead distribuído    | muitas mensagens                             |
| token-ring      | 1, 2, ..., N     | 0, ..., N-1      | simples                 | recriar do token, quando perdido, é complexo |