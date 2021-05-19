# Arquitetura P2P

Serviços podem ser implementados em qualquer maquina. Todas as maquinas são iguais e podem atuar como clientes e servidores a qualquer momento.

# Redes P2P não estruturadas:

## Gnutella, 2001

Primeiro serviço p2p totalmente descentralizado

Não tem uma estrutura pré-definida

- Cada nó começa com alguns vizinhos
- Nós trocam informações sobre vizinhos
  - Cada um pode escolher novos vizinhos
  - Critérios podem variar

A busca e feita por consulta aos vizinhos. Seria inviável perguntar para todos os nós (flooding). Cada nó tenta responder ou repassa a requisição para o próximo vizinho (Random Walk).

Consulta termina ao atingir um certo limite de nós visitados (TTL)

**Problemas**:
- Pode sobrecarregar um nó
- Saída de um nó pode particionar a rede
- A busca pode não chegar ao recurso desejado
- Limitada a algoritmos de "fofoca" (gossip)

# Redes hierárquicas:

## Gnutella 0.6

Possui nós de maior capacidade, "super-peers" que tem preferencia para serem escolhidos como vizinhos.


# Redes p2p Estruturadas:

**DHT: Distributed Hash Table**

Nós se organizam segundo uma estrutura pré-definida

Nós são mapeados no espaço de endereçamento baseado no seu identificador hash. Cada nó ocupada um pedaço do espaço e se torna responsável por ele.

**Buscas** são mair organizadas. Os valores de hash podem ser usados para mapear os arquivos do sistema e facilitar a pesquisa.

## P2P Chord

Espaço de endereçamento circular baseado em SHA-1

Cada pedaço do anel de endereços vai ser responsável por um nó.

Quando um nó novo aparece, ele avisa ao responsável do endereço dele que ele chegou e passa a ser responsável por parte do endereço desse responsável.

**Busca**

Inicia no valor do SHA-1 e continua pesquisando lenearmente.

Cada nó tem uma "finger table" com vizinhos a diferentes distancias, entao podemos pesquisar em vizinhos mais distandes diretamente.

