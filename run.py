#!/usr/bin/env python
import os
import argparse

def run():
    os.system("uvicorn friendlybit.server:app --reload")

def deploy():
    os.system("git push dokku master")

def dependencies():
    os.system("pip-compile requirements.in")
    os.system("pip-compile requirements-dev.in")
    os.system("pip-sync requirements-dev.txt")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--deploy', action="store_true", required=False)
    parser.add_argument('--deps', action="store_true", required=False)
    args = parser.parse_args()

    if args.deploy:
        deploy()
    elif args.deps:
        dependencies()
    else:
        run()


if __name__ == '__main__':
    main()
