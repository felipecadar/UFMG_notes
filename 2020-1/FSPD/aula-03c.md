# Exclusão Mútua

## Introdução

Veremos com controlar o acesso da **seção crítica** do código

```python
def worker(number):
    global global_acc  # Memória compartilhada
    global num_iters
    for i in range(num_inters):
    global_acc += 1     # Seção crítica
```

## Requisitos da solução

* **Exlusão mútua**: se $T_i$ está na seção crítica, nenhuma outra tarefa pode entrar nela
* **Porgresso garantido**: se nenhuma tarefa está na seção crítica e uma outra tenta entrar, ela deve conseguir
* **Espera limitada**: se uma tarefa deseja entrar na seçao crítica, ela não pode ser infinitamente adiada. O tempo de espeda deve ser limitado.

### 1. Solução trivial - Espera Ocupada

```C
int busy = 0;

void enter() {
    while(busy){ /* Espera Ocupada */ };
    busy = 1;
}

void leave(){
    busy = 0;
}
```

O problema é que ela **NÃO GARANTE** exclusão mútua, pois a variável **busy** é vuneravel á condição de corrida.

### 2. Alternância

```C

int turn = 0; /* duas tarefas, 0 e 1 */

void enter(int task) {
    while(turn != task) { /* Espera Ocupada */ };
}

void leave(int task) {
    turn = 1 - turn; /* a outra */
}

```

Ele garante exclusão mútua, pois só a tarefa da rodada pode mudar a variável **turn**, mas **NÃO GARANTE progresso** , pois uma ação depende das outras tareas. Se a $T_0$ não entrar e sair, $T_1$ nunca entra.

Só funciona em um sistema que tem alternância exata.

### 3. Trava de exclusão mútua (Mutex)

**Instruções atômicas**

Aproveita de instruções indivisíveis do processador para fazer acesso a registradores garantindo exclusão mútua. Esse acesso é usado então para a lógica do algorítmo de entrada e saída.

O `XCHG` é uma instrução atômica da Intel que troca o valor de dois registradores.

```C
int lock = 0;

void enter(int *lock) {
    int key = 1;
    while (key) {
        XGHG(lock, &key); /* Espera Ocupada */
    }
}

void leave(int *lock) {
    (*lock) = 0;
}
```

Essa sulução garante exclusão mútua e progresso independente. Estatisticamente ela tambêm garante espera limitada.

As implementações mais modernas não envolvem espera ocupada

```C
#include <pthread.h>

pthread_mutex_t mutex;
pthread_mutex_init( &mutex, NULL /* Atributos */ );

...

pthread_mutex_lock( &mutex );
// seção crítica
pthread_mutex_unlock( &mutex );

```

