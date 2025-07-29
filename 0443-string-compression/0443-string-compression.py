class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # pointer to write compressed data
        start = 0  # pointer to start of a group

        while start < len(chars):
            end = start
            while end < len(chars) and chars[end] == chars[start]:
                end += 1

            chars[write] = chars[start]
            write += 1

            count = end - start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            start = end

        return write
