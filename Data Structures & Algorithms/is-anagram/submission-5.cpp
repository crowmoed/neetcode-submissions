class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>map_s;
        unordered_map<char,int>map_t;

        for (int i =0;i< s.length();i++){
            if (map_s.contains(s[i])){
                map_s[s[i]]+=1;
            }
            else{
                map_s[s[i]]=1;
            }
        } 

        for (int i =0;i< t.length();i++){
            if (map_t.contains(t[i])){
                map_t[t[i]]+=1;
            }
            else{
                map_t[t[i]]=1;
            }
        }
        return map_s == map_t;
    }
};
