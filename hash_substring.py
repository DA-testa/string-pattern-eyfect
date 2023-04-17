#Vasīlijs Dvils-Dmitrijevs

import argparse

def read_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="path to input file")
    parser.add_argument("-p", "--pattern", help="pattern to search")
    parser.add_argument("-t", "--text", help="text to search in")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="UTF-8") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    elif args.pattern and args.text:
        pattern = args.pattern
        text = args.text
    else:
        exit()

    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 17
    bucket = 256
    def hasher(string: str) -> int:
        nonlocal prime, bucket
        result = 0
        for char in string:
            result = (prime * result + ord(char)) % bucket
        return result

    t_length = len(text)
    p_length = len(pattern)
    p_hash = hasher(pattern)

    window = None
    for i in range(t_length-p_length+1):
        window = text[i:i+p_length]
        if p_hash == hasher(window):
            if pattern == window:
                yield i

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
