<h1>Séries Temporais 02</h1>

# 1. ThemeRiver

Solução encontrada para substituir o gráfico de barras empilhadas. Mais fácil de compara sessões daas barras durante o tempo.

**pontos positivos**:
1. mesmo que uma barra suma e reapareça, é fácil acompanha-la
**limitação**:
1. número de termos limitado por problemas com cores


# 2. Baby Names

Gráfico de áreas empilhadas

**Mantra da visualização:** Overview first, zoom and filter, details on demand.

# 3. Stacked Graphs

Tipo gráfico de áreas empilhadas, mas tenta deixar as curvas simétricas e minimiza as inclinações em cada curva, priorizando as camadas mais espeças.

Não tem aspecto matemático, é mais organica e atraente visualmente.

Tentaram padronizar inclinações dos gráficos para melhorar a diferenciação entre camadas. Melhora da silhueta da curva. 

Temos ordenação das camadas, rótudos e cores que representam outra dimenção do gráfico.

Otimizam as posições dos labels com algoritmo genético

Ordenação de camadas de forma a balancear o gráfico.