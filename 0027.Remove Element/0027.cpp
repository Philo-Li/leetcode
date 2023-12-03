#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left= 0;
        int right = 0;
        while (right < nums.size()) {
            if(nums[right] == val) {
                right++;
            } else {
                nums[left] = nums[right];
                left++;
                right++;
            }
        }
        return left;
    }
};

int main () {
    Solution s;
    vector<int> v{3, 2, 2, 3};
    vector<int> v2{0, 1, 2, 2, 3, 0, 4, 2};
    int ans = s.removeElement(v2, 2);
    cout << ans << endl;

    return 0;
}
