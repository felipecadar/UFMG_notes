# Variáveis de Condição

Muitas vezes o acesso a uma seção crítica só pode acontecer se certas condições forem etendiadas.

Pensando em um programa com uma **fila circular**, **consumidores** e **produtores**, o nosso mutex simples não é suficiente.


<table>
<tr>
    <th>Fila</th>
    <th>Produtor</th>
    <th>Consumidor</th>
</tr>
<tr>
<td>

```C
#define N 1000

int buffer[N];

int in = 0;
int out = 0;
int count = 0;
```

</td>
<td>

```C
int nextProduced = /*...*/;
while (count==N)
    /* Espera ocupada */;

buffer[in] = nextProduced;
in = (in + 1) % N;
count++;
```
</td>
<td>

```C
int nextConsumed;
while (count==0)
    /* Espera ocupada */;

nextConsumed = buffer[out];
out = (out + 1) % N;
count--;
```
</td>
</tr>
</table>

<table>
<td>

Para um sistema paralelo temos que resolver as seções críticas, mas só incluir o loop com mutex não funciona

Nessa situação, se eu entrar no mutex com a fila cheia, ninguém mais vai conseguir mudar minha variáveis e eu nunca vou dair da espera ocupada.

Precisamos esperar por uma condição apropriada para travar ou destravar o mutex.

</td>
<td>

```C
int nextProduced = /*...*/;
mutex_lock( &mutex)
while (count==N)
    /* Espera ocupada */;

buffer[in] = nextProduced;
in = (in + 1) % N;
count++;
mutex_unlock( &mutex)
```

</td>
</table>


Temos duas condições nesse exemplo:
1. Quem remove da fila, tem que esperar se a fila estiver vazia
2. Quem insere na fila, tem que esperar se a fila estiver cheia

As variáveis de condição são associadas a travas, ao esperar pela condição, a trava é liberada, ao retormar da espera, a trava é devolvida.

<table>

<tr>
<th>
Novo Produtor
</th>
<th>
Novo Consumidor
</th>

</tr>

<tr>

<td>

```C
int nextProduced = /*...*/;
mutex_lock( &mutex)
while (count==N) /* Espera ocupada */;
    cond_wait(not_full, &mutex);

buffer[in] = nextProduced;
in = (in + 1) % N;
count++;
cond_signal(not_empty);
mutex_unlock( &mutex)
```

</td>

<td>

```C
int nextConsumed;
mutex_lock( &mutex);
while (count==0) /* Espera ocupada */;
    cond_wait(not_empty, &mutex);

nextConsumed = buffer[out];
out = (out + 1) % N;
count--;
cond_signal(not_full); 
mutex_unlock( &mutex)
```

</td>
</tr>

</table>


