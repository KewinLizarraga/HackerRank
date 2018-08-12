"""
Given a string, join with a hyphen "-"
    Hola mundo
    Hola-mundo
"""

def split_and_join(line):
    # whire your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
