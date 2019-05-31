import sys
import json
import requests

class querycensys():
	def __init__ (self,target):
		self.target=target
	def main(self):

		API_URL = "https://censys.io/api/v1/search/ipv4"
		UID = "5335de69-8719-4a09-8062-a52b5db0adf3"
		SECRET = "GrQ3HJMKjX28Bc7Gy6OjoweZzlLAPvzb"
	# res = requests.get('https://censys.io/api/v1' + "/data", auth=(UID, SECRET))
	# print(res.url)
		data={
		'page':1,
	'query':self.target,
	'fields':['ip']
	}
	
		content=requests.post(API_URL,data=json.dumps(data),auth=(UID, SECRET))
		result=content.json()
		if content.status_code != 200:
			print ("error occurred: %s" %content.json()["error"])
			sys.exit(1)
	# print(result)
		for ip in result['results']:
			print("%s" %ip['ip'])
		with open('ip.txt',mode='a') as f:
			for ip in result['results']:
				f.writelines(ip['ip']+'\n')


	# for name, series in res.json()["raw_series"].iteritems():
	# 	print (series["name"], "was last updated at", series["latest_result"]["timestamp"])
if __name__ == '__main__':
	a=querycensys(sys.argv[1])
	a.main()
