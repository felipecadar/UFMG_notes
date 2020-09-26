# Roteiro

# Slide 1

Olá, meu nome é Felipe Cadar, eu estou sendo orientado pelo professor Erickson Rangel e vou falar um pouco sobre meu POC II, intitulado "Gaze-based Semantic Hyperlapse"


# Slide 2

Qual é a nossa motivação?

# Slide 3

Graças a avanços tecnológicos em câmeras e dispositivos de armazenamento, e à crescente cultura de compartilhamento de momentos, aumentaram exponencialmente a quantidade de videos em primeira pessoa, também conhecidos como Egocêntricos.

Uma característica desses vídeos é que eles geralmente são longos. A pessoa coloca uma câmera na cabeça, começa a gravar e realiza sua atividade normalmente, seja ela um esporte ou um passeio de bicicleta pela cidade.

O problema desses vídeos é que, por serem longos, ninguém tem paciência para assisti-los depois. Uma forma de resolver o problema da duração é acelerar o vídeo. Porém, por se tratar de um vídeo em primeira pessoa, o vídeo acelerado fica visual instável

# Slide 4

Com isso em mente algumas metodologias mais complexas foram desenvolvidas.

Primeiro veio o Hyperlapse, que acelera o vídeo de forma que os frames selecionados tentavam manter a estabilidade visual.

Mesmo assim, apesar de resolver o problema da instabilidade no vídeo acelerado, tudo fica muito rápido, então os pequenos trechos que eram importantes para quem gravou acabam passando despercebidos.

Então surgiu o Hyperlapse Semântico, que além de produzir um vídeo estável, enfatiza as partes mais importântes, ou semânticas, atribuindo a elas uma velocidade menor, enquanto que o restante é acelerado a uma velocidade maior, de modo que a aceleração global do vídeo se mantenha.


O problema é definir o que é a semântica de um vídeo.

# Slide 5

Na proposta do método, a semântica era fixa e representada pela presença de faces no vídeo. É um bom começo, mas talvez existam mais coisas de interesse no vídeo que não foram cobertas.

# Slide 6

Em vez de definir semantica apenas como face, um outro trabalho permite que o usuário informe, dentre algumas classes de objetos, quais são relevantes para ele.

O problema é que a semântica ainda está limitada às classes disponíveis.

# Slide 7
 
Com o intúito de automatizar o processo, um grupo de autores propos que a semântica seja extraída dos interesses manifestados pelo usuário em redes sociais.

Mas imagine que você gravou o vídeo de um passeio pela cidade para conhecer uma igreja, e nas sua redes sociais você expressa seu amor por carros. Então o Hyperlapse Semântico do seu vídeo vai ignorar a semântica das igrejas e considerar como relevantes apenas os carros que passaram vídeo.

# Slide 8

Para extraír o interesse do usuário no momento que ele gravou o vídeo, foi proposto uma hyperlapse baseado gaze, ou seja, para onde o gravador está olhando durante a gravação. Desta forma podemos saber, com certa precisão, qual é o interesse desse usuário em todos os momento do vídeo.

# Slide 9

Agora, qual é o problema disso?

# Slide 10

É muito difícil conseguir a informação de gaze. Os equipamentos são muito caros e, mesmo que você mesmo faça o seu, ele vai ser desconfortável e difícil de usar, por questões de calibração e pós processamento.

# Slide 11

Então nós queremos um método de hyperlapse que use como semântica o interesse do usuário no momento que ele gravou o vídeo e sem precisar de equipamentos especiais.

Como pretendemos fazer isso?

# Slide 12

Já existem redes neurais que estimam a posição do gaze, mas elas não funcionam bem fora do seu domínio e também não classificam o gaze entre Fixação, quando estamos prestando atençao em algo, e Sacada, que é um movimento do gaze quando estamos procurando algo para fixar.

Dito isso, usaremos uma Rede Neural de Multitarefa para estimar, em conjunto, a **posição do Gaze**, o **tipo do Gaze** e a **relevância do frame**.


# Slide 13

A justificativa para usar esse tipo de rede é que ela não precisa ser muito boa nas duas primeiras tarefas, mas elas vão ajudar a relacionar o gaze com a métrica de relevância do frame durante o treinamento. Então usaremos apenas esse resultado de relevância para fazer o Hyperlapse.


# Slide 14
# Slide 15

Até agora já experimentamos bastante com redes de predição de gaze.

# Slide 16

E desenvolvemos um método de classificação de gaze que funciona bem para dados anotados, mas não para os dados estimados pela rede.

# Slide 17

Como próximo passo

# Slide 18

Devemos propor uma arquitetura e iniciar o treinamento da rede.

# Slide 19

Obrigado!

# Slide 14