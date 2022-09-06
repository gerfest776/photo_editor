from celery.schedules import crontab

from core.celery_app import celery_app


@celery_app.task(name="parser")
def check_magic_dir():
    ...
    # loop.run_until_complete(parser.get_channels())


celery_app.conf.beat_schedule = {
    "run_parser_worker": {
        "task": "parser",
        "schedule": crontab(),
    },
}
