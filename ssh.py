#!/usr/bin/python
#-*- coding:utf-8 -*-
import paramiko
import sys

#test
class ssh:
	def __init__(self,host,username,password,port):
		self.s=paramiko.SSHClient()
                self.s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.s.connect(hostname = host,port=port,username=username,password=password,timeout=10)

	def ssh_cmd(self,cmd):
		stdin,stdout,stderr = self.s.exec_command(cmd,timeout=30)
		result = stdout.read()
		return result

	def ssh_scp(self,localpath,remotepath):
		sftp = paramiko.SFTPClient.from_transport(self.s.get_transport())
		sftp.put(localpath,remotepath)
	
	def close(self):
		self.s.close()

def main():
	a = sys.argv[1]
	b = sys.argv[2]
	c = sys.argv[3]
	d = sys.argv[4]
	hostlist = b.split(',')
	for host in hostlist:
		try:
			conn = ssh(host,'test','test','22')
			re = conn.ssh_cmd(d)
			print '\033[1;32;40m'
			print '----------------'
			print host + ':'
			print '----------------'
			print '\033[0m',
			print re
		except Exception,e:
			print e
		finally:
			conn.close()

if __name__ == '__main__':
	main()
