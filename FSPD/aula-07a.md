# Chamadas de Procedimentos Remotos (RPC)

Ideia: Uso de procedimentos para executar tarefas remotas.

O ambiente (**middleware**) controla a comunicação, a execução da tarefa e a devolução da resposta.

Para o desenvolverdor, é uma chamada de procedimento como qualquer outra, mas na verdasde está em outra máquina.

Arquivos necessários:
1. Código que faz a chamada (cliente)
2. Implementação do procedimento (servidor)
   1. Não precisa ser a implementação do servidor inteiro, só o procedimento específico.
3. Arquivos de descrição de interface.

Dados os 3 arquivos, usamos um **Compilador Stub** para gerar o código necessário do clientes e do servido e usamos um **Protocolo RPC** para fazer a comunicação.

Suponha que temos **Client Machine** com o código do **Client process** e o **Client Stub**. Temos também a **Server Machine**, com o código **do procedimento *doit(a, b)*** e o **Server Stub**:

Quando o clientes quer executar `r = doit(a, b)`
1. O Cliente chama a função `r = doit(a, b)`
2. O código do stub vai montar uma mensagens descrevendo que queremos executar remotamente o procedimento `doit` com parametros `a` e `b`
3. O stub envia a mensagem ao servidor
4. O servidor recebe a mensagem
5. O servidor executa a chamada do procedimento `doit`
6. O server stub codifica o valor de retorno em uma mensagem
7. O server stub envia a mensagem de volta pro cliente
8. O stub do cliente recebe a mensagem e extrair o valor de retorno entregando para o cliente o valor de retorno para ser usado dentro do código do cliente.

# Representação de dados

Precisamos de uma forma de representar os dados que seja independendo da máquida e da linguagem do cliente e do servidor (potencialmente diferentes).

Usamos diferentes pacotes de serialização.

# Tecnologias relacionadas

- Arquitetuas orientadas a serviçõs
  - Web Services: Conjunto de servidores que usavam RPC e funcionavam sobre o protocole da Web
  - SOAP (simple object access protocol): conjunto de ferramentas para implementação de serviços sobre o protocolo HTTP
  - REST (Representational State Transfer): Também é feito sobre HTTP e as vezes é chamado de RPC