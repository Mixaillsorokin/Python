import argparse
import os
import logging
from collections import namedtuple

logging.basicConfig(filename='direct_info.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)
FileInfo = namedtuple(typename='FileInfo',
                      field_names='name, ext, is_direct, parent_direct')


def direct_info(file_p: str):
    try:
        file_list = os.listdir(file_p)
    except FileNotFoundError:
        logging.error(f"Directory '{file_p}' not found.")
        return []
    direct_info = []

    for item in file_list:
        file_path = os.path.join(file_p, item)
        name = os.path.splitext(item)[0] if os.path.isfile(file_path) else item
        ext = os.path.splitext(item)[1] if os.path.isfile(file_path) else None
        is_direct = os.path.isdir(file_path)
        parent_direct = os.path.basename(file_p)
        file_info = FileInfo(name, ext, is_direct, parent_direct)
        direct_info.append(file_info)

        logging.info(
            f"Имя: {name}, Расширение файла: {ext}, Каталог: {is_direct}, "
            f"Название родительского каталога: {parent_direct}")

    return direct_info


parser = argparse.ArgumentParser(description='Directory')
parser.add_argument('--direct', type=str, help='Путь до директории')
args = parser.parse_args()

if args.direct:
    direct_path = args.direct
    direct_info = direct_info(direct_path)
with open('directory_info.txt', 'w', encoding='utf-8') as file:
    for item in direct_info:
        file.write(
            f"Имя: {item.name}, Расширение файла: {item.ext}, Каталог: {item.is_direct},"
            f" Родительская директория: {item.parent_direct}\n")