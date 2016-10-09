import msvcrt
import time

finish=10
count=0

print "zigzag game"
print "press enter_key to get started!"

raw_input()
s_time=time.time()

while(1):
	key=msvcrt.getch()
	if key=='M':
		count=count+1
		print "---",
		if count==finish:
			print'\t press down arrow key till it stops and press right arrow key to finish'
			break
count=0	
print '\t\t\t\t\t',
while(1):			
	key=msvcrt.getch()
	if key=='P':
		count=count+1
		print "|"
		print '\t\t\t\t\t',
		if count==finish:
			#print "press right arrow key now"
			break
		
count=0	
#print '\t\t\t\t\t
while(1):			
	key=msvcrt.getch()		
	if key=='M':		
		count=count+1
		print "---",
		if count==finish:
			break

time_elapsed=time.time()-s_time
print "\ncongrats you have finished the game"
print "\ntime taken is "+str(round(time_elapsed))

'''
1. The game should be lost on pressing the wrong key
'''
