class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(),events.end());
        priority_queue<int,vector<int>,greater<int>>pq;
        int n=events.size(),i=0,d=0,res=0;
        while(i<n || pq.size()){
            if(pq.size()==0) d=events[i][0];
            while(i<n && events[i][0]<=d) pq.push(events[i++][1]);
            pq.pop();
            res++;d++;
            while(pq.size() && pq.top()<d) pq.pop();
        }
        return res;
    }
};