from pathlib import Path
from pdf2image import convert_from_path


# reference
# https://qiita.com/Gyutan/items/5e62420cc8f6bb106bed
# https://gammasoft.jp/blog/convert-pdf-to-image-by-python/


def main():
    pdf_path = Path('./pdf/pdf3009p.pdf')
    # 300DPI, 縦横比を維持したまま長辺を3508, 出力先は、'./img', 出力ファイル名は、'pdf3009p', JPEGファイルで出力する
    # convert_from_path(pdf_path, dpi=300, size=3508, output_folder='./img', output_file=pdf_path.stem, fmt='jpg')

    # 300DPI, 縦横比を維持したまま長辺を3508として変換
    pages = convert_from_path(pdf_path, dpi=300, size=3508)
    for i, page in enumerate(pages):
        page.save(f'img/{pdf_path.stem}-{i:02d}.jpg', 'JPEG')

if __name__ == '__main__':
    main()