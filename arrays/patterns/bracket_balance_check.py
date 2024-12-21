s = "[{]([])}]"
bracket_map = {")": "(", "}": "{", "]": "["}
stk = []

# Used stack DS and dictionary
# Keep adding to stack if any opening bracket found in map.values()
# Pop the element from stack if any closed bracket found and only if the closed bracket maches with openning bracket else retun False


def is_balanced(s):
    for ch in s:
        if ch in bracket_map.values():
            stk.append(ch)
        elif ch in bracket_map.keys():
            if stk and stk[-1] == bracket_map[ch]:
                stk.pop()
            else:
                return False
    return True


results = is_balanced(s)
print(results)
