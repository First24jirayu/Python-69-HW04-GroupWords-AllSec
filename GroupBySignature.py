def group_by_signature(words: list) -> list:
    groups = {}
    for word in words:
        if not word.isalpha() or not word.islower():
            continue
        count = {}
        for ch in word:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        signature = tuple(sorted(count.items()))
        if signature not in groups:
            groups[signature] = []
        groups[signature].append(word)
    return list(groups.values())
    pass

if __name__ == "__main__":
    # Example 1
    words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"]
    print(group_by_signature(words))
    # Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

    # Example 2
    words = ["apple", "pale", "leap", "plea", "papel", "hello"]
    print(group_by_signature(words))
    # Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]
