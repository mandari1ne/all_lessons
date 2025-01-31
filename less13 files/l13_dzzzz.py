ar = ['aaaa', 3, 5, 23, 'ff', 'd0', 0, 'ss', 12, 4, 'qwertyy']
nums = [str(c) for c in ar if isinstance(c, int)]
words = [c for c in ar if isinstance(c, str)]

with open('dz.txt', 'w') as f:
    f.write(' '.join(sorted(words, key=lambda c: len(c)) + sorted(nums, key=lambda c: int(c))))

