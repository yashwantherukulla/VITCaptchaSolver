from PIL import Image

img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/processed_imgs/pc1.jpeg")
pixel_map = img.load()
width, height = img.size
for i in range(width):
    for j in range(height):
        rel0 = pixel_map[i,j]
        rel1 = 255 - pixel_map[i,j]
        if pixel_map[i,j]!=0 and pixel_map[i,j]!=255:
            if rel0<rel1:
                pixel_map[i,j]=0
            else:
                pixel_map[i,j]=255
        
img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/processed_imgs/npc1.jpeg")