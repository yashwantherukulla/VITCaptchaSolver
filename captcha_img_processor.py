from PIL import Image

# for i in range(1,20):
#     rgba_img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/c{i}.jpeg")
#     img = rgba_img.convert('L')
#     pixel_map = img.load()
#     width, height = img.size

#     for x in range(width):
#         for y in range(height):
#             l = pixel_map[x,y]
#             if l<95:
#                 pixel_map[x,y]=0
#             else:
#                 pixel_map[x,y]=255

#     img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/processed_imgs/pc{i}.jpeg")

for i in range(1,20):
    rgba_img = Image.open(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/c{i}.jpeg")
    threshold = 95
    fn = lambda x : 255 if x > threshold else 0
    img = rgba_img.convert('L').point(fn, mode='1')
    pixel_map = img.load()
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if pixel_map[x,y]!=0:
                pixel_map[x,y]=255
    img.save(f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/captcha_img_data/processed_imgs/pc{i}.jpeg")