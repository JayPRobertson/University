import doctest

#represents score information about a music track
#tuple[tempo, popularity, danceability, energy]
#Precondition: tempo, popularity, danceability, and energy >= 0
SongScore = tuple[float, int, float, float]

#represents all information about music track
#tuple[id, title, artist, duration, list of tagged genres, score info]
#Precondition: duration is in ms, all str are not empty (ie. not '')
SongInfo = tuple[str, str, str, int, list[str], SongScore]

TITLE = 1
DURATION = 3
GENRES = 4
SONGSCORE = 5

DANCEABILITY = 2

MIN_TO_MS = 60000
SEC_TO_MS = 1000

def multiply_by(lst1:list, lst2:list[int]) -> None:
    '''
    multiplies values in the same positions in lst1 by lst2 and updates lst1 
    with the corresponding values
    
    Precondition: lst2 contains only ints >= 0
    
    >>> lst = []
    >>> multiply_by(lst, [2, 3, 2])
    >>> lst
    []
    
    >>> lst = [1, 2, 3]
    >>> multiply_by(lst, [2, 4, 0])
    >>> lst
    [2, 8, 0]
    
    >>> lst = [1, 2, 3]
    >>> multiply_by(lst, [2, 4])
    >>> lst
    [2, 8, 3]
    
    >>> lst = [1, 2, 3]
    >>> multiply_by(lst, [2, 4, 0, 2])
    >>> lst
    [2, 8, 0]
    
    >>> lst = ['cat', 'rat', 'bat']
    >>> multiply_by(lst, [3, 2])
    >>> lst
    ['catcatcat', 'ratrat', 'bat']
    
    >>> lst = [True, False]
    >>> multiply_by(lst, [10, 2])
    >>> lst
    [10, 0]
    
    >>> lst = [1.2, 2.3, 3.4]
    >>> multiply_by(lst, [1, 2, 3, 4])
    >>> lst
    [1.2, 4.6, 10.2]
    
    >>> lst = ['cat', True, 1.2, -2, 9]
    >>> multiply_by(lst, [4, 11, 2, 2, 3])
    >>> lst
    ['catcatcatcat', 11, 2.4, -4, 27]
    '''
    for index in range(len(lst1)):
        if index < len(lst2):
            lst1[index] *= lst2[index]

def create_scores(tempo:float, popularity:int, danceability:float,
                  energy:float) -> tuple[float]:
    '''
    returns a tuple of given values
    Precondition: tempo, popularity, danceability, and energy >= 0
    
    >>> create_scores(79.124, 5, 0.518, 0.805)
    (79.124, 5, 0.518, 0.805)
    >>> create_scores(111, 1, 2, 9.1)
    (111, 1, 2, 9.1)
    >>> create_scores(0.001, 10, 0.0001, 0.0001)
    (0.001, 10, 0.0001, 0.0001)
    '''
    score_tuple = (tempo, popularity, danceability, energy)
    return score_tuple

def create_music_track(track_id:str, title:str, artist:str, duration:float,
                       genres:str, scores:SongScore) -> tuple:
    '''
    creates a tuple of track_id, title, astrist, duration, genres, and scores
    
    Precondition: all str are not empty
    
    >>> create_music_track('001CyR8xqmmpVZFiTZJ5BC', \
    'She Knows How To Rock Me', 'Taj Mahal', 160107, '', \
    (90.048, 31, 0.826, 0.679)) # doctest: +NORMALIZE_WHITESPACE
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', \
    160107, [], (90.048, 31, 0.826, 0.679))
    
    >>> create_music_track('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', \
    'The Carters', 285200, 'R&B:Rap:Pop', \
    (0.001, 10, 0.0001, 0.0001)) # doctest: +NORMALIZE_WHITESPACE
    ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (0.001, 10, 0.0001, 0.0001))
    
    >>> create_music_track('3K7Yui8Q02wWjSg2XB5e1x', \
    'Enchante', 'Dirt Poor Robins', 216000, 'Indie:Alternative', \
    (100.12, 2, 0.999, 0.899)) # doctest: +NORMALIZE_WHITESPACE
    ('3K7Yui8Q02wWjSg2XB5e1x', 'Enchante', 'Dirt Poor Robins', 216000, 
    ['Indie', 'Alternative'], (100.12, 2, 0.999, 0.899))
    '''
    genres_list = genres.split(':')
    if genres_list == ['']:
        genres_list = []
        
    music_track = (track_id, title, artist, duration, genres_list, scores)
    return music_track

def get_titles(playlist:list[SongInfo]) -> list: 
    '''
    returns the titles of all songs in playlist
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_titles(tracks)
    ['Zangiefs Theme', 'She Knows How To Rock Me', 'SUMMER']
    
    >>> t1 = ('2PXpQ1R0z4WSuKkCEoZkW9', 'Blood Pact', 'Aviators', \
    360000, ['Indie', 'Rock', 'Synth'], (145.56, 25, 0.450, 0.138))
    >>> t2 = ('3K7Yui8Q02wWjSg2XB5e1x', 'Enchante', 'Dirt Poor Robins', \
    216000, ['Indie', 'Alternative'], (100.12, 2, 0.999, 0.899))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'The Anthem of Mr. Dark', \
    'The Arcadian Wild', 285200, ['Folk'], (124.51, 43, 0.741, 0.987))
    >>> t4 = ('5POEiHEJHjdb3Hw9pYeH1d0', 'A', 'B', 1, [], \
    (0.001, 10, 0.0001, 0.0001)) 
    >>> tracks = [t1, t2, t3, t4]
    >>> get_titles(tracks)
    ['Blood Pact', 'Enchante', 'The Anthem of Mr. Dark', 'A']
    '''
    titles_list = []
    
    for track in playlist:
        song = track[TITLE]
        titles_list.append(song)
    
    return titles_list

def is_track_of_genre(track:SongInfo, genre:str) -> bool:
    '''
    returns True if genre is in track, otherwise False
    
    >>> t = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> is_track_of_genre(t, 'Pop')
    False
    
    >>> t = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> is_track_of_genre(t, 'Pop')
    True
    
    >>> t = ('3K7Yui8Q02wWjSg2XB5e1x', 'Enchante', 'Dirt Poor Robins', \
    216000, ['Indie', 'Alternative'], (100.12, 2, 0.999, 0.899))
    >>> is_track_of_genre(t, 'alternative')
    True
    
    >>> t = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> is_track_of_genre(t, 'Indie')
    False
    
    >>> t = ('2PXpQ1R0z4WSuKkCEoZkW9', 'Blood Pact', 'Aviators', 360000, \
    ['Indie', 'Rock', 'Synth'], (145.56, 25, 0.45, 0.138))
    >>> is_track_of_genre(t, '')
    False
    '''
    genre_list = track[GENRES]
    if genre == []:
        return False
    genre = genre.lower()
    
    for song_type in genre_list:
        song_type = song_type.lower()
        if song_type == genre:
            return True
        
    return False

def get_length_of_playlist(playlist:list[SongInfo]) -> list[int]:
    '''
    returns the total duration of all music tracks as tuple converted to
    (minutes, seconds, milliseconds)
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    >>> tracks = [t1, t2, t3]
    >>> get_length_of_playlist(tracks)
    (10, 14, 480)
    
    >>> t1 = ('2PXpQ1R0z4WSuKkCEoZkW9', 'Blood Pact', 'Aviators', \
    360000, ['Indie', 'Rock', 'Synth'], (145.56, 25, 0.450, 0.138))
    >>> t2 = ('3K7Yui8Q02wWjSg2XB5e1x', 'Enchante', 'Dirt Poor Robins', \
    216000, ['Indie', 'Alternative'], (100.12, 2, 0.999, 0.899))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'The Anthem of Mr. Dark', \
    'The Arcadian Wild', 285200, ['Folk'], (124.51, 43, 0.741, 0.987))
    >>> t4 = ('5POEiHEJHjdb3Hw9pYeH1d0', 'A', 'B', 1, [], \
    (0.001, 10, 0.0001, 0.0001)) 
    >>> tracks = [t1, t2, t3, t4]
    >>> get_length_of_playlist(tracks)
    (14, 21, 201)
    '''
    duration_ms = 0
    
    for track in playlist:
        duration_ms += int(track[DURATION])
        
    duration_min = (duration_ms//MIN_TO_MS)
    duration_ms -= (duration_min * MIN_TO_MS)
    duration_sec = (duration_ms//SEC_TO_MS)
    duration_ms -= (duration_sec * SEC_TO_MS)
        
    return (duration_min, duration_sec, duration_ms) 

def get_tracks_with_genre(playlist:list[SongInfo],
                          genre:str) -> list[SongInfo]: 
    '''
    returns a list of music tracks that are of a given genre (ignores case)
    
    >>> t1 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.78, 0.729))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> tracks = [t1, t2, t3, t4]
    
    >>> get_tracks_with_genre(tracks, '') # doctest: +NORMALIZE_WHITESPACE
    []
    >>> get_tracks_with_genre(tracks, 'Folk') # doctest: +NORMALIZE_WHITESPACE
    []
    >>> get_tracks_with_genre(tracks, 'pop') # doctest: +NORMALIZE_WHITESPACE
    [('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', 250337, \
    ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.78, 0.729)), \
    ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', 285200, \
    ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))]
    >>> get_tracks_with_genre(tracks, 'aNimE') # doctest: +NORMALIZE_WHITESPACE
    [('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))]
    '''
    genre_playlist = []
    
    for track in playlist:
        if is_track_of_genre(track, genre) == True:
            genre_playlist.append(track)
            
    return genre_playlist

def get_highest_danceability_score(playlist:list[SongInfo]) -> float: 
    '''
    returns the highest danceability score in a playlist; if list is empty
    it returns 0
    
    >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', \
    'Taj Mahal', 160107, [], (90.048, 31, 0.826, 0.679))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'SUMMER', 'The Carters', \
    285200, ['R&B', 'Rap', 'pop'], (135.414, 55, 0.592, 0.569))
    >>> t4 = ('7y6c07pgjZvtHI9kuMVqk1', 'Get It Together', 'Drake', \
    250337, ['Hip-Hop', 'Pop', 'Rap'], (123.009, 69, 0.826, 0.729))
    >>> tracks = [t4, t2, t3, t1]
    >>> get_highest_danceability_score(tracks)
    0.826
    
    >>> get_highest_danceability_score([])
    0
    
    >>> t1 = ('2PXpQ1R0z4WSuKkCEoZkW9', 'Blood Pact', 'Aviators', \
    360000, ['Indie', 'Rock', 'Synth'], (145.56, 25, 0.450, 0.138))
    >>> t2 = ('3K7Yui8Q02wWjSg2XB5e1x', 'Enchante', 'Dirt Poor Robins', \
    216000, ['Indie', 'Alternative'], (100.12, 2, 0.999, 0.899))
    >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'The Anthem of Mr. Dark', \
    'The Arcadian Wild', 285200, ['Folk'], (124.51, 43, 0.741, 0.987))
    >>> t4 = ('5POEiHEJHjdb3Hw9pYeH1d0', 'A', 'B', 1, [], \
    (0.001, 10, 0.0001, 0.0001)) 
    >>> tracks = [t1, t2, t3, t4]
    >>> get_highest_danceability_score(tracks)
    0.999
    '''
    highest_dance = 0
    
    if playlist == []:
        return 0
    else:
        for track in playlist:
            scores = track[SONGSCORE]
            danceability = scores[DANCEABILITY]
            if danceability >= highest_dance:
                highest_dance = danceability
        
    return highest_dance