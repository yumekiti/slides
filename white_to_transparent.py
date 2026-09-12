import argparse
from PIL import Image


def white_to_transparent_and_crop(
    input_path: str,
    output_path: str,
    threshold: int
):
    """
    白っぽい色を透過し、透過後に要素サイズでトリミングする
    """
    img = Image.open(input_path).convert("RGBA")
    pixels = img.getdata()

    new_pixels = []
    for r, g, b, a in pixels:
        if r >= threshold and g >= threshold and b >= threshold:
            new_pixels.append((r, g, b, 0))
        else:
            new_pixels.append((r, g, b, a))

    img.putdata(new_pixels)

    # ---- ここが「要素の高さに合わせる」処理 ----
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    else:
        # 全部透過だった場合（保険）
        print("WARNING: 非透過ピクセルが見つかりませんでした")

    img.save(output_path, "PNG")


def main():
    parser = argparse.ArgumentParser(
        description="PNG画像の白背景を透過し、要素サイズにトリミングします"
    )
    parser.add_argument(
        "-i", "--input",
        required=True,
        help="入力PNGファイルパス"
    )
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="出力PNGファイルパス"
    )
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=245,
        help="白と判定する閾値 (0-255, デフォルト: 245)"
    )

    args = parser.parse_args()

    if not (0 <= args.threshold <= 255):
        raise ValueError("threshold は 0〜255 の範囲で指定してください")

    white_to_transparent_and_crop(
        input_path=args.input,
        output_path=args.output,
        threshold=args.threshold
    )


if __name__ == "__main__":
    main()
