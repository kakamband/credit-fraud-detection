import requests

url = 'http://localhost:5000/predict_api'

r = requests.post(url,json={'V1':-0.1,	'V2':0.2,	'V3':0.3,	'V4':3.2,
                            'V5':3.2,	'V6':0.1,	'V7':-0.9,	'V8':-0.1,	'V9':2.1,	
                            'V10':-1.4,	'V11':-0.9,	'V12':2.4,	'V13':-1.8,	'V14':4.1,	
                            'V15':-0.1,	'V16':-0.7,	'V17':5.1,	'V18':-9.1,	'V19':0.6,	
                            'V20':-0.2,	'V21':6.1,	'V22':0.1,	'V23':-0.7,	'V24':-2.6,	
                            'V25':8.1,	'V26':-0.8,	'V27':2.7,	'V28':-0.8,	'Amount':530
	
})

print(r.json())