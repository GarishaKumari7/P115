import os
source='main.txt'
dest='newfile.txt'
if os.path.exists(source):
    os.rename(source,dest)
    print("done!")
else:
    print("no!")


