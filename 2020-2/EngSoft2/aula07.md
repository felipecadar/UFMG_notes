# Code Smells
 
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