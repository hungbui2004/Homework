def makePlaylist(songs, artists):
    if (len(songs) > 10**3 or len(artists) > 10**3):
        return "Không hợp lệ"
    playlist = {}
    for i in range(0,len(songs),1):
        playlist[songs[i]] = artists[i]
    return playlist

print(makePlaylist(["Tầng Thượng 102", "Đốt", "Cho Tôi Đi Theo"], ["Cá Hồi Hoang",
"Ngọt", "Ngọt"]))
