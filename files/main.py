__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

# Code doet volgens mij wat het hoort te doen, maar de wincpy check die failt. 
# Ik ben benieuwd waar het mis gaat. 

# FileNotFoundError: [Errno 2] No such file or directory: 'C:\\Users\\Michiel\\Documents\\Winc Academy\\Back-end Development\\files\\cache\\throwaway'

# Verder maakt de wincpy check een cache folder aan, maar een niveu te hoog. Dus op het zelfde niveau als de files folder. 


import os
import zipfile
import shutil

cache_dir = "./cache"


def clean_cache():
    if os.path.isdir(cache_dir):
        shutil.rmtree(cache_dir)
    os.makedirs(cache_dir)


def cache_zip(file_path, cache_folder):
    clean_cache()
    with zipfile.ZipFile(file_path) as zip_ref:
        zip_ref.extractall(cache_folder)


def cached_files():
    files = os.listdir(cache_dir)
    files_absolute = []
    for file in files:
        files_absolute.append(os.path.abspath(cache_dir + "/" + file))
    return files_absolute


def find_password(files_list):
    for file in files_list:
        open_file = open(file, "r")
        for line in open_file:
            if "password" in line:
                return line.split(" ")[-1]


if __name__ == "__main__":
    cache_zip("data.zip", cache_dir)
    print(find_password(cached_files()))
