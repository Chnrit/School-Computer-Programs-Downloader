# School Computer Programs Downloader
학교 컴퓨터 (주로 학교 컴퓨터실 안에 있는 컴퓨터)에서 사용되는 프로그램을 모아 한꺼번에 다운로드받을 수 있는 프로그램

다운로드되는 파일
* Firefox Setup
* Firefox Developer Edition Setup
* Git for Windows Setup
* nProtect Uninstall
* PowerToys Setup
* DiscordSetup
* Python 3.9.7 Installer

더 추가되었으면 하는 것이 있는 경우 문의를 해주세요.

## 사용법

### exe 파일 다운로드받기
1. [exe 파일](https://static.chnrit.com/downloads/SCPD/1.0.1.3/SCPDServer1.0.1.3.exe)을 바로 다운로드받거나 [릴리즈 페이지](https://github.com/Chnrit/School-Computer-Programs-Downloader/releases/)에 방문하여 다운받습니다.
2. exe 파일을 더블클릭하여 실행합니다.
3. 콘솔 표시가 뜨고 파일이 다운로드될 때까지 기다립니다.
4. 다운로드가 완료되면 파일 탐색기가 열립니다.

### Python 파일을 직접 실행하기 (최신 버전)
1. 이 레포지토리를 다운로드합니다.
2. [python.org](https://www.python.org)에서 Python을 다운로드합니다.
3. 이 레포지토리로 이동하여 `python -u dlfromserver.py` 로 파일을 실행합니다.

## 주의사항
* dlfromchnrit.py 는 더이상 유지관리되지 않습니다.
* 본 프로그램은 파일 (.py, .exe)이 존재하는 폴더에서 `SCPD` 하위 폴더를 생성한 후 그 위치에 파일을 다운로드합니다. 따라서 파일과 같은 위치에 SCPD 폴더가 이미 존재하는 경우 작동하지 않습니다.
* 인터넷이 연결되어 있어야만 프로그램이 정상적으로 작동합니다.

## 개인정보와 안전성
**본 프로그램은 사용자의 개인정보를 전혀 수집하지 않으며 PC에 변형을 발생시키지 않습니다.**

다만 본 프로그램의 사용에 따라 인터넷에서 서버로 요청을 보내므로 해당 서버에 IP 주소와, 접속 로그가 기록될 수 있습니다. 이때 요청을 저의 서버로 보낸 경우 저도 이 정보를 확인할 수 있습니다.

## 참고
* Python 버전: 3.9.8
* 컴파일: Windows 11 Pro (ARM64 Insider Preview), pyinstaller
* Windows 10, 11 이외 운영체제에서의 작동을 보장하지 않습니다.
* **중요! 본 소프트웨어의 exe 파일은 .py 확장자의 파일을 그대로 사용해 컴파일되었습니다. 그 어떤 변형도 존재하지 않음을 알려드립니다. Microsoft Edge를 비롯한 브라우저들에서 악성 소프트웨어로 감지하고 있는데 이것을 사용하고자 하시면 무시하고 진행하시기 바랍니다.** 이 프로그램을 신뢰하지 않을 경우 진행하지 마세요.