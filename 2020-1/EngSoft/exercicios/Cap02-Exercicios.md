# Exercícios Cap. 2

#### 1
Abertos, de modo que a cada iteração o contrato é renovado e as especificações dos sistema atualizadas.

#### 2
Scrum não é só para projeto de software, logo não define práticas de programação. Scrum define um "Processo" mais rígido que XP

#### 3
Os times cross-funcionais não dependem de membros externos. Todos os especialistas, dono da empresa e Scrum Master fazem parte do time. Além disso são auto-organizáveis pois decidem quem vai assumir cada tarefa (história) e como ela vai ser implementada.

#### 4
O backlog possui um ranking de histórias, então quanto mais no topo maior a prioridade de implementação.

#### 5
Os story points são uma unidade de medida para estimar a duração do desenvolvimento de uma história. Ela serve também para medir a velocidade de um time, com o número de story points em cada iteração.

#### 6
O sprint review serve para aprensentar os resultados do Sprint, nesse evento todo o time está presente. A retrospectiva não serve para apresentar resultados, mas para aprimorar o método refletindo sobre pontos de melhora que foram identificados durante a iteração.

#### 7
Sim, apenas o PO pode fazer isso. Ele deve cancelar o sprint quando o Sprint Goal fica obsoleto.

#### 8

Aguardando a triagem

- O usuário deve conseguir cadastrar um paciente para ser chamado para a triagem. Esse sistema deve possuir uma ordem de prioridade para acelerar casos de urgencia ou prioritários.


Divisão de tarefas:
- [FRONT] Tela de cadastro de paciente
- [BACK] Endpoint da API para receber um paciente e adicionar no BD
- [BACK] Sistema prioridade de filas
- [FRONT] Tela que mostra a fila e o proximo paciente a ser chamado
- [FRONT] Tela para requisitar o próximo paciete da fila
- [BACK] Endpoint da API para requisitar o próximo paciente da fila
- [FRONT] Tela para remover um paciente da fila
- [BACK] Endpoint da API para remover um paciente da fila

##### 9

Não, pois os ponto crescem exponencialmente, então se um time faz uma tarefa de muitos pontos e o primeiro time faz várias tarefas de poucos pontos, a escala de produção não é linear entre os dois times.

