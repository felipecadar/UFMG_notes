# Replicação

Problema: Manter várias replicas de forma útil e sem confusão.

Mapa mental: [https://gitmind.com/app/doc/71f837059](https://gitmind.com/app/doc/71f837059)

**Motivação**:
1. Disponibilidade:
   1. Resistencia a falhas
   2. Proteção contra dados corrompidos (temos várias cópias)
2. Desempenho
   1. Replicação Local: Podemos ter muitas cópias de um serviço em um datacenter
      1. Atender vários processos
      2. Aumentar banda de acesso
   2. Replicação geográfica: 
      1. Redução de latência
         1. Cópias mais próximas do cliente
      2. Resistência a particionamento (não explicou)


**Implementação**: Fatores para levar em conta parar implementar um sistema distribuído
1. **Posicionamento**
   1. Onde estão os **servidores**
      1. Limitada pela disponibilidade de datacenters
      2. Depende da posição dos clientes
      3. Problema menos crítico pela boa conectividade (internet boa)
   2. Onde estão os **dados** (conteúdo)
      1. Réplicas **permante**
         1. Eu defino na criação do sistema. Estão juntas aos servidores principais. Normalmente são poucas e bem colocadas para atender as demandas do sistema.
      2. Réplicas **definifas pelos servidores**
         1. Adiciono uma cópia em caso de tráfego elevado, ou uma demanda elevada e eu sei identificar onde ela está.
      3. Réplicas **definifas pelos clientes**
         1.  A medida que os clientes fazem requisições, eles mesmos podem optar por quardar cópias do que estão fazendo. Cache
2. **Formato de atualização**: Como eu atualizo os dados uma vez que as coisas mudaram. O que eu tenho que enviar para as réplicas
   1. Notificação de mudança:
      1. Quando algo muda, a réplica não é atualizada. Ela apenas recebe uma notificação "você não está mais atual".
      2. Vantagem: Mensagem curta
      3. Desvantagem: Tempo de acesso maior pois tenho que buscar o dado de novo quando quiser
      4. Muito comum em protocolo de Cache
   2. Cópia dos dados
      1. Quando algo muda, eu atualizo o conteúdo e mando uma cópia do conteúdo para a replica
      2. Simples para quem recebe a cópia
   3. Comando a ser executado
      1. Faz ela executar o comando de mudaça.
      2. Simplifica a troca de mensagems.
      3. Requer que todas as réplicas tenha capacidade de processamento.
3. **Controle da atualização**
   1. Push
      1. Feitas e normalmente oriundas dos servidores centrais.
      2. Usado quando é importante garantir que as cópias são fieis\
      3. Assim que a mudança ocorre ela já é comunicada
      4. É útil quando a taxa de atualizações é consideravel e a taxa de acesso também.
      5. Aumenta a demanda do servidor
   2. Pull
      1. Os clientes fazem a demanda
      2. A responsabilidade é da replica
      3. Reduz a carga do servidor mas aumenta o tempo de resposta por precisar verificar se as informações estão atualizadas
   3. Hibrido, Lease:
      1. O servidor envia um dado com um tempo de garantia (push)
      2. Depois que o tempo acaba, o cliente precisa fazer a consulta (pull)
4. Padrão de comunicação de hardware: Como é a comunicação entre o servidor e o cliente
   1. Unicast
   2. Multicast *em hardware*: 
      1. só faz sentido quando estou em uma rede local em que se uma mudaça ocorre eu fazer um broadcast que chega em todas as réplicas com uma mensagem só. Ganho em tempo de comunicação

**Consistência**: o grande desafio em um sistema com replicação. Já que eu tenho muitas cópidas e os dados mudam ao longo do tempo, como garantir que o cliente vai ser uma visão consistente dos dados.
1. [Modelos de consistência](aula-11b.md)
2. Protocolos para implementar esse modelos