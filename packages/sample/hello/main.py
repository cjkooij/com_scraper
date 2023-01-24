import os


def main(args):
    name = args.get("name", "stranger")
    greeting = "Hello there" + name + f"!, {os.getenv('ENV_VAR')}"
    print(greeting)
    print('test deploy on push')
    return {"body": greeting}
