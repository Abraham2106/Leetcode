import os

folder = "C:\\Users\\solan\\OneDrive\\Documents\\Leetcode\\Leetcode\\JavaSolutions\\Easy"  # change this to your actual folder name
for filename in os.listdir(folder):
    if filename.endswith(".py"):
        number = filename.split(".")[0]
        new_name = number.zfill(4) + ".py"  # pad to 4 digits
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        
