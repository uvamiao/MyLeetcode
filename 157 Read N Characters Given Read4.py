"""
Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". We read a total of 3 characters from the file,
so return 3. Note that "abc" is the file's content, not buf. buf is the destination buffer that you will have to write the results to.
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
"""
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1

    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # Idea, create length 4 buffer, for i in range(n/4+1), obtain size = read4(buffer), if size > 0, update buf
        # [cnt, cnt+size] with buffer, cnt += size; else, break. output the min of (cnt, n). Time O(n), Space O(1).
        buffer = [''] * 4
        cnt = 0
        for i in range(n//4 + 1):
            size = read4(buffer)
            if size > 0:
                buf[cnt: cnt+size] = buffer
                cnt += size
            else:  # size == 0, read all file
                break
        return min(cnt, n)

if __name__ == '__main__':
    global file_content
    buf = ['' for _ in range(100)]
    file_content = "a"
    print(buf[:Solution().read(buf, 9)])
    file_content = "abcdefghijklmnop"
    print(buf[:Solution().read(buf, 9)])
