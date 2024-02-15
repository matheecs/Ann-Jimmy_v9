# DIY Albums

![IMG_5525](https://github.com/matheecs/AJ_Vol9/assets/16047052/bc865aff-5552-451b-8c75-148e1cff215c)

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

5. **线装书**：折页、打孔和缝线 <https://www.bilibili.com/video/BV1pu411Q7mM>

## tips

* convert `heic` to `jpg`

  ```shell
  magick mogrify -monitor -define preserve-timestamp=true -format jpg *.heic
  magick mogrify -monitor -define preserve-timestamp=true -format jpg *.HEIC
  ```

  <https://unix.stackexchange.com/a/758639/602051>

  **NOTE: always use JPEG format!** (iPhone 12 mini, Fujifilm X100V)

* merge images by OmniGraffle
* IDE: <https://www.texstudio.org/>
