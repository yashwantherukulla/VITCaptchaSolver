from PIL import Image, ImageDraw
import numpy as np

def save_img(img, path):
    img.save(path)

def rgba_to_bw(rgba_img):
    threshold = 95
    fn = lambda x : 255 if x > threshold else 0
    img = rgba_img.convert('L').point(fn, mode='1')
    pixel_map = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if pixel_map[x,y]!=0:
                pixel_map[x,y]=255
    #img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/temp_processed_imgs/tpc{i}.jpeg")
    return img


def remove_white_cols(processed_img):
    arr = np.array(processed_img)
    pixel_map = processed_img.load()
    width, height = processed_img.size
    white_cols = []
    for x in range(width-3):
        white = True
        for y in range(height):
            if pixel_map[x,y]==0:
                white = False
                break
            if pixel_map[x+1,y]==0:
                white = False
                break
            if pixel_map[x+2,y]==0:
                white = False
                break
            if pixel_map[x+3,y]==0:
                white = False
                break
        if white:
            white_cols.append(x)
    try:
        new_arr = np.delete(arr,white_cols,axis=1)
        white_col_removed_img = Image.fromarray(new_arr)
        #white_col_removed_img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/temp_processed_imgs/tclpc{i}.jpeg")
        return white_col_removed_img
    except:
        print("No white column found")

def remove_white_rows(white_col_removed_img):
    arr = np.array(white_col_removed_img)
    pixel_map = white_col_removed_img.load()
    width, height = white_col_removed_img.size
    white_rows = []
    for y in range(height-2):
        white = True
        for x in range(width):
            if pixel_map[x,y]==0:
                white = False
                break
            if pixel_map[x,y+1]==0:
                white = False
                break
            if pixel_map[x,y+2]==0:
                white = False
                break
        if white:
            white_rows.append(y)
    try:
        new_arr = np.delete(arr,white_rows,axis=0)
        white_row_removed_img = Image.fromarray(new_arr)
        #white_row_removed_img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/temp_processed_imgs/trlpc{i}.jpeg")
        return white_row_removed_img
    except:
        print("No white row found")

def img_splitter(img):
    width,height = img.size
    pixel_map = img.load()
    splits = []
    for x in range(width-3):
        white = True
        for y in range(height):
            if pixel_map[x,y]==0:
                white = False
                break
            if pixel_map[x+1,y]==0:
                white = False
                break
            if pixel_map[x+2,y]==0:
                white = False
                break
        if white:
            splits.append(x)
    

    if len(splits)<6:
        for i in range(len(splits)-1):
            if 37<splits[i+1]-splits[i]<=50:
                new_split = splits[i] + int(round((splits[i+1]-splits[i])/2,0))
                splits.append(new_split)
            elif splits[i+1]-splits[i]>50:
                ns1 = splits[i] + int(round((splits[i+1]-splits[i])/3,0))
                ns2 = ns1 + int(round((splits[i+1]-splits[i])/3,0))
                splits.append(ns1)
                splits.append(ns2)

    splits.append(width-3)
    splits.sort()
    print(splits)

    # line_img = ImageDraw.Draw(img)
    # for x in white_cols:
    #     line_img.line([(x,0),(x,height)], width=1)
    # img.show()

    return splits

def bitmap_generator(img, splits):
    width, height = img.size
    cropped_imgs = []
    for i in range(len(splits)-1):
        xi, xf = splits[i], splits[i+1]
        cropped_img = img.crop((xi,0,xf,height))
        cropped_img = remove_white_rows(cropped_img)
        cropped_imgs.append(cropped_img)
    return cropped_imgs


def solver(img, white_cols):
    pixel_map = img.load()
    width, height = img.size
    captcha = ""
    for i in white_cols:
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
    return captcha

x = 1
for i in range(1,20):    
    rgba_img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/c{i}.jpeg")
    b_img = bitmap_generator(remove_white_rows(remove_white_cols(rgba_to_bw(rgba_img))),splits=img_splitter(remove_white_rows(remove_white_cols(rgba_to_bw(rgba_img)))))
    for letter in b_img:
        letter.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/bitmap_images/{x}.jpeg")
        x+=1