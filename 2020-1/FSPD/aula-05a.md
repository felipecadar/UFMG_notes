# Problemas Clássicos de sincronização

1. Produtor/Consumidor
2. Leitor/Escritor
3. Jantar dos selvagens
4. Barbeiro dorminhoco (Sleeping Barber)
5. Jandar dos filósofos (Dinning philosophers)

# Produtores/Consumidoes

## Intro

Os produtores geram Dados e os colocam em uma fila. Os consumidores devem remover cada elemento e processar.

## Desafios

- Exclusão mutua entre tarefas iguais ou diferentes.
- Condições limite: 
  - Se a fila enche, o produtor tem que parar
  - Se a fila esta vazia, o consumidor tem que parar

## Solução

- Mutex com condições
- Semáforos
- Monitores

# Leitores/Escritores

## Intro

Temos uma estrutura de dados compartilhada. Os leitores acessam essa estrutura e leem dados sem alterar nada. Os escritores alteram a estrutura de dados (Precisam de mutex)

## Solução

Solução Simplista: Usar um mutex global. O Problema é não podemos ler em paralelo. Em uma solução melhor podemos deixar os leitores em paralelo e prioprizar entre escrita e leitura.

Solução mais tradicional:

```C
mutex marea; // controla o acesso à área
int num_leitores = 0; // número de leitores acessando a área
mutex mcount; // controla o acesso ao contador
```

<table>
<td>

```C
task escritor() {
    while(1){
        lock(marea);
        ...
        unlock(marea);
        ...
    }
}
```
</td>
<td>


```C
task leitor(){
    while(1) {
        lock(mcont);
        num_leitores++;
        
        // Se não e o primeiro, não precisa travar
        if (num_leitores == 1) 
            lock(marea);
        unlock(mcount);
        ...

        lock(mcount)
        num_leitores--;

        // Se ele e o ultimo leitor a sair
        if (num_leitores == 0)
            unlock(marea);
        ...
        
    }


}
```

</td>
</table>

Essa solução não garante que os escritores vão conseguir entrar. Se tivermos infinitos leitores entrando, eles travarão no mutex de area para sempre. (starvation)

# Jantar dos selvagens

Temos uma estrutura compartilhada, o caldeirão, que tem capacidade N. O cozinheiro enche o caldeirão e vai dormir. Cada selvagem se serve separadamente. Se o caldeirão estiver vazio, o selvagem acorda o cozinheiro.

<table>
<td>

```C
task cozinheiro(){
    while (1){
        encher_caldeirao();
        dormir();
    }
}
```

</td>

<td>

```C

task selvagem(){
    while(1){
        if(caldeirão_vazio)
            acordar_cozinheiro()
        servir();
        comer();
    }
}
```

</td>

</table>



## Solução

```C
int porcoes = 0; // Porçoes no caldeirao
mutex mc; // controla acesso ao caldeirao
semaphore cald_vazio(0), // indica caldeirao vazio 
          cald_cheio(0); // indica caldeirao cheio
```

<table>
<td>

```C
task selvagem(){
    while(1){
        lock(mc); // tenta acessar o caldeirao
        if (porcoes == 0){ // caldeirao vazio ?
            up(cald_vazio); // avisa que o caldeirao esvaziou
            down(cald_cheio); // espera ficar cheio
        } // aqui o caldeirao não está vazio
        porcoes--; // serve a porção
        unlock(mc); // libera o caldeirao
        comer()
    }
}
```

</td>

<td>

```C
task cozinheiro(){
    while(1){
        down(cald_vazio); // aguarda o caldeirão esvaziar
        porcoes += M; //enche o caldeirão com M porções
        up(cald_cheio); // avisa que encheu o caldeirão
                        // So precisa de 1 up pois só tem 1 selvagem 
                           // servindo de cada vez
    }
}
```

</td>

</table>

# Barbeiro Dorminhoco

Temos uma barbearia com certo número de cadeiras e um barbeiro que dorme quanto não tem ninguém para cortar o cabelo. Quando existe um clinente, o barbeiro é acordado. Se alguem chegar na barbearia com ela cheia, ele vai embora para voltar uma outra hora.

## Soluçoes

1. Tanenbaum, Sistemas Operacionais Avançados
2. Wikipedia

# Jantar dos filósofos

Talvez o mais famoso. Temos N filósofos sentados em uma mesa redonda. Cada filósofo pensa durante um tempo, fica com fome e come. Para comer ele precisa pegar os talheres da direita e da esquerda, um de cada vez, e depois de comer ele solta os dois. Só existe um talher entre cada filósofo

```C
task filosofo(){
    while(1){
        meditar();
        pegar_talher_direita();
        pegar_talher_esquerda();
        comer();
        soltar_talher_direita();
        soltar_talher_esquerda();
    }
}
```

# Solução


<table>
<td>

```C
int N = 6; // N Filosofos e Hashis
semaphore hashi[N](1); // todos iniciam com 1


task filosofo(int i){ // filosofo i (entre 0 e N-1)
    while(1){
        meditar();
        down(hashi[i]);
        down(hashi[(i+1) % N]);  // Estrutura circular
        comer();
        up(hashi[i]);
        up(hashi[(i+1) % N]);  // Estrutura circular
    }
}
```

</td>
<td>

**Problema**: Todos podem pegar o hashi da direita ao mesmo tempo e travar todos os processos para sempre. Isso é o **Deadlock**

</td>

</table>

