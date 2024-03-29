import time
import socket

def getInput():
	motd = input('MOTD: ')
	host = input('IP Address: ')
	while True:
		try:
			port = int(input('Port: '))
		except TypeError:
			print ('Error: Invalid port number.')
			continue
		else:
			if (port < 1) or (port > 65535):
				print ('Error: Invalid port number.')
				continue
			else:
				return (host, port, motd)

def writeLog(client, data=''):
	separator = '='*50
	fopen = open('./honey.mmh', 'a')
	fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, separator))
	fopen.close()

def main(host, port, motd):
	print ('Starting honeypot!')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(100)
	while True:
		(insock, address) = s.accept()
		print ('Connection from:{1}:{2}'.format(address[0], address[1]))
		try:
			insock.send('%s\n'%(motd))
			data = insock.recv(1024)
			insock.close()
		except socket.error as e:
			writeLog(address)
		else:
			writeLog(address, data)
        
if __name__=='__main__':
	try:
		stuff = getInput()
		main(stuff[0], stuff[1], stuff[2])
	except KeyboardInterrupt:
		print ('Bye!')
		exit(0)
	except BaseException as e:
		print('Error: {0}'.format(str(e)))
exit(1)