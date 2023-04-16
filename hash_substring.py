# Vasīlijs Dvils-Dmitrijevs

def read_input():
    choice = input()

    if 'I'in(choice):
        return (input().rstrip(), input().rstrip())
    else:
        with open('tests/06', "r") as fails:
            return (fails.readline().rstrip(),fails.readline().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    listik = []
    mejik_namber = 7
    mejik_mef = lambda s: sum(ord(c) for c in s)
    
    pattern_hash = mejik_mef(pattern) * mejik_namber
    
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i+len(pattern)]
        substring_hash = mejik_mef(substring) * mejik_namber
        
        if substring_hash == pattern_hash:
            if substring == pattern:
                listik.append(i)
    
    return listik

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


