/*
https://leetcode.com/problems/valid-anagram/description/

242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

*/

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        unordered_map<char, int> sMap;
        unordered_map<char, int> tMap;

        //for each strings' map, count the number of occurences of each character
        for (int i = 0; i < s.length(); i++) {
            sMap[s[i]]++;
            tMap[t[i]]++;
        }

        //Compare the two hash maps, if they do not have the same count of a given character, they are not valid anagrams
        for (int i = 0; i < s.length(); i++) {
            if (tMap[s[i]] != sMap[s[i]]) return false;
        }

        return true;
    }
};