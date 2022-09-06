import os

from editors.water_mark import ImageWaterMark


def check(dir: str, ready_dir: str):
    if os.listdir(dir):
        for image in os.listdir("magic_dir"):
            ImageWaterMark((0, 0), "media/watermark.png").render(f"{dir}/{image}")
            os.replace(f"{dir}/{image}", f"{ready_dir}/{image}")


if __name__ == "__main__":
    check("magic_dir", "processed_image")
