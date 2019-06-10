### 302. Smallest Rectangle Enclosing Black Pixels
#An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels 
#are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. 
#Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

#Input:
#[
#  "0010",
#  "0110",
#  "0100"
#]
#and x = 0, y = 2
#
#Output: 6

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # idea, use dfs and obtain the min/max of x and y. Since black pixel is connected, go four directions, dfs again. set x,y as '#' if visited. Time O(mn) and Space O(1)
        # corner case
        if not image or len(image)==0 or len(image[0])==0:
            return 0
        res = [x, x, y, y] # row_min, row_max, col_min, col_max
        self.dfs(image, x, y, res) # could also pass row_min, row_max, col_min, col_max in dfs
        return (res[1]-res[0]+1)*(res[3]-res[2]+1) # (2-1+1)*(2-0+1)=6
    # define dfs
    def dfs(self, image, x, y, res):
        m, n = len(image), len(image[0])
        # when row/col are valid and image[x][y]=='1' connected
        if x>=0 and x<m and y>=0 and y<n and image[x][y] == '1':
            # set as '#' for visited
            image[x][y] = '#'
            # update the min/max row/col
            res[0]=min(x, res[0])
            res[1]=max(x, res[1])
            res[2]=min(y, res[2])
            res[3]=max(y, res[3])
            # dfs for four directions
            self.dfs(image, x+1, y, res)
            self.dfs(image, x-1, y, res)
            self.dfs(image, x, y+1, res)
            self.dfs(image, x, y-1, res)

class Solution2(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        # idea, improve to binary search for top/bottom/left/right, and (right-left)*(bottom-top) is smallest rectangle; define searchRows and searchCols, Time O(mlogn+nlogm), Space 0(1).
        top = self.searchRows(image, 0, x, True) # ind whether update j or i
        bottom = self.searchRows(image, x+1, len(image), False)
        left = self.searchCols(image, 0, y, top, bottom, True)
        right = self.searchCols(image, y+1, len(image[0]), top, bottom, False)
        return (right-left)*(bottom-top)
    # define searchRows and searchCols
    def searchRows(self, image, i, j, ind):
        while i < j:
            mid = i + (j - i) / 2
            if ('1' in image[mid]) == ind: # True update j, False update i
                j = mid
            else:
                i = mid + 1
        return i
    def searchCols(self, image, i, j, top, bottom, ind):
        while i < j:
            mid = i + (j - i) / 2
            if any(image[k][mid] == '1' for k in range(top, bottom)) == ind: # for ym top to bottom connected, any k connected and True could update j, else update i
                j = mid
            else:
                i = mid + 1
        return i


