# Detalhes de Implementação e Aplicação de RPC

RPC: Abstração de programação para implementação de sistemas distribuídos

RPC **não** é uma chamada local.

**Arquitetura de camadas: Qual  o protocolo abaixo da RPC?**
- Protocolos padrão da internet:
  - UDP: Rápido e sem garantias.
  - TCP: Mais lento porem confiável.

- Web services atuam sobre HTTP e contumam ter mais uma cama de criptografia TLS/SSL

**Localização do servidor**

Para localizar um procedimento na internet usamos:
- Endereço da máquina (IP)
- Número do porto (número atribuído pelo servido)

Mas essas solução é muito limitante, principal,ente quanto tempos muitos clientes e muitos servidores.

Muitas soluções criam algum tipo de diretório:
1. Port Mapper
2. Service directort/registry

No caso do **port mapper**: Conhecemos o IP do servidor e dentro dele temos um "repositório". O cliente pergunta ao repositório do servidor qual e o número de porto do procedimento desejado, o servidor responde e depois o cliente chama o procedimento em sí.

No caso do **service directort/registry**: Aqui temos um servidor mais geral que possui apenas um repositório global com o endereço dos servidores que possuem algum procedimento. Então o cliente só sabe esse servido geral a princípio. O cliente pergunta para o servidor geral onde está o servido que possui o procedimento, aí então o cliente pode consultar esse servido específico do mesmo jeito que o **por mapper**.

**Implementação do servidor**

A estrutura do servidor é contruída pelo middleware, então o programador só precisa fornecer o código do procedimento. Temos 3 formas de fazer isso:
1. **Multi-processos** (forked): Cria um processo sempre que o cliente pede.
2. **Multi-threaded**: Cria uma thread sempre que o cliente pede.
3. **Thread pool**: já possui uma pool de threads criadas e só utiliza elas quando o cliente pede.

**Comunicação em Pipeline**: Quando as mensagens são grandes demais e podem ser divididas.


**Operação assíncrona**:  O cliente recebe uma confirmação de que o processo foi iniciado. Então o cliente pode fazer outras coisas sem precisar esperar pelo servidor.

**Multicast**: Quando enviamos requisições a vários servidores ao mesmo tempo com particionamento ou replicação dos dados.

**Tolerância a falhas**

Os middlewares possuem duas semânticas sobre a quantidade de vezes que um procesimento vai ser chamado:
1. at most once: No máximo uma vez
2. at leat once: Pelo menos uma vez

