class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]

        if image[sr][sc] == color:
            return image

        image[sr][sc] = color
    
        if 0 <= sr - 1 and image[sr - 1][sc] == old:
            image = self.floodFill(image, sr - 1, sc, color)
        if 0 <= sc - 1 and image[sr][sc - 1] == old:
            image = self.floodFill(image, sr, sc - 1, color)
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == old:
            image = self.floodFill(image, sr, sc + 1, color)
        if sr + 1 < len(image) and image[sr + 1][sc] == old:
            image = self.floodFill(image, sr + 1, sc, color)

        return image
        