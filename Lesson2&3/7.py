data = [
    {
        "name": "Paris, Texas",
        "country": "USA",
        "year": 1984,
        "director": "Wim Wenders",
        "watchedStatus": True
    },
    {
        "name": "Three Seasons",
        "country": "Vietnam",
        "year": 1999,
        "director": "Tony Bui",
        "watchedStatus": False
    },
    {
        "name": "Chungking Express",
        "country": "Hong Kong",
        "year": 1994,
        "director": "Wong Kar-wai",
        "watchedStatus": True
    },
    {
        "name": "Cemetery of Splendour",
        "country": "Thailand",
        "year": 2015,
        "director": "Apichatpong Weerasethakul",
        "watchedStatus": False
    },
    {
        "name": "The Scent of Green Papaya",
        "country": "Vietnam",
        "year": 1992,
        "director": "Tran Anh Hung",
        "watchedStatus": False
    },
    {
        "name": "Parasite",
        "country": "South Korea",
        "year": 2019,
        "director": "Bong Joon-ho",
        "watchedStatus": True
    },
    {
        "name": "Before Sunrise",
        "country": "USA",
        "year": 1995,
        "director": "Richard Linklater",
        "watchedStatus": True
    },
    {
        "name": "Breathless",
        "country": "France",
        "year": 1960,
        "director": "Jean-Luc Godard",
        "watchedStatus": False
    },
    {
        "name": "Cyclo",
        "country": "Vietnam",
        "year": 1994,
        "director": "Tran Anh Hung",
        "watchedStatus": True
    }
]


 #a
for i in range(0,len(data),1):
    if (data[i]["country"] == "Vietnam"):
        print(data[i]["name"])
 #b
director = []
current_max = 0
current_max_dir = ""
for j in range(0,len(data),1):
    director.append(data[j]["director"])
for x in director:
    if (director.count(x) > current_max):
        current_max = director.count(x)
        current_max_dir = x
print(f"{x} xuất hiện nhiều nhất với {current_max} bộ phim")
