import json,glob
pr=json.load(open('prices.json'))
stocks=[]
for f in sorted(glob.glob('data/*.json')):
    d=json.load(open(f)); t=d['ticker']
    d['series']={'d':pr[t]['d'],'p':pr[t]['p']}; d['mc']=pr[t]['mc']
    d.pop('price',None); d.pop('from_high_pct',None)
    stocks.append(d)
html=open('template.html',encoding='utf-8').read().replace('/*DATA*/',json.dumps({'stocks':stocks},ensure_ascii=False,separators=(',',':')))
open('../index.html','w',encoding='utf-8').write(html)
print(len(html)//1000,'KB')
