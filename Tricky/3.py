Longest Substring with K Distinct Characters

def longest_k_distinct(s: str, k: int) -> int:
    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] += 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
