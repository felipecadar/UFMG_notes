# Código Limpo: legibilidade, comentários e formatação

**Legibilidade**

- Usar nomes descritivos e pronunciáveis.
- Usar nomes buscáveis.

**Comentários**

- Um bom comentário compensa a falta de expressão no código.
- Código comentado é válido, mas não pode ir para a produção.

**Formatação**

- Formatação Vertical
  - Iniciamos um arquivo com um nome simples e explicativo, no topo temos as funções de alto nível e mais abaixo funções com mais detalhes.
- Separação de Conceitos
  - Agrupar linhas de um mesmo fluxo
- Afinidade Conceitual
  - Funções proximas entre si pois são parecidas
- Formatação horizontal
  - Quao comprida uma linha deve ser (20 a 60)
- Identação
  - Cada nível representa um escopo


# Código Limpo: funções

- Função deve ser pequena
  - Idealmente ifs, elses, whiles devem ter uma linha
- Função deve realizar apenas uma tarefa
  - Switches são perigosos pois podem crescer com o tempo se violarem o principio open closed e são facilmente duplicados.
  - Uma fábrica abstrata é uma boa solução para usar melhor os switches.
-  Usar nomes descritivos e consistentes
-  Quanto menos parametros melhor.
-  Evitar funções que realizam efeitos escondidos, ou efeitos colaterais.
-  Evitar duplicação.

# Código Limpo: código externo e testes

- Código externo: Libs ou código de outros times.
  - Produtores querem interfaces que funcionem em todos os ambientes, mas os Usuários querem uma interface mais específica.
  - É comum encapsular os códigos externos para concentrar um ponto de mudança caso necessário.
  - Quebra de contrato de APIs são mais comum do que imaginamos.
- Teste limpo: os mesmos motivos que tornam um código qualquer limpo.
  - Evitar detalhes desnecessários
  - Evitar código complexo
  - Evitar vários asserts (priorizar apenas um)
  - Apenas um conceito por teste
  - Seguem o princípio FIRST (Fast Independent Repeatable Self-Validating Timely)

# Código Limpo: Classes

- Pequenas
- Única responsabilidade
  - Apenas uma razão para ser alterada
  

- Classes com baixa coesao devem ser divididas em classes menores, e mais coesas.
- Quebrar métodos longos tambem podem gerar classes coesas