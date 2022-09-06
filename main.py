from PIL import ImageFont

from editors.water_mark import ImageWaterMark


def check():
    ImageWaterMark(
        (0, 0),
        "media/watermark.png"
    ).render("magic_dir/file.jpeg")


if __name__ == '__main__':
    check()
