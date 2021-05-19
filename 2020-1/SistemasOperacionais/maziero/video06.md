# Gestão de tarefas - Escalonamento de tarefas

**Tipos de tarefas** em relação ao comportamento temporal:
- Tempo real: exigem tempos de resposta precisos.
- Interativas: respondem rapidamente a eventos externos.
- Em lote: não tem requisitos explícitos.

**Tipos de tarefas** em relação ao uso de CPU:
- *CPU-bound*: usam intensivamente a CPU.
- *IO-bound*: realizam mais entrada/saída.

**Escalonamento de CPU** define a ordem de execução das tarefas prontas (*ready*). Responsabilidade do **escalonador** de CPU que é acionado pelo **despachante** durante as trocas de contexto.


**Critérios de escalonamento** são usados para comparar métodos de escalonamento.
1. Tempo de vida ($t_t$ turnaround time): tempo entre criação de uma tarefa e seu encerramento
2. Tempo de espera ($t_w$): tempo perdido em estado de *ready*.
3. Tempo de resposta ($t_r$): tempo entre a chegada de um evento no sistema e a tarefa que é responsável por aquele evento sair do estado suspenso, acordar, ir para a fila, ganhar a CPU e começar a tratar esse evento. Importante para tarefas de tempo real e interativas.
4. Justiça: distribuição adequada do processador entre as tarefas prontas.

**Modos de escalonamento**:
1. Cooperativo: A tarefa só perde o processador ao terminar, solicitar uma entrada/saída ou liberar explicitamente a CPU(*syscall* `sched_yield`). Esse sistema só funciona se as tarefas cooperarem entre si.
2. Preemptivo: A cada interrupção, exceção ou chamada de sistema, o escalonador reavalia a fila de prontas e pode "preemptar" a tarefa em execução.


# Primeiros Escalonadores

## Escalonamento FCFS: First Come, First Served

Tambem conhecido como FIFO. Quem chegar primeiro, executa primeiro.

## Escalonamento RR: Round-Robin

Usa preempção por tempo. A ordem da fila continua FIFO.

Permite que as tarefas chegem mais cedo a CPU

## Escalonamento SJF:Shortest Jot First

Sempre escolhe a tarefa com menor duração total.

Pode fazer com que as tarefas muito grandes nunca sejam executadas.

Problema: Como calcular a duração de uma tarefa.

Pode ser usado com conjunto com Round-Robin se guardarmos a quantidade de quantum que cada tarefa usa, podemos prever quais tarefas vão usar menos quantum e dar prioridade a elas.

## Escalonamento SRTF: Shortest Remainning Time First

Dar prioridade para as tarefas que possuem menor tempo restante. É preemptiva.

Precisa analisar a fila sempre que uma tarefa entra na fila.

## Escalonamento PRIOc: Prioridade Cooperativo

Decide por uma prioridade predefinida. Só analisa quando tarefas terminam por ser cooperativo.

## Escalonamento PRIOp: Prioridade Preemptivo

Decide por uma prioridade predefinida. Analisa a fila sempre que uma tarefa entra na fila e é preemptivo.

# Escalonamento com Prioridades Dinâmicas

**Problemas de prioridades estáticas**: 
1. Tarefas de baixa prioridadee tem pouco acesso à CPU
2. Se houverem muitas tarefas, podem ficar paradas
3. Starvation.

**Solução com prioridades dinâmicas**: 
1. Aumenar aos poucos a prioridade das tarefas paradas.
2. Ao executar, a tarefa volta à sua prioridade original.
3. Algoritmo de "envelhecimento" (*aging*).

Definições:
- $N$ : número de tarefas no sistema
- $t_i$ : tarefa $i$, $i \le 1 \le N$
- $pe_i$ : prioridade estátida da tarefa $t_i$
- $pd_i$ : prioridade dinâmina da tarefa $t_i$
- $\alpha$ : *agin factor*

Quando uma tarefa nova $t_{nova}$ ingressa no sistema:
1. $pe_{nova} =$ prioridade fixa
2. $pd_{nova} = pe_{nova}$ 

Para escolher $t_{prox}$, a próxima tarefa a executar:
1. escolher $t_{prox} | pd_{prox} == max_{i=1}^{N}(pi_i)$
2. $pd_{prox} = pe_{prox}$ (reinicia a prioridade)
3. $\forall \ne t_{prox}: pd_i = pd_i + \alpha$

## Escalonamento PRIOd: Prioridade Preemptivo Dinâmico

Mesmo esquema de PRIOp mas com *aging*. Enquanto a tarefa está esperando a sua prioridade aumenta.

___________________________________________

**Definiçao de prioridades**

**Fatores externos**: Informações proviadas pelo usuário ou o administrador. Prioridade estática.

**Fatores internos**: Informações que podem ser obtidas pelo escalonador. Permite calcular a prioridade dinâmica.

**No Linux**

Temos duas escalas de prioridade:
1. Tarefas de tempo real:
   1. Vai de 0 (mais importante) a 99 (menos importante).
   2. Tem precedência sobre tarefas interativas.
   3. Somente o administrador pode definir.
2. Tarefas interativas:
   1. Quase todas as tarefas dos usuários.
   2. Escala negativa de -20(mais importante) a +19 (menos importante).
   3. Ajustável através dos comandos `nice` e `renice` 

Usa um sistema com multiplas filas e cada fila tem uma política:
1. `SCHE_DEADLINE`: tarefas de tempo real com prazos, usa o algoritmo Earliest Deadline First (EDF).
2. `SCHED_FIFO`: prioridades fixas preemptivo, sem quantum.
3. `SCHED_RR`: SCHED_FIFO + Round-Robin, quantum 10-200ms.
4. `SCHED_NORMAL`: algoritmo CFS - Completely Fair Scheduler (Round-Robin c/ quantum variável, prioridades dinâmicas).
5. `SCHED_BATCH`: tarefas CPU-bound de baixa prioridade.
6. `SCHED_IDLE`: só recebe CPU se não houver tarefa ativa.

**No Windows**

Prioridades:
1. **24**: tempo real
2. **13**: alta
3. **10**: acima do normal
4. **8**: normal
5. **6**: abaixo do normal
6. **4**: baixa ou ociosa

A tarefa com **janela ativa** recebe mais prioridade (+1 pu +2)
