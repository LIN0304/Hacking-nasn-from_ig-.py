import time
from tqdm import tqdm

for i in range(0, 101, 1):
    print(f"Hacking Nasa:{i}%")
    time.sleep(0.1)
for index in tqdm(range(100), desc="loading...", ascii=False, ncols=75):
    time.sleep(0.1)
print("Access Granted......!")