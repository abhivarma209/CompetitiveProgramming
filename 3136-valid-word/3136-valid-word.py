class Solution(object):
    def isValid(self, word):
        length=len(word)
        if length<3:
            return 0
        
        v = [0]*4
        
        for i in range(length):
            if word[i]>='0' and word[i]<='9':
                v[0]=v[0]+1
            elif word[i]>='a' and word[i]<='z':
                if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u':
                    v[1]=v[1]+1
                else:
                    v[2]=v[2]+1
            elif word[i]>='A' and word[i]<='Z':
                if word[i]=='A' or word[i]=='E' or word[i]=='I' or word[i]=='O' or word[i]=='U':
                    v[1]=v[1]+1
                else:
                    v[2]=v[2]+1
            else:
                v[3]=v[3]+1
        
        if v[3]>0 or v[1]==0 or v[2]==0:
            return 0
        return 1
        """
        :type word: str
        :rtype: bool
        """
        