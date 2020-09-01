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
**Contexto**:
```Java
```
**Problema**:
**Solução**:
```Java
```

# Model
**Contexto**:
```Java
```
**Problema**:
**Solução**:
```Java
```