'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

sentences=[]
sentences.append(len(input('Write something for me.')))
sentences.append(len(input('Got anyhting else for me?')))
sentences.append(len(input('Is there nothing left to say?')))

print(f'Your longest sentences was number {sentences.index(max(sentences))}. Just so you know...')

