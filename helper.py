#!/usr/bin/python3 -u
import os
import os.path
import re
import subprocess
import urllib.parse

def show_file(real_filepath):
  print(os.path.join('/tmp/https%3A%2F%2Fgithub%2ecom%2FAmitMendl%2Flegit%2egit', real_filepath))
  result = subprocess.run(["cat", os.path.join("/tmp/https%3A%2F%2Fgithub%2ecom%2FAmitMendl%2Flegit%2egit/", real_filepath)], capture_output=True)
  # if result.returncode != 0:
  #   print("Error while retrieving file content.")
  #   return
  print(result)
  print(result.stdout.decode())

if __name__ == '__main__':
  show_file('/flag')