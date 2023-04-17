#Vasīlijs Dvils-Dmitrijevs

def read_input():
    input_choice = input().upper()
    if "I" in input_choice:
        return input().rstrip(), input().rstrip()
    elif "F" in input_choice:
        with open("tests/06") as x:
            result= x.readline().rstrip(),x.readline().rstrip()
            return result
def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    oc = []
    if len(pattern) > len(text):
        return oc
    hashP = hash(pattern)
    hashT = hash(text[:len(pattern)])
    for i in range(len(text)-len(pattern)+1):
        if hashP == hashT:
            if text[i:i+len(pattern)] == pattern:
                oc.append(i)
        if i < len(text) - len(pattern):
            hashT = hash(text[i+1:i+len(pattern)+1])
    return oc
if __name__ == '__main__':
    print_oc(get_oc(*read_input()))
