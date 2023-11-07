// define a TreeNode
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// 二叉树的统一迭代法



// 递归法遍历
// 前序遍历
class Solution {
public:
    void traversal(TreeNode* cur, vector<int>& vec) {
        if (cur == NULL) return;
        vec.push_back(cur->val);
        traversal(cur->left, vec);
        traversal(cur->right, vec);
    }
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        traversal(root, result);
        return result;
    }
};

// 中序遍历
void traversal(TreeNode* cur, vector<int>& vec) {
    if (cur == NULL) return;
    traversal(cur->left, vec); //left
    vec.push_back(cur->val); //middle
    traversal(cur->right, vec);  //right
}

// 后序遍历
void traversal(TreeNode* cur, vector<int>& vec) {
    if (cur == NULL) return;
    traversal(cur->left, vec); //left
    traversal(cur->right, vec); // right
    vec.push_back(cur->val); // middle
}

// 迭代法遍历
// 利用堆栈的特性，本质实现了递归的效果

// 前序遍历(middle -> left -> right) 
// push back root node, then right, and then left into the stack
// so when it pop: first top(middle), then left, then right 
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> result;
        if (root == NULL) return result;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top(); // middle
            st.pop();
            result.push_back(node->val);
            if (node->right) st.push(node->right); // right (empty node do not into stack)
            if (node->left) st.push(node->left); //left
        }
    }
};

//中序遍历(left, middle, right)
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> st;
        TreeNode* cur = root;
        while (cur != NULL || !st.empty()) {
            if (cur != NULL) { // 指针来访问节点，访问到最底层
                st.push(cur); // 将访问的节点放进栈
                cur = cur-> left;   // left
            }   else {
                cur = st.top(); // 从栈里弹出的数据，就是要处理的数据（result）
                st.pop();
                result.push_back(cur->val); // middle
                cur = cur->right; // right
            }
        } 
        return result;
    }
};

//后序遍历(left -> right -> middle)
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> st;
        vector<int> result;
        if (root == NULL) return result;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top();
            st.pop()
            result.push_back(node->val);
            // 相对于前序遍历，这更改一下入栈顺序（空节点不入栈
            if (node->left) st.push(node->left);
            if (node->right) st.push(node->right); // 空节点不入栈
            reverse(result.begin(), result.end()); // 将结果反转就是左右中的顺序了
            return result;
        }
    }
};

// 二叉树的层序遍历（广度优先遍历）
// 使用队列实现
class Solution {
public:
    vector<vector<int> levelOrder(TreeNode* root) {
        queue<TreeNode*> que;
        if (root !- NULL) que.push(root);
        vector<vector<int>> result;
        while (!que.empty()) {
            int size = que.size();
            vector<int> vec;
            // 这里一定要使用固定大小size，不要使用que.size()
            // 因为que.size是不断变化的
            for (int i = 0; i < size; i++) {
                TreeNode* node = que.front();
                que.pop();
                vec.push_back(node->val);
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
            result.push_back(vec);
        }
        return result;
    }
}

