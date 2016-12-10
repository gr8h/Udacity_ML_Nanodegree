"""
First solution by sorting and comparing each window
Time: O(n log n)
Space: O(1)
"""
def question1_nlogn(s, t):
    if not s or not t or s == "" or t == "":
        return False

    if type(s) != str and type(t) != str:
        return False

    if len(t) > len(s):
        return False

    s = s.lower()
    t = sorted(t.lower())
    window_size = len(t)
    num_of_windows = len(s) - len(t) + 1

    for win in range(num_of_windows):
        current_window = sorted(s[win:win+window_size])
        if current_window == t:
            return True

    return False


"""
Second solution by assuming that the string input is ASCII so the max value will be 256,
The compare a counter by maintaining a window of target input size
"""
def question1(s, t):
    if not s or not t or s == "" or t == "":
        return False

    if type(s) != str and type(t) != str:
        return False

    if len(t) > len(s):
        return False

    s = s.lower()
    t = t.lower()

    t_count = [0] * 256
    s_count = [0] * 256

    for i in range(len(t)):
        t_count[ord(t[i])] += 1
        s_count[ord(s[i])] += 1

    win = len(t)
    while win <= len(s):
        if compareCounter(t_count, s_count):
            return True

        s_count[ord(s[win])] += 1
        s_count[ord(s[win - len(t)])] -= 1
        win += 1

    return False

def compareCounter(t_count, s_count):
    return t_count == s_count

    # for i in range(len(t_count)):
    #     if t_count[i] != s_count[i]:
    #         return False
    # return True


print question1("udacity", "ad")  # True
print question1("udacitty", "yt")  # True
print question1("nAnodegree", "gedo")  # True
print question1("helloworlD", "dlr")  # True
print question1("", "xyz")  # False
print question1("xyz", "")  # False
print question1("", "")  # False
print question1(None, None)  # False
print question1(123, 456)  # False
