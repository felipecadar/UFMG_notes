# Variáveis de Condição

Muitas vezes o acesso a uma seção crítica só pode acontecer se certas condições forem etendiadas.

Pensando em um programa com uma **fila circular**, **consumidores** e **produtores**, o nosso mutex simples não é suficiente.

Fila:

```C
#define N 1000

int buffer[N];

int in = 0;
int out = 0;
int count = 0;
```

Produtor:

```C
int nextProduced = /*...*/;
while (count==N)
    /* Espera ocupada */;
buffer[in] = nextProduced;
in = (in + 1) % N;
count++;
```

Consumidor:

```C
int nextConsumed;
while (count==0)
    /* Espera ocupada */;

nextConsumed = buffer[out];
out = (out + 1) % N;
count--;
```
