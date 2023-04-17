#Vasīlijs Dvils-Dmitrijevs

def read_input():
    input_choice = input().upper()
    if input_choice == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_choice == "F":
        filename = input().rstrip()
        with open(filename) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    if len(pattern) > len(text):
        return occurrences
    prime = 1000000007
    x = 263
    p_hash = sum(ord(pattern[i]) * pow(x, i, prime) for i in range(len(pattern))) % prime
    t_hash = sum(ord(text[i]) * pow(x, i, prime) for i in range(len(pattern))) % prime
    x_to_len_pattern = pow(x, len(pattern), prime)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            t_hash = (t_hash - ord(text[i]) * pow(x, len(pattern)-1, prime)) % prime
            t_hash = (t_hash * x + ord(text[i+len(pattern)])) % prime
            t_hash = (t_hash + prime) % prime
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
