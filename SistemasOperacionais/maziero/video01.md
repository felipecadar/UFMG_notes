# Introdução - Conceitos básicos

## Definição

Camada de software que opera entre o hardware e os programas e aplicativos

Ele faz a **abstração** de recursos para prover interfaces simples e homogêneas.

Ele **gerencia** o uso dos recursos pelos programas
- Permitir o uso compartilhado 
- Sequenciar acesso a recursos
- impedir ataques de negação de serviço

Areas de gerência:
- **Processador**: Executar tarefas dos usuários
- **Memória**: fornecer areas de memória
- **Dispositivos**: configurar e criar abstrações
- **Arquivos**: Criar e manter arquivos e diretórios
- **Proteção**: Definir e garantir regras de acesso aos recursos

Outras áreas: Interface gráfica, suporte de rede, multimídia, energia, localização, etc...

Tipo de sistemas operacionais:
- Batch: executa tarefas sequenciais
- De rede: acessa recursos em outros computadores
- Distribuído: acessa recursos de forma transparente
  - Mais abstração do que sistemas de rede
- Multiusuário: cada recurso tem um "dono" e regras de acesso
- Servidor: gestão eficiente de grandes volumes de recursos
- Desktop: Intrerface gráfica e suporte a interatividade
- Móvel: gestão de energia, conectividade e sensores
- Embarcado: hardware com poucos recursos e energia
- Tempo real: tem comportamento temporal previsível
  - soft real-time
  - hard real-time

