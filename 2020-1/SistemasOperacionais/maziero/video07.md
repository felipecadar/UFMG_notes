# Tópicos em gestão de tarefas

## Inversão de prioridades

**Problema**: Uma tarefa de baixa prioridade impede uma de alta prioridade por falta de rescursos compartilhados.

1. Uma tarefa de prioridade baixa adquire o mutex de um recurso
2. Uma tarefa de prioridade alta entra no processador 
3. A tarefa de prioridade alta espera o mutex, mas ele nunca é liberado pois a tarefa de prioriade baixa está parada.

**Solução**: Protocolos de herança de prioridade
- Quando a tarefe de alta prioriade pede o recurso, o processo que tem o recurso herda a prioridade alta e termina rapidamente para liberar o recurso.

