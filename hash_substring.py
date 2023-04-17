#Vasīlijs Dvils-Dmitrijevs

def read_input():
    fileorno = input("Enter I for input from user or F for input from file: ")
    pattern = ""
    text = ""
    if "I" in fileorno or "i" in fileorno:
        pattern = input("Enter pattern: ").rstrip()
        text = input("Enter text: ").rstrip()
    elif "F" in fileorno or "f" in fileorno:
        filename = input("Enter filename: ")
        try:
            with open(filename, 'r') as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
        except FileNotFoundError:
            print("File not found.")
            exit(0)
    return pattern, text

def print_occurrences(output):
    if output:
        print(' '.join(map(str, output)))
    else:
        print("No occurrences found.")

def get_occurrences(pattern, text):
    prime = 1_000_000_007
    p_len, t_len = len(pattern), len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(prime, i) for i in range(p_len))
    text_hash = sum(ord(text[i]) * pow(prime, i) for i in range(p_len))
    occurrences = []
    for i in range(t_len - p_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+p_len]:
                occurrences.append(i)
        if i < t_len - p_len:
            text_hash = (text_hash - ord(text[i]) * pow(prime, p_len-1)) * prime + ord(text[i+p_len])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
