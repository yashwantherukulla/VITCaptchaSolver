import shutil

file_titles = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
file_names = ['NA', '18', '34', '89', '30', '69', '45', '48', '74', 'NA', '100', '36', '92', '29', '35', '82', '27', '4', 'NA', '17', 'NA', '70', 'NA', '23', 'NA', '11', '101', '99', '113', '85', '57', '73', '24', '66', '41', '83']

aft = '23456789ABCDEFGHJLNPQRSTUVWXYZ' #actual_file_titles
afn = ['18', '34', '89', '30', '69', '45', '48', '74', '100', '36', '92', '29', '35', '82', '27', '4', '17', '70', '23', '11', '101', '99', '113', '85', '57', '73', '24', '66', '41', '83']
#print(list(zip(afn,aft)))

for i,j in list(zip(afn,aft)):
        src = f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/bitmap_images/{i}.jpeg"
        dst = f"D:/tech/Coding/python/python_projects/VIT CourseEnroller/bitmap_images/Final/{j}.jpeg"
        shutil.copyfile(src, dst)
