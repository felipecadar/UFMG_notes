# Introdução


- "Primeira Lei": Conseguimos fazer análises que levam em conta a posição das coisas.

- Site:
  - [https://homepages.dcc.ufmg.br/~clodoveu/DocuWiki/doku.php?id=bdg](https://homepages.dcc.ufmg.br/~clodoveu/DocuWiki/doku.php?id=bdg)

- Playlist:
  - [https://www.youtube.com/playlist?list=PLj18xoEmBR9me-FiiECUOUxdC8CcpimUm](https://www.youtube.com/playlist?list=PLj18xoEmBR9me-FiiECUOUxdC8CcpimUm)

- Livro:
  - Casanova, M. A., Câmara, G., Davis Jr., C. A., Vinhas, L., Queiroz, G. R. (Eds.) Bancos de Dados Geográficos. Curitiba (PR): EspaçoGeo, 2005, p. 93-146. In Portuguese. [PDFs (e-book)](http://www.dpi.inpe.br/livros/bdados/)


## Como baixar o livro

```bash
#!/usr/bin/env bash

if ! command -v wget &>/dev/null; then
  printf "wget não encontrado!\n"
  exit 1
fi

prefix="http://www.dpi.inpe.br/livros/bdados/cap"

for cnt in {1..14}; do
  [ ! -f ./$prefix$cnt.pdf ] &&
    wget $prefix$cnt.pdf     ||
    printf "Capítulo %s encontrado, ignorando...\n" $cnt
done

# Juntando os capitulos
if [ -f livro.pdf ]; then printf "Arquivo livro.pdf já existe!\n"; exit 0; fi
if ! command -v pdfunite &>/dev/null; then
  printf "poppler não encontrado! Instale para unir os PDFs\n"
  exit 1
fi
printf "Juntando os capitulos...\n"
pdfunite cap{1..14}.pdf livro.pdf
printf "Pronto! Para remover os capitulos individuais:\n  rm cap*.pdf\n"
```

