from sys import argv	

script, userName = argv
prompt = '>'

print "hi %s, i am the %s script." % (userName, script)
print "do you like me %s?" % userName
likes = raw_input(prompt)

print "you said %r about liking me" % (likes)