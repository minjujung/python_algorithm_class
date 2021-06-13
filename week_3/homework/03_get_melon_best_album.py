genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    music_dict = {}
    genre_plays = {}
    for i in range(len(genre_array)):
        genre_plays[genre_array[i]] = play_array[i]
        # music_dict["i"] = genre_plays[i] 
    return genre_plays


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!