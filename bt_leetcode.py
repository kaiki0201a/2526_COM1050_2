#Sliding Window
def lengthOfLongestSubstring(s: str) -> int:
    seen = set()    # luu cac ky tu da thay trong cua so
    left =0     # con tro trai
    max_len = 0     # ket qua
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])    # loai bo ky tu ben trai
            left += 1   #thu hep cua so

        seen.add(s[right])      # them ky tu moi vao cua so
        max_len = max(max_len, right - left + 1)    # cap nhat ket qua

    return max_len
print(lengthOfLongestSubstring("pwwkew"))
