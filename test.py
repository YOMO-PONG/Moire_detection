import os
from PIL import Image

def find_min_size(directory):
    min_width, min_height = float('inf'), float('inf')
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                path = os.path.join(root, file)
                with Image.open(path) as img:
                    width, height = img.size
                    if width < min_width:
                        min_width = width
                    if height < min_height:
                        min_height = height
    return min_width, min_height

def crop_images_to_min_size(input_dir, output_dir, min_size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                input_path = os.path.join(root, file)
                with Image.open(input_path) as img:
                    cropped_img = img.crop((0, 0, min_size[0], min_size[1]))
                    output_path = os.path.join(output_dir, file)
                    cropped_img.save(output_path)
                    print(f"Processed and saved: {output_path}")

# 使用示例
input_directory = '/home/pengchi/ID_classfication0311/classfication/dataset/test_shoupai/photograph'  # 替换成你的目标输入目录
output_directory = './test_moire_idcard'  # 替换成你想保存输出图片的目录

# 查找最小尺寸
min_size = find_min_size(input_directory)
print(f"Minimum size found: Width = {min_size[0]}, Height = {min_size[1]}")

# 裁剪并保存图片
crop_images_to_min_size(input_directory, output_directory, min_size)