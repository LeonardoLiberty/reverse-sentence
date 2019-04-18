class Solution:
    def ReverseSentence(self, s):
        # write code here
        if not s:
            return ""
        if len(s) <= 0:
            return ""
        st = 0
        word = []
        for i in range(len(s)):
            if s[i] == ' ':
                word.append(s[st:i])
                st = i+1
            if i == len(s) -1:
                word.append(s[st:i+1])
        return " ".join(word[::-1])


if __name__ == '__main__':
    t = Solution().ReverseSentence("student. a am I")
    print t