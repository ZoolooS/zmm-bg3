################################################################################
# Copyright © 2023 Ilya Popov aka ZoolooS. All rights reserved.                #
# Author: Ilya Popov aka ZoolooS                                               #
# Description:                                                                 #
#     This file is the part of "ZoolooS's mods merger for BG3" application     #
################################################################################
from pathlib import Path
import shutil
import zipfile

from bin.consts import AppConsts


# TODO: Реализовать классы (
#           Mod,
#           ModArchived,
#           ModUnarchived,
#           ModPaked,
#           ModUnpaked,
#           Archiver,
#           Paker
#       ) и вынести в нужные модули (если нужно)
class Mod:
    # TODO: Mod - abstract parent without exemplars.
    #       Bunch of exact mod type classes - children with exact params and methods.
    def __init__(self,
                 name,
                 file_name,
                 mod_path,
                 path_to_destination):
        self.name = name
        self.file_name = file_name
        self.mod_path = mod_path
        self.path_to_destination = path_to_destination


class Archiver:
    def __init__(self, path_to_archiver, archiver_type):
        self.path_to_archiver = path_to_archiver
        self.archiver_type = archiver_type

    def path(self):
        return self.path_to_archiver

    def arch_type(self):
        return self.archiver_type


class ModArchived(Mod):
    def __init__(self,
                 name,
                 file_name,
                 mod_path,
                 path_to_destination,
                 arch_type):
        super().__init__(name, file_name, mod_path, path_to_destination)
        self.arch_type = arch_type  # 'zip', '7z', 'rar'
        # path_to_archive = ''  # Mod.mod_path
        # path_to_destination = ''  # Mod.path_to_destination

    def unpack_archive(self, arch_type, path_to_archiver, path_to_archive, path_to_destination):
        if arch_type == 'zip':
            self.unpack_zip(path_to_archiver, path_to_archive, path_to_destination)
        if arch_type == '7z':
            self.unpack_7z(path_to_archiver, path_to_archive, path_to_destination)
        if arch_type == 'rar':
            self.unpack_rar(path_to_archiver, path_to_archive, path_to_destination)
        else:
            pass  # TODO: Rise Exception

    def unpack_zip(self, path_to_archiver, path_to_archive, path_to_destination):
        if path_to_archiver:
            self.unpack_zip_c(path_to_archiver, path_to_archive, path_to_destination)
            # TODO: and exit

        shutil.unpack_archive(path_to_archive, path_to_destination)
        # or
        # with zipfile.ZipFile(path_to_archive, 'r') as zip_ref:
        #     zip_ref.extractall(path_to_destination)

    def unpack_zip_c(self, path_to_archiver, path_to_archive, path_to_destination):
        pass

    def unpack_7z(self, path_to_archiver, path_to_archive, path_to_destination):
        pass

    def unpack_rar(self, path_to_archiver, path_to_archive, path_to_destination):
        pass


class ModUnarchived(Mod):
    def __init__(self):
        arch_type = ''  # 'zip', '7z', 'rar'
        # path_to_source = ''  # Mod.path
        # path_to_destination = ''  # Mod.path_to_destination


class Paker:
    """ Mod-files for BG3 is *.pak files, so class name is Paker not Packer. """
    def __init__(self):
        path_to_paker = ''


class ModPaked(Mod):
    pass


class ModUnpaked(Mod):
    pass


# TODO: Классы ArchiveUnpacker, ArchivePacker, PakUnpacker, PakPacker переделать в классы
#       Mod, ModArchived, ModUnarchived, ModPaked, ModUnpaked, Archiver, Paker
class ArchiveUnpacker:
    arch_type = ''  # 'zip', '7z', 'rar'
    path_to_archiver = ''
    path_to_archive = ''
    path_to_destination = ''

    def unpack_archive(self, arch_type, path_to_archiver, path_to_archive, path_to_destination):
        if arch_type == 'zip':
            self.unpack_zip(path_to_archiver, path_to_archive, path_to_destination)
        if arch_type == '7z':
            self.unpack_7z(path_to_archiver, path_to_archive, path_to_destination)
        if arch_type == 'rar':
            self.unpack_rar(path_to_archiver, path_to_archive, path_to_destination)
        else:
            pass  # TODO: Rise Exception

    def unpack_zip(self, path_to_archiver, path_to_archive, path_to_destination):
        if path_to_archiver:
            self.unpack_zip_cmd(path_to_archiver, path_to_archive, path_to_destination)
            # TODO: and exit

        shutil.unpack_archive(path_to_archive, path_to_destination)
        # or
        # with zipfile.ZipFile(path_to_archive, 'r') as zip_ref:
        #     zip_ref.extractall(path_to_destination)

    def unpack_zip_cmd(self, path_to_archiver, path_to_archive, path_to_destination):
        pass

    def unpack_7z(self, path_to_archiver, path_to_archive, path_to_destination):
        pass

    def unpack_rar(self, path_to_archiver, path_to_archive, path_to_destination):
        pass


class ArchivePacker:
    arch_type = ''  # 'zip', '7z', 'rar'
    path_to_archiver = ''
    path_to_source = ''
    path_to_destination = ''

    def pack_archive(self, arch_type, path_to_archiver, path_to_source, path_to_destination, archive_name='archive'):
        if arch_type == 'zip':
            self.pack_zip(path_to_archiver, path_to_source, path_to_destination, archive_name)
        if arch_type == '7z':
            self.pack_7z(path_to_archiver, path_to_source, path_to_destination)
        if arch_type == 'rar':
            self.pack_rar(path_to_archiver, path_to_source, path_to_destination)
        else:
            pass  # TODO: Rise Exception

    def pack_zip(self, path_to_archiver, path_to_source, path_to_destination, archive_name):
        if path_to_archiver:
            self.pack_zip_cmd(path_to_archiver, path_to_source, path_to_destination)
            # TODO: and exit

        # shutil.make_archive(archive_name, 'zip', path_to_source, path_to_destination)
        shutil.make_archive(archive_name, 'zip', path_to_source)
        # or
        # with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        #     zip_ref.extractall(directory_to_extract_to)

    def pack_zip_cmd(self, path_to_archiver, path_to_source, path_to_destination):
        pass

    def pack_7z(self, path_to_archiver, path_to_source, path_to_destination):
        pass

    def pack_rar(self, path_to_archiver, path_to_source, path_to_destination):
        pass


class PakUnpacker:
    pass


class PakPacker:
    pass
