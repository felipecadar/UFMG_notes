4. Suponha uma rede social como o Facebook. (1) Escreva um conjunto de cinco histórias para essa rede, assumindo o papel de um usuário típico; (2) Pense agora em mais um papel de usuário e escreva pelo menos duas histórias para ele.

(1)
```
1. Como um usuário típico, eu gostaria de fazer postagens na timeline
2. Como um usuário típico, eu gostaria de curtir postagens na timeline
3. Como um usuário típico, eu gostaria de compartilhar postagens na timeline
4. Como um usuário típico, eu gostaria de comentar em postagens na timeline
5. Como um usuário típico, eu gostaria de pesquisar por amigos
```

(2)
```
1. Como um desenvolvedor, eu gostaria de usar o sistema de autenticação do facebook
2. Como um desenvolvedor, eu gostaria de usar fazer postagens por meio de uma API
```
 ____________________

9. O seguinte caso de uso possui apenas o fluxo normal. Escreva então algumas extensões para ele.

```
Comprar Livro
Ator: Usuário da loja virtual

Fluxo normal:

1. Usuário pesquisa catálogo de livros
2. Usuário seleciona livros e coloca no carrinho de compra
3. Usuário decide fechar a compra
4. Usuário seleciona endereço de entrega
5. Usuário seleciona tipo de entrega
6. Usuário seleciona modo de pagamento
7. Usuário confirma pedido
```

```
Extensões:
1a. Se o livro não exitir, sugerir títulos semelhantes
2a. Se o livro não estiver no estoque, perguntar o cliente se ele quer ser avisado
4a. Se a entrega estiver indisponível, pedir um novo endereço
5a. Se for uma entrega agendada, perguntar a data de entrega
5b. Se for presente, cobrar o embrulho.
```


12. O artigo Failures to be celebrated: an analysis of major pivots of software startups ([link](https://arxiv.org/abs/1710.04037)) apresenta uma discussão sobre quase 50 casos reais de pivôs em startups da área de software. Na Seção 2.3, o artigo apresenta uma classificação de dez tipos de pivô comuns nessas startups. Leia essa parte do artigo, liste pelo menos cinco tipos de pivôs e faça uma breve descrição de cada um deles.

- Zoom-in Pivot: Quando uma das features do MVP é muito promissora e vira um produto por sí só.
- Technology Pivot: Entregar o mesmo produto em outra plataforma (mudar de IOS pra Android)
- Platform Pivot: Mudar de aplicação para a plataforma que possibilita a aplicação ou vice versa. Como um ecommerce que vira uma plataforma de hostear ecommerce.
- Customer Need Pivot: Como resultado de conhecer bem os clientes, mudamos o MVP para um problema relacionado mais interessante para os clientes.
- Customer Segment Pivot: Oferecer o mesmo produto para outro segmento de clientes.
_________________________________

13.  Quando começou, a EasyTaxi — a empresa brasileira de aplicativos para solicitação de táxis — construiu um MVP que usava um software muito simples e uma parte operacional realizada de forma manual. Pesquise na Internet sobre esse MVP (basta usar as palavras EasyTaxi e MVP) e faça uma descrição do mesmo.

Era um sistema quase sem Backend, sempre que um cliente requisitava um taxi, os donos recebiam um email e ligavam eles mesmos para a cooperativa pedindo um taxi.

A segunda versão não era um MVP real pois demorou muito a sair e possuia muitas features que não eram essenciais.

Eles tentaram focar nas cooperativas, mas elas não gostaram do sistema. Então a EasyTaxi pivotou para focar nos clientes.

Eles tambem sofreram por smartphones não serem populares na época, então compraram 1000 smartphones com plano 3G e distribuíram para os taxistas da cidade do Rio de Janeiro e conseguiram validar o app para motoristas.

_________________________________

15. Suponha que você seja responsável por um sistema de comércio eletrônico. Suponha que na versão atual desse sistema (versão A) a mensagem do carrinho de compra seja Adicionar ao Carrinho. Suponha que você pretenda fazer um teste A/B testando a mensagem alternativa Compre Já, a qual vai corresponder à versão B do teste.

(1) Qual seria a métrica usada como taxa de conversão nesse teste?

(2) Supondo que no sistema original a taxa de conversão seja de 5% e que você deseja avaliar um ganho de 1% com a mensagem da versão B, qual seria o tamanho da amostra que deveria testar em cada uma das versões? Para responder, use uma calculadora de tamanho de amostras de testes A/B, como aquela que citamos na Seção 3.6.


(1) A métrica seria a porcentagem de pessoas que clicaria no botao e a porcentagem que concluiriam a compra
(2) 4,700,000