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