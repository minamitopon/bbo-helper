import os
import urllib.request, urllib.error
import time

def download_file(url, dst_path):
    with urllib.request.urlopen(url) as web_file:
        with open(dst_path, 'wb') as local_file:
            local_file.write(web_file.read())

count = 30001
file_dir = './files'
interval = 1
while count < 40001:
  url = f'https://www.bridgebase.com/tools/vugraph_linfetch.php?id={count}'
  try:
    download_file(url, os.path.join(file_dir, os.path.basename(url)))
    time.sleep(interval)
  except urllib.error.HTTPError as e:
    print(e)
  count += 1