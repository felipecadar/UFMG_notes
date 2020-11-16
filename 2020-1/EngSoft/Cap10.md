# DevOps

Três práticas do DevOps
1. Controle de Versões
2. Integração Contínua
3. Deployment Contínuo

# Intro


**Antigamente**:
- **Departamento de Sistemas (ou Desenvolvimento)**: formado por desenvolvedores programadores, analistas, arquitetos, etc.

- **Departamento de Suporte (ou Operações)**: alocados os administradores de rede administradores de bancos de dados, técnicos de suporte, técnicos de infraestrutura, etc.


**Problemas**:
- Falta de hardware
- problema de desempenho
- incompatibilidade de banco de dados
- vunerabilidade de segurança


**DevOps**: um movimento que visa unificar as culturas de desenvolvimento (Dev) e de operação (Ops), visando permitir a implantação mais rápida e ágil de um sistema. DevOps advoga a automatização de todos os passos necessários para colocar um sistema em produção e monitorar o seu correto funcionamento.

Quando migra-se para uma cultura de DevOps, os times ágeis podem incluir um profissional de operações, que participará dos trabalhos em tempo parcial ou mesmo em tempo integral.

**Princípios**
- Crie um processo repetível e confiável para entrega de software.
  -  Esse princípio é o mais importante deles. Colocar um software em produção deve ser tão simples como apertar um botão.
- Automatize tudo que for possível.
  - Advoga-se que todos os passos para entrega de um software devem ser automáticos, incluindo seu build, a execução dos testes, a configuração e ativação dos servidores e da rede, a carga do banco de dados, etc. 
- Mantenha tudo em um sistema de controle de versões.
- Se um passo causa dor, execute-o com mais frequência e o quanto antes.
  - A ideia é antecipar os problemas, antes que eles se acumulem e as soluções fiquem complicadas. 
  - O exemplo clássico é o de Integração Contínua. Se um desenvolvedor passa muito tempo trabalhando de forma isolada, ele e o seu time podem depois ter uma grande dor de cabeça para integrar o código. Logo, como integração pode causar dor, a recomendação consiste em integrar código novo com mais frequência e o quanto antes, se possível, diariamente. 
- Concluído significa pronto para entrega. 
  - Esse princípio defende então que concluído, em projetos de software, deve ter uma semântica clara, isto é: 100% pronto para entrar em produção.
- Todos são responsáveis pela entrega do software. 
  - Ou seja, não admite-se mais que os times de desenvolvimento e de operações trabalham em silos independentes e troquem informações apenas na véspera de uma implantação.

# Controle de versões

Sistema de Controle de Versões
- repositório para armazenar a versão mais recente do código
- permite que se recupere versões mais antigas de qualquer arquivo

DVCS tem as seguintes vantagens:
- Pode-se trabalhar e gerenciar versões de forma offline
- Pode-se realizar commits com mais frequência, incluindo commits com implementações parciais, pois eles não vão chegar imediatamente até o repositório central.
- Commits são executados em menos tempo, isto é, eles são operações mais rápidas e leves. O motivo é que eles são realizados no repositório local de cada máquina.
- A sincronização não precisa ser sempre com o repositório central. Em vez disso, dois nodos podem também sincronizar os seus repositórios.

## Multirepos vs Monorepos

Vantagens de monorepos:
- Como existe um único repositório, não há dúvida sobre qual repositório possui a versão mais atualizada de um arquivo.
- Monorepos incentivam o reúso e compartilhamento de código.
- Mudanças são sempre atômicas. Com multirepos, dois commits podem ser necessários para implementar uma única mudança, caso ela afete dois sistemas. 
- Facilita a execução de refactorings em larga escala. 

Por outro lado, monorepos requerem ferramentas para navegar em grandes bases de código.

# Integração Contínua

Existe um branch principal, conhecido pelo nome de master (quando usa-se Git) ou trunk (quando usa-se outros sistemas, como svn). Além do branch principal, os usuários podem criar seus próprios branches. Por exemplo, antes de implementar uma nova funcionalidade, pode ser comum criar um branch para conter o seu código. Tais branches são chamados de branches de funcionalidades (feature branches)

Quando a implementação da nova funcionalidade terminar, o código do branch deve ser copiado de volta para o master, por meio de um comando do sistema de controle de versões chamado merge. 

Os termos integration hell ou merge hell são usados para descrever os problemas que ocorrem durante a integração de branches de funcionalidades.

## O que é Integração Contínua?

Você deve integrar e testar o seu código em intervalos menores do que algumas horas. 

## Boas Práticas para Uso de CI

Quando usa-se CI, o master é constantemente atualizado com código novo. 
- Build Automatizado: Build é o nome usado para designar a compilação de todos os arquivos de um sistema, até a geração de uma versão executável. 
- Testes Automatizados: Além de garantir que o sistema compila sem erros após cada novo commit, é importante garantir também que ele continua com o comportamento esperado. 
- Servidores de Integração Contínua: um desenvolvedor somente deve avançar para uma próxima tarefa de programação após receber o resultado do servidor de CI

**Desenvolvimento Baseado no Trunk**

Trunk based development ou TBD é desenvolver sem branchs.

**Programação em Pares**

## Quando não usar CI?

Os proponentes de CI definem um limite rígido para integrações no master: pelo menos uma integração por dia por desenvolvedor. No entanto, dependendo da organização, do domínio do sistema (que pode ser um sistema crítico) e do perfil dos desenvolvedores (que podem ser iniciantes), pode ser difícil seguir esse limite.

CI também não é compatível com projetos de código livre. Na maioria das vezes, os desenvolvedores desses projetos são voluntários e não têm disponibilidade para trabalhar diariamente no seu código.

# Deployment Contínuo (Continuous Deployment ou CD)

Quando usa-se CD, todo novo commit que chega no master entra rapidamente em produção, em questões de horas, por exemplo. 

**vantagens**
- CD reduz o tempo de entrega de novas funcionalidades.
- CD torna novas releases (ou implantações) um não-evento.
- Além de reduzir o stress causado por deadlines, CD ajuda a manter os desenvolvedores motivados, pois eles não ficam meses trabalhando sem receber feedback.
- Em linha com o item anterior, CD favorece experimentação e um estilo de desenvolvimento orientado por dados e feedback dos usuários.

##  Entrega Contínua (Continuous Delivery)

A ideia é simples: quando se usa entrega contínua, todo commit pode entrar em produção imediatamente. Ou seja, os desenvolvedores devem programar como se isso fosse acontecer. No entanto, existe uma autoridade externa — um gerente de projetos ou de releases, por exemplo — que toma a decisão sobre quando os commits, de fato, serão liberados para os usuários finais. Inclusive forças de mercado ou de estratégia da empresa podem influenciar nessa decisão.

- **Deployment** é o processo de liberar uma nova versão de um sistema para seus usuários.
- **Delivery** é o processo de liberar uma nova versão de um sistema para ser objeto de deployment.

## Feature Flags

Evitar que um código não finalizado entre em produção.

```python
featureX = false;
...
if (featureX):
   "aqui tem código incompleto de X"
...
if (featureX):
   "mais código incompleto de X"
```

Para facilitar a execução de releases canários e testes A/B, pode-se usar uma estrutura de dados para armazenar os flags e seu estado (ligado ou desligado). 