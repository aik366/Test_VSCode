import os

PATH = os.path.dirname(os.path.abspath(__file__))

def write_file():
    with open(os.path.join(PATH, "test.txt"), "a", encoding="utf-8") as f:
        f.write("Hello World\n")

def read_file():
    with open(os.path.join(PATH, "test.txt"), "r", encoding="utf-8") as f:
        print(f.read().splitlines())
        
        
if __name__ == "__main__":
    write_file()
    read_file()