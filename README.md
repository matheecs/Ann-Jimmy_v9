# Albums

## convert `heic` to `jpg`

```shell
magick mogrify -monitor -format jpg *.heic
magick mogrify -monitor -format jpg *.HEIC
```

## rename images

```shell
python rename_tools.py
```

## code gen

```shell
python read_imgs_code_gen_tex.py
```

## merge images

OmniGraffle

## LaTeX IDE

<https://www.texstudio.org/>

## build

```shell
latexmk -xelatex root.tex
latexmk -c
```

## reduce PDF size

```shell
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=small.pdf root.pdf
```

<https://tex.stackexchange.com/questions/14429/pdftex-reduce-pdf-size-reduce-image-quality>
