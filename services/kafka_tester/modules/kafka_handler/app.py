import os
import sys
import faust
from kafka import KafkaProducer
from django.conf import settings

# Append parent directory to syspath so is possible to import other apps here
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

os.environ.setdefault('FAUST_LOOP', 'eventlet')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kafka_tester.settings')


faustApp = faust.App('kafka_tester-kafka_handler', autodiscover=True, origin='modules')
kafkaProducer = KafkaProducer(bootstrap_servers=[settings.KAFKA_BROKER_URL]) 


@faustApp.on_configured.connect
def configure_from_settings(app, conf, **kwargs):
    conf.broker = "kafka://"+settings.KAFKA_BROKER_URL
    conf.store = settings.FAUST_STORE_URL

@faustApp.agent("kafka_tester-income")
async def test(events):
    async for event in events:
        print(event)


def main():
    faustApp.main()

if __name__ == '__main__':
    main()
