"""
752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists
of turning one wheel one slot. The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will
stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns
required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

"""

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # idea, use bfs + queue to search from 0000, change 1 digit, if fails in the deadends set, or visited before return;
        # output the min step to reach the target. for i, neighbor is (i+1) % 10, (i+9) % 10
        deadset = set(deadends)
        if '0000' in deadset or target in deadset:
            return -1
        queue = collections.deque()
        queue.append(('0000', 0))
        visited = set()
        visited.add('0000')
        while queue:
            node, step = queue.popleft()
            if node == target:
                return step
            for i in range(4):
                val = int(node[i])
                for neigh in ((val + 1) % 10, (val + 9) % 10):
                    new_node = node[:i] + str(neigh) + node[i+1:]
                    if new_node not in deadset and new_node not in visited:
                        visited.add(new_node)
                        queue.append((new_node, step + 1))
        return -1

# import collections
#
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
#
# print(Solution().openLock(deadends, target))
