import doctest

MS_PER_SECOND = 1000
MS_PER_MIN = 60000

# represents the characteristic score of a song as:
# (tempo, popularity score, danceability score, energy score)
# where all values are >=0
Scores = tuple[float, int, float, float]
TEMPO = 0
POPULARITY = 1
DANCEABILITY = 2
ENERGY = 3

# represents a music track as:
# (track id, name, artist, duration (in ms), genre tags, scores)
# where id, name, artist != '', duration>0, and genre tags can be empty
MusicTrack = tuple[str, str, str, int, list[str], Scores]
TRACK_ID = 0
TITLE = 1
ARTIST = 2
DURATION = 3
GENRES = 4
SCORES = 5

# represents time as: (minutes, seconds, milliseconds)
# where all values are >= 0
Time = tuple[int, int, int]
MINUTES = 0
SECONDS = 1
MSECONDS = 2


# column numbers of data within input csv file
INPUT_TRACK_ID = 0
INPUT_TITLE = 3
INPUT_ARTIST = 2
INPUT_DURATION = 7
INPUT_GENRE = 1
INPUT_POPULARITY = 4
INPUT_TEMPO = 15
INPUT_DANCEABILITY = 6
INPUT_ENERGY = 8 

# place of dicts within read_file return tuple
GENRE_TO_TRACK_ID = 0
TRACK_ID_TO_TRACK_INFO = 1

def read_file(filename: str) -> (dict[str, list[str]],
                                 dict[str, MusicTrack]):
    '''
    Populates and returns a tuple with the following 2 dictionaries
    with data from valid filename.

    2 dictionaries returned as a tuple:
    - dict[genre tag: list of track ids associated with the tag]
    - dict[unique track id: music track information]

    Precondition: file is csv with data in expected columns
        and contains a header row with column titles
        Track ids are considered unique.

    >>> read_file('0lines_data.csv')
    ({}, {})

    >>> read_file('4lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    ({'Movie': ['000CzNKC8PEt1yC3L8dqwV'],
      'Reggae': ['000DfZJww8KiixTKuk9usJ'],
      'Jazz': ['000EWWBkYaREzsBplYjUag'],
      'R&B': ['000EWWBkYaREzsBplYjUag']},
    {'00021Wy6AyMbLP2tqij86e':
        ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme',
         'Capcom Sound Team', 169173, [], (129.578, 13, 0.617, 0.862)),
     '000CzNKC8PEt1yC3L8dqwV':
        ('000CzNKC8PEt1yC3L8dqwV', 'Coeur Brise √† Prendre - Remastered',
         'Henri Salvador', 130653, ['Movie'], (79.124, 5, 0.518, 0.805)),
     '000DfZJww8KiixTKuk9usJ':
        ('000DfZJww8KiixTKuk9usJ', 'Earthlings', 'Mike Love',
         357573, ['Reggae'], (120.365, 30, 0.631, 0.513)),
     '000EWWBkYaREzsBplYjUag':
        ('000EWWBkYaREzsBplYjUag', 'Fewerdolr', 'Don Philippe',
         104924, ['Jazz', 'R&B'], (76.43, 39, 0.768, 0.137))})


    >>> read_file('20lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    ({'Anime': ['00021Wy6AyMbLP2tqij86e'],
      'Reggae': ['000DfZJww8KiixTKuk9usJ', '52TDNHSeWey4NFAfLDgfjL',
                 '01w7h4gfJMHtUnykpD6M3f', '01yvyZWcqtI2ZqGhPB2uZq',
                 '02C5QgRFecna4B8Sv406WA', '02cW3CN4DC1QV6D4XRH9UV'],
      'Jazz': ['000EWWBkYaREzsBplYjUag'],
      'Dance': ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy',
                '00S35gEf40z03JTJgvQMqi', '01qMOMudbkIHZS9BFPUGNk',
                '02D9uD9WQb834Lb54xCvDS', '02UYYPOGSBXxGEMce927XV',
                '02ZorlDGq0uTnMobHNh4EL'],
      'Pop': ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy',
              '01qMOMudbkIHZS9BFPUGNk', '02ZorlDGq0uTnMobHNh4EL'],
      'Comedy': ['0017XiMkqbTfF2AUOzlhj6'],
      'Blues': ['001CyR8xqmmpVZFiTZJ5BC'],
      'Soundtrack': ['001VMKfkHZrlyj7JlQbQFL'],
      'Ska': ['001YQlnDSduXd5LgBd66gT'],
      'R&B': ['003eoIwxETJujVWmNFMoZy', '02D9uD9WQb834Lb54xCvDS'],
      'Soul': ['02D9uD9WQb834Lb54xCvDS', '02UYYPOGSBXxGEMce927XV']},
     {'00021Wy6AyMbLP2tqij86e':
        ('00021Wy6AyMbLP2tqij86e',
         'Zangiefs Theme',
         'Capcom Sound Team', 169173, ['Anime'],
         (129.578, 13, 0.617, 0.862)),
      '000DfZJww8KiixTKuk9usJ':
        ('000DfZJww8KiixTKuk9usJ',
         'Earthlings',
         'Mike Love', 357573, ['Reggae'],
         (120.365, 30, 0.631, 0.513)),
      '000EWWBkYaREzsBplYjUag':
        ('000EWWBkYaREzsBplYjUag',
         'Fewerdolr',
         'Don Philippe', 104924, ['Jazz'],
         (76.43, 39, 0.768, 0.137)),
      '000xQL6tZNLJzIrtIgxqSl':
        ('000xQL6tZNLJzIrtIgxqSl',
         'Still Got Time',
         'ZAYN', 188491, ['Dance', 'Pop'],
         (120.963, 70, 0.748, 0.627)),
      '0017XiMkqbTfF2AUOzlhj6':
        ('0017XiMkqbTfF2AUOzlhj6',
         'Thanksgiving Chicken',
         'Chad Daniels', 127040, ['Comedy'],
         (173.912, 27, 0.536, 0.78)),
      '001CyR8xqmmpVZFiTZJ5BC':
        ('001CyR8xqmmpVZFiTZJ5BC',
         'She Knows How To Rock Me',
         'Taj Mahal', 160107, ['Blues'],
         (90.048, 31, 0.826, 0.679)),
      '52TDNHSeWey4NFAfLDgfjL':
        ('52TDNHSeWey4NFAfLDgfjL',
         'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
         'Bob Marley & The Wailers', 278987, ['Reggae'],
         (180.043, 31, 0.675, 0.808)),
      '001VMKfkHZrlyj7JlQbQFL':
        ('001VMKfkHZrlyj7JlQbQFL',
         '"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"',
         'Ramin Djawadi', 120840, ['Soundtrack'],
         (113.655, 41, 0.168, 0.0354)),
      '001YQlnDSduXd5LgBd66gT':
        ('001YQlnDSduXd5LgBd66gT',
         'El Tiempo Es Dinero - Remasterizado 2007',
         'Soda Stereo', 177267, ['Ska'],
         (183.571, 38, 0.554, 0.921)),
      '003eoIwxETJujVWmNFMoZy':
        ('003eoIwxETJujVWmNFMoZy',
         'Growing Pains',
         'Alessia Cara', 193680, ['Dance', 'Pop', 'R&B'],
         (191.153, 66, 0.353, 0.755)),
      '00S35gEf40z03JTJgvQMqi':
        ('00S35gEf40z03JTJgvQMqi',
         'Its You - Radio Edit',
         'Syn Cole', 211875, ['Dance'],
         (127.957, 57, 0.646, 0.831)),
      '01qMOMudbkIHZS9BFPUGNk':
        ('01qMOMudbkIHZS9BFPUGNk',
         'Let It Be Me (feat. Ava Max)',
         'David Guetta', 172933, ['Dance', 'Pop'],
         (102.048, 62, 0.743, 0.529)),
      '01qNIJfMc14nxpOoM0Xwb0':
        ('01qNIJfMc14nxpOoM0Xwb0',
         'The Fool and Me - 2007 Remaster',
         'Robin Trower', 235720, [],
         (122.692, 31, 0.409, 0.766)),
      '01w7h4gfJMHtUnykpD6M3f':
        ('01w7h4gfJMHtUnykpD6M3f',
         'See Dem Fake Leaders - Dub Remix',
         'Ziggy Marley', 249740, ['Reggae'],
         (77.501, 24, 0.801, 0.636)),
      '01yvyZWcqtI2ZqGhPB2uZq':
        ('01yvyZWcqtI2ZqGhPB2uZq',
         'Lost Our Way',
         'I-Octane', 232091, ['Reggae'],
         (133.936, 5, 0.733, 0.492)),
      '02D9uD9WQb834Lb54xCvDS':
        ('02D9uD9WQb834Lb54xCvDS',
         'Love U 4 Life',
         'Jodeci', 290067, ['Dance', 'R&B', 'Soul'],
         (118.106, 53, 0.695, 0.638)),
      '02C5QgRFecna4B8Sv406WA':
        ('02C5QgRFecna4B8Sv406WA',
         'Get Up  Stand Up - Thievery Corporation Remix',
         'Bob Marley & The Wailers', 261693, ['Reggae'],
         (166.067, 27, 0.676, 0.702)),
      '02UYYPOGSBXxGEMce927XV':
        ('02UYYPOGSBXxGEMce927XV',
         'Nobody (feat. Athena Cage) - Remastered Single Version',
         'Keith Sweat', 251760, ['Dance', 'Soul'],
         (117.896, 47, 0.712, 0.511)),
      '02ZorlDGq0uTnMobHNh4EL':
        ('02ZorlDGq0uTnMobHNh4EL',
         'Bravado',
         'Lorde', 221409, ['Dance', 'Pop'],
         (175.879, 60, 0.489, 0.536)),
      '02cW3CN4DC1QV6D4XRH9UV':
        ('02cW3CN4DC1QV6D4XRH9UV',
         'Cant Dweet Again',
         'Christopher Martin', 144000, ['Reggae'],
         (99.531, 44, 0.71, 0.645))})
    '''
    genre_to_track_id = {}
    track_id_to_track_info ={}
    
    filehandle = open(filename, 'r')
    filehandle.readline()
    for line in filehandle:
        line = line.strip()
        line = line.split(',')
        track_id = line[INPUT_TRACK_ID]
        
        if line[INPUT_GENRE] == '':
            genre_list = []
        else:
            genre_list = line[INPUT_GENRE].split(':')
        for genre in genre_list:
            if not genre in genre_to_track_id:
                genre_to_track_id[genre] = []
            genre_to_track_id[genre].append(track_id)
        
        tempo = float(line[INPUT_TEMPO])
        popularity = int(line[INPUT_POPULARITY])
        danceability = float(line[INPUT_DANCEABILITY])
        energy = float(line[INPUT_ENERGY])
        
        scores_tuple = (tempo, popularity, danceability, energy)
        track_info_tuple = (track_id, line[INPUT_TITLE], line[INPUT_ARTIST],
                        int(line[INPUT_DURATION]), genre_list, scores_tuple)
        
        track_id_to_track_info[track_id] = track_info_tuple    
        
    filehandle.close()
    return (genre_to_track_id, track_id_to_track_info)
    
def genre_in_logenres(dict_tuple:(dict[str, list[str]], dict[str, MusicTrack]),
                      logenres:list[str]) -> list[str]:
    '''
    creates of list of unique track ids from genre_to_track_id with genres
    in logenres; returns list of all track ids if logenres = []
    
    Precondition: assumes all genres in logenres have proper capitalization
    
    >>> dict_tuple = ({'Anime': ['00021Wy6AyMbLP2tqij86e'], 'Reggae': ['000DfZJww8KiixTKuk9usJ', '52TDNHSeWey4NFAfLDgfjL', \
    '01w7h4gfJMHtUnykpD6M3f', '01yvyZWcqtI2ZqGhPB2uZq', \
    '02C5QgRFecna4B8Sv406WA', '02cW3CN4DC1QV6D4XRH9UV'], 'Jazz': \
    ['000EWWBkYaREzsBplYjUag'], 'Dance': ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy', '00S35gEf40z03JTJgvQMqi', \
    '01qMOMudbkIHZS9BFPUGNk', '02D9uD9WQb834Lb54xCvDS', \
    '02UYYPOGSBXxGEMce927XV', '02ZorlDGq0uTnMobHNh4EL'], 'Pop': \
    ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy', \
    '01qMOMudbkIHZS9BFPUGNk', '02ZorlDGq0uTnMobHNh4EL'], 'Comedy': ['0017XiMkqbTfF2AUOzlhj6'], 'Blues': ['001CyR8xqmmpVZFiTZJ5BC'], \
    'Soundtrack': ['001VMKfkHZrlyj7JlQbQFL'], 'Ska': \
    ['001YQlnDSduXd5LgBd66gT'], 'R&B': ['003eoIwxETJujVWmNFMoZy', \
    '02D9uD9WQb834Lb54xCvDS'], 'Soul': ['02D9uD9WQb834Lb54xCvDS', '02UYYPOGSBXxGEMce927XV']}, {'00021Wy6AyMbLP2tqij86e': ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', 'Capcom Sound Team', 169173, ['Anime'], \
    (129.578, 13, 0.617, 0.862)), '000DfZJww8KiixTKuk9usJ': ('000DfZJww8KiixTKuk9usJ', 'Earthlings', 'Mike Love', 357573, ['Reggae'], (120.365, 30, 0.631, 0.513)), '000EWWBkYaREzsBplYjUag': ('000EWWBkYaREzsBplYjUag', 'Fewerdolr', 'Don Philippe', 104924, ['Jazz'], (76.43, 39, 0.768, 0.137)), '000xQL6tZNLJzIrtIgxqSl': ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', 188491, ['Dance', 'Pop'], \
    (120.963, 70, 0.748, 0.627)), '0017XiMkqbTfF2AUOzlhj6': ('0017XiMkqbTfF2AUOzlhj6', 'Thanksgiving Chicken', 'Chad Daniels', 127040, ['Comedy'], \
    (173.912, 27, 0.536, 0.78)), '001CyR8xqmmpVZFiTZJ5BC': \
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', 160107, \
    ['Blues'], (90.048, 31, 0.826, 0.679)), '52TDNHSeWey4NFAfLDgfjL': ('52TDNHSeWey4NFAfLDgfjL', 'Natural Mystic - Banjamin Devigne Deep Jazz Remix', \
    'Bob Marley & The Wailers', 278987, ['Reggae'], (180.043, 31, 0.675, 0.808)), '001VMKfkHZrlyj7JlQbQFL': ('001VMKfkHZrlyj7JlQbQFL', \
    '"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"', \
    'Ramin Djawadi', 120840, ['Soundtrack'], (113.655, 41, 0.168, 0.0354)), '001YQlnDSduXd5LgBd66gT': ('001YQlnDSduXd5LgBd66gT', 'El Tiempo Es Dinero - Remasterizado 2007', 'Soda Stereo', 177267, ['Ska'], (183.571, 38, 0.554, 0.921)), '003eoIwxETJujVWmNFMoZy': ('003eoIwxETJujVWmNFMoZy', \
    'Growing Pains', 'Alessia Cara', 193680, ['Dance', 'Pop', 'R&B'], \
    (191.153, 66, 0.353, 0.755)), '00S35gEf40z03JTJgvQMqi': \
    ('00S35gEf40z03JTJgvQMqi', 'Its You - Radio Edit', 'Syn Cole', 211875, ['Dance'], (127.957, 57, 0.646, 0.831)), '01qMOMudbkIHZS9BFPUGNk': \
    ('01qMOMudbkIHZS9BFPUGNk', 'Let It Be Me (feat. Ava Max)', 'David Guetta', \
    172933, ['Dance', 'Pop'], (102.048, 62, 0.743, 0.529)), '01qNIJfMc14nxpOoM0Xwb0': ('01qNIJfMc14nxpOoM0Xwb0', 'The Fool and Me - 2007 Remaster', \
    'Robin Trower', 235720, [], (122.692, 31, 0.409, 0.766)), \
    '01w7h4gfJMHtUnykpD6M3f': ('01w7h4gfJMHtUnykpD6M3f', \
    'See Dem Fake Leaders - Dub Remix', 'Ziggy Marley', 249740, ['Reggae'], \
    (77.501, 24, 0.801, 0.636)), '01yvyZWcqtI2ZqGhPB2uZq': \
    ('01yvyZWcqtI2ZqGhPB2uZq', 'Lost Our Way', 'I-Octane', 232091, ['Reggae'], \
    (133.936, 5, 0.733, 0.492)), '02D9uD9WQb834Lb54xCvDS': \
    ('02D9uD9WQb834Lb54xCvDS', 'Love U 4 Life', 'Jodeci', 290067, \
    ['Dance', 'R&B', 'Soul'], (118.106, 53, 0.695, 0.638)), '02C5QgRFecna4B8Sv406WA': ('02C5QgRFecna4B8Sv406WA', 'Get Up  Stand Up - Thievery Corporation Remix', \
    'Bob Marley & The Wailers', 261693, ['Reggae'], (166.067, 27, 0.676, 0.702)), '02UYYPOGSBXxGEMce927XV': ('02UYYPOGSBXxGEMce927XV', \
    'Nobody (feat. Athena Cage) - Remastered Single Version', 'Keith Sweat', 251760, ['Dance', 'Soul'], (117.896, 47, 0.712, 0.511)), '02ZorlDGq0uTnMobHNh4EL': ('02ZorlDGq0uTnMobHNh4EL', 'Bravado', 'Lorde', 221409, ['Dance', 'Pop'], \
    (175.879, 60, 0.489, 0.536)), '02cW3CN4DC1QV6D4XRH9UV': \
    ('02cW3CN4DC1QV6D4XRH9UV', 'Cant Dweet Again', 'Christopher Martin', 144000, \
    ['Reggae'], (99.531, 44, 0.71, 0.645))})

    
    >>> genre_in_logenres(dict_tuple, ['Jazz', 'Comedy'])
    ['000EWWBkYaREzsBplYjUag', '0017XiMkqbTfF2AUOzlhj6']
    >>> genre_in_logenres(dict_tuple, ['Jazz', 'Indie', 'Ska'])
    ['000EWWBkYaREzsBplYjUag', '001YQlnDSduXd5LgBd66gT']
    
    >>> genre_in_logenres(dict_tuple, []) 
    ['00021Wy6AyMbLP2tqij86e', '000DfZJww8KiixTKuk9usJ', '000EWWBkYaREzsBplYjUag', '000xQL6tZNLJzIrtIgxqSl', '0017XiMkqbTfF2AUOzlhj6', '001CyR8xqmmpVZFiTZJ5BC', '52TDNHSeWey4NFAfLDgfjL', '001VMKfkHZrlyj7JlQbQFL', '001YQlnDSduXd5LgBd66gT', '003eoIwxETJujVWmNFMoZy', '00S35gEf40z03JTJgvQMqi', '01qMOMudbkIHZS9BFPUGNk', '01qNIJfMc14nxpOoM0Xwb0', '01w7h4gfJMHtUnykpD6M3f', '01yvyZWcqtI2ZqGhPB2uZq', '02D9uD9WQb834Lb54xCvDS', '02C5QgRFecna4B8Sv406WA', '02UYYPOGSBXxGEMce927XV', '02ZorlDGq0uTnMobHNh4EL', '02cW3CN4DC1QV6D4XRH9UV']
    
    >>> genre_in_logenres(({}, {}), [])
    []
    >>> genre_in_logenres(({}, {}), ['Jazz', 'Comedy'])
    []
    
    >>> dict1 = {'00021Wy6AyMbLP2tqij86e': ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme', 'Capcom Sound Team', 169173, ['Anime'], \
    (129.578, 13, 0.617, 0.862)), '000DfZJww8KiixTKuk9usJ': ('000DfZJww8KiixTKuk9usJ', 'Earthlings', 'Mike Love', 357573, ['Reggae'], (120.365, 30, 0.631, 0.513)), '000EWWBkYaREzsBplYjUag': ('000EWWBkYaREzsBplYjUag', 'Fewerdolr', 'Don Philippe', 104924, ['Jazz'], (76.43, 39, 0.768, 0.137)), '000xQL6tZNLJzIrtIgxqSl': ('000xQL6tZNLJzIrtIgxqSl', 'Still Got Time', 'ZAYN', 188491, ['Dance', 'Pop'], \
    (120.963, 70, 0.748, 0.627)), '0017XiMkqbTfF2AUOzlhj6': ('0017XiMkqbTfF2AUOzlhj6', 'Thanksgiving Chicken', 'Chad Daniels', 127040, ['Comedy'], \
    (173.912, 27, 0.536, 0.78)), '001CyR8xqmmpVZFiTZJ5BC': \
    ('001CyR8xqmmpVZFiTZJ5BC', 'She Knows How To Rock Me', 'Taj Mahal', 160107, \
    ['Blues'], (90.048, 31, 0.826, 0.679)), '52TDNHSeWey4NFAfLDgfjL': ('52TDNHSeWey4NFAfLDgfjL', 'Natural Mystic - Banjamin Devigne Deep Jazz Remix', \
    'Bob Marley & The Wailers', 278987, ['Reggae'], (180.043, 31, 0.675, 0.808)), '001VMKfkHZrlyj7JlQbQFL': ('001VMKfkHZrlyj7JlQbQFL', \
    '"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"', \
    'Ramin Djawadi', 120840, ['Soundtrack'], (113.655, 41, 0.168, 0.0354)), '001YQlnDSduXd5LgBd66gT': ('001YQlnDSduXd5LgBd66gT', 'El Tiempo Es Dinero - Remasterizado 2007', 'Soda Stereo', 177267, ['Ska'], (183.571, 38, 0.554, 0.921)), '003eoIwxETJujVWmNFMoZy': ('003eoIwxETJujVWmNFMoZy', \
    'Growing Pains', 'Alessia Cara', 193680, ['Dance', 'Pop', 'R&B'], \
    (191.153, 66, 0.353, 0.755)), '00S35gEf40z03JTJgvQMqi': \
    ('00S35gEf40z03JTJgvQMqi', 'Its You - Radio Edit', 'Syn Cole', 211875, ['Dance'], (127.957, 57, 0.646, 0.831)), '01qMOMudbkIHZS9BFPUGNk': \
    ('01qMOMudbkIHZS9BFPUGNk', 'Let It Be Me (feat. Ava Max)', 'David Guetta', \
    172933, ['Dance', 'Pop'], (102.048, 62, 0.743, 0.529)), '01qNIJfMc14nxpOoM0Xwb0': ('01qNIJfMc14nxpOoM0Xwb0', 'The Fool and Me - 2007 Remaster', \
    'Robin Trower', 235720, [], (122.692, 31, 0.409, 0.766)), \
    '01w7h4gfJMHtUnykpD6M3f': ('01w7h4gfJMHtUnykpD6M3f', \
    'See Dem Fake Leaders - Dub Remix', 'Ziggy Marley', 249740, ['Reggae'], \
    (77.501, 24, 0.801, 0.636)), '01yvyZWcqtI2ZqGhPB2uZq': \
    ('01yvyZWcqtI2ZqGhPB2uZq', 'Lost Our Way', 'I-Octane', 232091, ['Reggae'], \
    (133.936, 5, 0.733, 0.492)), '02D9uD9WQb834Lb54xCvDS': \
    ('02D9uD9WQb834Lb54xCvDS', 'Love U 4 Life', 'Jodeci', 290067, \
    ['Dance', 'R&B', 'Soul'], (118.106, 53, 0.695, 0.638)), '02C5QgRFecna4B8Sv406WA': ('02C5QgRFecna4B8Sv406WA', 'Get Up  Stand Up - Thievery Corporation Remix', \
    'Bob Marley & The Wailers', 261693, ['Reggae'], (166.067, 27, 0.676, 0.702)), '02UYYPOGSBXxGEMce927XV': ('02UYYPOGSBXxGEMce927XV', \
    'Nobody (feat. Athena Cage) - Remastered Single Version', 'Keith Sweat', 251760, ['Dance', 'Soul'], (117.896, 47, 0.712, 0.511)), '02ZorlDGq0uTnMobHNh4EL': ('02ZorlDGq0uTnMobHNh4EL', 'Bravado', 'Lorde', 221409, ['Dance', 'Pop'], \
    (175.879, 60, 0.489, 0.536)), '02cW3CN4DC1QV6D4XRH9UV': \
    ('02cW3CN4DC1QV6D4XRH9UV', 'Cant Dweet Again', 'Christopher Martin', 144000, \
    ['Reggae'], (99.531, 44, 0.71, 0.645))}
    >>> genre_in_logenres(({}, dict1), ['Ska'])
    []
    >>> genre_in_logenres(({}, dict1), [])
    ['00021Wy6AyMbLP2tqij86e', '000DfZJww8KiixTKuk9usJ', '000EWWBkYaREzsBplYjUag', '000xQL6tZNLJzIrtIgxqSl', '0017XiMkqbTfF2AUOzlhj6', '001CyR8xqmmpVZFiTZJ5BC', '52TDNHSeWey4NFAfLDgfjL', '001VMKfkHZrlyj7JlQbQFL', '001YQlnDSduXd5LgBd66gT', '003eoIwxETJujVWmNFMoZy', '00S35gEf40z03JTJgvQMqi', '01qMOMudbkIHZS9BFPUGNk', '01qNIJfMc14nxpOoM0Xwb0', '01w7h4gfJMHtUnykpD6M3f', '01yvyZWcqtI2ZqGhPB2uZq', '02D9uD9WQb834Lb54xCvDS', '02C5QgRFecna4B8Sv406WA', '02UYYPOGSBXxGEMce927XV', '02ZorlDGq0uTnMobHNh4EL', '02cW3CN4DC1QV6D4XRH9UV']
    '''
    lo_track_ids = []
    
    genre_to_track_id = dict_tuple[GENRE_TO_TRACK_ID]   
    track_id_to_track_info = dict_tuple[TRACK_ID_TO_TRACK_INFO]
    
    if logenres == []:
        for track_id in track_id_to_track_info:
            if not track_id in lo_track_ids:
                lo_track_ids.append(track_id)
    else:
        for genre in logenres:
            if genre in genre_to_track_id:
                for track_id in genre_to_track_id[genre]:
                    if not track_id in lo_track_ids:
                        lo_track_ids.append(track_id)                              
    
    return lo_track_ids

def is_score_above(lo_track_info:MusicTrack, threshold:float, 
                   score_type:str) -> bool:
    '''
    returns whether the value of a given score_type in a given track info list
    is above a given threshold
    
    Precondition: score_type is one of: 'tempo', 'popularity', 'danceability', 
    or 'energy'
    Precondition: all values in MusicTrack structure exist in lo_track_info
    
    >>> lo_track_info = ('00021Wy6AyMbLP2tqij86e','Zangiefs Theme', \
    'Capcom Sound Team', 169173, ['Anime'], (129.578, 13, 0.617, 0.862))
    >>> is_score_above(lo_track_info, 130.0, 'tempo')
    False
    >>> is_score_above(lo_track_info, 12, 'popularity')
    True
    >>> is_score_above(lo_track_info, 0.862, 'energy')
    False
    
    >>> lo_track_info = ('02ZorlDGq0uTnMobHNh4EL', 'Bravado', 'Lorde', 221409, \
    ['Dance', 'Pop'], (175.879, 60, 0.489, 0.536))
    >>> is_score_above(lo_track_info, 0.312, 'danceability')
    True
    '''
    track_scores = lo_track_info[SCORES]
    scores_dict = create_scores_dict(track_scores)
    
    return scores_dict[score_type] > threshold

def create_scores_dict(track_scores:Scores) -> dict[str, float]:
    '''
    creates of a dictionary of score values in a given track_scores tuple
    Precondition: track_scores != [] and follows Scores type
    
    >>> create_scores_dict((129.578, 13, 0.617, 0.862))
    {'tempo': 129.578, 'popularity': 13, 'danceability': 0.617, 'energy': 0.862}
    >>> create_scores_dict((30.123, 2, 1.01, 0.981))
    {'tempo': 30.123, 'popularity': 2, 'danceability': 1.01, 'energy': 0.981}
    >>> create_scores_dict((0, 0, 0, 0))
    {'tempo': 0, 'popularity': 0, 'danceability': 0, 'energy': 0}
    '''
    tempo = track_scores[TEMPO]
    popularity = track_scores[POPULARITY]
    danceability = track_scores[DANCEABILITY]
    energy = track_scores[ENERGY] 
    
    scores_dict = {'tempo':tempo, 'popularity':popularity, 
                   'danceability':danceability, 'energy':energy}
    
    return scores_dict
    
def msec_to_time_tuple(millisec:int) -> Time:
    '''
    converts milliseconds to a tuple of (minutes, seconds, milliseconds) and
    returns it
    
    Precondition: millisec >= 0
    
    >>> msec_to_time_tuple(861201)
    (14, 21, 201)
    >>> msec_to_time_tuple(614480)
    (10, 14, 480)
    >>> msec_to_time_tuple(0)
    (0, 0, 0)
    >>> msec_to_time_tuple(1)
    (0, 0, 1)
    '''
    duration_min = (millisec//MS_PER_MIN)
    millisec -= (duration_min * MS_PER_MIN)
    duration_sec = (millisec//MS_PER_SECOND)
    millisec -= (duration_sec * MS_PER_SECOND)
        
    return (duration_min, duration_sec, millisec)   

def make_playlist(filename: str, logenres: list[str], loartists: list[str],
                  score_type: str, threshold: float
                  ) -> (list[str], Time):
    """ 
    creates a playlist of all tracks that fit the given criteria below,
    returns a sorted list of the track titles and the duration of the playlist

    Criteria: the titles added to the playlist must...
    - have at least one of the given genre(s) in logenres.
      If no genre is specified (empty list), all genres in library are valid;
    
    - have at least one of the given artist(s) in loartists.
      If no artist is specified (empty list), all artists in library are valid;
    - have the given score_type value above the given threshold
    
    Preconditions:
     - given genre terms must match case exactly.
       For example: 'blues' doesn't match 'Blues'
     - given artist ignores case:
         ('lorDE' is found in 'Lorde'),
       and matches on a substring:
         ('marley' is found in 'Bob Marley & The Wailers' and 'Ziggy Marley')
     - score_type is one of: 'tempo', 'popularity', 'danceability', 'energy'

    You MUST call read_file and use look ups in the returned dictionaries
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.


    >>> make_playlist('0lines_data.csv', [], [], 'tempo', 0.2)
    ([], (0, 0, 0))

    >>> make_playlist('20lines_data.csv', \
                       [], [], 'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"',
      'Bravado',
      'Cant Dweet Again',
      'Earthlings',
      'El Tiempo Es Dinero - Remasterizado 2007',
      'Fewerdolr',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Growing Pains',
      'Its You - Radio Edit',
      'Let It Be Me (feat. Ava Max)',
      'Lost Our Way',
      'Love U 4 Life',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'Nobody (feat. Athena Cage) - Remastered Single Version',
      'See Dem Fake Leaders - Dub Remix',
      'She Knows How To Rock Me',
      'Still Got Time',
      'Thanksgiving Chicken',
      'The Fool and Me - 2007 Remaster',
      'Zangiefs Theme'],
     (69, 9, 370))


    >>> make_playlist('20lines_data.csv', \
                       ['Dance', 'Pop', 'Reggae', 'not found'], \
                       [], 'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Cant Dweet Again',
      'Earthlings',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Growing Pains',
      'Its You - Radio Edit',
      'Let It Be Me (feat. Ava Max)',
      'Lost Our Way', 'Love U 4 Life',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'Nobody (feat. Athena Cage) - Remastered Single Version',
      'See Dem Fake Leaders - Dub Remix', 'Still Got Time'],
     (50, 54, 299))

    >>> make_playlist('20lines_data.csv', \
                       [], \
                       ['zayn', 'Marley', 'not there', 'LORDE', 'robin'], \
                       'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'See Dem Fake Leaders - Dub Remix',
      'Still Got Time',
      'The Fool and Me - 2007 Remaster'],
     (23, 56, 40))

    >>> make_playlist('20lines_data.csv', \
                       ['Dance', 'Pop', 'not found'], \
                       ['zayn', 'Marley', 'not there', 'LORDE'], \
                       'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Still Got Time'],
     (6, 49, 900))
    """
    lotitles = []
    total_duration = 0
    
    dict_tuple = read_file(filename)
    track_id_to_track_info = dict_tuple[TRACK_ID_TO_TRACK_INFO]
    
    lo_track_ids = genre_in_logenres(dict_tuple, logenres)
    if lo_track_ids == []:
        return ([], (0, 0, 0))

    for track_id in lo_track_ids:
        lo_track_info = track_id_to_track_info[track_id]
        score_above = is_score_above(lo_track_info, threshold, score_type)
        if score_above == True:  
            if loartists == []:
                total_duration += lo_track_info[DURATION]
                lotitles.append(lo_track_info[TITLE])
            else:
                for artist in loartists:
                    if artist.lower() in lo_track_info[ARTIST].lower():
                        total_duration += lo_track_info[DURATION]
                        lotitles.append(lo_track_info[TITLE])
    
    duration_tuple = msec_to_time_tuple(total_duration)
    return (sorted(lotitles), duration_tuple)