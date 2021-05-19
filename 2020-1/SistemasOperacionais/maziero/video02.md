# Introdução - Estrutura de um SO


O Sistema operacional trabalha em nível de software e possui uma divisão entre **Sistema** e **Usuário**. Essa divisão muda o modo de operação do SO.

No **Sistema** temos:
1. Núcleo
   1. Gerência de tarefas
   2. Gerência de proteção
   3. Gerência de arquivos
   4. Gerência de memória
   5. Protocolos de rede
   6. Gerência de energia
2. Código de inicialização: Carrega e configura todo o resto do núcleo
3. Driver de dispositivos: Conversa com os controladores de hardware

No **Usuário** temos:
1. Programas utilitários: Programas que auxiliam o usuário a utilizar o restante do sistema.

Uma parte importante da estrutura de um SO é separar **políticas** de **mecanismos**

**Política**: Tomar decisões de alto nível. Decidir a quantidade de um recurso para cada aplicação.

**Mecanismo**: Implementação das política. Como iniciar um processo, como reservar uma área da memória.

As políticas devem ser independentes dos mecanismos e os mecanismos devem ser genéricos para várias políticas e para suportar mudança nas políticas.


**Arquitetura de um computador**: Usamos barramentos para a comunicação entre os dispositivos. Cada dispositivo tem um endereço

**Desvio de execução**: Existe um mecanismo de hardware a desviar a execução do procesador em caso de eventos. Um pulso é enviado a um dos pinos do processador, então o processador para o que estiver fazendo, passa a executar uma rotina em um endereço já definido e depois volta a execução da tarefa que foi pausada. Temos 3 eventos:
- **Interrupção**: Evento externo. Gerada por um periférico, como teclado ou controlador de rede.
- **Exceção**: Evento interno. Gerado por, por exemplo, erro numérico
- **Trap**: Quando um programa pede para gerar um desvio.


**Níveis de provilégio**: Operações da CPU são gerenciadas por dois flags. Eles podem valer:
- 00: Núcleo do SO
  - O código pode fazer o que quiser. Ele é dono da máquina e pode executar qualquer instrução.
  - Usado pelo Kernel e pelos Drivers
- 01: não usado
- 10: não usado
- 11: Aplicações
  - Não pode executar todas as instruções
  - Se houver uma tentativa de acessar instruções proibidas, são geradas exeções.

Os outros níveis normalmente são usados em ambientes de virtualização.

**Chamadas de sistema**: Forma das aplicações de pedir serviços para o kernel. Mas como um programa consegue executar uma função que está fora da sua área de memória? Ele usa interrupções para desviar a rotina para o endereçoo do serviço oferecido pelo kernel e depois retornar a sua área de memória.

Conjuntos de chamadas de sistema:
- **Processos**: Criar, carregar código, terminal, esperar...
- **Memória**: Alocal/liberar/modificar áreas de memória.
- **Arquivos**: Criar, remover, abrir, fechar, ler, escrever.
- **Comunicação**: Criar/destruir canais, receber/enviar dados.
- **Dispositivos**: Ler/mudar configs, ler/escrever dados.
- **Sistema**: ler/mudar data e hora, desligfar o sistema...

Cada SO define seu próprio conjunto de *syscalls*, as OS API.