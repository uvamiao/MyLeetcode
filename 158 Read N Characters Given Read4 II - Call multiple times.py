"""
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

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
    # define buffer, size, and buffer_pt as control variable. be same across all calls.
    def __init__(self):
        self.buffer_pt = 0
        self.size = 0
        self.buffer = [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while i < n:
            if self.buffer_pt >= self.size: # if the buffer_pt is over the buffer size, need to read4 again
                self.size = read4(self.buffer)
                self.buffer_pt = 0 # reset buffer point from beginning !!
                if self.size == 0: # if file_content is empty
                    break
            # buffer point is within buffer size
            buf[i] = self.buffer[self.buffer_pt]
            i += 1
            self.buffer_pt += 1
        return i


if __name__ == '__main__':
    global file_content
    file_content = "filetestbuffer"
    buf = ['' for _ in range(100)]
    test = Solution()
    print(test.read(buf, 6))
    print(test.read(buf, 5))
    print(test.read(buf, 4))
    print(test.read(buf, 3))
