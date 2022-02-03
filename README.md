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

## For Vs Code Intellisense
If you wish to use intellisense in vscode, please install all libraries in intellisense.txt, some of then aren't been used right now in development, but propably will be in some point
```bash
pip install -r intellisense.txt
```
