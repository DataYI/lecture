from pathlib import Path
import shutil
from config import Config

root = Path(Config.YD_ROOT)

folders = {
    'class_02': '6F2AF872F07440E69BB9B9A35153A2E5',
    'class_03': 'D107F40433C2415D8520D4224AC863C7',
    'class_04': 'F60FA2F7BDBE477D9DD3E66E97642519'
}

def update(file_name):
    source =  root / f'{folders[file_name]}/{file_name}.md'
    destination = Path(f'files/{file_name}.md')
    shutil.copy(source, destination)

