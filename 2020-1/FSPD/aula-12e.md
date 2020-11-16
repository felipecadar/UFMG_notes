# 2PC (two-phase commit)

É o clássico problema dos dois generais...

## Comit de uma fase

Se um coordenador manda os processos realizarem uma ação, não pra da informar um coordenador de um processo falhar.

Viola a regra de consenso na decisão. Ou todos fazem ou nenhum faz.

## Comit de duas fases

- Primeiro o coordenador pergunta para todos os processos se eles concordam com a operação. Se todos concordam, a transação vai ser feita.
- Na segunda fase o coordenador envia o resultado da votação.

**Premissas**
- Sistema parcialmente síncronas.
- Mensagems podem ser perdidas( ou não).
- Nós falham silenciosamente, mas podem ser reiniciados.
  - Depois de algum tempo ele volta
  - Crash-recovery
  - Possui aramzenamento confiável sobre o que estava fazendo antes de falhar

**Casos de Falhas**
- Se o coordenador não recebe respostas de todos
  - Da timeout e aborta
- Se um participante não recebe consulta inicial
  - Da timeout e aborta
- Participando esperando depois de votar e não receber a segunda mensagem
  - Contacta outros participantes para decidir
  - Se os outros participantem não receberam a primeira mensagem, aborta.
  - Se os outros participantem estambém estão esperando a segunda mensagem, espera o coordenador voltar a ficar online, pois o sistema é Crash-recovery.


**3PC**: Remove o bloqueio do 2PC usando uma fase de pré-commit

