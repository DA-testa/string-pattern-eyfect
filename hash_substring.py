#Vasīlijs Dvils-Dmitrijevs

def read_input():
   
    choice = input()
    if 'I' in choice:
  
        return (input().rstrip(), input().rstrip())
    else:
        with open('tests/06', 'r') as file:
            return (file.readline().rstrip(), file.readline().rstrip())

def print_occurrences(output):
    
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    
    occurrences = []
    prime = 10 ** 9 + 7
    base = 131
    pattern_len = len(pattern)
    text_len = len(text)

    
    pattern_hash = sum(ord(c) * pow(base, i, prime) for i, c in enumerate(pattern)) % prime
    window_hash = sum(ord(c) * pow(base, i, prime) for i, c in enumerate(text[:pattern_len])) % prime

    
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == window_hash:
            
            if pattern == text[i:i+pattern_len]:
                occurrences.append(i)
        if i < text_len - pattern_len:
            
            window_hash = (window_hash - ord(text[i]) * pow(base, pattern_len-1, prime)) % prime
            window_hash = (window_hash * base + ord(text[i+pattern_len])) % prime
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
