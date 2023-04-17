#Vasīlijs Dvils-Dmitrijevs

from sys import stdin

def read_input():
    mode = input("Enter mode of input F or I: ").strip().upper()
    if mode == "I":
        file = stdin
    elif mode == "F":
        file_path = input("Enter file path: ")
        file = open(file_path, encoding="UTF-8")
    else:
        exit("Invalid input mode")

    pattern = file.readline().rstrip()
    text = file.readline().rstrip()

    file.close()

    return (pattern, text)

def print_occurrences(output):
    if output:
        print(' '.join(map(str, output)))
    else:
        print("No occurrences found")

def get_occurrences(pattern, text):
    prime = 17
    bucket = 256

    def hasher(string: str) -> int:
        result = 0
        for char in string:
            result = (prime * result + ord(char)) % bucket
        return result

    t_length = len(text)
    p_length = len(pattern)
    p_hash = hasher(pattern)

    for i in range(t_length-p_length+1):
        window = text[i:i+p_length]
        if p_hash == hasher(window):
            if pattern == window:
                yield i

if __name__ == '__main__':
    print_occurrences(list(get_occurrences(*read_input())))
