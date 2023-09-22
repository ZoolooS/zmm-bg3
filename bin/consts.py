################################################################################
# Copyright © 2023 Ilya Popov aka ZoolooS. All rights reserved.                #
# Author: Ilya Popov aka ZoolooS                                               #
# Description:                                                                 #
#     This file is the part of "ZoolooS's mods merger for BG3" application     #
################################################################################
from dataclasses import dataclass


@dataclass
class AppConsts:
    SETTINGS = {
        'FILE_NAME_BKP': 'settings_bkp',
        'FILE_NAME_CUSTOM': 'settings',
        'FILE_TYPE': 'json',
    }
    DIRS = {
        'SETTINGS': '_settings',
        'ARCHIVES': 'archivers',
        'WD': 'wd',
        'WD_IN': '_in',
        'WD_OUT': '_out',
        'WD_LOGS': 'logs',
        'WD_TMP': 'tmp'
    }
    ARCHS = ['zip', '7z', 'rar']
    DEFAULT_ARCHIVER = 'zip'
