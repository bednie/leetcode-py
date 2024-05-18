from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str]) -> str:
            if len(line) == 1:
                if line[0] == maxWidth:
                    return line[0]
                width = len(line[0])
                line[0] = line[0] + (" " * (maxWidth - width))
                return line[0]

            width = 0
            for i in line:
                width += len(i)

            while width < maxWidth:
                for i in range(len(line) - 1):
                    line[i] += " "
                    width += 1
                    if width == maxWidth:
                        break

            justified_line = ""
            for i in line:
                justified_line += i

            return justified_line

        def left_justify(line: List[str]) -> str:
            justified_line = " ".join(line)
            width = len(justified_line)
            justified_line = justified_line + (" " * (maxWidth - width))

            return justified_line

        chunks = []
        chunk = []
        while words:
            word = words.pop(0)

            if len(" ".join(chunk)) + 1 + len(word) <= maxWidth:
                chunk.append(word)

            elif len(word) == maxWidth:
                if chunk != []:
                    chunks.append(chunk[:])
                    chunk.clear()
                chunks.append([word])

            else:
                chunks.append(chunk[:])
                chunk.clear()
                chunk.append(word)

            if not words and chunk != []:
                chunks.append(chunk[:])

        message = []
        for c in range(len(chunks) - 1):
            message.append(justify_line(chunks[c]))

        message.append(left_justify(chunks[-1]))

        return message


# test
sol = Solution()
assert sol.fullJustify(["What", "must", "be", "shall", "be."], 5) == [
    "What ",
    "must ",
    "be   ",
    "shall",
    "be.  ",
], "Wrong"
