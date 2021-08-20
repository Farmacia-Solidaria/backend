import argparse
import subprocess
from os import listdir

from PyInquirer import prompt
from prompt_toolkit.output import Output

parser = argparse.ArgumentParser(description="A tool to help building containers")
parser.add_argument("--env", dest="env", help="Set the enviroment")
parser.add_argument("--containers", dest="containers", help="Select containers to build (all, same, none)")

def main(args):
    containers = listdir("services")
    toCompile = []
    with open("lastoptions", 'r+') as file:
        selectedBefore = [i for i in file.read().splitlines()]
        options = []
        
        if args.env not in ['dev', 'prod', 'staging']:
            options.append({
                'type': 'list',
                'name': 'env',
                'message': "In what enviroment?",
                'choices': [
                    "dev",
                    "prod",
                    "staging"
                ],
            })
        
        if args.containers not in ['same', 'all', 'none']:
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

            echo "Building {container}:{args.env}:" &&
            
            cd services/{container} &&
            docker build -t farmacia-solidaria/{container}:{args.env} . &&
            docker tag farmacia-solidaria/{container}:{args.env} farmacia-solidaria/{container}:latest &&
            """

            out = subprocess.call(command.split(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(out)




if __name__ == "__main__":
    try:
        open("lastoptions", 'r').close()
    except:
        open("lastoptions", 'w').close()

    main(parser.parse_args())