class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pref_sum = 0
        odd_sum = 0
        even_sum = 0
        for num in arr:
            pref_sum += num
            if pref_sum % 2 == 1:
                odd_sum+=1
            else:
                even_sum += 1
        
        mod = pow(10,9)+7
        res = odd_sum%mod
        for i in range(1,len(arr)):
            if arr[i-1]%2 == 1:
                odd_sum -= 1
                temp = even_sum
                even_sum = odd_sum
                odd_sum = temp
            else:
                even_sum -= 1
            res += odd_sum
            res %= mod
        return res

            

        