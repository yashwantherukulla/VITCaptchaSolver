from PIL import Image
from bitmaps import bitmaps

img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/temp_processed_imgs/trlpc4.jpeg")
pixel_map = img.load()
width, height = img.size

captcha = ""
for i in range(0,width,width//6):
    matches = []
    chars = "123456789ABCDEFGHIJKLMNPQRSTUVWXYZ"
    for ch in chars:
        match = 0
        black = 0
        mask = bitmaps[ch]
        for y in range(32):
            for x in range(30):
                y1 = y+8
                x1 = x+i-30
                if pixel_map[x1,y1]==0 and mask[y][x]==0:
                    match+=1
                if mask[y][x]==0:
                    black+=1
        ratio = match/black
        matches.append([ratio,ch])
    matches.sort(key = lambda x:x[0],reverse=True)
    captcha+=matches[0][1]
    
    print(matches[0])
    # for p in range(len(matches)-1):    
    #     if matches[p][1]=='4':
    #         print(matches[p])
        

print(captcha)
