def read_input():
    choice = input("Enter input type (I for keyboard input, F for file input): ")

    if choice.upper() == 'I':
        # input from keyboard
        pattern = input("Enter pattern: ").strip()
        text = input("Enter text: ").strip()
    else:
        # input from file
        with open('tests/06.txt', "r") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()

    return pattern, text


def print_occurrences(output):
    if output:
        print(' '.join(map(str, output)))
    else:
        print("Pattern not found in text.")


def get_occurrences(pattern, text):
    # Rabin-Karp algorithm for pattern matching
    occurrences = []
    prime = 101  # prime number for hashing
    d = 256     # number of characters in the input alphabet

    def hash(string, length):
        # function to calculate the hash value of a string
        h = 0
        for i in range(length):
            h = (d*h + ord(string[i])) % prime
        return h

    def rehash(string, old_index, new_index, old_hash, length):
        # function to update the hash value of a string after a shift
        new_hash = old_hash - ord(string[old_index])*pow(d, length-1)
        new_hash = (new_hash*d + ord(string[new_index])) % prime
        return new_hash

    m = len(pattern)
    n = len(text)
    p_hash = hash(pattern, m)
    t_hash = hash(text, m)

    for i in range(n-m+1):
        if p_hash == t_hash:
            if text[i:i+m] == pattern:
                occurrences.append(i)

        if i < n-m:
            t_hash = rehash(text, i, i+m, t_hash, m)

    return occurrences


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
