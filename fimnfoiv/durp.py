import os
GB = 1024*1024*1024 # 1GB 
x = 1
if x == 1:
    with open('large_file', 'wb') as fout:
        fout.write(os.urandom(GB)) 