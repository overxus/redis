import os, sys, shutil


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: selfbuild <xtool_source_path> <xtool_destination_directory>')
        exit(0)
    TEMPORARY_DIR = '.xtool.selfbuild.tmp'
    if os.path.exists(TEMPORARY_DIR):
        shutil.rmtree(TEMPORARY_DIR)
    os.mkdir(TEMPORARY_DIR)
    os.chdir(TEMPORARY_DIR)
    os.system(f'pyinstaller -F "{sys.argv[1]}"')
    shutil.move(
        os.path.join(os.getcwd(), 'dist', 'xtool.exe'),
        os.path.join(sys.argv[2], 'xtool.update.exe')
    )
    os.chdir(os.pardir)
    shutil.rmtree(TEMPORARY_DIR)
