# Teste de Integração e Sistema

# Outros tipos de teste

**Técnicas de Teste**
- Caixa Preta: testes escritos com base apenas na interface do sistema sob testes
  - Testes funcionais
- Caixa Branca: considera informações sobre o código e a estrutura so sistema sob teste
  - Testes estruturais


**Testes de aceitação**: Realizado pelo cliente em uma sessão manual de uso. Determina se o cliente validou o sistema ou não. Os outros testes (anteriores) são de verificação.

**Teste Alfa**: Pequeno grupo de usuários selecionados e em ambiente controlado. Acontece na presença dos desenvolvedores.
**Teste Beta**: Maior, sem a presença dos devs e em ambientes não controlados. Uma versao de marketing tambem.

**Testes de Requisitos não funcionais**:
- Teste de desempenho: Verifica o comportamento do sistema sobre carga.
- Teste de Usabilidade: Envolve usuários reais fazendo observações sobre a UI
- Teste de Falhas: Simula eventos anormais em um sistema

**Teste de Regressão**: Ocorre sempre que o sistema é modificado ou novo módulo é adicionado. Garante que não introduzimos comportamentos inesperados. xUnit + CI

**Seleção de Dados de Teste**: Como avaliar quais inputs usaremos nos testes
- Classe de Equivalencia: Para cada conjuntos de valores, usar apenas um desses valores, já que eles são equivalentes e apresentariam o mesmo comportamento.
- Valor Limite: Testar com os limites entre os conjuntos de valores para buscar bugs do tratamento inadequado desses valores de fronteira