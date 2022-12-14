from __future__ import absolute_import, unicode_literals

import decouple

accept_content = ["json"]
enable_utc = False
task_serializer = "json"
timezone = "UTC"
task_track_started = True
worker_hijack_root_logger = False
worker_redirect_stdouts_level = "ERROR"
broker = decouple.config("CELERY_BROKER")
