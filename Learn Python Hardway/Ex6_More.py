# -*- coding: utf-8 -*-
x = "There are %d types of people" % 10
binary ="binary"
do_not = "do not"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r" %x
print "I also said '%s' " %y

hilarious = False
joke_evaluation= "Is not that joke so funny?! %r"

print joke_evaluation % hilarious

w ="This is bad"
e = "This is good"
print w+" "+ e