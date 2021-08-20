# Felipe Cadar Chamone - 2016006417

# Questão 1: 
1. O Objetivo desse campo é descrever as condições da exceção. Muitas vezes essa string é capaz de fornecer informação suficiente ao programador para que ele entenda a falha que aconteceu.
2. Exemplo:

```java
public class IlegalMoveException extends Exception { 
    public IlegalMoveException(String errorMessage) {
        super(errorMessage);
    }
}

public class OutOfBoardException extends Exception { 
    public OutOfBoardException(String errorMessage) {
        super(errorMessage);
    }
}

...

Xadrez board = new Xadrez();

...

String position = "A2";
try{
    board.WhiteMove("K", position); // mover o cavalo para posição A2
}catch (IlegalMoveException e) {
    if (!isOnBoard(position)){
        throw new OutOfBoardException("Posição fora do tabuleiro");
    }
    System.out.println(" Posição " + position + " Ilegal. Tente novamente.");
    ...
    tryAgain();
}
```
Saída:
```
Posição A2 Ilegal. Tente novamente.
```


# Questão 2:

Se a programação por contrato for bem implementada, o programador consegue prever quais entradas possíveis seu programa pode possuir e tratar todas as exceções, deixando o código mais robusto. Nesse caso, o tratamento de exceção pode até mesmo realizar correções para o correto funcionamento do código.


# Questão 3:

Na Programação Orientada a Aspectos, os pontos de junção são pontos onde se pode ser aplicado um aspecto, e o ponto de corte é uma maneira de selecionar pontos de junção, fazendo uma consuta sobre eles no programa.

# Questão 4:


1. ;
2. Java usa o pilimorfismo de inclusão para implementar heranças. Com esse polimorfismo uma classe pode sobrescrever um método herdado, fornecendo apenas uma nova implementação e mantendo nome, tipo de retorno e argumentos.
3. Todo objeto tem uma interface pública e uma estrutura de dados que o representa. A interface, que é acessível para todos, é o estado abstrato, é a visão que os métodos tem de um objeto sem conhecer sua estrutura de dados, é que seu estato concreto.