import os
import sys
import faust
from django.conf import settings

# Append parent directory to syspath so is possible to import other apps here
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('FAUST_LOOP', 'eventlet')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gateway.settings')

faust = faust.App('kafka_handler-service', autodiscover=True, origin='gateway')

@faust.on_configured.connect
def configure_from_settings(app, conf, **kwargs):
    conf.broker = "kafka://"+settings.KAFKA_BROKER_URL
    conf.store = settings.FAUST_STORE_URL

def main():
    faust.main()

if __name__ == '__main__':
    main()
