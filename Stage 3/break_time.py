import time
import webbrowser

total_breaks = 3
break_count = 0

print "This program started on " + time.ctime()

while break_count < total_breaks: 
    break_count += 1
    print "Start sleep, round: " + str(break_count) + " of 3 @ " + time.ctime()
    time.sleep(15)
    print "End sleep, round: " + str(break_count) + " of 3 @ " + time.ctime()
    webbrowser.open("https://radio.nrk.no/direkte/mp3")

print "This program ended on " + time.ctime()
