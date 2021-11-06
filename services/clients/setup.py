from pathlib import Path
from setuptools import find_packages, setup

requirements = [
    #Django
    "Django==3.2.5",
    "djangorestframework==3.12.4",
    "django-cors-headers==3.5.0",
    "psycopg2==2.9.1",
    "requests==2.26.0",

    #Kafka
    "faust[rocksdb]==1.10.4",
    "kafka-python==1.4.7",

    #S3 Bucket
    "django-minio-backend==3.2.1",
    "minio==7.1.1",
    
    #Others
    "PyJWT==2.1.0",
    "cryptography==3.4.8",

    #Build
    "build==0.6.0.post1",

    #Others
    "Pillow==8.4.0",

]

setup(
    name="clients",
    version="0.0.1",
    description="Sample Description",
    author="Farmácia Solidária Devs",
    author_email="dev@dev.com",
    url="https://github.com/Farmacia-Solidaria",
    platforms=['any'],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.8.0',
    keywords=[],
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'service-django = clients.__main__:main',
            'service-faust = modules.kafka_handler.app:main',
        ],
    },
)
