# Organização de sistemas distribuídos

Sistemas muito complexos precisam ser divididos em elementos menores

Abstrações:
- Camadas
- Objetos

## Camadas

O Processamento e dividido em camadas de dorma que a camada mais superior tem o maior nivel de abstração.

**Camada D**
```Python
def processa_texto(t):
    parags = quebra_texto_em_paragrafos(t)
    for p in parags:
        camadaC.processa_paragrafo()
```

**Camada C**
```Python
def processa_paragrafo(p):
    sents = quebra_paragrafo_em_sentencas(p)
    for s in sents:
        camadaB.processa_sentenca(s)
```

**Camada B**
```Python
def processa_sentenca(s):
    pals = quebra_sentenca_em_palavras(s)
    for p in pals:
        print(p)
```

Variantes:
- Podemos ter casos também que algumas camadas intermediárias são opcionais
- Podemos ter também casos que camadas mais abaixo chamam procedimentos de camadas mais acima (upcall)

## Sistema Orientados a Objetos

Ao invés de camadas, as funcionalidades são encapsuladas em objetos (serviços) e eles se comportam mais como um grafo.


## Sistema orientado a eventos (publish/subscribe)

Ao invés de se preocupar com qual objeto específico vai fazer a tarefa, apenas disparamos um evento "preciso que essa função seja executada" e quem estiver escutando por eventos pode executa-la.

O sistema provê o barramento de comunicação.
(mais detalhes nas próximas aulas)

# Arquiteturas distribuídas

Temos dois tipos:
1. Cliente/Servidor
2. Par-a-par

