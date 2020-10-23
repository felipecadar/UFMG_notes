# Modelos de Falhas

Conceito: Um sistema tolerante a falhas precisa saber exatamente qual é o comportamento esperado
- Como processos se comportam
- O que esperar dos canais de comunicação
- O que se pode dizer sobre o tempo no sistema
- Qual compromisso complexidade x desempenho esperado/possível
---------------------
**Tipos de falhas**
- Crash Failure: Na hora que falhar, o servidor para de funcionar, mas está funcionado corretamente até que falhe.
  - Fail-Stop: Falha e avisa que falhou
  - Fail-Noisy: Falha, mas durate um certo tempo o comportamento é duvidoso e eventualmente todo sabem que ele falhou
  - Fail-Silent: Falha, mas não é possível ter certeza
  - Fail-Safe: Pode falhar de forma arbitrária, mas sem causar danos
  - Fail-Arbitrary: Qualquer tipo de falha é possível, inclusive com ações maliciosas
- Omission Failure: O servidor não responde a comandos, não recebe nem envia mensagens.
  - Receive Omission
  - Send Omission
- Timing Failure: Reage da forma certa no tempo errado. Ou antes do esperado ou depois do esperado.
  - Normalmente é erro de desempenho
- Response Failure: O server responde incorretamente ou deriva do fluxo de execução esperado.
  - Value Failure
  - State Transition failure
- Arbitrary (byzantine) failure: Falhas aleatórias em tempos aleatórios.
---------------
**Falhas de paradas (Halting Failures)**: Mais comum
- Exemplos: SegFault, ZeroDiv
- Sistema Assíncrono:
  - Não há premissas sobre tempo de processamento
  - Não é possível determinar se o sistema parou, se deu falha de parada, com confiança
- Sistema Síncrono:
  - Tempos de processamento e comunicação são definidos
  - É possível detectar crash failure por estouro de tempo
- Na prática assusmimos sistemas parcialmente síncronos
  - Na maior parte do tempo ele é síncrono, mas pode ser que vc erre o tempo eventualmente.
  - Estatísticamente pode ter um casa que foi detectado falha mas o sistema só estava lento
------------------------
**Redundância**
- Conceito: Uma falha acontece em uma parte do sistema mas não em outra, de forma que podemos esconder a falha.
- Redundância de informação
  - Bits de paridade (hamming)
  - Réplicas 
- Redundância temporal
  - Executa ações novamente para comparar resultados
  - Ações são repetidas somente se necessário
- Redundância física/lógica
  - Hardware/processos extras adicionados para tolerar falha de alguns
  - funcionamento depende da cooperação entre as partes
----------------------------
**Redundância/Resiliência de processos**
- Em sistemas distribuídos temos a replicação de processos
- O desafio passa a ser coordenar os processos durante a execução
  - Manter noção de grupos
  - Fazer com que grupos concordem em suas respostas