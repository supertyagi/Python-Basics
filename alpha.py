print "check any word or alphabet".center(80)
string=input("Write Anything:")
word=input("which alphabet to check ?:")
count={}.fromkeys(word,0)
for (char or str) in string:
 if (char or str) in count:
  count[(char or str)]+=1
print(count)