##############
# 
# SCPDL
# (School Computer Programs Downloader, 학교컴 프로그램 다운)
# 
# Author: Chnrit (Chnrit@github)
# License: MIT
# Version: 1.0.1.1
# 
##############

from urllib.request import urlretrieve
import os
import os.path
import shutil
from time import sleep

# download에 대한 함수를 정의
def download(filename, fileurl):
    print(filename + " 다운로드 중...")
    print("요청: " + fileurl)
    urlretrieve(fileurl, "./SCPD/" + filename)
    print(filename + "파일 다운로드가 완료되었습니다.\n")

# 폴더 체크 단계
dir = "SCPD"
print(dir +" 폴더 생성을 시도합니다...")
if os.path.isdir(dir):
    print(dir + " 폴더가 이미 존재합니다.")

    SCPDFileList = os.listdir(dir)
    modifiedFileList = ', '.join(SCPDFileList)

    print("폴더에 존재하는 파일: {}".format(modifiedFileList))
    print("**중요** 폴더를 삭제한 후 프로그램을 다시 실행해 주세요.")

    deldir = input("폴더를 삭제할까요? [Y/n] ")

    if deldir == "Y" or deldir == "y":
        shutil.rmtree(dir)
        print(dir + " 폴더를 삭제했습니다.")
    else:
        print(dir + " 폴더 삭제를 취소했습니다.")
else:
    os.mkdir("SCPD")
    print("SCPD 폴더 생성이 완료되었습니다.\n")

    download("nProtectOnlineSecurity_Uninstall.exe", "https://update.nprotect.net/cs/nos/uninstall/nProtectOnlineSecurity_Uninstall.exe")

    download("Firefox.exe", "https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=ko")

    download("PowerToysSetup-0.45.0.exe", "https://github.com/microsoft/PowerToys/releases/download/v0.45.0/PowerToysSetup-0.45.0-x64.exe")

    download("Git-2.33.0.2-64-bit.exe", "https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe")

    location = os.getcwd()

    # open explore.exe
    print("자동으로 창이 닫히고 파일 탐색기가 열립니다...")
    sleep(0.5)
    os.startfile(location + "/SCPD/")