import os
import sys
from PIL import Image

input_path = sys.argv[1] if len(sys.argv) > 1 else "LaserBeam.png"
base, ext = os.path.splitext(input_path)
output_path = sys.argv[2] if len(sys.argv) > 2 else f"{base}_mirrored{ext}"

try:
    with Image.open(input_path) as img:
        mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
        mirrored.save(output_path)
    print(f"Saved mirrored image to {output_path}")
except FileNotFoundError:
    print(f"Error: input file '{input_path}' not found.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error processing image: {e}", file=sys.stderr)
    sys.exit(1)
