# 네이버 스마트스토어 매크로 for Mac M1

네이버 스마트스토어 상품을 자동으로 구매해주는 매크로입니다.

- Mac M1에 최적화되어 있습니다.

- python3가 설치되어 있다고 가정합니다.

## How to macro

1. 현 레포지토리를 clone 합니다.
```
git clone https://github.com/redorangeyellowy/naver_smartstore_macro.git
```
2. Clone한 디렉토리에 가상환경을 만들어줍니다.
```
cd naver_smartstore_macro
python3 -m venv macro
source macro/bin/activate
```
3. `selenium` 라이브러리를 설치합니다.
```
pip install selenium
```
4. 크롬 드라이버를 다운받은 후, clone한 디렉토리에 넣어줍니다.
- [여기](https://chromedriver.chromium.org/downloads)에 들어가서 자신의 크롬 버전과 일치하는 드라이버를 다운받습니다.
- 크롬 버전은 `크롬 오른쪽 상단 ... 클릭 -> 도움말 -> Chrome 정보`에 들어가면 확인할 수 있습니다.
5. 자신의 네이버 아이디, 비밀번호를 base64 인코딩합니다.
- [여기](https://www.base64encode.org/)에 들어가서 아이디, 비밀번호를 각각 인코딩합니다.
- 인코딩한 값을 `config.json`에 입력해줍니다.
6. 파이썬 스크립트를 실행합니다.
```
python3 run_macro.py --target "해당 상품 링크"
```
- `sh: Pause: command not found`와 같은 에러가 뜬다면, 크롬 드라이버가 있는 디렉토리로 들어간 후 아래 커맨드를 실행합니다.
```
xattr -d com.apple.quarantine chromedriver
```
