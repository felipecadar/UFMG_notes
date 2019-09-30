# Algebra relacional 

1. Intro
2. Seleção
3. Projeção
4. Sequencia
5. Conjunto
6. Produto Cartesiano
7. Junções

## Intro

### Linguagens de Consulta Relacionais Formais

Duas LCs matemáticas forma base para as implementações:
1. Algebra Relacional : Imperativa 
2. Cálculo Relacional : Declarativa

### Algebra Relacional

Dadas duas relações R1 e R2

Operações básicas 
    - Selection (o) -> Seleciona um sub-conjunto de fileiras da relação
    - Projection (n) -> Deleta colunas indesejadas da relação
    - Cross-product (x) -> Combina R1 e R2
    - Set-diferrence (-) -> Diferença de conjuntos
    - Union (u) -> União de conjuntos

Operações Adicionais
    - Intersect (  )
    - Join (  )
    - Division ( % )
    - Rename ( p )

Exemplos:

Selection:
`< SELECT > (DNO = 4 AND SALARY > 2500) OR (DNO = 5 ) (EMPLOYEE)`

Projection:
`< PROJECT > (DNO, SALARY) (EMPLOYEE)`

Projection:
`< PROJECT > (DNO, SALARY) (EMPLOYEE)`

Considere a relação:

```
Autor (CodAutor, NomeAutor, CodEndereco, CodInst)
    CodEndereco -> Endereco
    CodInst -> Instituicao

Artigo (CodArtigo, Titulo, AnoPublicacao)

AutorArtigo (CodAutor, CodArtigo)
    CodAutor -> Autor
    CodArtigo -> Artigo

Instituicao (CodInst, NomeInst, CodEndereco)
    CodEndereco -> Endereco

Endereco (CodEndereco, Rua, Numero, Bairro, Cidade, Estado, Pais,
Cep)
```

Obter os títulos dos artigos seguidos do nome seus autores:

```
<PROJ> Artigo.Título, Autor.Nome (Artigo <JOIN> AutorArtigo <JOIN> Autor)
```

Obter os nomes dos autores que publicaram artigos em 1998 e 1999 :

```
<PROJ> Autor.Nome <SELECT> (Artigo.AnoPublicacao=1998) (Artigo <JOIN> AutorArtigo <JOIN> Autor)

<INTERSECT>

<PROJ> Autor.Nome <SELECT> (Artigo.AnoPublicacao=1999) (Artigo <JOIN> AutorArtigo <JOIN> Autor)

```