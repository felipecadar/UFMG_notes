# Manutenção de Software

- Lida com mudanças de código e documentação depois da entrega do software ao cliente.
- Representa até 90% dos custos.

## Manutenibilidade 

- Facilidade de manutenção de um sistema
- Difícil de quantificar
- Existem algumas métricas:
  - Métricas CKL
    - Produndidade de Herança
    - Número de filhos
    - ....

## Desenvolvimento x Manutenção

Adicionar uma nova funcionalidade durante o desenvolvimento é teoricamente mais fácil que durante a manuntenção. Na manutenção devemos respeitar certos parâmetros e restrições existentes.

## Razões para manutenção de software

Se um sistema é utilizado ele nunca está finalizado pois precisa evoluir:
- Adicionar funcionalidades
- Corrigir bugs
- Melhorar design
- Refatoração
- ...

## Categorias de manutenção

- Requisição de Modificação
  - Correção
    - **1** Corretiva
    - **2** Preventiva
  - Melhoria
    - **3** Adaptativa
    - **4** Perfectiva

Manutenção corretiva e evolutiva são mais visíveis para o usuário e trazem mais valor direto ao usuário. Manutenção preventiva e adaptativa trazem valor indireto.

### Manutenção Corretiva

- Modificações para corrigir defeitos
- Pode gerar aumento de complexidade o outros efeitos cascatas

### Manutenção Preventivas

- Para previnir potenciais problemas no futuro
- Lida com deterioramento de estruturas
- Ex: Otimização, Refatoração e atualização de documentação

### Manutenção Adaptativa

- Manter o software usável devido a alterações no ambiente externo
- Atualizar bibliotecas, hardware, etc...

### Manutenção Perfectiva (ou Evolutiva)

- Fornece melhorias aos usuários finais
- Expande os requisitos do sistema
- Quando o software se torna útil, os usuátios solicitam melhoras além do escopo inicial

## Relacionamento entre as Manutenções

- Uma adaptativa pode introduzir erros e ser seguida de uma corretiva
- Uma evolutiva pode requerer refatoração, sendo seguida de uma preventiva

