def first_non_repeating(s):
    count = {}

    # Count frequency of each character
    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    # Find first non-repeating character
    for ch in s:
        if count[ch] == 1:
            return ch

    return None


# Sample Input
text = "leetcode"

# Function Call
result = first_non_repeating(text)

print("First non-repeating character is:", result)