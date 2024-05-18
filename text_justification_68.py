from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify_line(line: List[str]) -> str:
            width = sum([len(word) for word in line])
            while width < maxWidth:
                for i in line[: len(line) - 1]:
                    i += " "
                    width += 1

            justified = ""
            for i in line:
                justified += justified + i

            return justified

        chunks = []
        chunk = []
        while words:
            word = words.pop(0)
            if len(" ".join(chunk)) + 1 + len(word) <= maxWidth:
                chunk.append(word)

            else:
                chunks.append(chunk[:])
                chunk.clear()
                chunk.append(word)

            if not words:
                chunks.append(chunk[:])

        print(chunks)

        message = []
        for i in chunks[: len(chunks) - 1]:
            message.append(justify_line(i))

        # append last chunk with right padding
        message.append(" ".join(chunks[-1]))

        print(message)

        return [0]


# test
sol = Solution()
print(sol.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"]))
