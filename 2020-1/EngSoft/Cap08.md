<h1> Testes </h1>

- Pirâmide de classificação
- Foco em testes de unidade


# Intro

Testes servem para evitar que erros cheguem ao usuário final.

No desenvolvimento em cascata, os testes vinham depois de tudo e existia uma equipe separada para eles. O Objetivo era apenas detectar bugs antes que o sistema entrasse em produção.

Com métodos ágeis:
- Grande parte dos testes foram automatizados. **auto-testáveis**
- Muitas vezes são implementado primeiro
- O desenvolvedor que implementa uma classe, também implementa os testes para ela.
- Testes agora são usados como documentação e para garantir que uma parte do sistema não vai parar se funcionar quando um bug for corrigido.

Michael Feathers: Código sem teste = baixa qualidade / legado

Mike Cohn: Pirâmide

- Topo: 
  - Maior granulalidade 
  - Menor quantidade
  - Mais lentos
- Base
  - Menor granulalidade 
  - Maior quantidade
  - Mais rápidos
  - Menor custo

1. **Testes de sistema**
   1. Também chamados de testes de interface com o usuário
   2. Simulam de forma fiel uma sessão de uso ponta-a-ponta.
   3. Caros e lentos.
   4. Os mais frágeis. Alterações mínimas nos componentes podem demandar modificações nesses testes
2. **Testes de integração** 
   1. Também chamados de testes de serviços
   2. Verificam a funcionalidade ou transação completa de um sistema.
   3. Usam várias classes.
   4. Pode testar até banco de dados
   5. Mais lentos e mais complexos
3. **Testes de unidade**
   1. Verificam automaticamente pequenas partes do código. Normalmente apenas uma classe.
   2. Simples, rápidos e numerosos.


Proporção desejada: 10% - 20% - 70%

- **defeito** ou **bug**: Quando um código não está de acordo com a sua especificação.
- **falha**: Se um código com defeito for executado e levar o programa a apresentar um resultado ou comportamento incorreto

# Testes de Unidade

Testes de unidade são testes automatizados de pequenas unidades de código

Testados de forma isolada do restante do sistema.

Um teste de unidade é um programa que chama métodos de uma classe e verifica se eles retornam os resultados esperados.

Frameworks conhecidos: *x*Unit onde x = linguagem
 1. JUnit: Testes para Java

```Java
import org.junit.Test;
import static org.junit.Assert.assertTrue;

public class StackTest {

  @Test
  public void testEmptyStack() {
    Stack<Integer> stack = new Stack<Integer>();
    boolean empty = stack.isEmpty();
    assertTrue(empty);
  }

}
```

## Definições:

- **Teste**: método que implementa um teste. O nome deriva da anotação `@Test`.
- **Fixture**: estado do sistema que será testado por um ou mais métodos de teste, incluindo dados, objetos, etc.
- **Casos de Teste**: classe com os métodos de teste.
- **Suíte de Testes**: conjunto de casos de teste.
- **Sistema sob Teste**: sistema que está sendo testado.


## Quando escrever testes de unidade:
1. Após implementar uma pequena funcionalidade.
2. Antes de escrever o código de produção.
   1. Test-Driven Development.
3. Para depurar
   1. Evite de colocar vários `print`s no método que serão removidos depois. Use um teste para depurar

Não é recomendável deixar todos os testes para depois do sistema ficar pronto. Isso pode gerar testes de baixa qualidade ou pode ser que eles nem chegem a serem implementados.

É recomendado que a Classe e seu Teste sejam implementados pelo menos desenvolvedor.

## Benefícios

1. Encontrar Bugs antes da produção.
2. Rede de proteção contra **regressões** no código.
3. Ajudam na documentação.

# Princípios e Smells

Questões importantes para implementar bons testes

## Princípios FIRST

- **Fast** (rápidos): Devem executar rapidamente e oferecer feedback rápido. Se isso não for possível, podemos divir a suíte em dois grupos, o rápidos e os mais demorados.
- **Independent** (Independentes): A ordem de execução dos testes de unidade não é importante.
- **Repeatable** (Determinísticos): Testes de unidade devem ter sempre o mesmo resultado. A falhe nesse quesito gera *Testes Flaky* ou *Testes Erráticos*.
- **Self-checking** (Auto-verificáveis): O resultado de um teste de unidades deve ser facilmente verificável
- **Timely** (Escritos o quanto antes): Se possível escrever o teste antes mesmo do código que vai ser testado.

## Test Smells

Test Smells representam estruturas e características **preocupantes** no código de testes de unidade, as quais, a princípio deveriam ser **evitadas**.

1. **Teste Obscuro**: É um teste longo, complexo e difícil de entender.
2. **Teste com Lógica Condicional**: Inclui código que pode ou não ser executado.
3. **Duplicação de Código em Testes**: Quando temos código repetido em diversos métodos de teste

No entanto, um test smell não deve ser interpretado ao pé da letra. Em vez disso, eles devem ser considerados como um alerta para os implementadores do teste.

## Número de assert por Teste

Alguns autores recomendam que deve existir no máximo um assert por teste.

No entanto, não devemos ser dogmáticos no emprego dessa regra. Por exemplo, suponha que precisamos testar uma função `getBook` que retorna um objeto com dados de um livro, incluindo `título`, `autor`, `ano` e `editora`. Nesse caso, justifica-se ter quatro comandos `assert` no mesmo teste.

Uma segunda exceção é quando temos um método simples, que pode ser testado por meio de um único assert.

# Cobertura de Testes

Cobertura de testes é uma métrica que ajuda a definir o número de testes que precisamos escrever para um programa. Ela mede o percentual de comandos de um programa que são cobertos por testes.

## Qual a Cobertura de Testes Ideal?

Não existe um número mágico e absoluto para cobertura de testes.

Recomenda-se também avaliar cuidadosamente os trechos não cobertos por testes, para confirmar que eles não são relevantes ou então são difíceis de serem testados.

Deve-se monitorar a evolução dos valores de cobertura ao longo do tempo para verificar se não estão relaxando na escrita de testes.

Times que valorizam a escrita de testes costumam atingir facilmente valores de cobertura próximos de 70%.

Por outro lado, valores abaixo de 50% tendem a ser preocupantes.

## Outras Definições de Cobertura de Testes
1. **Cobertura de funções**: Percentual de funções que são executadas por um teste.
2. **Cobertura de chamadas de funções**: Dentre todas as linhas de um programa que chamam funções, quantas são de fato, exercitadas por testes)
3. **Cobertura de branches**: % de branches de um programa que são executados por testes; um comando if sempre gera dois branches

Cobertura de comandos: Cobertura C0
Cobertura de branches: Cobertura C1

# Testabilidade

Testabilidade é uma medida de quão fácil é implementar testes para um sistema. **design for testability**.

A boa notícia é que código que segue as propriedades e princípios de projeto tende a apresentar boa testabilidade.

# Mocks

**Aviso**: Neste capítulo, usamos **mock** como sinônimo de **stub**.

Usado para evitar o uso de servições externos ao objetivo do teste. Então criamos esses serviços simulados.

## Frameworks de Mocks

Mocks são tão comuns em testes de unidade que existem frameworks para facilitar a criação e programação de mocks (e/ou stubs). 

Exemplo: Mockito

## Mocks vs Stubs

Alguns autores, como Gerard Meszaros, fazem uma distinção entre mocks e stubs.

- Mocks devem verificar não apenas o estado do Sistema sob Testes (SUT), mas também o seu comportamento.
- Se os mocks verificam apenas o estado, eles deveriam ser chamados de stubs.

**teste comportamental**: verifica eventos que ocorreram no SUT

Segundo Gerard Meszaros, mocks e stubs são casos especiais de **objetos dublê**:
1. **Objetos Dummy**: são passados como argumento para um método, mas que não são usados. Apenas para satisfazer o sistema de tipos da linguagem.
2. **Objeto Fake**: são objetos que possuem uma implementação mais simples do que o objeto real.

# Desenvolvimento Dirigido por Testes

Desenvolvimento Dirigido por Testes (Test Driven Development, TDD) é uma das práticas de programação propostas por Extreme Programming (XP). 

Quando se escreve o teste primeiro, ele vai falhar. Então, no fluxo de trabalho defendido por TDD, o próximo passo consiste em escrever o código que faz esse teste passar, mesmo que seja um código trivial. Em seguida, esse primeiro código deve ser finalizado e refinado. Por fim, se necessário, ele deve ser refatorado, para melhorar seu projeto, legibilidade, manutenibilidade, para seguir princípios e padrões de projeto, etc.

Objetivos:
1. TDD ajuda a evitar que os desenvolvedores esqueçam de escrever testes. 
2. TDD favorece a escrita de código com alta testabilidade. 
3. TDD é uma prática relacionada não apenas com testes, mas também com a melhoria do design de um sistema. 

Ciclo: 
- Teste Falha
- Teste Passa
- Refatoração
 
# Outros Tipos de Testes

## Testes Caixa-Preta e Caixa-Branca

No entanto, não é trivial classificar testes de unidade em uma dessas categorias. Na verdade, a classificação vai depender de como os testes são escritos.

**Caixa-Preta**:
- Os testes são escritos com base apenas na interface do sistema sob testes.
- Testes funcionais

**Caixa-Branca**:
- a escrita dos testes considera informações sobre o código e a estrutura do sistema sob teste
- Testes estruturais
- Tira proveito do conhecimento do código escrito para fazer testes mais eficientes, como forçar a entrada branches.


## Seleção de Dados de Teste

Testes **exaustivos**, isto é, testar um programa com todas as entradas possíveis, na prática, é impossível, mesmo em programas pequenos.

**Classe de Equivalência**: Uma técnica que recomenda dividir as entradas de um problema em conjuntos de valores que têm a mesma chance de apresentar um bug.

**Análise de Valor Limite**: Uma técnica complementar que recomenda testar uma unidade com os valores limites de cada classe de equivalência e seus valores subsequentes (ou antecedentes).****

## Testes de Aceitação

São testes realizados pelo cliente, com dados do cliente. Os resultados desses testes irão determinar se o cliente está de acordo ou não com a implementação realizada. Se estiver de acordo, o sistema pode entrar em produção. Se não estiver de acordo, os devidos ajustes devem ser realizados.

- São manuais
- Não constituem exclusivamente uma atividade de verificação (como os testes anteriores), mas também uma atividade de validação do sistema ( se o sistema é aquele que o cliente pediu e precisa).

Testes de aceitação podem ser divididos em duas fases:
1. **Testes alfa**: São realizados com alguns usuários, mas em um ambiente controlado.
2. **Testes beta**: Um teste com um grupo maior de usuários e não mais em um ambiente controlado.

## Testes de Requisitos Não-Funcionais

- **Testes de desempenho**: para verificar o comportamento de um sistema com alguma carga
- **Testes de usabilidade**: são usados para avaliar a interface do sistema e, normalmente, envolvem a observação de usuários reais usando o sistema
- **Testes de falhas**: simulam eventos anormais em um sistema, por exemplo a queda de alguns serviços ou mesmo de um data-center inteiro.

