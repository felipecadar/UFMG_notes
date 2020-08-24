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

```C
task cozinheiro(){
    while (1){
        encher_caldeirao();
        dormir();
    }
}
```

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

