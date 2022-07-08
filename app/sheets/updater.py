from apscheduler.schedulers.background import BackgroundScheduler
from .views import run_updater


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(run_updater, 'interval', seconds=10)
    scheduler.start()
