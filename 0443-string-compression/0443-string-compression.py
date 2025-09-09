class Solution:
    def compress(self, chars: List[str]) -> int:
        read,write,n=0,0,len(chars)
        while read<n:
            temp=read
            count=0
            while read<n and chars[temp]==chars[read]:
                read+=1
                count+=1
            chars[write]=chars[temp]
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write
