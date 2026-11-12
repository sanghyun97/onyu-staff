# 온유 작가 내려받기 사이트

https://sanghyun97.github.io/onyu-staff/ — 소개, 맥 앱 내려받기, 설치 안내, 변경 기록.

- 페이지는 `_build.py`가 만든다: 내용·버전 기본값을 고치고 `python3 _build.py`.
- 모양은 온유 리모트 사이트(`~/Documents/onyu-remote-site`)와 같은 `style.css`를 쓴다.
- 맥 설치 파일은 이 저장소의 Releases에 `OnyuStaff-<버전>.dmg`와 고정 이름 `OnyuStaff.dmg` 두 개로 올린다. 앱 저장소(`~/Documents/OnyuStaff`)의 `scripts/release.sh`가 배포 끝에 올린다. 페이지는 최신 릴리스 정보를 읽어 버전·크기·SHA-256을 채운다(`site.js`).
- 앱 소스는 비공개 저장소 `sanghyun97/OnyuStaff`에 있다. 이 저장소에는 사이트와 설치 파일만 둔다.
- 검색에 나오지 않도록 모든 페이지에 `noindex`를 넣었다. 주소를 아는 사람은 누구나 받을 수 있다.
