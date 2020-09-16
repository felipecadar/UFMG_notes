# Resolução de nomes

O que é nome: qualquer padrão associado a uma entidade (servidor, programa, etc...)

Ele tem dois tipos:
1. Endereços: Nomes que oferecem localização
   - Tradicionalmente podem mudar ao longo do tempo
2. Identificadores: Nomes que permitem individualização.
   - Valem por um longo período de tempo


Dado um nome, eu quero recuperar informações associadas a ele.

## Mapeamento nome-endereço

Recuperação do endereço de um ponto de acesso ligado a uma entidade com um certo nome

Ex: Qual é o endereço do servidor de correio do DCC/UFMG?

Classes de sistemas de nomes:
1. Planos (flat): Sequencias de bits não estruturada
   1. Resolução envolve uma busca exaustiva ou tabela de índices.
      1. Arquivo Local
      2. Consulta direta na rede (broadacast)
         1. ARP (Address Relosution Protocol): Pergunta na rede toda.
      3. Serviço centralizado (RPC registry)
         1. Existe uma máquina bem conhecida que sabe de todos os outros serviços
      4. Rede P2p ([Chord](aula-06e.md))
         1. Temos uma DHT (tabela de hash distribuida) e sempre que alguem entra na rede, eles se reorganizam. Cada nó conhece alguns vizinhos (finger table)
2. Estruturados
   1. Cada parte do nome tem um significado próprio. 
   2. A estrutura permite divisão da tarefa em vários servidores
      1. Servidores mantêm referências entre si
   3. Exemplo [DNS](aula-06b.md)
3. Baseados em atributos
   1. Cada endidate tem diversos pares (atributo, valor)
   2. Atributos podem ter estrutura (hoerarquia) associada para permitir divisão entre servidores
   3. Buscas podem incluir combinações de atributos.
      1. Exigem busca exaustiva ou tabelas de índices
   4. Exemplo: [LDAP](aula-09b.md)

