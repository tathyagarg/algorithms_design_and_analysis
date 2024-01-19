import os

dirs = []
for item in os.listdir():
    if item == '.git': continue
    if os.path.isdir(os.path.join(os.path.abspath('.'), item)):
        for file in os.listdir(item):
            with open(f".\\{item}\\{file}", "r") as f:
                contents = " ".join([i.strip('\n') for i in f.readlines()])
            with open(f".\\{item}\\{file}", "w") as f:
                f.write(contents)
                f.flush()
        print('='*50)
