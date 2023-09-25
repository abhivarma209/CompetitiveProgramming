class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int v[9][9];
        memset(v,0,sizeof(v));
        for(int i=0;i<9;i++){
            vector<int>v1(9);
            vector<int>v2(9);
            for(int j=0;j<9;j++){
                if(board[i][j]!='.'){
                    int x=board[i][j]-'0';
                    if(v1[x-1]==0) v1[x-1]=1;
                    else return false;
                    if(v[(i/3)*3+(j/3)][x-1]==0) v[(i/3)*3+(j/3)][x-1]=1;
                    else return false;
                }
                if(board[j][i]!='.'){
                    int y=board[j][i]-'0';
                    if(v2[y-1]==0) v2[y-1]=1;
                    else return false;
                }
            }
        }
        return true;
    }
};