public class Solution {
    public int MaxEvents(int[][] events) {
        Array.Sort(events, (a,b)=>a[0]==b[0]?a[1].CompareTo(b[1]):a[0].CompareTo(b[0]));
        var pq = new PriorityQueue<int,int>();
        int n=events.Length,i=0,d=0,res=0;
        while(i<n || pq.Count>0){
            if(pq.Count==0) d=events[i][0];
            while(i<n && events[i][0]<=d){
                pq.Enqueue(events[i][1],events[i][1]);i++;
            }
            pq.Dequeue();
            res++;d++;
            while(pq.Count>0 && pq.Peek()<d) pq.Dequeue();
        }
        return res;
    }
}