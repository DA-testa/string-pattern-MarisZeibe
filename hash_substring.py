# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    inputType = input().rstrip()
    if inputType and inputType == "I":
        # input from keyboard
        pattern = input().rstrip()
        text = input().rstrip()
    elif inputType and inputType == "F":
        # input from file
        file = open("tests/06", "r").readlines()
        pattern = file[0].rstrip()
        text = file[1].rstrip()
    else:
        return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def hash(text):
    result = 0
    for char in text:
        result = (127 * result + ord(char)) % 101184257
    return result

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    textLen = len(text)
    patternLen = len(pattern)
    patternHash = hash(pattern)
    for i in range(textLen-patternLen+1):
        substring = text[i:i+patternLen]
        if hash(substring) == patternHash and substring == pattern:
            result.append(i)
    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

