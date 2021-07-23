def makePlaylist(song, artists):
    playlist = {}
    for i in range(0,len(song),1):
        playlist[song[i]] = artists[i]
    return playlist

print(makePlaylist(["Tầng Thượng 102", "Đốt", "Cho Tôi Đi Theo"], ["Cá Hồi Hoang",
"Ngọt", "Ngọt"]))