import os
import shutil

base_dir = 'pliki/' 
copy_dir = os.path.join(base_dir, 'kopie')

os.makedirs(copy_dir, exist_ok=True)
current_dir = os.getcwd()

report = []

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if os.path.isdir(folder_path) and folder != 'kopie':
        report.append(f'Folder: {current_dir}/{folder_path}')
        for i, file in enumerate(os.listdir(folder_path)):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path) and file.lower().endswith(('.jpg', '.png', '.jpeg')):
                new_file_name = f'{folder}_{i}{os.path.splitext(file)[1]}'
                report.append(f'\tOld file name: {file} -> New file name: {new_file_name}')
                shutil.copy2(file_path, os.path.join(copy_dir, new_file_name))

with open(base_dir + 'raport.txt', 'w') as f:
    for line in report:
        f.write(f'{line}\n')