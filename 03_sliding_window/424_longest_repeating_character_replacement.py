class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        st = {}
        m = 0
        for r in range(len(s)):
            st[s[r]] = st.get(s[r], 0) + 1
            while (r - l + 1 - max(st.values())) > k:
                st[s[l]] = st.get(s[l]) - 1
                l += 1
            m = max(m, r - l + 1)
        return m
