from PIL import Image, ImageDraw
 

class Map:
    """
    Establishes starting dimensions and color for new image in pillow module, then reads in contents of txt file using with statement. That data is then placed into a list comprehension which uses a for loop to split up numbers by space and line and conmverts into integers. The max elevation is also established by the with statement."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.image = Image.new("RGB", (width, height))
        with open("elevation_small.txt") as data:
            self.list = [[int(x) for x in line.split()] for line in data] 
        self.maxelevation = max([max(n) for n in self.list])            
   



    def map_the_list(self,filename):
        for y, row in enumerate(self.list): 
            for x, num in enumerate(row):
                grayscale = int((num/self.maxelevation)*255)
                self.image.putpixel((x,y), (grayscale, grayscale, grayscale))
        return self
       

   

if __name__=="__main__":
    
    my_map = Map(600,600) 
    my_map = my_map.map_the_list("elevation_small.txt")
    my_map.image.show("elevation.png")