playlist = {}
def makePlaylist(song, artists):
    for i in range(0,len(song),1):
        playlist[song[i]] = artists[i]
    return playlist

print(makePlaylist(["Tang Thượng 102", "Đốt", "Cho Tôi Đi Theo"], ["Cá Hồi Hoang",
"Ngọt", "Ngọt"]))