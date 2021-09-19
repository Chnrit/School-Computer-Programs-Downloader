##############
# 
# SCPDL
# (School Computer Programs Downloader, 학교컴 프로그램 다운)
# 
# Author: Chnrit (Chnrit@github)
# License: MIT
# 
##############

from urllib.request import urlretrieve
import os
from time import sleep

os.mkdir("SCPDL")

print("nProtectOnlineSecurity_Uninstall.exe 다운로드 중...")
urlretrieve("https://update.nprotect.net/cs/nos/uninstall/nProtectOnlineSecurity_Uninstall.exe", "./SCPDL/nProtectOnlineSecurity_Uninstall.exe")
print("nProtectOnlineSecurity_Uninstall.exe 파일 다운로드가 완료되었습니다.")

print("Firefox.exe 다운로드 중...")
urlretrieve("https://download.mozilla.org/?product=firefox-latest-ssl&os=win&lang=ko", "./SCPDL/Firefox.exe")
print("Firefox.exe 파일 다운로드가 완료되었습니다.")

print("PowerToysSetup-0.45.0.exe 다운로드 중...")
urlretrieve("https://github.com/microsoft/PowerToys/releases/download/v0.45.0/PowerToysSetup-0.45.0-x64.exe", "./SCPDL/PowerToysSetup-0.45.0.exe")
print("PowerToysSetup-0.45.0.exe 파일 다운로드가 완료되었습니다.")

print("Git-2.33.0.2-64-bit.exe 다운로드 중...")
urlretrieve("https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe", "./SCPDL/Git-2.33.0.2-64-bit.exe")
print("Git-2.33.0.2-64-bit.exe 파일 다운로드가 완료되었습니다.")

location = os.getcwd()

# open explore.exe
print("자동으로 창이 닫히고 파일 탐색기가 열립니다...")
sleep(0.5)
os.startfile(location + "/SCPDL/")