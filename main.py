################################################################################
# Copyright © 2023 Ilya Popov aka ZoolooS. All rights reserved.                #
# Author: Ilya Popov aka ZoolooS                                               #
# Description:                                                                 #
#     This file is the part of "ZoolooS's mods merger for BG3" application     #
################################################################################
import json
from os import listdir
from os.path import isfile, join

from bin.consts import AppConsts
from bin.archivers import *


def main(name):
    print(f'Hi, {name}')

    CONSTS = AppConsts()
    print(f'{CONSTS.SETTINGS["FILE_NAME_BKP"]}.{CONSTS.SETTINGS["FILE_TYPE"]}')

    # Archives
    # some code
    print('Unpacking start!!!!!!!')
    # unpack = ArchiveUnpacker(arch_type, path_to_archiver, path_to_archive, path_to_destination)

    source = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_IN"]}'
    destination = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_OUT"]}'
    onlyfiles = [f for f in listdir(source) if isfile(join(source, f)) and f != '.gitignore']
    for file in onlyfiles:
        archive = ArchiveUnpacker()
        archive.unpack_archive('zip', None, f'{source}/{file}', f'{destination}/{file[:-4]}')

    print('Done!!!!!!!')


if __name__ == '__main__':
    main('Boo')
