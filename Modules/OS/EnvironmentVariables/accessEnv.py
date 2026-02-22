import os
for key, value in os.environ.items():
    print(f"{key} = {value}")
# we get all the paths in ENV from system key = name and value = path