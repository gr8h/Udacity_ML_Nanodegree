def question1(s, t):
    if not s or not t or s == "" or t == "":
        return False

    if type(s) != str and type(t) != str:
        return False

    if len(t) > len(s):
        return False

    s = s.lower()
    t = t.lower()

    tt_sum = 0
    for ch in t:
        tt_sum += ord(ch)

    window_size = len(t)
    start = 1
    end = len(s)

    ss_sum = 0
    current_window = s[0:window_size]
    for ch in current_window:
        ss_sum += ord(ch)
    if ss_sum == tt_sum:
        return True

    while start + window_size <= end:
        ss_remove = ord(s[start-1])
        ss_add = ord(s[window_size+start-1])
        ss_sum += ss_add
        ss_sum -= ss_remove

        if ss_sum == tt_sum:
            return True

        start += 1

    return False


print question1("udacity", "ad")  # True
print question1("nAnodegree", "gedo")  # True
print question1("helloworlD", "dlr")  # True
print question1("", "xyz")  # False
print question1("xyz", "")  # False
print question1("", "")  # False
print question1(None, None)  # False
print question1(123, 456)  # False
