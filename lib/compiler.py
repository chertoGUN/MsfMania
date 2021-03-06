from lib import core
import subprocess


def ADD_ICON():
    core.ICON()

    ICON = core.CORE_INPUT()

    return ICON


def AUTO_COMPILE(FILENAME, ARCHITECTURE, ICON):
    if ARCHITECTURE == "X64":
        if ICON != "":

            core.COMPILATION_STARTED()

            RC = 'id ICON "icon/'
            RC += ''.join((ICON, '"\n'))

            with open('icon/MsfMania.rc', 'w') as f:
                f.write(RC)

            WINDRES = ['windres', 'icon/MsfMania.rc', '-O', 'coff', '-o', 'icon/MsfMania.res']
            subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            EXE = ['x86_64-w64-mingw32-gcc', 'source.c', 'icon/MsfMania.res', '-s', '-w', '-o', FILENAME]
            subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_SOURCEFILE = ['rm', 'source.c']
            subprocess.run(RM_SOURCEFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_RCFILE = ['rm', 'icon/MsfMania.rc']
            subprocess.run(RM_RCFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_RESFILE = ['rm', 'icon/MsfMania.res']
            subprocess.run(RM_RESFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            core.COMPILATION_COMPLETED()

        else:

            core.COMPILATION_STARTED()

            EXE = ['x86_64-w64-mingw32-gcc', 'source.c', '-s', '-w', '-o', FILENAME]
            subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_SOURCEFILE = ['rm', 'source.c']
            subprocess.run(RM_SOURCEFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            core.COMPILATION_COMPLETED()

    elif ARCHITECTURE == "X86":
        if ICON != "":

            core.COMPILATION_STARTED()

            RC = 'id ICON "icon/'
            RC += ''.join((ICON, '"\n'))

            with open('icon/MsfMania.rc', 'w') as f:
                f.write(RC)

            WINDRES = ['windres_1', 'icon/MsfMania.rc', '-O', 'coff', '-o', 'icon/MsfMania.res']
            subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            EXE = ['i686-w64-mingw32-gcc', 'source.c', 'icon/MsfMania.res', '-s', '-w', '-o', FILENAME]
            subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_SOURCEFILE = ['rm', 'source.c']
            subprocess.run(RM_SOURCEFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_RCFILE = ['rm', 'icon/MsfMania.rc']
            subprocess.run(RM_RCFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_RESFILE = ['rm', 'icon/MsfMania.res']
            subprocess.run(RM_RESFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            core.COMPILATION_COMPLETED()

        else:

            core.COMPILATION_STARTED()

            EXE = ['i686-w64-mingw32-gcc', 'source.c', '-s', '-w', '-o', FILENAME]
            subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            RM_SOURCEFILE = ['rm', 'source.c']
            subprocess.run(RM_SOURCEFILE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            core.COMPILATION_COMPLETED()
