
import os, glob

def analyze_codebase(path='.'):
    """Traverse files under path and return a small context dictionary."""
    files = []
    for root, dirs, filenames in os.walk(path):
        for fn in filenames:
            if fn.endswith(('.py', '.md', '.ipynb')):
                rel = os.path.relpath(os.path.join(root, fn), path)
                files.append(rel)
    return {'files': sorted(files)}
