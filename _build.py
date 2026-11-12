#!/usr/bin/env python3
"""온유 작가 사이트 만들기 — python3 _build.py
버전이 바뀌면 아래 RELEASE 값과 VERSIONS만 고치고 다시 실행한다(페이지는 GitHub에서 최신 값을 읽어
덮어쓰지만, 읽지 못할 때 보여 줄 기본값이 이것이다). 모양은 온유 리모트 사이트와 같은 style.css를 쓴다."""
import html, pathlib

RELEASE = {
    "version": "1.3",
    "date": "2026년 11월 13일",
    "size": "3.2MB",
    "sha256": "6e1e3de23d0e326a1f79daa246ac1cbeab0a3eb6901ab95179e35e264624b462",
}
REPO = "sanghyun97/onyu-staff"
DMG = f"https://github.com/{REPO}/releases/latest/download/OnyuStaff.dmg"
SITE = "https://sanghyun97.github.io/onyu-staff/"
DESC = "온유포토그라피 작가용 맥 앱 — SD카드 백업과 사진 셀렉."


def page(name, title, body, desc=DESC, sub_title="온유 작가"):
    out = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}{'' if name == 'index.html' else name}">
<meta property="og:image" content="{SITE}icon.png">
<meta name="theme-color" content="#000000">
<link rel="icon" href="icon.png">
<link rel="apple-touch-icon" href="icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<nav class="global-nav" aria-label="사이트">
  <div class="inner">
    <a class="brand" href="./"><img src="icon.png" alt="" width="20" height="20">온유 작가</a>
    <a href="./#features" class="optional">기능</a>
    <a href="install.html">설치 안내</a>
    <a href="changelog.html">변경 기록</a>
  </div>
</nav>
<div class="sub-nav">
  <div class="inner">
    <span class="title">{html.escape(sub_title)}</span>
    <div class="links">
      <a class="btn small" href="./#download">맥 앱 받기</a>
    </div>
  </div>
</div>
<main>
{body}
</main>
<footer class="footer">
  <div class="inner">
    <div class="cols">
      <div><h4>온유 작가</h4><a href="./">소개</a><a href="./#features">기능</a><a href="./#download">맥 앱 내려받기</a></div>
      <div><h4>도움말</h4><a href="install.html">설치 안내</a><a href="changelog.html">변경 기록</a></div>
      <div><h4>버전</h4><a href="https://github.com/{REPO}/releases">모든 버전</a></div>
    </div>
    <p class="legal">© 2026 SANGHYUN LEE. 온유 작가는 온유포토그라피 작가용 앱입니다. Apple, Mac, macOS는 미국 및 그 밖의 나라에 등록된 Apple Inc.의 상표입니다.</p>
  </div>
</footer>
<script src="site.js" defer></script>
</body>
</html>
"""
    pathlib.Path(name).write_text(out, encoding="utf-8")


def icon(d):
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'


def card(ic, title, text):
    return f'<div class="card">{icon(ic)}<h3>{title}</h3><p>{text}</p></div>'


R = RELEASE
FEATURES = "".join([
    card('<path d="M4 7a2 2 0 0 1 2-2h4l2 2h6a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2z"/>', "촬영 폴더 만들기", "날짜·신랑·신부를 넣으면 '2026-11-08 김철수 이영희' 폴더와 그 안의 본인 JPG·RAW 폴더를 만듭니다."),
    card('<path d="M12 3v12M8 11l4 4 4-4"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>', "SD카드 백업", "카드를 넣고 '복사 시작'을 누르면 JPG와 RAW를 나눠 복사합니다. 카드를 여러 장 이어서 넣을 수 있고, 폴더 이름 끝에 장수가 붙습니다."),
    card('<path d="M5 12l4 4L19 6"/>', "안전한 복사", "같은 이름·크기의 사진은 이미 백업된 것으로 건너뛰고, 이름만 같은 다른 사진은 _2를 붙여 따로 둡니다."),
    card('<path d="M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9z"/>', "별점 셀렉", "별점과 색상 라벨을 매기고, 별점 기준으로 걸러 보거나 한꺼번에 복사·삭제합니다. 라이트룸에서도 그대로 보입니다."),
    card('<rect x="3" y="5" width="8" height="14" rx="1.5"/><rect x="13" y="5" width="8" height="14" rx="1.5"/>', "연사 묶음과 비교", "연속 촬영한 사진은 자동으로 묶이고, 두 장을 골라 나란히 비교합니다."),
    card('<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>', "원본 RAW 찾기", "고른 JPG와 짝이 되는 원본 RAW를 다른 폴더에서 찾아 복사합니다. 이름이 바뀌어도 촬영시각으로 찾습니다."),
])

page("index.html", "온유 작가 — SD카드 백업과 셀렉", f"""
<section class="tile">
  <div class="wrap">
    <h1 class="hero-display">백업부터 셀렉까지.</h1>
    <p class="lead">온유포토그라피 작가용 맥 앱입니다.</p>
    <div class="cta">
      <a class="btn" href="#download">맥 앱 받기</a>
      <a class="btn ghost" href="install.html">설치 안내</a>
    </div>
    <p class="caption" style="margin-top:17px">맥 앱 <span data-version>{R['version']}</span> · macOS 14 이상</p>
  </div>
</section>

<section class="tile parchment" id="features">
  <div class="wide">
    <p class="eyebrow">기능</p>
    <h2 class="display-lg">촬영 끝나고 하는 일, 두 탭으로.</h2>
    <div class="grid">{FEATURES}</div>
  </div>
</section>

<section class="tile dark-2">
  <div class="wrap">
    <p class="eyebrow">알아 두기</p>
    <h2 class="display-lg">별점은 사진 파일에 기록됩니다.</h2>
    <p class="copy">별점과 색상 라벨은 사본이 아니라 원본 사진 파일에 직접 기록됩니다. 원본은 따로 백업해 두시길 권합니다.</p>
  </div>
</section>

<section class="tile" id="download">
  <div class="wrap">
    <p class="eyebrow">내려받기</p>
    <h2 class="display-lg">맥용 온유 작가</h2>
    <p class="copy">Apple의 공증을 받은 설치 파일이라 경고 없이 열립니다. 새 버전이 나와도 이 주소에서 받으면 됩니다.</p>
    <div class="cta">
      <a class="btn hero" href="{DMG}" data-dmg>내려받기 (DMG)</a>
    </div>
    <div class="card download-card">
      <div class="row"><span>버전</span><span><span data-version>{R['version']}</span> · <span data-date>{R['date']}</span></span></div>
      <div class="row"><span>크기</span><span data-size>{R['size']}</span></div>
      <div class="row"><span>요구 사항</span><span>macOS 14 이상 · Apple 실리콘·Intel</span></div>
      <div class="row"><span>서명</span><span>Developer ID · Apple 공증</span></div>
      <details class="more">
        <summary>자세히</summary>
        <div class="row"><span>SHA-256</span><code data-sha>{R['sha256']}</code></div>
        <p class="fine">받은 파일이 원본과 같은지 확인하는 값입니다. 터미널에서 <code>shasum -a 256 OnyuStaff.dmg</code>를 실행해 같은 값이 나오면 변조되지 않은 파일입니다. 확인하지 않아도 맥이 설치할 때 Apple 공증으로 따로 검증합니다.</p>
      </details>
    </div>
    <p class="caption" style="margin-top:17px"><a href="changelog.html">변경 기록</a> · <a href="https://github.com/{REPO}/releases">이전 버전</a></p>
  </div>
</section>
""")

page("install.html", "설치 안내 — 온유 작가", f"""
<article class="article">
  <h1>설치 안내</h1>
  <p class="caption">설치부터 첫 백업까지, 순서대로 따라 하면 됩니다.</p>

  <h2>1. 설치하기</h2>
  <ol>
    <li><a href="./#download">맥 앱(DMG)을 내려받습니다.</a></li>
    <li>내려받은 <code>OnyuStaff.dmg</code>를 열고, 앱을 <b>응용 프로그램</b> 폴더로 끌어 놓습니다.</li>
    <li>응용 프로그램에서 <b>OnyuStaff</b>를 엽니다.</li>
  </ol>

  <h2>2. 본인 이름 넣기</h2>
  <p>사진 복사 탭 또는 설정 › 내 정보에 본인 이름을 <b>성까지</b> 적습니다. 이 이름이 'JPG 홍길동', 'RAW 홍길동' 폴더 이름에 쓰이고, 한 번 넣으면 바꾸기 전까지 그대로입니다.</p>

  <h2>3. 사진 복사 (SD카드 백업)</h2>
  <ol>
    <li>'촬영 폴더 만들기'에 날짜·신랑·신부를 넣고 만들 위치를 고른 뒤 [폴더 만들기]를 누릅니다. 이미 있는 폴더에 넣으려면 [기존 폴더 고르기]를 씁니다.</li>
    <li>[SD카드 추가]로 카드를 넣고 [복사 시작]을 누릅니다. JPG와 RAW가 본인 폴더로 나뉘어 복사됩니다.</li>
    <li>복사 중이나 끝난 뒤에도 카드를 계속 넣을 수 있습니다. 넣은 순서대로 이어서 복사합니다.</li>
  </ol>
  <div class="note">동영상 등 JPG·RAW가 아닌 파일은 복사하지 않습니다. 다른 작가의 카드는 이름을 바꾼 뒤 넣으세요.</div>

  <h2>4. 셀렉</h2>
  <ul>
    <li>[사진 불러오기]를 누르거나 폴더를 창에 끌어 놓습니다.</li>
    <li>별표를 눌러 별점을 매기고, 상단 필터로 별점 기준 이상·이하만 걸러 봅니다.</li>
    <li>[일괄 RAW 찾기]는 고른 JPG와 짝이 되는 원본 RAW를 다른 폴더에서 찾아 복사합니다.</li>
    <li>단축키는 설정 › 키보드 단축키에서 바꿀 수 있습니다.</li>
  </ul>

  <h2>업데이트와 삭제</h2>
  <ul>
    <li><b>업데이트</b> — 앱을 종료하고, 새 DMG를 받아 응용 프로그램 폴더의 앱을 바꿔 넣습니다. 본인 이름과 단축키 설정은 그대로 남습니다.</li>
    <li><b>삭제</b> — 응용 프로그램 폴더에서 앱을 휴지통으로 옮깁니다.</li>
  </ul>
  <p style="margin-top:32px"><a class="btn" href="./#download">맥 앱 받기</a> &nbsp; <a class="btn ghost" href="changelog.html">변경 기록</a></p>
</article>
""", desc="온유 작가 설치 방법 — 설치, 본인 이름 넣기, SD카드 백업, 셀렉.", sub_title="설치 안내")

VERSIONS = [
    ("1.3", "2026년 11월 13일", [
        "원본 RAW 찾기가 연사로 같은 초에 찍힌 옆 컷이나 이름만 같은 다른 사진을 원본으로 잡던 문제를 고쳤습니다. 촬영시각을 1초 미만까지 비교하고, 카메라 기종·시리얼 번호가 다르면 다른 사진으로 봅니다.",
        "원본이 폴더에 없으면 비슷한 옆 컷을 대신 내놓지 않고 '찾지 못함'으로 표시합니다. 예전보다 '찾지 못함'이 늘 수 있습니다.",
    ]),
    ("1.2", "2026년 11월 11일", [
        "셀렉: Shift+방향키로 선택이 그 방향으로 넓어지지 않던 문제를 고쳤습니다.",
        "셀렉을 Finder처럼 다룹니다 — 빈 곳을 끌어 여러 장 고르기, ⌘C 파일 복사, ⌘V 붙여넣기, ⌘⌫ 휴지통, ⌘R Finder에서 보기, 사진 오른쪽 클릭 메뉴.",
        "새 단축키는 설정 › 키보드 단축키에서 바꿀 수 있습니다.",
    ]),
    ("1.1", "2026년 11월 5일", [
        "셀렉 확대 보기: 오른쪽 정보 칸의 폭을 끌어서 조절합니다.",
        "설정 화면에 앱 버전을 표시합니다.",
    ]),
    ("1.0", "2026년 11월 5일", ["첫 배포. 셀렉과 사진 복사."]),
]
vhtml = "".join(f'<div class="version"><h2>{v}</h2><p class="caption">{d}</p><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for v, d, items in VERSIONS)

page("changelog.html", "변경 기록 — 온유 작가", f"""
<article class="article">
  <h1>변경 기록</h1>
  <p class="caption">버전별로 달라진 점입니다. 설치 파일은 <a href="./#download">내려받기</a>, 이전 버전은 <a href="https://github.com/{REPO}/releases">모든 버전</a>에 있습니다.</p>
  {vhtml}
</article>
""", desc="온유 작가 버전별 변경 기록.", sub_title="변경 기록")

print("만든 페이지: index install changelog")
