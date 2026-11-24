import os
import shutil

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))
