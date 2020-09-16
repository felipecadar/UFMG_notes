# LDAP

Surgiu para resolver alguns problemas no DNS. Apesar de ser altamente eficiente, o DNS só conseguia mapear poucos campos pré-definidos e pouco mutáveis.

Precisamos de diversas outras informações como:
- Informações sobre usuários
- Configuração de máquinas e dispositivos
- etc...

**X.500 (1988)**: Proposta da CCIT para criar um diretório global baseado no DNS que pudesse ser extensível e mutável. A proposta era grande, complexa e difícil de implementar.

**LDAP (1993)** (Lightweight Directory Access Protocol): Solução de compromisso para dados organizaciomais:
- Mais rápido que um banco de dados genérico
- Mais flexível que um serviço como dns

Estritamente falando LDAP é apenas um protocolo, mas uma aplicação que monta a resolução de nomes ao redor do LDAP é normalmente identificada como serviço LDAP.

Possui entrutura cliente-servidor tradicional
- Servidores podem ser replicados para tolerância a falhas.
- Diretório pode ser distribuído entre vários servidores.


**Princípios gerais**:
- Entidades descritas como conjunto de pares (atributo, valor)
- Conjuntos de atributos descritos por schemas, pre-definidos.
- Atributos defines hierarquia (Directory Information Tree, DIT). Baseado em certos atribuitos que vão ser considerados de hierarquia superior a outros.
- Cada entidade tem:
  - um nome local (commonname, cn) que a identifica dentro do seu domínio menor 
  - um nome global( distinguised name, dn) que permite encontrar esse objeto dentro dessa estrutura hierárquica completa do LDAP
    - É a combinação dos atributos da árvore que levam até esse nó específico.

Normalmente usamos como os primeiros níveis da árvore, os nomes dos domínios do DNS. Aí usamos o DNS para achar o servidor de LDAP desejado.

Sobre os atributos:
- globais: podem existir vários atributos pois são globais, mas nem todos precisam sem preenchidos
- podem ser indexados
- podem ser definidos por objetos (schemas)
- podem ter múltiplos valores
- podem conter conteúdos binários, como fotos.
- tamanho limitado só pelo ambiente (sem limitação de espaço a priori).

**Operações básicas**:
- `bind` : Conexão e autenticação de clientes.
- `search`  : bsuca por entidades, leitura de dados
- `add`: criação de objetos
- `modify`: alterações
- `delete`: remoção

Note que é muito mais rico, em operações, do que o DNS.

**Busca baseada em atributos**:

A busca se inicia de um ponto base, desse ponto eu digo qual é o escopo da minha busca, ate onde eu vou procurar. Esse escopo pode ser:
- base: só a entidade base (usado para ler o objeto).
- one: só procura um nível abaixo da base.
- subtree: procura em toda a sub-árvore abaixo da base.

Dizemos o filtro: o padrão da busca

Pedimos uma lita de atributos que podem ser retornadas (opcional)

Exemplos de busca:
- (&(givenName=`Guedes`)(sn=`Dorgival`))
  - Busca por nós que tem os dois atributos simultâneos.

**Aplicação real**: É muito encontrado no serviço Microsoft Active Directory

**Mais informações**:
1. Wikipedia
2. Roadmap: RFC 4510