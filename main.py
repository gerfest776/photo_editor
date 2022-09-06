from PIL import ImageFont

from editors.water_mark import TextWaterMark


def check():
    TextWaterMark(
        (0, 0),
        "aboba",
        "black",
        ImageFont.truetype("arial.ttf", 100)
    ).render("magic_dir/file.jpeg")


if __name__ == '__main__':
    check()
