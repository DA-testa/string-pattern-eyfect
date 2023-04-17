#Vasīlijs Dvils-Dmitrijevs

from sys import stdin

def read_input():
file = None
test_file = "./tests/06"

mode = input()
if "I" in mode:
    file = stdin

elif "F" in mode:
    file = open(test_file, encoding="UTF-8")

else:
    exit()

pattern = file.readline().rstrip()
text = file.readline().rstrip()

return (pattern, text)
def print_occurrences(output):
print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
prime = 17
bucket = 256
def hasher(string):
nonlocal prime, bucket
result = 0
for char in string:
result = (prime * result + ord(char)) % bucket
return result
t_length = len(text)
p_length = len(pattern)
p_hash = hasher(pattern)

window = None
for i in range(t_length - p_length + 1):
    window = text[i:i + p_length]
    if p_hash == hasher(window):
        if pattern == window:
            yield i
            if name == 'main':
print_occurrences(get_occurrences(*read_input()))
