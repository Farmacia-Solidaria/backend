from pathlib import Path
from setuptools import find_packages, setup

requirements = [
    "Django==3.2.5",
    "djangorestframework==3.12.4",
    "django-cors-headers==3.5.0",
    "psycopg2==2.9.1",
    "requests==2.26.0",
    "faust[rocksdb]==1.10.4",
    "kafka-python==1.4.7",
    "build==0.6.0.post1",
]

setup(
    name="Kafka_Tester",
    version="1.0.0",
    description="Simple Description",
    author="Otavio",
    author_email="otavio",
    url="https://github.com/Farmacia-Solidaria",
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9.0',
    keywords=[],
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'start-django = kafka_tester.__main__:main',
            'start-faust = modules.kafka_handler.app:main',
        ],
    },
)
