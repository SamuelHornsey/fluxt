import importlib
import argparse

parser = argparse.ArgumentParser(description='Run an example app')
parser.add_argument('app', help='App module')
args = parser.parse_args()

module = importlib.import_module(args.app)

if __name__ == '__main__':
    module.app.run()
