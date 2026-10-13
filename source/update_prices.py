"""일별 종가를 yfinance로 받아 prices.json을 갱신한다. 한 종목이 실패하면 기존 값을 유지한다."""
import glob, json, os, sys
import yfinance as yf

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
tickers = sorted(os.path.basename(f)[:-5] for f in glob.glob('data/*.json'))
try:
    old = json.load(open('prices.json'))
except Exception:
    old = {}
out, failed = {}, []
for t in tickers:
    try:
        tk = yf.Ticker(t)
        c = tk.history(start='2025-12-31', auto_adjust=False).Close.dropna()
        if len(c) < 5:
            raise ValueError('데이터 부족')
        try:
            mc = tk.fast_info.market_cap
        except Exception:
            mc = old.get(t, {}).get('mc')
        out[t] = {'d': [str(i.date()) for i in c.index], 'p': [round(float(v), 2) for v in c.values], 'mc': mc}
    except Exception as e:
        failed.append(f'{t}: {e}')
        if t in old:
            out[t] = old[t]
if failed:
    print('실패(기존 값 유지):', *failed, sep='\n  ')
missing = [t for t in tickers if t not in out]
if missing:
    print('가격 없음:', missing)
    sys.exit(1)
json.dump(out, open('prices.json', 'w'), separators=(',', ':'))
print('마지막 날짜:', max(v['d'][-1] for v in out.values()))
