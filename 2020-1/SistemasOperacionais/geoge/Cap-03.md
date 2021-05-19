# Processos

#### Definição de processo

SO executa vários programas:
- Sistemas em batch: jobs
- Sistemas de tempo compartilhado: programas

Processo: um programa em execução.

Informações associadas com cada processo ficam no Bloco de controle de processo(PCB). São estruturas opacas, que não temos visibilidade de como ela é organizada.

O PCB é uma estrutura de dados que o SO aloca para cada processo.

Um processo tem 3 etapas:
- Criação
    - Aloca o PCB
    - Inicializa o PCB
- Execução
    - Escalonamento pelo núcleo
    - Comunicação entre processos
    - Acesso a dispositivos
- Terminação
    - Liberar recursos, como arquivos abertos e dispositivos usados.

Um processo pai cria processos filhos, que por sua vez podem criar mais processos. Isso estabelece uma árvode de dependencias entre processos.

Arvore no Unix:

- root
    - Pagedeamon (gerenciador de memória)
    - Swapper (mantido por questão história, n faz nada)
    - init (deriva tudo que o usuário tem acesso)
        - user 1
        - user 2
        - user 3

A crianção de processos funcioa com clones. Um processo se clona para criar outro.

Quando um pai morre, geralmente os filhos passam a pertencer ao init.

Na terminação um processo pede para o S.O. para retirá-lo do sistema, isso na terminação suave, intencionada.

#### Estado de um processo

- Novo
    - Acabou de ser criado  
- Executando
    - Está na CPU
- Em espera
    - Não pode ser executado, ta esperando algo acontecer
- Pronto
    - não ta na CPU mas pode ser executado a qualquer momento
- Terminado
    - terminou de executar ou morreu

Ciclo de vida de um processo

1. Novo
2. Fase de Admissão
    - o sistema decide se temos recursos para o processo
3. Pronto
    - O escalonador decide quando ele via ser executado, e ele passa para executando
4. Executando
    - Pode ir para 
        - Pronto -> Decisão do escalonador
        - Espera -> Requisição de entrada E/S
        - Terminado -> Saída
5. Terminado
    - LIbera os recursos

Toda mudança de estado é feita por uma interrupção

#### Escalonamento de processos

Aumentar a uilização do processador

Paralelismo aparente e transparente

Aparente -> passar a impressão pro usuário que ele tem vários programas executando ao mesmo tempo, mas não estão.

Transparente -> O usuário n tem que fazer nada para isso existir.

#### Filas de escalonamento

- Fila de jobs 
    - conjunto de todos os processos
    - Sistemas batch
- Filas de prontos
    - Todos os processos prontos esperando a CPU
    - Pode ter várias filas de prontos com níveis de prioridades diferentes
- FIlas de dispositivos
    - Porcessos aguardando respota de um dispositivo E/S

Decisôes muito complexas de tomar, pois temos que compartilhar muitos recursos entre processos muito diferentes. Geralme essas decisoes são tomadas com heurísticas.

Ciclo de filas mostrando os monivos de um processo parar está no slide 14-Processos.

#### Escalonadores

De longo prazo, de jobs
- É chamado com menos frequência.

De curto prazo, de CPU
- Deve ser rápido

De médio
- Existe para corrigir erros do escalonador de longo prazo
- Ele tirar um processo que está executando e o move para o disco
- Usado em caso de sobrecarga de sistema

Os processos podem ser descritos como:
- I/O bound
    - Passa mais tempo esperando por E/S que computando
    - muitas rajadas curtas de processamento
- CPU bound
    - passa mais tempo em processamento
    - pedríodos longos de processamento, na CPU

#### Troca de contexto

Operação simples, que é tirar um processo da execução e colocar outro.
Para tirar um processo precisamos garantir que podemos voltar a executar ele de novo. Então guardamos o estado do processo no PCB.

Troca de contexto é overhead, custosa! Guarda informações que não fazem parte do processo em si.

O tempo gasto depende do hardware e da estrutura do processo

#### Comunicação entre processos (IPC)

Troca de informação entre fluxos de execução (duas regioes da memória)
- Memória compartilhada (shmem)
    - Os dois processos escrevem e leem na mesma área de memória.
    - Primitivas dependem do SO.
    - Mesmo princípio das therads.
- Troca de mensagens (send/receive)
    - Um canal de comunicação, tipo sockets.
    - Envolve system call, que é caro.
    - Envolve troca de contexto, que também é caro.
    - Por outro lado a interface é de bem mais alto nível.

Envolve muitas decisoes de ĩmplementação... qual a capacidade do canal ? um canal pode ligar mais de dois processos ? O tamanho das mensagens é fixo? O que acontece quando o canal está cheio e etc...


NOTE: Pulamos as seções 3.5 e 3.6 e passamos por alto pela 3.4 (comunicação entre processos)

