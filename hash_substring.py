#Vasīlijs Dvils-Dmitrijevs

def read_input():
    input_choice = input().upper()
    if "I" in input_choice:
        return input().rstrip(), input().rstrip()
    elif "F" in input_choice:
        filename = input().rstrip()
        with open(filename) as f:
            return f.readline().rstrip(), f.readline().rstrip()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    if len(pattern) > len(text):
        return occurrences
    hashP = hash(pattern)
    hashT = hash(text[:len(pattern)])
    for i in range(len(text)-len(pattern)+1):
        if hashP == hashT:
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            hashT = hash(text[i+1:i+len(pattern)+1])
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
