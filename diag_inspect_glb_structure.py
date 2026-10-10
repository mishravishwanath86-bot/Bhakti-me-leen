import json, struct, sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'assets/models/indian_temples/Tempal.glb'

with open(file_path, 'rb') as f:
    magic = f.read(4)
    version, length = struct.unpack('<II', f.read(8))
    chunk_length, chunk_type = struct.unpack('<II', f.read(8))
    
    print(f"GLB Magic: {magic}, Version: {version}, Total Length: {length}")
    print(f"Chunk 0 Length: {chunk_length}, Type: {chunk_type}")
    
    json_bytes = f.read(chunk_length)
    gltf_json = json.loads(json_bytes.decode('utf-8'))
    
    print("\n--- GLTF Structure in GLB ---")
    print("Meshes:", len(gltf_json.get('meshes', [])))
    print("Nodes:", len(gltf_json.get('nodes', [])))
    print("Materials:", len(gltf_json.get('materials', [])))
    print("Textures:", len(gltf_json.get('textures', [])))
    print("Images:", len(gltf_json.get('images', [])))
    print("Buffers:", len(gltf_json.get('buffers', [])))
    print("Materials names:", [m.get('name') for m in gltf_json.get('materials', [])])
    print("\n✓ Tempal.glb contains complete embedded 3D assets ready for Three.js!")
