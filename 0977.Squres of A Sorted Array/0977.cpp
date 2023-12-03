#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        // define a same size array
        vector<int> res(nums.size(), 0);
        int left = 0;
        int right = nums.size() - 1;
        int p = nums.size() - 1;
        while (left <= right) {
            // cout << "left = " << nums[left] << ", right = " << nums[right];
            if (abs(nums[left]) > abs(nums[right])) {
                res[p] = nums[left] * nums[left];
                left++;
            } else if (abs(nums[left]) <= abs(nums[right])) {
                res[p] = nums[right] * nums[right];
                right--;
            }
            // cout << ", nums[p] = " << res[p] << endl;
            p--;
        }
        return res;
    }
};

int main () {
    Solution s;
    // vector<int> v{-4, -1, 0, 3, 10};
    vector<int> v{-7, -3, 2, 3, 11};
    vector<int> res = s.sortedSquares(v);
    for ( int i = 0; i < v.size(); i++) {
        cout << res[i] << " ";
    }
}