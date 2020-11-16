# Arquitetura 

Na frase de Ralph Johnson, arquitetura de software inclui as decisões de projeto mais importantes em um sistema. Essas decisões são tão importantes que, uma vez tomadas, dificilmente poderão ser revertidas no futuro.

**Padrões arquiteturais** propõem uma organização de mais alto nível para sistemas de software, incluindo seus principais módulos e as relações entre eles.
1. Arquitetura em Camadas
2. Arquitetura Model-View-Controller ou MVC
3. Microsserviços
4. Arquitetura Orientada a Mensagens
5. Arquitetura Publish/Subscribe

**Estilos arquiteturais**: **padrões** focam em soluções para problemas específicos de arquitetura; enquanto **estilos** arquiteturais propõem que os módulos de um sistema devem ser organizados de uma determinado modo, o que não necessariamente ocorre visando resolver um problema específico.

# Arquitetura em Camadas

As camadas são dispostas de forma hierárquica, como em um bolo. Assim, uma camada somente pode usar serviços — isto é, chamar métodos, instanciar objetos, estender classes, declarar parâmetros, lançar exceções, etc — da camada imediatamente inferior.

**Vantagens**:
1. Uma arquitetura em camadas particiona a complexidade envolvida no desenvolvimento de um sistema em componentes menores
2. Ela disciplina as dependências entre essas camadas
3. Fica mais fácil também o reúso de uma camada por mais de uma camada superior

## Arquitetura em Três Camadas

Usada para migras os sistemas mainframes.

As três camadas dessa arquitetura são as seguintes:
1. **Camada de apresentação**: é responsável por toda interação com o usuário.
2. **Camada de aplicação**: implementa as regras de negócio do sistema. Implementa a lógica do programa
3. **Banco de Dados**: armazena os dados manipulados pelo sistema

Normalmente, uma arquitetura em três camadas é uma arquitetura distribuída.

É possível ter sistemas em duas camadas. Nesses casos, as camadas de interface e de aplicação são unidas em uma única camada, que executa no cliente. **Desvantagem**: todo o processamento ocorre nos clientes, que, portanto, devem ter um maior poder de computação.


# Arquitetura MVC

Especificamente, MVC define que as classes de um sistema devem ser organizadas em três grupos:
1. **Visão**: classes responsáveis pela apresentação da interface gráfica.
2. **Controladoras**: classes que tratam e interpretam eventos gerados por dispositivos de entrada
3. **Modelo**: classes que armazenam os dados manipulados pela aplicação e que têm a ver com o domínio do sistema em construção. Objetos de domínio não incluem código visual, mas apenas lógica de negócios

**Vantagens**:
1. MVC favorece a especialização do trabalho de desenvolvimento.
2. MVC permite que classes de Modelo sejam usadas por diferentes Visões.
3. MVC favorece testabilidade. É mais fácil testar objetos não-visuais, isto é, não relacionados com a implementação de interfaces gráficas. Por isso, ao separar objetos de apresentação de objetos de Modelo, fica mais fácil testar esses últimos.

**Exemplo**: Single Page Applications

# Microsserviços

A ideia é simples: certos grupos de módulos são executados em processos independentes, sem compartilhamento de memória.

**Vantagens:**
1. **Independência**: Alterações em um serviço tem uma chance menor de afetar os outros.
2. **Escalabilidade**: Permitem replicar apenas os componentes diretamente relacionados com problemas de performance.
3. Como os microsserviços são autônomos e independentes eles podem ser implementados em tecnologias diferentes, incluindo linguagens de programação, frameworks e bancos de dados.
4. Arquiteturas baseadas em microsserviços podemos ter **falhas parciais**.

**A Lei de Conway** afirma o seguinte: empresas tendem a adotar arquiteturas de software que são cópias de suas estruturas organizacionais. Em outras palavras, a arquitetura dos sistemas de uma empresa tende a espelhar seu organograma.

## Gerenciamento de Dados

Pelo menos na sua forma pura, microsserviços devem ser autônomos também do ponto de vista de dados. Isto é, eles devem gerenciar os dados de que precisam para prover o seu serviço. 

## Quando não usar microsserviços?

Desvantagens:
1. **Complexidade**
2. **Latência**: Pela comunicação entre serviçoes de um sistema distribuído.
3. **Transações Distribuídas**: Em arquiteturas baseadas em microsserviços, protocolos de transações distribuídas, como two-phase commit, podem ser necessários para garantir uma semântica de transações em operações que escrevem em mais de um banco de dados.

# Arquiteturas Orientadas a Mensagens

A comunicação entre clientes e servidores é mediada por um terceiro serviço que têm a única função de prover uma fila de mensagens

**Desacoplamento**:
1. no espaço: clientes não precisam conhecer os servidores e vice-versa.
2.  no tempo: clientes e servidores não precisam estar simultaneamente disponíveis para se comunicarem.

**Vantagem:** Filas de mensagens permitem também escalar mais facilmente um sistema distribuído. Para isso, basta configurar múltiplos servidores consumindo mensagens da mesma fila.

**Exemplo: Empresa de Telecomunicações**

solução **batch**: Nesse tipo de solução, o sistema de vendas geraria ao final de cada dia um arquivo com todos os pacotes vendidos. Esse arquivo seria processado durante a noite pelo sistema de engenharia.

# Arquiteturas Publish/Subscribe

Em arquiteturas publish/subscribe, as mensagens são chamadas de **eventos**. Os componentes da arquitetura são chamados de **publicadores** (publishers) e **assinantes** (subscribers) de eventos.

Publicadores produzem eventos e os publicam no serviço de publish/subscribe, que normalmente executa em uma máquina separada. Assinantes devem previamente assinar eventos de seu interesse. Quando um evento é publicado, os seus assinantes são notificados.

Assim como ocorre quando se usa filas de mensagens, arquiteturas publish/subscribe também oferecem desacoplamento no espaço e no tempo.

**Diferenças**:
1. Em publish/subscribe, um evento gera notificações em todos os seus assinantes. Por outro lado, em filas de mensagens, as mensagens são sempre consumidas — isto é, retiradas da fila — por um único servidor. Portanto, em publish/subscribe temos um estilo de comunicação de 1 para n, também conhecido como **comunicação em grupo**. Já em filas de mensagens, a comunicação é 1 para 1, também chamada de **comunicação ponto-a-ponto**.

2. Em publish/subscribe, os assinantes são notificados assincronamente. Primeiro, eles assinam certos eventos e, então, continuam seu processamento. Quando o evento de interesse ocorre, eles são notificados por meio da execução de um determinado método. Por outro lado, quando se usa uma fila de mensagens, os servidores — isto é, os consumidores das mensagens — têm que puxar (pull) as mensagens da fila.

**Exemplo: Companhia Aérea**

Vamos agora usar os sistemas de uma companhia aérea para ilustrar uma arquitetura publish/subscribe. Suponha que essa companhia tem um sistema de vendas, que é usado pelos clientes para comprar passagens aéreas. Após efetuar uma venda, esse sistema pode gerar um evento, com todos os dados da venda (data, horário, número do vôo, dados do passageiro, etc). O evento venda será então assinado por três sistemas da companhia aérea: (1) sistema de milhagens, pois as milhas relativas à passagem devem ser creditadas na conta do passageiro; (2) sistema de marketing, que pode usar os dados da venda para fazer ofertas para o cliente, como aluguel de carros, promoção para classe executiva, etc; (3) Sistema de contabilidade, pois a venda que foi realizada precisa ser incluída na contabilidade da empresa.

# Outros Padrões Arquiteturais

## Pipes e Filtros
**filtros** têm como função processar os dados recebidos na entrada e gerar uma nova saída.  Os filtros são conectados por meio de **pipes**, que agem como buffers

`ls | grep csv | sort`

## Cliente/Servidor
**Clientes** e **servidores** são os dois únicos módulos desse tipo de arquitetura e eles se comunicam por meio de uma rede.

Arquiteturas **peer-to-peer** são arquiteturas distribuídas nas quais os módulos da aplicação podem desempenhar tanto o papel de cliente, como o papel de servidor.

# Anti-padrões Arquiteturais

**anti-padrão**: uma organização de sistemas que não é recomendada.

## big ball of mud

Descreve sistemas nos quais qualquer módulo comunica-se com praticamente qualquer outro módulo

**Problemas**:
1. O tempo de aprendizado aumenta com o tempo
2. Frequentemente, a correção de bugs introduz novos bugs
3. O tempo de implementação de novas funcionalidades, mesmo que simples, também aumenta com o tempo.


