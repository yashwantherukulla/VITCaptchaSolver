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
            if splits[i+1]-splits[i]>37 and splits[i+1]-splits[i]<=48:
                new_split = splits[i] + int(round((splits[i+1]-splits[i])/2,0))
                splits.append(new_split)
            elif splits[i+1]-splits[i]>48:
                ns1 = splits[i] + int(round((splits[i+1]-splits[i])/3,0))
                ns2 = ns1 + int(round((splits[i+1]-splits[i])/3,0))
                splits.append(ns1)
                splits.append(ns2)

    splits.append(width-3)
    splits.sort()
    print(splits)
    if len(splits)<7:
        print("Something went wrong with Image splitting")

    # line_img = ImageDraw.Draw(img)
    # for x in splits:
    #     line_img.line([(x,0),(x,height)], width=1)
    # img.show()

    cropped_imgs = []
    for i in range(len(splits)-1):
        xi, xf = splits[i], splits[i+1]
        cropped_img = img.crop((xi,0,xf,height))
        cropped_img = remove_white_rows(cropped_img)
        cropped_imgs.append(cropped_img)
        # cropped_img.show()
    return cropped_imgs

def bitmap_generator(folder_path_bitmaps): #till folder name (../folder/)
    bitmaps = {}
    for j in "23456789ABCDEFGHJLNPQRSTUVWXYZ":
        
        path = folder_path_bitmaps+f"{j}.jpeg"
        img = Image.open(path)
        bitmaps[j] = img.load()

    return bitmaps

def bmap_img_cropper(img, bitmap_img):
    img_map = img.load()
    bitmap_map = bitmap_img.load()
    iw, ih = img.size
    bw, bh = bitmap_img.size

    if iw<bw:
        iw = bw
    else:
        bw = iw

    if ih<bh:
        ih = bh
    else:
        bh = ih

    new_img = Image.new('L', (iw,ih), 255)
    new_img.paste(img, (iw//2, ih//2))
    new_bmap = Image.new('L', (bw,bh), 255)
    new_bmap.paste(bitmap_img, (bw//2,bh//2))


    return new_img, new_bmap

def solver(images, folder_path_bitmaps):
    bitmaps = []
    for j in "23456789ABCDEFGHJLNPQRSTUVWXYZ":
        path = folder_path_bitmaps+f"{j}.jpeg"
        bmap_img = Image.open(path)
        bitmaps.append(bmap_img)
    
    captcha = ''
    for img in images:
        matches = []
        chars = "23456789ABCDEFGHJLNPQRSTUVWXYZ"
        for ch in chars:
            match = 0
            black = 0
            mask = bitmaps[chars.index(ch)]
            new_img, new_bmap = bmap_img_cropper(img, mask)
            new_img_map = new_img.load()
            new_bmap_map = new_bmap.load()
            nw, nh = new_img.size
            for y in range(nh):
                for x in range(nw):
                    if new_img_map[x,y]==0 and new_bmap_map[x,y]==0:
                        match+=1
                    if new_bmap_map[x,y]==0:
                        black+=1
            if black==0:
                ratio = 1.1
            else:
                ratio = match/black
            matches.append([ratio,ch])
        matches.sort(key = lambda x:x[0],reverse=True)
        captcha+=matches[0][1]
        print(matches[0],matches[1],matches[2])
    return captcha






i = 3
rgba_img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/c{i}.jpeg")
folder_path_bitmaps = "D:/tech/Coding/python/python_projects/VIT CourseEnroller/bitmap_images/Final/"
#D:\tech\Coding\python\python_projects\VIT CourseEnroller\bitmap_images\Final
ans = solver(img_splitter(remove_white_rows(remove_white_cols(rgba_to_bw(rgba_img)))), folder_path_bitmaps)

print(ans)
