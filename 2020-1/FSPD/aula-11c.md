# Consistência eventual

Aquela consistencia onde a ordem dos eventos podem variar de um observador para o outro, mas dado tempo suficiente todas as replicas vão convergir para um mesmo estado.

Exemplo: chaces na Web

Essa consistência fica mais complicada com:
1. Mobilidade de clientes:
   1. Se o cliente mudar de réplica durante a operação, pode ser que a segunda réplica não esteja extamente igual. O desafio é manter a visão.
2. Serviços que exigem dados de várias fintes
   1. Podemos juntar dados de versões diferentes e pode demorar para que ele chegem ao mesmo estado
3. Situações que combinam visões de vários clientes

Anomalias: Dados podem estar temporariamente inconsistentes, então podemos observar comportamentos inesperados. Pode ser causado por comunicação externa que não sincroniza as informações.

Solucionando conflitos:
1. Usar apenas opeções comutativas: Muitor raro
2. Definir ordem total: Muito difícil e perde o princípio da consistência eventual
3. Sinalizar para o usuário (Dropbox)
4. Resolver baseado na semântica da aplicação 
5. Desfazer tudo (rollback) e seguir nova ordem: Alguns sistemas de arquivo trabalham dessa forma

