import os
print(os.path.abspath("chromedriver-win64/chromedriver.exe")) # 印出當前檔案的絕對路徑
import subprocess
chrome_version = subprocess.getoutput(r"D:\nutn_school\python_class\chromedriver-win64\chromedriver.exe --version")
print("Install Chrome version: ", chrome_version) # 印出 Chrome Driver 的版本