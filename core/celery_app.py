from celery import Celery

celery_app = Celery("celery_worker")
celery_app.config_from_object("core.celery_config")
celery_app.autodiscover_tasks(["core"])
