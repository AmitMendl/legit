#!/usr/bin/python3 -u
import os
import os.path
import re
import subprocess
import urllib.parse

_REPO_DIR = '/mnt/c/Users/amitm/Downloads/googlectf2022/LEGIT/legit'

def show_file(filepath):
      
  real_filepath = os.path.realpath(os.path.join(_REPO_DIR, filepath))
  print(_REPO_DIR + filepath)
  print(os.path.join(_REPO_DIR, filepath))
  print(real_filepath)
  if _REPO_DIR != os.path.commonpath((_REPO_DIR, real_filepath)):
    print("Hacker detected!")
    return    
  result = subprocess.run(["cat", os.path.join(_REPO_DIR, real_filepath)], capture_output=True)
  if result.returncode != 0:
    print("Error while retrieving file content.")
    return
  print(result)
  print(result.stdout.decode())

if __name__ == '__main__':
  show_file('test/file')