

def read_md(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None




