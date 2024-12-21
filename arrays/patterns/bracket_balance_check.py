s = "[{]([])}]"
bracket_map = {")": "(", "}": "{", "]": "["}
stk = []


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
