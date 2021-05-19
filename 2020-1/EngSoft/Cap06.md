# Padrões de Projeto - Intro

Soluções para padrões de projetos

> Padrões de projeto descrevem objetos e classes que se relacionam para resolver um problema de projeto genérico em um contexto particular.
> 
>  -- <cite> Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides </cite>

Para entender um padrão precisamos entender :
1. O Problema que o padrão quer resolver
2. O contexto em que esse problema ocorre 
3. A solução proposta

Os nomes dos padrões de projetos passaram a ser adotados em documentações.

O conhecimento dos padrões de projeto podem ajudar tando no desenvolvimento do próprio software quando no entendimento de software de terceiros

"design for change" - Devemos projetar um sistema pensando em mudaças que vão ocorrer.

São propostas 23 padrões divididos em 3 categorias: (Estudaremos os em negrito)
1. Criacionais:
   1. **Abstract Factory**
   2. Factory Method
   3. **Singleton**
   4. **Builder**
   5. Prototype
2. Estruturais
   1. **Proxy**
   2. **Adapter**
   3. **Facade**
   4. **Decorator**
   5. Bridge
   6. Composite
   7. Flyweight
3. Comportamentais
   1. **Strategy**
   1. **Observer**
   1. Template **Method**
   1. **Visitor**
   1. Chain of Responsibility
   1. Command
   1. Interpreter
   1. **Iterator**
   1. Mediator
   1. Memento
   1. State.


# Fábrica Abstrata

**Contexto**: Um sistema baseado em TCP/IP possui 3 funções, `f`, `g` e `h`, que criam objetos do tipo `TCPChannel`.

```Java
void f() {
  TCPChannel c = new TCPChannel();  
  ...
}

void g() {
  TCPChannel c = new TCPChannel();
  ...
}
```

**Problema**: O sistema não atende ao Princípio Aberto/Fechado, podemos querer trocar o protocolo de comunicação.

**Solução**: Usar um método cria e retorna o objeto desejado, ocultado o tipo desse objeto por trás de um interface.

```Java
class ChannelFactory {
  public static Channel create() {// método fábrica estático
    return new TCPChannel();
  }
}

void f() {
  Channel c = ChannelFactory.create();  
  ...
}

void g() {
  Channel c = ChannelFactory.create();
  ...
}
void h() {
  Channel c = ChannelFactory.create();
  ...
}
```

Ainda aplicamos o princípio "Prefira Interfaces a Classes" (ou Inversão de Dependências)

Em uma variação do padrão Fábrica, uma classe abstrata é usada para concentrar vários métodos de fábrica.

```Java
abstract class ProtocolFactory { // Fábrica Abstrata
  abstract Channel createChannel();
  abstract Port createPort();  
  ...
}

void f(ProtocolFactory pf) {
  Channel c = pf.createChannel();
  Port p = pf.createPort();
  ...
}
```

# Singleton

**Contexto**: Suponha uma classe `Logger`

```Java
void f() {
  Logger log = new Logger();  
  log.println("Executando f");
  ...
}
void g() {
  Logger log = new Logger();  
  log.println("Executando g");
  ...
}
void h() {
  Logger log = new Logger();  
  log.println("Executando h");
  ...
}
```

**Problema**: Não gostomas de criar um logger para cada função.

**Solução**: Tranformar Logger em um Singleton. Uma classe que terá, no máximo, uma instância.

```Java
class Logger {

  private Logger() {} // proíbe clientes chamar new Logger()

  private static Logger instance; // instância única

  public static Logger getInstance() {
    if (instance == null) // 1a vez que chama-se getInstance
      instance = new Logger();
    return instance;
  }

  public void println(String msg) {
    // registra msg na console, mas poderia ser em arquivo
    System.out.println(msg);      
  }
}
```

É um padrão polêmico pois camufla a criação de variáveis globais, que gera acoplamento ruim (ou forte). Nesse caso não tem problema pois é exatamente o que queremos.

Isso pode dificultar testes automáticos por fazer com que métodos dependam de variaáveis globais.

# Proxy

**Contexto**: Suponha a classe `BookSearch`

```Java
class BookSearch {
  ...
  Book getBook(String ISBN) { ... }
  ...
}
```

**Problema**: Queremos implementar um requisito não funcional, "usar um cache nas pesquisas por livros" e não queremos implmenta-lo na classe `BookSearch` pelo Princípio da Responsabilidade Única.

**Solução**: Adicionamos um Proxy entre o cliente e o Objeto, adicionando funcionalidades sem que ele perceba. 

```Java
class BookSearchProxy implements BookSearchInterface {

  private BookSearchInterface base;

  BookSearchProxy (BookSearchInterface base) {
    this.base = base;
  }

  Book getBook(String ISBN) {
    if("livro com ISBN no cache")
      return "livro do cache"
    else {
      Book book = base.getBook(ISBN);
      if(book != null)
        "adicione book no cache"
      return book;
    }
  }
  ...
}
```

Deve ser criada também uma interface BookSearchInterface, não mostrada no código.Mais uma vez, estamos lançando mão do Princípio "Prefira Interfaces a Classes".

Além de ajudar na implementação de caches, proxies podem ser usados para implementar outros requisitos não-funcionais. Alguns exemplos incluem:
1. Comunicação com um cliente remoto, isto é, pode-se usar um proxy para encapsular protocolos e detalhes de comunicação. Esses proxies são chamados de stubs.
2. Alocação de memória por demanda para objetos que consomem muita memória.
3. Controlar o acesso de diversos clientes a um objeto base.

# Adaptador
**Contexto**: Suponha um sistema que tenha que controlar projetores multimídia. Para isso ele deve instanciar objetos de classes fornecidas pelos fabricantes de cada projetor

```Java
class ProjetorSamsung {
  public void turnOn() { ... }
  ...
}

class ProjetorLG {
  public void enable(int timer) { ... }
  ...
}
```
**Problema**: No sistema queremos ter uma classe única "projetor" com um método "liga" padrão.
**Solução**: Adaptador ou Wrapper. Recomenda-se usar esse padrão quando temos que converter a interface de uma classe para outra interface, esperada pelos seus clientes
```Java
class AdaptadorProjetorSamsung implements Projetor {

   private ProjetorSamsung projetor;

   AdaptadorProjetorSamsung (ProjetorSamsung projetor) {
     this.projetor = projetor;
   }

   public void liga() {
     projetor.turnOn();
   }
}
```

# Fachada
**Contexto**: Imagine que X é uma linguagem para consulta a dados, semelhante a SQL. Para executar programas X, a partir de um código em Java, os seguintes passos são necessários:
```Java
Scanner s = new Scanner("prog1.x");
Parser p = new Parser(s);
AST ast = p.parse();
CodeGenerator code = new CodeGenerator(ast);
code.eval()
```
**Problema**:O código acima requer conhecimento de classes internas do interpretador de X. Logo, os usuários frequentemente pedem uma interface mais simples para chamar o interpretador da linguagem X.
**Solução**: Uma Fachada é uma classe que oferece uma interface mais simples para um sistema. 
```Java
class InterpretadorX {

  private String arq;

  InterpretadorX(arq) {
    this.arq = arq;
  }

  void eval() {
    Scanner s = new Scanner(arq);
    Parser p = new Parser(s);
    AST ast = p.parse();
    CodeGenerator code = new CodeGenerator(ast);
    code.eval();
  }
}
```

# Decorador
**Contexto**:Suponha que as classes TCPChannel e UDPChannel implementam uma interface Channel
```Java
interface Channel {
   void send(String msg);
   String receive();
}

class TCPChannel implements Channel {
   ...
}

class UDPChannel implements Channel {
   ...
}
```
**Problema**: Se quisermos adicionar funcionalidades diferentes para diferentes clientes fica inviável o uso de heranças pela explosão combinatória do número de classes.
**Solução**: Em vez de usar herança, usa-se composição para adicionar tais funcionalidades dinamicamente nas classes base. Portanto, Decorador é um exemplo de aplicação do princípio de projeto "Prefira Composição a Herança"
```Java
channel = new ZipChannel(new TCPChannel());
// TCPChannel que compacte/descompacte dados 

channel = new BufferChannel(new TCPChannel());
// TCPChannel com um buffer associado

channel = new BufferChannel(new UDPChannel());
// UDPChannel com um buffer associado

channel = new BufferChannel(new ZipChannel(new TCPChannel()));
// TCPChannel com compactação e um buffer associado
```

E como esses decoradores funcionam ?

```Java
class ChannelDecorator implements Channel {

  protected Channel channel;

  public ChannelDecorator(Channel channel) {
    this.channel = channel;
  }

  public void send(String msg) {
    channel.send(msg);
  }

  public String receive() {
    return channel.receive();
  }

}
```

Ela é uma Channel, isto é, ela implementa essa interface e, portanto, os seus dois métodos. Assim, sempre que for esperado um objeto do tipo Channel podemos passar um objeto do tipo ChannelDecorator no lugar.

Ela possui internamente um objeto do tipo Channel para o qual delega as chamadas aos métodos send e receive. Em outras palavras, um decorador, no nosso caso, vai sempre referenciar um outro decorador. Após implementar a funcionalidade que lhe cabe — um buffer, compactação, etc — ele repassa a chamada para esse decorador.

```Java
class ZipChannel extends ChannelDecorator {

   public ZipChannel(Channel c) {
    super(c);
   }  

   public void send(String msg) {
    "compacta mensagem msg"
    super.channel.send(msg);
   }

   public String receive() {
    String msg = super.channel.receive();
    "descompacta mensagem msg"
    return msg;
   }

}
```

Cod completo [aqui](https://gist.github.com/mtov/c8d65378a2904af01c20c53922f5ae1d)

# Strategy
**Contexto**: Suponha a seguinte classe Lista
```Java
class MyList {

  ... // dados de uma lista
  ... // métodos de uma lista: add, delete, search

  public void sort() {
    ... // ordena a lista usando Quicksort
  }
}
```
**Problema**: Os nossos clientes estão solicitando que novos algoritmos de ordenação. Eles querem ter a opção de alterar e definir, por conta própria, o algoritmo de ordenação.
**Solução**: Deixar o algoritmo de ordenação parametrizável.
```Java
class MyList {

  ... // dados de uma lista
  ... // métodos de uma lista: add, delete, search

  private SortStrategy strategy;

  public MyList() {
    strategy = new QuickSortStrategy();
  }

  public void setSortStrategy(SortStrategy strategy) {
    this.strategy = strategy;
  }

  public void sort() {
    strategy.sort(this);
  }
}


abstract class SortStrategy {
  abstract void sort(MyList list);
}

class QuickSortStrategy extends SortStrategy {
  void sort(MyList list) { ... }
}

class ShellSortStrategy extends SortStrategy {
  void sort(MyList list) { ... }
}

```
# Observador
**Contexto**: Temos que manupular objetos de duas classes, Temperatura e Termometro. Se a temperatura mudar devemos atualizar o termometro.
```Java
```
**Problema**: Não queremos acoplar Temperatura (classe de modelo) a Termometro (classe de interface). O motivo é simples: classes de interface mudam com frequência.
**Solução**: Esse padrão define como implementar uma relação do tipo um-para-muitos entre objetos sujeito e observadores. Quando o estado de um sujeito muda, seus observadores devem ser notificados.
```Java
void main() {
  Temperatura t = new Temperatura();
  t.addObserver(new TermometroCelsius());
  t.addObserver(new TermometroFahrenheit());
  t.setTemp(100.0);
}

//////////////////////////////////////////

class Temperatura extends Subject {

  private double temp;

  public double getTemp() {
    return temp;
  }

  public void setTemp(double temp) {
    this.temp = temp;
    notifyObservers();
  }
}

class TermometroCelsius implements Observer {

  public void update(Subject s){
    double temp = ((Temperatura) s).getTemp();
    System.out.println("Temperatura Celsius: " + temp);
  }
}

```
Código completo [aqui](https://gist.github.com/mtov/5fadb0e599cb84fd6bd124b2ff37c03c)


# Template Method
**Contexto**: Suponha que estamos desenvolvendo uma folha de pagamento. Nela, temos uma classe Funcionario, com duas subclasses: FuncionarioPublico e FuncionarioCLT
```Java
```
**Problema**: As subclasses precisam saber o método que devem implementar.
**Solução**: O padrão de projeto Template Method resolve o problema que enunciamos. Ele especifica como implementar o esqueleto de um algoritmo em uma classe abstrata X, mas deixando pendente alguns passos — ou métodos abstratos. Esse recurso de sistemas orientados a objetos é chamado de inversão de controle.
```Java
abstract class Funcionario {

   double salario;
   ...
   abstract double calcDescontosPrevidencia();
   abstract double calcDescontosPlanoSaude();
   abstract double calcOutrosDescontos();

   public double calcSalarioLiquido() { // template method
     double prev = calcDescontosPrevidencia();
     double saude = calcDescontosPlanoSaude();
     double outros = calcOutrosDescontos();
     return salario - prev - saude - outros;
   }
}
```
# Visitor
**Contexto**: Suponha que nesse sistema existe uma classe Veiculo, com subclasses Carro, Onibus e Motocicleta. Suponha ainda que todos esses veículos estão armazenados em uma lista. Dizemos que essa lista é uma estrutura de dados polimórfica, pois ela pode armazenar objetos de classes diferentes, desde que eles sejam subclasses de Veiculo.
**Problema**: Com frequência, no sistema de estacionamentos, temos que realizar uma operação em todos os veículos estacionados. Como simular double dispatch em uma linguagem como Java?
**Solução**: A solução para o nosso problema consiste em usar o padrão de projeto Visitor. Esse padrão define como adicionar uma operação em uma família de objetos, sem que seja preciso modificar as classes dos mesmos. Além disso, o padrão Visitor deve funcionar mesmo em linguagens com single dispatching de métodos, como Java.
```Java
abstract class Veiculo {
  abstract public void accept(Visitor v);
}

class Carro extends Veiculo {
  ...
  public void accept(Visitor v) {
   v.visit(this);
  }
  ...
}

class Onibus extends Veiculo {
  ...
  public void accept(Visitor v) {
    v.visit(this);
  }
  ...
}

// Idem para Motocicleta
///////////////////////////////

PrintVisitor visitor = new PrintVisitor();
foreach (Veiculo veiculo: listaDeVeiculosEstacionados) {
  veiculo.accept(visitor);
}

```

Antes de concluir, é importante mencionar que visitors possuem uma desvantagem importante: eles podem forçar uma quebra no encapsulamento das classes que serão visitadas. Por exemplo, Veiculo pode ter que implementar métodos públicos expondo seu estado interno para que os visitors tenham acesso a eles.

# Outros Padrões de Projeto
**Iterador** é um padrão de projeto que padroniza uma interface para caminhar sobre uma estrutura de dados. Normalmente, essa interface inclui métodos como hasNext() e next(). Um iterador permite percorrer uma estrutura de dados sem conhecer o seu tipo concreto.
```Java
List<String> list = Arrays.asList("a","b","c");
Iterator it = list.iterator();
while(it.hasNext()) {
  String s = (String) it.next();
  System.out.println(s);
}
```

**Builder** é um padrão de projeto que facilita a instanciação de objetos que têm muitos atributos, sendo alguns deles opcionais.
```Java
Livro esm = new Livro.Builder().
                  setNome("Engenharia Soft Moderna").
                  setEditora("UFMG").setAno(2020).build();

Livro gof = new Livro.Builder().setName("Design Patterns").
                  setAutores("GoF").setAno(1995).build();
```



```Java
```

# Quando Não Usar Padrões de Projeto

Antes de usar uma **fábrica**, devemos fazer (e responder) a seguinte pergunta: vamos mesmo precisar criar objetos de tipos diferentes no nosso sistema? Existem boas chances de que tais objetos sejam, de fato, necessários? Se sim, então vale a pena usar uma Fábrica para encapsular a criação de tais objetos. Caso contrário, é melhor criar os objetos usando o operador new, que é a solução nativa para criação de objetos em linguagens como Java.

De forma semelhante, antes de incluir o padrão **Strategy** em uma certa classe devemos nos perguntar: vamos mesmo precisar de parametrizar os algoritmos usados na implementação dessa classe? Existem, de fato, usuários que vão precisar de algoritmos alternativos? Se sim, vale a pena usar o padrão Strategy. Caso contrário, é preferível implementar o algoritmo diretamente no corpo da classe.

No entanto, em muitos sistemas observa-se um uso exagerado de padrões de projeto, em situações nas quais os ganhos de flexibilidade e extensibilidade são questionáveis. Existe até um termo para se referir a essa situação: **paternite**, isto é, uma inflamação associada ao uso precipitado de padrões de projeto.

