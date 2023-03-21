from celery import Celery

app = Celery("Tooling", backend="redis", broker='redis://127.0.0.1:6379/0')
app.autodiscover_tasks(['tooling'], force=True)
