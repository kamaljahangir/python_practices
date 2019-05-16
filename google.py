# Searching object
import sys, time
import webbrowser   # deal with web browser

data=sys.argv[1:]

print(data)

#searching object
for i in data:
	# code for web search
	print(i)
	time.sleep(3)
	webbrowser.open_new_tab("http://www.google.com/search?q="+i)
