class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char,int>last_idx;
        int n=s.size();
        for(int i=0;i<n;i++){
            last_idx[s[i]]=i;
        }
        stack<char> st;
        unordered_set<char>seen;
        for(int i=0;i<n;i++){
            char temp=s[i];
            if(seen.find(temp)==seen.end()){
                while(!st.empty() && temp<st.top() && last_idx[st.top()]>i){
                    seen.erase(st.top());
                    st.pop();
                }
                seen.insert(temp);
                st.push(temp);
            }
        }
        string res="";
        while(st.size()){
            res+=st.top();
            st.pop();
        }
        reverse(res.begin(),res.end());
        return res;
    }
};