def swap_case(s):
    new_s = ""
    for ch in s:
        if ch.isupper():
            new_s += ch.lower()
        else:
            new_s += ch.upper()
        
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
