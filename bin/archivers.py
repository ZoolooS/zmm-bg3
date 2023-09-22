################################################################################
# Copyright © 2023 Ilya Popov aka ZoolooS. All rights reserved.                #
# Author: Ilya Popov aka ZoolooS                                               #
# Description:                                                                 #
#     This file is the part of "ZoolooS's mods merger for BG3" application     #
################################################################################
import shutil
import zipfile

from bin.consts import AppConsts


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

    def pack_archive(self, arch_type, path_to_archiver, path_to_source, path_to_destination):
        pass

    def pack_zip(self, path_to_archiver, path_to_source, path_to_destination):
        if path_to_archiver:
            self.pack_zip_cmd(path_to_archiver, path_to_source, path_to_destination)
            # TODO: and exit

        shutil.make_archive(path_to_source, path_to_destination)
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
