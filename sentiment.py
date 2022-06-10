from textblob import TextBlob

#Wildest Dreams (Taylor's Version)!
t = '''
He's so tall and handsome as hell
He's so bad but he does it so well
'''

t = TextBlob(t)
print(t.sentiment)

#Love Story (Taylor's Version)!
s = '''You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"'''

s = TextBlob(s)
print(s.sentiment)

#Forever & Always (Taylor's Version)!
r = ''''And I stare at the phone, he still hasn't called
And then you feel so low you cant feel nothing at all"'''

r = TextBlob(r)
print(r.sentiment)




