import os
i = 1
files = os.listdir('C:\\Users\Administrator\\Downloads')
for file in files:
    if file.endswith('.png'):
        os.rename(f'C:\\Users\Administrator\\Downloads\\{file}',f'C:\\Users\Administrator\\Downloads\\{i}.png')
        i += 1
        