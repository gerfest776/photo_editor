import os

from celery.schedules import crontab

from core.celery_app import celery_app
from editors.water_mark import ImageWaterMark
from filter_build import Builder


@celery_app.task(name="handler")
def check_magic_dir():
    magic_dir = "magic_dir"
    ready_dir = "processed_image"

    if os.listdir(magic_dir):
        for image in os.listdir(magic_dir):
            if image.startswith("."):
                continue
            Builder(f"{magic_dir}/{image}").edit_photo(
                ImageWaterMark((0, 0), "media/watermark.png")
            )
            os.replace(f"{magic_dir}/{image}", f"{ready_dir}/{image}")


celery_app.conf.beat_schedule = {
    "check_magic_dir": {
        "task": "handler",
        "schedule": crontab(),
    },
}
