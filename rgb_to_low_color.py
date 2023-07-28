from PIL import Image, ImageFilter
import cv2

vidcap = cv2.VideoCapture('vid.mp4')
success, image = vidcap.read()
count = 0
height, width, layers = image.shape
size = (width,height)
out = cv2.VideoWriter('cartoon.avi',cv2.VideoWriter_fourcc(*'DIVX'), 3, size)

h = 2
n = 25
new = 7
while success:
    rows,cols,_ = image.shape
    img1 = Image.new("RGB", (cols, rows), 'black')
            
    for i in range(rows):
        for j in range(cols):
            r = image[i,j][2] // new*new
            g = image[i,j][1] // new*new
            b = image[i,j][0] // new*new

            img1.putpixel((j,i), (r // n * n + (n//h), g // n * n + (n//h), b // n * n + (n//h)))

##    img1 = img1.filter(ImageFilter.FIND_EDGES)
    img1 = img1.convert("L")
    img1.save(str(count) + ".jpg")
        
    count += 1

    success, image = vidcap.read()
