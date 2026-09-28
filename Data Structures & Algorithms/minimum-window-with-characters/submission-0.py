class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        needed_char_freq = {}
        for char in t:
            needed_char_freq[char] = needed_char_freq.get(char, 0) + 1

        current_char_freq = {}
        unique_chars_needed = len(needed_char_freq)
        unique_chars_correct = 0

        left_pointer = 0
        right_pointer = 0

        best_window_len = len(s) + 1
        best_window_left = None
        best_window_right = None

        while right_pointer < len(s):
            current_char = s[right_pointer]
            current_char_freq[current_char] = current_char_freq.get(current_char, 0) + 1
            
            if current_char in needed_char_freq:
                if current_char_freq[current_char] == needed_char_freq[current_char]:
                    unique_chars_correct += 1

            while unique_chars_correct == unique_chars_needed:
                current_window_len = right_pointer - left_pointer + 1
                if current_window_len < best_window_len:
                    best_window_len = current_window_len
                    best_window_left = left_pointer
                    best_window_right = right_pointer

                char_at_left = s[left_pointer]
                current_char_freq[char_at_left] -= 1
                if char_at_left in needed_char_freq:
                    if current_char_freq[char_at_left] < needed_char_freq[char_at_left]:
                        unique_chars_correct -= 1

                left_pointer += 1

            right_pointer += 1

        if best_window_len > len(s):
            return ""

        return s[best_window_left : best_window_right + 1]









