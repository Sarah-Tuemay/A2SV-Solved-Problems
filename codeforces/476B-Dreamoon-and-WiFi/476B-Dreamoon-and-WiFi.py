def backT(i, y):
    if i == len(t):
        y_vals.append(y)
        return
    
    if s[i] == "+":
        backT(i+1, y+1)
    if s[i] == "-":
        backT(i+1, y-1)
    if s[i] == "?":
        backT(i+1, y+1)
        backT(i+1, y-1)

backT(0, 0)
print(y_vals.count(x)/len(y_vals))