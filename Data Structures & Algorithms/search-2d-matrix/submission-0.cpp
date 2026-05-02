class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size();
        int COLS = matrix[0].size();

        int top = 0, bot = ROWS - 1; //[0,1,2]
        while(top <= bot){
            int row = (top + bot)/ 2;
            if(target > matrix[row][COLS - 1]){// if target > last element of that row
                top = row + 1; //=>target must be below
            } else if(target < matrix[row][0]){//if target < 1st element of that row
                bot = row - 1;
            } else {
                break;
            }
        }

        if(!(top <= bot)){
            return false;
        } 

        //binary search with the row
        int row = (top + bot)/2;
        int l = 0, r = COLS - 1;
        while (l <= r){
            int m = (l + r) / 2;
            if(target > matrix[row][m]){// if target > middle element
                l = m + 1; //search right half
            } else if(target < matrix[row][m]){// if target < middle element
                r = m - 1; //search left half
            } else{
                return true; //if equal -> target found
            }
        }

        return false;
    }
};
