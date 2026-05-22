class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""

        for i in strs:
            enc_str+= f"{len(i)}:{i}"
        return enc_str

        return f"{strs[0]}{strs[1]}"
    def decode(self, s: str) -> List[str]:
        retval = []
        while s != "":

            length_str = ""
            c = s[0]

            while c != ":":
                length_str += c
                s=s[1:]
                c = s[0]

            

            length = int(length_str)
            s=s[1:]
            retval.append(s[:length])
            s = s[length:]
        return retval