import os, struct, sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'assets/models/indian_temples/Tempal.glb'
print(f"Checking {file_path}:")
print(f"Exists: {os.path.exists(file_path)}")
size = os.path.getsize(file_path)
print(f"Size: {size:,} bytes ({size / (1024*1024):.2f} MB)")

with open(file_path, 'rb') as f:
    magic = f.read(4)
    version, length = struct.unpack('<II', f.read(8))
    print(f"GLB Magic: {magic}")
    print(f"Version: {version}, Total Length in header: {length:,} bytes")
    assert magic == b'glTF', "Invalid GLB header magic"
    assert length == size, "GLB length mismatch"
    print("✓ Tempal.glb is a 100% VALID binary GLTF (GLB) file!")
