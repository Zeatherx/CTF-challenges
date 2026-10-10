# Challenge : Time Is Important
## Solution
1. To Solve this challange the player must notice several things.First Notice that the flag changing every second, so the time format used to decrypt it is ```YearMonthDayHourMinuteSecond```
2. Second, notice that ```"c2FsdA"``` in ```material =# time_str + "c2FsdA"``` is actually a base64 that when you converted it to text it become ```"salt"```
3. Third, notice that in the description, the author mentioned, ```Btw, i like Japan```. This is actually a hint that they were using the Tokyo time zone rather than Hong Kong's.
4. Fourth, note that the message was encrypted using a XOR method. Since XOR is a symmetric cipher, it can also be decrypted using the exact same process. After Notice those four things we can start to create a script to decrypt this. 
5. Below is the script used to decrypt it. What we need to do is make the minute is the same and the second can be brute force easily.
```python
from datetime import datetime
import hashlib

CIPHERTEXT_HEX = (
    "65bef725c9da25eedea37362bb8e831e9eca9ba0ad1b74020aeb1f2fc5cf7224058d8d12b88d21f1bea82837e69cd04ef7f087"
)

def xor_crypt(data: bytes, key: bytes) -> bytes:
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

def key_from_timestr(time_str: str) -> bytes:
    material = time_str + "Salt"
    return hashlib.sha256(material.encode()).digest()

def main():
    ct = bytes.fromhex(CIPHERTEXT_HEX)
    base = "202601300042"

    for ss in range(60):
        time_str = f"{base}{ss:02d}"
        key = key_from_timestr(time_str)
        pt = xor_crypt(ct, key)

        if b"PUCTF26{" in pt:
            print(pt.decode("utf-8", errors="replace"))
            return

    print("Not found")

if __name__ == "__main__":
    main()
```
6. After running the program it will output the flag.
```
PUCTF26{Tim3lsk3Y_a3f9c2e4b1d8aa0f9c7e2d4b6f1a8c0e}
```