# Backend

## Installation

To install please compile everything using:
```bash
python3 safeBuild.py --containers all --update-commons --env dev
```

To deploy use:
```bash
docker-compose --env-file ./secrets/.{ENV}.env up
```

### Important
> Remember to create the user in Minio on production or development