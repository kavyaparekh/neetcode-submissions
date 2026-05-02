class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        //Count how many times each task appears.
        vector<int> count(26, 0);
        for(char task : tasks){
            count[task - 'A']++;
        }

        //Max Heap of task frequencies.
        priority_queue<int> maxHeap;
        //this max heap always picks the tasks with the highest remaining count
        for(int cnt : count){
            if(cnt > 0){
                maxHeap.push(cnt);//push only tasks that actually exist
            }
        }

        int time = 0;
        //keeps track of totatl time units passed => output

        //cooldown queue:{remainingCount, timeWhenTaskCanRunAgain}
        queue<pair<int,int>> q;

        // run while there are tasks left OR tasks cooling down
        while(!maxHeap.empty() || !q.empty()){
            time++;//move forward one unit of time
            if(maxHeap.empty()){
                //no task can be executed right now -> must be idle
                time = q.front().second;//jump time directly to when the next task becomes available
            } else {
                //execute the most frequent available task
                //and reduce its frequency since we just ran this task
                int cnt = maxHeap.top()-1;   
                maxHeap.pop();

                if(cnt>0){
                    //if the task that was just run still has 
                    //remaining counts then we put it in the
                    //cooldown queue until(curr time + n)
                    q.push({cnt,time+n});
                }         
            }
            //check if any task has finished colling down at this time
            if(!q.empty()&&q.front().second == time){
                maxHeap.push(q.front().first);//task is available again now
                q.pop();//remove it from cooldown queue
            }
        }
        return time;
    }
};
