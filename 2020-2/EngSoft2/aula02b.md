# Reengenharia de Software

## Leis de Lehman

1. **Mudança contínua**: deve ser continuamente adaptado, senão torna-se menos satisfatório
2. **Complexidade Crescente**: se nenhuma medida for tomada, a complexidade continuará a crescer
3. **Crescimento Contínuo**: deve ter funcionalidades ampliadas para manter a satisfação dos seus usuários
4. **Declínio de qualidade**: ele se deprecia se não receber as mudanças necessárias

## Reengenharia de Software

Entra para reconstruir um sistema que precisa de uma melhora de desempenho, melhor manutenabilidade, segurança, documentação, etc...

Geralmente é aplicada em sistemas legados. É bem maior que a manutenção de software.

## Software Legado

Ele é valioso para a empresa mas usa tecnologias ultrapassadas

## Quando aplicar a reengenharia

- Documentação obsoleta ou não documentado
- Desenvolvedores principais deixaram a empresa
- Conhecimento limitado do sistema (mesmo caso anterior)
- Muito tempo gasto com pequenas mudanças
- Bugs frequentes
- Problemas de manutenção (efeito cascata)

## Engenharia x Reengenharia

- **Engenharia**:
    1. Especificação
    2. Projeto e implementação
    3. Novo Sistema
- **Reengenharia**
    1. Sistema de software existente
    2. Compreensão e transformação
    3. Sistema de reengenharia

## Engenharia Reversa x Reengenharia

Engenharia Reversa trata mais do entendimento do sistema para realizar uma função. A reengenharia envolve alteração e reestruturação. Podemos ver a engenharia reversa como um dos passos da reengenharia.


## Processo de Reegenharia

1. Análise de Inventário: 
   - Os sistemas vão ser selecionados e priorizados
2. Reestruturação de Documentação
   - Sistemas legados geralmente tem documentação fraca
3. Engenharia Reversa
   - Extrair informação do código para facilitar o entendimento
   - Gerar diagramas pode ser útil
4. Reestruturação
   - Modifica o código ou dados, mas não altera a arquitetura
5. Engenharia Avante
   - Recuperar o projeto e continuar a melhorar a qualidade do sistema e adicionar funcionalidades, resultando em uma nova configuração do sistema.

