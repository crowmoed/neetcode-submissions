class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_count ;
        for (char i : s){
            if(s_count.count(i) == 0 ){
                s_count[i]=0;
            }
            s_count[i]+=1;
        }
        map<char, int> t_count ;
        for (char i : t){
            if(t_count.count(i) == 0 ){
                t_count[i]=0;
            }
            t_count[i]+=1;
        }



        return s_count==(t_count);
    }
};
