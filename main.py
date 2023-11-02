################################################################################
# Copyright © 2023 Ilya Popov aka ZoolooS. All rights reserved.                #
# Author: Ilya Popov aka ZoolooS                                               #
# Description:                                                                 #
#     This file is the part of "ZoolooS's mods merger for BG3" application     #
################################################################################
import json
import time
from os import listdir
from os.path import isfile, join
from pathlib import Path

from bin.consts import AppConsts
from bin.archivers import *


def main(name):
    # TODO: It need's to be just runner for:
    #       - read settings
    #       - set settings (when GUI will appears)
    #       - run unarch process: - get next archived mod ->
    #                             - unarch to destination (to unique folder name each) ->
    #                             - repeat
    #       - run unpak process: - get next pak file ->
    #                            - unpak to destination (to unique folder name each) ->
    #                            - move/copy settings json to destination if exist ->
    #                            - repeat
    #       - run merge process: - get old Result mod or create empty Result mod ->
    #                            - get next unpaked mod (sets of folders and files) ->
    #                            - merge mod to Result mod (with rewrite old mod datastrings or ask user what to do) ->
    #                            - merge mod names to Result mod settings file ->
    #                            - merge mod settings to Result mod settings if needed ->
    #                            - repeat
    #       - run pak process: - get Result mod folder ->
    #                          - pak Result mod folder to *.pak
    #       - place *.pak to game mod folder (optional)
    #       - place unpaked Result mod to game raw mod folder (optional)
    #       - clear all tmp files and folders (optional)

    print(f'Hi, {name}')

    CONSTS = AppConsts()
    print(f'{CONSTS.SETTINGS["FILE_NAME_BKP"]}.{CONSTS.SETTINGS["FILE_TYPE"]}')

    # Archives
    print('Unpacking start!!!!!!!')
    source = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_IN"]}'
    destination = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_OUT"]}'
    onlyfiles = [f for f in listdir(source) if isfile(join(source, f)) and f != '.gitignore']
    for file in onlyfiles:
        archiveUnpack = ArchiveUnpacker()
        archiveUnpack.unpack_archive('zip', None, f'{source}/{file}', f'{destination}/{file[:-4]}')
    print('Done!!!!!!!')

    time.sleep(5)

    print('Packing start!!!!!!!')
    source = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_OUT"]}'
    destination = f'{CONSTS.DIRS["WD"]}/{CONSTS.DIRS["WD_TMP"]}'
    dirs = [d for d in listdir(source) if d != '.gitignore']
    for dir_ in dirs:
        archivePack = ArchivePacker()
        archivePack.pack_archive('zip', None, f'{source}/{dir_}', destination, dir_)
    print('Done!!!!!!!')


if __name__ == '__main__':
    main('Boo')
