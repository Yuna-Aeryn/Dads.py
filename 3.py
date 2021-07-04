places = ['Paris', 'Greece', 'Korea', 'Libya', 'France']
friend_places = places[:]
places.append('Czech')
friend_places.append('sokovia')

print("my favorite places are:")
for x in places:
    print(x)
print("\n my friends favorite places are:")
for x in friend_places:
    print(x)