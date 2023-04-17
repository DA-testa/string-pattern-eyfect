#Vasīlijs Dvils-Dmitrijevs

from sys import stdin

def read_input():
    file = None
    TEST_FILE = "./tests/06"

    input_mode = input("Enter mode of input (F for file or I for stdin): ").strip().upper()
    if "I" in input_mode: 
        file = stdin
    elif "F" in input_mode: 
        file = open(TEST_FILE, encoding="UTF-8")
    else:
        exit("Invalid input mode")

    pattern = file.readline().rstrip()
    text = file.readline().rstrip()

    file.close()

    return (pattern, text)

def print_occurrences(occurrences):
    # this function should control output, it doesn't need any return
    if occurrences:
        print(' '.join(map(str, occurrences)))
    else:
        print("No occurrences found")

def find_occurrences(pattern, text):
    prime = 17
    bucket = 256

    def hash_string(string: str) -> int:
        nonlocal prime, bucket
        result = 0
        for char in string:
            result = (prime * result + ord(char)) % bucket
        return result

    text_length = len(text)
    pattern_length = len(pattern)
    pattern_hash = hash_string(pattern)

    for i in range(text_length-pattern_length+1):
        window = text[i:i+pattern_length]
        if pattern_hash == hash_string(window):
            if pattern == window:
                yield i

if __name__ == '__main__':
    occurrences = list(find_occurrences(*read_input()))
    print_occurrences(occurrences)
