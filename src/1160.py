#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1160. Find Words That Can Be Formed by Characters

# 
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        char_dict = {}
        for c in chars:
            char_dict[c] = chars.count(c)
        
        for w in words:
            w_dict = {}
            for c in w:
                w_dict[c] = w.count(c)
            is_in = True
            for k in w_dict:
                if k not in char_dict or w_dict[k] > char_dict[k]:
                    is_in = False
                    break
            if is_in:
                res += len(w)
        return res

if __name__ == '__main__':
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"

    # words = ["hello","world","leetcode"]
    # chars = "welldonehoneyr"

    res = Solution().countCharacters(words, chars)
