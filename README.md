# School Computer Programs Downloader
학교 컴퓨터 (주로 학교 컴퓨터실 안에 있는 컴퓨터)에서 사용되는 프로그램을 모아 한꺼번에 다운로드받을 수 있는 프로그램

## 사용법

### exe 파일 다운로드받기
1. [Chnrit 서버 버전](https://static.chnrit.com/downloads/SCPD/1.0.0/SCPDChnrit1.0.0.exe) 또는 [원본 서버 버전](https://static.chnrit.com/downloads/SCPD/1.0.0/SCPDServer1.0.0.exe)을 택하여 exe 파일을 바로 다운받거나 [릴리즈 페이지](https://github.com/Chnrit/School-Computer-Programs-Downloader/releases/)에 방문하여 다운받습니다.
2. exe 파일을 더블클릭하여 실행합니다.
3. 콘솔 표시가 뜨고 파일이 다운로드될 때까지 기다립니다.
4. 다운로드가 완료되면 파일 탐색기가 열립니다.

### Python 파일을 직접 실행하기 (최신 버전)
1. 이 레포지토리를 다운로드합니다.
2. [python.org](https://www.python.org)에서 Python을 다운로드합니다.
3. 이 레포지토리로 이동하여 `python -u dlfromserver.py` 로 파일을 실행합니다.

## 주의사항
본 프로그램은 파일 (.py, .exe)가 존재하는 폴더에서 `SCPD` 하위 폴더를 생성한 후 그 위치에 파일을 다운로드합니다. 따라서 파일과 같은 위치에 SCPD 폴더가 이미 존재하는 경우 어떤 오류가 발생할지 모릅니다.

인터넷이 연결되어 있어야만 프로그램이 정상적으로 작동합니다.

## 개인정보와 안전성
**본 프로그램은 사용자의 개인정보를 전혀 수집하지 않으며 PC에 번형을 발생시키지 않습니다.** 다만 본 프로그램의 사용에 따라 인터넷에서 서버로 요청을 보내므로 해당 서버에 IP 주소와, 접속 로그가 기록될 수 있습니다. 이때 요청을 저의 서버로 보낸 경우 저도 이 정보를 확인할 수 있습니다.