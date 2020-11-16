# Estruturas do S.O.

#### Modo de Operação Dual

Dois modos de execução: Monitor ou Usuário
Sempre que uma interrupção(hardware)/trap(software) acontece, chaveia para o modo monitor e a passagem para modo usuário é feita por instrução... Isso é um problema pois qualquer programa conseguia ter privilégios de monitor.

#### Passagem de parâmetros

Para fazer chamadas de sistema precisamos passar alguns parametros. Então podemos usar registradores ou, para ser mais avançado, tabelas.


#### Boot

Responsavel por fazer os primeiros processos, que vão iniciar o filesystem e iniar o pc
Nele é rodado a BIOS (bootstrap loader), que é pré-armazenada na ROM
O loader deve reconhecer minimamente os dispositivos de armazenamento essenciais. Em geral lê o primeiro bloco do disco e executa-o.
Com o passar do tempo esse loader foi expandido e ficando mais complexos.

BIOS -> Le um cara bem simples -> que lê um loader mais complexo -> que monta o filesystem.
