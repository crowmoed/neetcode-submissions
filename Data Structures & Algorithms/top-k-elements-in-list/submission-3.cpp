class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> found;
        vector<int> found_un(nums.size());
        int count = 0;

        for (int i =0; i< nums.size();i++){
            int val = nums[i];
            if (found.contains(val)){
                found[val]++;
            }
            else{
                found_un[count] = val;
                count++;
                found[val] = 1;
            }
            }
        vector<int> retval(k);
        for(int i = 0;i<k;i++){
            int max= -1;
            int maxv= -1;
            for (int j = 0;j<count;j++){
                
                int val = found_un[j];
                int vc = found[val];
                if (max < vc){
                    max = found[val];
                    maxv = val;
                    
                }
            }
            found[maxv] = -1;
            retval[i] = maxv;
        }
        return retval;

    }
};
