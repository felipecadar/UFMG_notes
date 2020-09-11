# Introdução - Arquiteturas de Sistemas Operacionais

Arquiteturas são formas como o sistema operacional é organizado. Como devemos juntar todos os módulos de um SO considerando alguns aspectos:
- Isolamento do núcleo: modo Nucleo e modo Usuário.
- Modularização
- Desempenho
- Segurança

## Sistemas monolíticos

O kernel é grande e possui tudo dentro dele e ele executa em modo privilegiado.

**Vantagens**:
- Todo está muito proximo e de fácil acesso.
- Compacto no sentido que temos um bloco só de código.
- Bom desempenho.

**Desvantagens**:
- Complexidade: Muitas funcionalidades.
- Fragilidade: Se houver um bug em um módulo, ele pode derrubar todo o SO.

## Sistema micronúcleo

Tentativa de fazer um kernel com apenas o necessário.

O núcleo implementa (**Mecanismos**):
1. Espaços de memória protegidos
2. Atividades (thread, ...)
3. Comunicação entre atividades

Ficam fora do núcleo (**Políticas**):
1. Políticas de escalonamento
2. Poíticas de uso de memória
3. Sistemas de arquivos
4. Protocolos de rede

**Vantagens**:
- Estabilidade
- Modularidade

**Desvantagens**:
- Baixo desempenho

Exemplo: Minix 3 

## Sistemas de camadas

Organizar camadas de abstrações

Caracteristicas gerais:
- Camada inderior: iterface com o hardware.
- Cadadas intermediárias: Abstrações e gerência.
- Camada Supetior: define as chamadas de sistema.

Existe um problema nas camadas intermediárias pois são componentes interdependentes, então é difícil dizer quem fica acima de quem.

## Sistemas híbridos

Eles misturam características do 3 tipos de arquiteturas e, atualmente, é usada pela maioria dos sistemas.

## Máquinas virtuais

Simular no software um sistema sobre outro sistema

Temos 3 partes:
- **Host**: Sistema anfitrião que contem os recursos reais.
- **Hypervisor**: Camada de software que recria um sistema computacional virtual.
- **Guest**: O sistema hospedeiro.

**Hypervisors** podem ser classificados em famílias:

1. Quanto ao ambiente virtual provido:
   - HV de aplicação: Suporta aplicação convidada (Java, C#)
   - HV de sistema: Suporta SOs convidados (VMWare, VirtualBox, QEMU)
2. Quanto ao suporte de execução:
   - HV nativo: executa diretamente sobre o hardware (Xen)
   - HV convidade: executa soibre um SO anfitrião. (VirtualBox, QEMU)

**Contêiners**: Ao invés de simular um sistema operacional completo, dividimos o espaço do usuário em domínios isolados. Cada domínio possui seus próprios usuários, procesos, semáforos, áreias de memórias... Com isso todos os containers continuam executando no mesmo núcleo, sem divisão de recursos. Interações e migrações entre domínios são proibidas.

Tem um custo de baixíssimo, então roda praticamente na mesma velocidade do OS, mass todos executam no mesmo núcleo.

