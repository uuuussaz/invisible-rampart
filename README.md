# 보이지 않는 성벽

미·중 패권 경쟁, 군비 경쟁, 공급망 내재화로 수요가 달라지는 미국 상장 종목 19개를 정리한 정적 웹사이트입니다.

- 분류: 미국우선 16개, 구분 전 3개(PLUG, SPCX, TSLA)
- 종목별 일별 종가 차트, 주요 사건, 강세·약세 논리, 내부자·정부 거래, 증권사 목표가, 용어 풀이 포함
- 가격 기준: 2026-10-12 종가 (상세 본문 숫자는 10/7~10/9 기준)

## 열기
`index.html` 한 파일로 동작합니다. GitHub Pages를 켜면 바로 공개됩니다.
(Settings → Pages → Branch: main, folder: / (root))

## 수정
`source/data/<TICKER>.json`을 고친 뒤 `source/` 폴더에서 `python3 build.py`를 실행하면 `index.html`이 다시 만들어집니다.
가격은 `source/prices.json`(yfinance 일별 종가)입니다.

## 출처
SEC EDGAR(Form 4, 13G/13D), 미 정부윤리청 OGE 278-T, 하원 서기처 공시, 각 회사 IR·보도자료. 종목별 출처는 사이트 각 종목 하단에 있습니다.
