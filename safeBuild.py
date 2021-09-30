import argparse
import subprocess
from os import listdir

from PyInquirer import prompt
from prompt_toolkit.output import Output

parser = argparse.ArgumentParser(description="A tool to help building containers")
parser.add_argument("--env", dest="env", help="Set the enviroment")
parser.add_argument("--containers", dest="containers", help="Select containers to build (all, same, none)")
parser.add_argument("--only", dest="only", help="Select which containers to build (gateway, login, ...). For more than one, use ,. Ex.: gateway,login,products")
parser.add_argument("--update", dest="update", const=True, default=False, action="store_const", help="Update container if running")
parser.add_argument("--update-commons", dest="common", const=True, default=False, action="store_const", help="Update commons")

enviroments = [
    "development",
    "production",
    "staging"
]

def main(args):
    containers = listdir("services")
    toCompile = []
    with open("lastoptions", 'r+') as file:
        selectedBefore = [i for i in file.read().splitlines()]
        options = []
        
        if args.env not in enviroments:
            options.append({
                'type': 'list',
                'name': 'env',
                'message': "In what enviroment?",
                'choices': enviroments,
            })

        if args.only:
            toCompile = args.only.split(",")
        
        if args.containers not in ['same', 'all', 'none'] and not args.only:
            options.append({
                'type': 'checkbox',
                'name': 'toCompile',
                'message': "What containers do you want to compile?",
                'choices': [ {'name': i,"checked": i in selectedBefore} for i in containers] 
            })
        elif args.containers == "all":
            toCompile = containers
        elif args.containers == "same":
            toCompile = selectedBefore

        opt = prompt(options)

        if "toCompile" in opt:
            toCompile = opt["toCompile"]

            file.seek(0)
            file.truncate()
            file.writelines([str(i)+"\n" for i in toCompile])
    
        for container in toCompile:
            command = f"""
            cd services/{container} &&
            docker build --network=host -t farmacia-solidaria/{container}:{args.env} . &&
            docker tag farmacia-solidaria/{container}:{args.env} farmacia-solidaria/{container}:latest
            """

            if args.common:
                command = f"""
                rm -r -f services/{container}/common/ &&
                cp -r common/ services/{container} &&
                """ + command

            print(f"\n\nBuilding {container}:{args.env}:")
            subprocess.run(command, shell=True, check=True)

            if args.update:
                command = f"""            
                docker-compose stop {container} &&
                docker-compose kill {container} &&
                docker-compose --env-file ./secrets/.{args.env}.env up -d --no-deps {container}
                """

                print(f"\nKilling and updating container {container}:{args.env}:")
                subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    try:
        open("lastoptions", 'r').close()
    except:
        open("lastoptions", 'w').close()

    main(parser.parse_args())