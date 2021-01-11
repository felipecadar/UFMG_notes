# Test Smells

Estruturas que devem ser evitadas nos testes.

- **Teste Obscuro**: longo, complexo e difícil de entender
- **Teste com lógica condicional**: inclui código que pode não ser executado
- **Duplicação de códifo em testes**: código repetidos em testes diferentes

Não deve ser interpretado ao pé da letra. Os testes devem ser refatorados ao longo do tempo

Alguns autores recomendam apenas um assert por teste, no entanto existem casos onde justifica-se ter mais de um assert por método.

Existe a ferramenta **test smell detector** [link](https://testsmells.github.io/) que detecta 18 test smells.

Testes detectados:
- Assertion Roulette
- Conditional Test Logic
- Constructor Initialization
- Default Test
- Duplicate Assert
- Eager Test:
  - Onde chamamos diversos métodos de uma mesma classe
  - confuso de saber quem é testado
- Empty Test
- Exception Handling
- General Fixture:
  - Uma fixture que contem muitas inicializações.
  - Genérica demais, acaba atrasando os testes.
- Ignored Test
- Lazy Test
- Magic Number Test
- Mystery Guest:
  - Arquivo está sendo criando dentro do teste
  - Viola o FIRST pq ele depende do sistema de arquivos e ele pode não ser deterministico
- Redundant Print
- Redundant Assertion
- Resource Optimism
- Sensitive Equality
- Sleepy Test:
  - Existe um sleep() dentro do teste.
  - Introduz um fator não deterministico.
- Unknown Test
  - Não tem nenhum assert dentro

<details><summary>Descrição completa explicada no site:</summary>


Assertion Roulette
Occurs when a test method has multiple non-documented assertions. Multiple assertion statements in a test method without a descriptive message impacts readability/understandability/maintainability as it’s not possible to understand the reason for the failure of the test.

Detection: A test method contains more than one assertion statement without without an explanation/message (parameter in the assertion method).


Conditional Test Logic
Test methods need to be simple and execute all statements in the production method. Conditions within the test method will alter the behavior of the test and its expected output, and would lead to situations where the test fails to detect defects in the production method since test statements were not executed as a condition was not met. Furthermore, conditional code within a test method negatively impacts the ease of comprehension by developers.

Detection: A test method that contains one or more control statements (i.e if, switch, conditional expression, for, foreach and while statement).


Constructor Initialization
Ideally, the test suite should not have a constructor. Initialization of fields should be in the setUp() method. Developers who are unaware of the purpose of setUp() method would give rise to this smell by defining a constructor for the test suite.

Detection: A test class that contains a constructor declaration.


Default Test
By default Android Studio creates default test classes when a project is created. These classes are meant to serve as an example for developers when wring unit tests and should either be removed or renamed. Having such files in the project will cause developers to start adding test methods into these files, making the default test class a container of all test cases. This also would possibly cause problems when the classes need to be renamed in the future.

Detection: A test class is named either `ExampleUnitTest' or `ExampleInstrumentedTest'.


Duplicate Assert
This smell occurs when a test method tests for the same condition multiple times within the same test method. If the test method needs to test the same condition using different values, a new test method should be utilized; the name of the test method should be an indication of the test being performed. Possible situations that would give rise to this smell include: (1) developers grouping multiple conditions to test a single method; (2) developers performing debugging activities; and (3) an accidental copy-paste of code.

Detection: A test method that contains more than one assertion statement with the same parameters.


Eager Test
Occurs when a test method invokes several methods of the production object. This smell results in difficulties in test comprehension and maintenance.

Detection: A test method contains multiple calls to multiple production methods.


Empty Test
Occurs when a test method does not contain executable statements. Such methods are possibly created for debugging purposes and then forgotten about or contains commented out code. An empty test can be considered problematic and more dangerous than not having a test case at all since JUnit will indicate that the test passes even if there are no executable statements present in the method body. As such, developers introducing behavior-breaking changes into production class, will not be notified of the alternated outcomes as JUnit will report the test as passing.

Detection: A test method that does not contain a single executable statement.


Exception Handling
This smell occurs when a test method explicitly a passing or failing of a test method is dependent on the production method throwing an exception. Developers should utilize JUnit's exception handling to automatically pass/fail the test instead of writing custom exception handling code or throwing an exception.

Detection: A test method that contains either a throw statement or a catch clause.


General Fixture
Occurs when a test case fixture is too general and the test methods only access part of it. A test setup/fixture method that initializes fields that are not accessed by test methods indicates that the fixture is too generalized. A drawback of it being too general is that unnecessary work is being done when a test method is run.

Detection: Not all fields instantiated within the setUp method of a test class are utilized by all test methods in the same test class.


Ignored Test
JUnit 4 provides developers with the ability to suppress test methods from running. However, these ignored test methods result in overhead since they add unnecessary overhead with regards to compilation time, and increases code complexity and comprehension.

Detection: A test method or class that contains the @Ignore annotation.


Lazy Test
Occurs when multiple test methods invoke the same method of the production object.

Detection: Multiple test methods calling the same production method.


Magic Number Test
Occurs when assert statements in a test method contain numeric literals (i.e., magic numbers) as parameters. Magic numbers do not indicate the meaning/purpose of the number. Hence, they should be replaced with constants or variables, thereby providing a descriptive name for the input.

Detection: An assertion method that contains a numeric literal as an argument.


Mystery Guest
Occurs when a test method utilizes external resources (e.g. files, database, etc.). Use of external resources in test methods will result in stability and performance issues. Developers should use mock objects in place of external resources.

Detection: A test method containing object instances of files and databases classes.


Redundant Print
Print statements in unit tests are redundant as unit tests are executed as part of an automated process with little to no human intervention. Print statements are possibly used by developers for traceability and debugging purposes and then forgotten.

Detection: A test method that invokes either the print or println or printf or write method of the System class.


Redundant Assertion
This smell occurs when test methods contain assertion statements that are either always true or always false. This smell is introduced by developers for debugging purposes and then forgotten.

Detection: A test method that contains an assertion statement in which the expected and actual parameters are the same.


Resource Optimism
This smell occurs when a test method makes an optimistic assumption that the external resource (e.g., File), utilized by the test method, exists.

Detection: A test method utilizes an instance of a File class without calling the exists(), isFile() or notExists() methods of the object.


Sensitive Equality
Occurs when the toString method is used within a test method. Test methods verify objects by invoking the default toString() method of the object and comparing the output against an specific string. Changes to the implementation of toString() might result in failure. The correct approach is to implement a custom method within the object to perform this comparison.

Detection: A test method invokes the toString() method of an object.


Sleepy Test
Explicitly causing a thread to sleep can lead to unexpected results as the processing time for a task can differ on different devices. Developers introduce this smell when they need to pause execution of statements in a test method for a certain duration (i.e. simulate an external event) and then continuing with execution.

Detection: A test method that invokes the Thread.sleep() method.


Unknown Test
An assertion statement is used to declare an expected boolean condition for a test method. By examining the assertion statement it is possible to understand the purpose of the test method. However, It is possible for a test method to written sans an assertion statement, in such an instance JUnit will show the test method as passing if the statements within the test method did not result in an exception, when executed. New developers to the project will find it difficult in understanding the purpose of such test methods (more so if the name of the test method is not descriptive enough).

Detection: A test method that does not contain a single assertion statement and @Test(expected) annotation parameter.

</details>



# Code Smells ( ou Bad Smells)

Indicadores de código de baixa qualidade (não cheira bem). Dificíl de manter, entender e modificar

Tipos:
- Código Duplicado
  - Como eliminar: Extract Method, Pull Up Method, Extract Class
  - Tipos:
    - 1: Mesmo código 
    - 2: Variáveis com nomes diferentes
    - 3: Mesmo que o 2, mas com pequenas mudanças de comandos
    - 4: Semanticamento equivalentes, mas com sitaxe diferente
  - % de código duplicado:
    - Todo sistema tem algum código duplicado
- Métodos Longos
  - Como eliminar: Extract Method
- Classes Grandes:
  - Como eliminar: Extract Class
  - Baixa coesao e grande número de campos
  - Dificíl reusar classes grandes
  - God Class: Monopoliza grande parte da inteligência do sistema
  - Code City
- Feature Envy:
  - Métodos que usam muitos métodos de outra classe.
  - Avaliar a possibilidade a mover esse método para lá.
  - Como tratar: Movimentação de método
- Métodos com muitos parametros
  - Facilita teste e utilização
  - Como tratar: Agrupar os parametros ou obte-los diretamente no corpo do método.
- Outros Code Smells:
  - Classes de Dados
  - Obsessão por Tipos Primitivos
  - Comentários
  - Shotgun Surgery
  - Heranças Paralelas
  - Message Chains
    - `pbj.getA().getB().getC().getD().getFinal();`