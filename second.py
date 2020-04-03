#word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")
        
        
 # word <-- has an even length!
#in <-- has an even length!
# this <-- has an even length!
#sentence <-- has an even length!
#that <-- has an even length!
#an <-- has an even length!
#even <-- has an even length!
#number <-- has an even length!
#of <-- has an even length!      
        
