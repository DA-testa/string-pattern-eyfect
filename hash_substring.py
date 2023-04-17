#Vasīlijs Dvils-Dmitrijevs

def read_input():
    choice = input()
    if 'I' in choice:
        # input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open('tests/06', "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    magic_number = 7
    hash_func = lambda s: sum(ord(c) for c in s)
    pattern_hash = hash_func(pattern) * magic_number
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]
        substring_hash = hash_func(substring) * magic_number
        if substring_hash == pattern_hash:
            if substring == pattern:
                occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input())
