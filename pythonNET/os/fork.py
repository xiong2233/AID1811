import os
pid = os.fork()
if pid < 0:
    print("Create process Error")
elif pid == 0:
    print("New　process")
else:
    print("The old process")
print("fork test end...")