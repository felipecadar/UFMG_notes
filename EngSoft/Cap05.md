# Princípios de Projeto - Intro

**Aviso: Os assuntos discutidos neste capítulo aplicam-se a projeto orientado a objetos**

Começando a resolver os problemas de projeto. 

Projeto: quebrar um problema grande em partes menores e mais faceis de resolver.

em ingles -> Design: desenho ou proposta de uma solução.

Conseguimos quebrar um projeto em partes menores por meio de **abstrações**

Em um projeto de software precisamos conseguir decompor um problem em partes menores, abstrações. Além disse deve ser possível implementá-las individualmente.

# Propriedades de projeto:

## Integridade Conceitual

É a coerencia entre os módulos do sistemas. 

Existe um certo consenso de que decisões importantes de projeto não devem ficar nas mãos de um grande comitê, no qual cada membro tem direito a um voto. Quando isso ocorre, a tendência é a produção de sistemas com mais funcionalidades do que o necessário, isto é, sistemas sobrecarregados (bloated systems).


A integridade deve existir tanto no produto final quando no desenvolvimento. Um código padronizado é essencial para o projeto.

## Ocultamento de Informação

Devemos esconder decisões de projeto que são sujeitas a mudanças.

Os métodos publicos de uma classe compoem a interface da classe. A interface nunca deve ser alterada, já que é por ela que que códigos externos (cliente) utilizam a classe.

Vantagens:
1. Desenvolvimento em paralelo.
2. Flexibilidade a mudanças.
3. Facilidade de entendimento.

### Getters e Setters

Todo dado deve ser privado e seu acesso controlado por meio de funções `get` e `set`

## Coesão

Implementação coesa: toda classe deve implementar apenas uma única funcionalidade ou serviço e deve possuir apenas um **interesse** (separation of concerns)

Vantagens:
1. Facilita implementação
2. Facilita alocação de um responsável para manutenção
3. Facilita reúso e testes.

## Acoplamento

Acoplamento é a força da conexão entre duas classes, ele pode ser **aceitável** ou **ruim**.

Um acoplamente de uma classe A para B é **aceitável** quando:
1. a classe A utiliza apenas métodos públicos de B.
2. a interface de B é estável. São raras as mudaças em B que terão impacto em A.

Um acoplamento de uma classe A para B é **ruim** quando:
1. a classe A realiza acesso direto a dados da B.
2. A e B compartilham dados globais.
3. A interface de B não é estável.

**Acoplamento estrutural** entre A e B ocorre quando uma classe A possui uma referência explícita em seu código para uma classe B

**Acoplamento evolutivo (ou lógico)** entre A e B ocorre quando mudanças na classe B tendem a se propagar para a classe A.

Acoplamento evolutivo representa um acoplamento ruim.

# SOLID e Outros Princípios de Projeto

Princípios são recomendações em nível operacional, enquanto as propriedades são mais genéricas.

Os princípios de projeto que estudaremos tentam reduzir ou postergar essa contínua degradação da qualidade interna de sistemas de software

| Princípio                    | Propriedade               |
| ---------------------------- | ------------------------- |
| Responsabilidade Única       | Coesã                     |
| Segragação de Interfaces     | Coesão                    |
| Inversão de Dependências     | Acoplamento               |
| Prefira Composição a Herança | Acoplamento               |
| Demeter                      | Ocultamento de informação |
| Aberto/Fechado               | Extensibilidade           |
| Substituição de Liskov       | Extensibilidade           |

5 deles são conhecidos como princípios SOLID: 
- Single Responsibility Principle
- Open Closed/Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle

## Princípio da Responsabilidade Única

Cada classe deve possuir apenas uma responsabilidade. Ou seja, deve existir um único motivo para modificar qualquer classe em um sistema.

## Princípio da Segregação de Interfaces

O princípio define que interfaces têm que ser pequenas, coesas e, mais importante ainda, específicas para cada tipo de cliente. O objetivo é evitar que clientes dependam de interfaces com métodos que eles não vão usar.

## Princípio de Inversão de Dependências

Esse princípio recomenda que uma classe cliente deve estabelecer dependências com abstrações (**interfaces**) e não com implementações concretas (**classes**)

## Prefira Composição a Herança

Temos dois tipos de heranças:
1. Herança de classes (`class A extends B`): envolve reúso de código e é a herança padrão.
   1. É um **reúso caixa-branca**, pois as subclasses costumam ter detalhes de implementação.
2. Herança de interfaces (`class I implements J`): não envolve reúso de código
   1. É um **reúso caixa-preta**

Trouxe problemas pelo forte acoplamento entre subclasses e superclasses.

O princípio não proibe as heranças de, mas ele da preferencia sempre ao uso de composição sobre o uso de herança. o padrão de projeto **padrão decorador** ajuda a seguir esse princípio. 

<table>
<tr>
<th>Solução via Herança</th>
<th>Solução via Composição</th>
</tr>

<tr>
<td>

```C++
class Stack extends ArrayList {
  ...
}
```

</td>
<td>

```C++
class Stack {
  private ArrayList elementos;
  ...
}
```

</td>
</tr>

</table>

## Princípio de Demeter

Conjunto de regras propostas por um grupo de pesquisa.\

O princípio defende que a implementação de um método deve invocar apenas os seguintes outros métodos:
1. de sua própria classe
2. de objetos passados como parâmetros
3. de objetos criados pelo próprio método
4. de atributos da classe do método

<table>

<td>

```C++
class PrincipioDemeter {

  T1 attr;

  void f1() { 
    ...
  }

  void m1(T2 p) {  // método que segue Demeter
    f1();           // caso 1: própria classe
    p.f2();         // caso 2: parâmetro
    new T3().f3();  // caso 3: criado pelo método
    attr.f4();      // caso 4: atributo da classe
  }

  void m2(T4 p) {  // método que viola Demeter
    p.getX().getY().getZ().doSomething();
  }

}
```
</td>

<td>

O método `m1` está de acordo com o princípio. 

O método `m2` **viola** o princípio.

</td>

</table>


## Princípio Aberto/Fechado

Uma classe deve estar fechada para modificações e aberta para extensões. O Princípio Aberto/Fechado tem como objetivo a construção de classes flexíveis e extensíveis, capazes de se adaptarem a diversos cenários de uso, sem modificações no seu código fonte.

## Princípio de Substituição de Liskov

As subclasses não podem violar as regras de interface da superclasse.

Exemplo de **quebra de contrato**

```C++
class A {
  int soma(int a, int b) {
    return a+b;
  }
}

class B extends A {

  int soma(int a, int b) {
    String r = String.valueOf(a) + String.valueOf(b);
    return Integer.parseInt(r);
  }

}

class Cliente {

  void f(A a) {
    ...
    a.soma(1,2); // pode retornar 3 ou 12
    ...
  }

}

class Main {

  void main() {
    A a = new A();
    B b = new B();
    Cliente cliente = new Cliente();
    cliente.f(a);
    cliente.f(b);
  }

}
```

# Métricas de Código Fonte

Quantificar características do código fonte. Não é muito popular por os valores e faixas admissíveis são muito subjetivas.

## Tamanho (LOC)

Número de linhas de um código. Não representa produtividade e não deve ser vista como meta.

## Coesão - LCOM (Lack of Cohesion Between Methods)

Mede a falta de coesão de uma classe. Quanto maior o valor da métrica, pior a qualidade do código ou do projeto.

LCOM(C) é o número de pares de métodos — dentre todos os possíveis pares de métodos de C — que não usam atributos em comum, isto é, a interseção deles é vazia

## Acoplamento - CBO (Coupling Between Objects)

É uma métrica para medir acoplamento estrutural entre duas classes

Dada uma classe A, CBO conta o número de classes das quais A depende de forma sintática (ou estrutural). 

Diz-se que A depende de uma classe B quando:
- A chama um método de B
- A acessa um atributo público de B
- A herda de B
- A declara uma variável local, um parâmetro ou um tipo de retorno do tipo B
- A captura uma exceção do tipo B
- A levanta uma exceção do tipo B
- A cria um objeto do tipo B.

## Complexidade - CC (Complexidade Ciclomática)

CC = número de comandos de decisão em uma função + 1

Onde comandos de decisão podem ser if, while, case, for, etc

McCabe sugere que um limite superior razoável, mas não mágico para CC é 10.