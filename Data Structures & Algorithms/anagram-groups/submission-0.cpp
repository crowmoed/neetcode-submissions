class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> anagram_matches;

        for (string word : strs){
            string srt_wrd = word;
            sort(srt_wrd.begin(),srt_wrd.end());
            anagram_matches[srt_wrd].push_back(word);
        }

        vector<vector<string>> retval;

        for (auto l : anagram_matches){
            retval.push_back(l.second);
        }

        return retval;
    }
};
