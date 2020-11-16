# Protocolos de consistência

Tipos de protocolos que podem ser usados para implementar modelos de consistência.

## Escrita remota (remote-write)

**Para escrita**:
1. O cliente escolhe um servidor para escrever o item X
2. Esse servidor recebe o pedido e encaminha a escrita para o servidor responsável pelo item X (pré-definido)
3. O servidor responsável recebe a ordem e manda todos ous outros servidores backups atualizarem.
4. Todos os servidores de backup confirman a atualização
5. O Cliente recebe a confirmação que a escrita acabou

**Para leitura**: (Bem simples)
1. O cliente requisita leitura 
2. O servidor responde com o item atualizado


### Protocolos baseados em escrita remota (remote-write)
Também conhecidos como protocolos primário/backup
- Oferecem consistência sequencial
- Atualização pode demorar até todas as réplicas responderem
- Pode haver diferentes servidores para diferentes dados

**Limitação**: Centralização que ocorre pela existência do primário

## Escrita Local (local-write)

**Para escrita**:
1. O cliente escolhe um servidor para escrever o item X
2. O servidor recebe o pedido, o primário para o item X e pede para que mova o item X para sí.
3. Agora esse servidor se torna o novo primário para o item X.
4. Esse novo primário faz a escrita e confirmar para o cliente que a escrita foi feita
5. Por ultimo ele manda os outros servidores de backup se atualizarem e espera pela confirmação.

**Para leitura**: (Bem simples)
1. O cliente requisita leitura 
2. O servidor responde com o item atualizado

### Protocolos baseados em Escrita Local (local-write)
- Variação dos protocolos primário/backup
- Modo não bloqueante aumenta o desempenho se ha escritas sucessivas
- Usado em situações de operação desconectada
  - Computador se torna primário para o que pretende atualizar
  - Enquanto estiver desconectado pode mudar os dados
  - Demais computadores podem ler réplicas
  - Ao se conectar de novo, atualiza réplicas


## Replicação Ativa (active replication)

Cada réplica tem um processo que faz atualizações
- Atualizações são propagadas para todos como comandos
- Implementação mais simples: total ordered multicast
- Opção: usar coordenador/sequenciador central
  - Toda escrita é enviada para o sequenciador, que lhe dá um ID geral
  - Escritas são então enviadas para todos os nós
  - ID geral determina ordem de escrita e identifica comandos perdidos


## Protocos baseados em quórum (wuorum-based)
- Todo conteúdo é mantido em N réplicas
- Escritas são enviadas para NW réplicas, leituras para NR
  - NW > N/2 (evita conflitos de escrita)
  - NW + NR > N (evita leitura de dados antigos)

Desafio: Como n tem um primário, todas escritas tem que ser feitas por um acordo entre os nós.
Quem escreve precisa de conseguir exclusão mútua, verificar qual foi o último número de sequencia, criar um número de sequencia seguinte, verificar que todos os participantes do grupo de escrita foram atualizados com o novo valor de sequencia e então liberar o conjunto de escrita.


# Exemplo Real

Facebook e seu sistema regional de caches raiz e folha. Ele s garante consistência eventual.