import sys

def compose(musicalNotes, indexes, startPosition):
    song = []
    song.insert(0, musicalNotes[startPosition])
    print(song)
    lastPosition = startPosition
    for index in indexes:
        if(lastPosition + index > len(musicalNotes)):
            song.append(musicalNotes[(lastPosition + index) % len(musicalNotes)])
        else:
            song.append(musicalNotes[int(lastPosition + index)])
        lastPosition = lastPosition + index
    return song

if __name__ == '__main__':
    song = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    print(song)

