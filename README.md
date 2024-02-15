# DIY Albums

## usage

1. rename images

   ```shell
   python rename_tools.py
   ```

2. code gen

   ```shell
   python read_imgs_code_gen_tex.py
   ```

3. build

   ```shell
   latexmk -xelatex root.tex
   latexmk -c
   ```

4. reduce PDF size

   ```shell
   gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=small.pdf root.pdf
   ```

   <https://tex.stackexchange.com/questions/14429/pdftex-reduce-pdf-size-reduce-image-quality>

## tips

* convert `heic` to `jpg`

  ```shell
  magick mogrify -monitor -format jpg *.heic
  magick mogrify -monitor -format jpg *.HEIC
  ```

  **NOTE: always use JPEG format!** (iPhone 12 mini, Fujifilm X100V)

* merge images by OmniGraffle
* IDE: <https://www.texstudio.org/>
