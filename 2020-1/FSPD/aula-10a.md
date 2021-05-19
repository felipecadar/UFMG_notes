# Sincronização de Relógios

Tempo pode:
1. Deterinar ordem sem comunicação.
2. Definir limites de duração para programas
3. Resolver disputas (chegou primeiro)

# Tempo com relógio global

Perfeitamente sincronizados. Todos iniciam com o mesmo valor ou mesmo tempo e nunca divergem.

Todo evento tem um *timestamp* com valor global.

Só é viável quando estamos na mesma máquina.


# Tempo com relógio local

Em ambientes distribuídos.

Podem divergir.

Os timestamps de máquinas diferentes não são comparáveis.

## Mecanismos de sincronização

Trocarem informações periodicamente para ajudar os relógios.

### Network Time Protocol (NTP)

Assume computadores de referência em níveis (strata)
- Nível 0: relógio atômico, GPS, etc...
- ...
- Nível i+1: computador conexão para um servidor do nível **i**

Considera atrasos pela medida de 4 tempos

Considere A no nível i+1 e B no nível i

1. A mede **T1** e envia uma mensagem para B
2. B mede **T2** quando a mensagem de A chegar
3. B mede **T3** e envia uma mensagem para A
4. A mede **T4** quando a mensagem de B chegar

Com esses 4 tempos o NTP consegue fazer ajustes com erro na casa de 50 ms.

### Algoritmo de Berkeley

Não tem "relógio melhor"

1. Um servido mede seu próprio tempo e reporta para todas as máquinas da rede
2. Clientes recebem e reportan a diferença de seus relógios para o servidor
3. O servidor faz a médida das diferenças e reporta um tempo de ajuste para cada máquina, incluindo a sí mesmo.