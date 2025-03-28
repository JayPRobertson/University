import doctest

# represents a country population as (number of people, country name)
# number of people > 0
PopulationInfo = tuple[int, str]

# represents an index of countries and their populations 
# dict[country name, number of people]
# number of people > 0
PopulationDict = dict[str, int]

# in file
COUNTRY = 0
POPULATION = 1

# in tuple
POPULATION_DICT = 0
GRANULARITY_DICT = 1

def count_evens_odds(filename: str) -> dict[str, int]:
    """ returns a dictionary with exactly two key:value pairs
    {'Even': count of even numbers, 'Odd': count of odd numbers}
    >>> count_evens_odds('empty.txt')
    {'Even': 0, 'Odd': 0}
    >>> count_evens_odds('numbers_small.txt')
    {'Even': 6, 'Odd': 8}
    >>> count_evens_odds('numbers.txt')
    {'Even': 588, 'Odd': 565}
    """
    count_dict = {'Even':0, 'Odd':0}
    
    filehandle = open(filename, 'r')
    for num in filehandle:
        num = int(num.strip())
        if num%2 == 0:
            count_dict['Even'] += 1
        else:
            count_dict['Odd'] += 1       
    filehandle.close()
    
    return count_dict

def get_number_frequencies(filename: str) -> dict[int, int]:
    """ returns a dictionary with counts of unique numbers found in filename
    and the frequency they occur within filename:
    - Dict[unique number: number of occurances in filename]
    >>> get_number_frequencies('empty.txt')
    {}

    >>> get_number_frequencies('numbers_small.txt')
    {865: 2, 771: 5, 633: 1, 200: 5, 866: 1}

    >>> get_number_frequencies('numbers.txt')
    {865: 1, 633: 2, 798: 1, 905: 2, 866: 2, 842: 1, 793: 1, 771: 2, 200: 1, \
701: 2, 861: 1, 510: 4, 158: 3, 985: 3, 573: 4, 575: 3, 435: 2, 645: 4, \
478: 2, 403: 2, 227: 5, 122: 1, 294: 1, 914: 1, 368: 2, 605: 1, 163: 2, \
297: 2, 770: 4, 111: 1, 363: 2, 105: 2, 713: 1, 57: 2, 12: 2, 306: 1, 582: 2, \
869: 1, 494: 3, 930: 2, 524: 2, 355: 2, 38: 1, 378: 1, 653: 1, 891: 1, 509: 2, \
523: 2, 452: 3, 253: 3, 339: 2, 941: 2, 67: 2, 391: 2, 99: 1, 958: 2, 920: 5, \
347: 1, 323: 2, 949: 1, 169: 2, 706: 2, 858: 1, 704: 3, 727: 1, 116: 1, \
448: 1, 991: 2, 796: 4, 789: 1, 192: 2, 970: 3, 20: 4, 724: 2, 142: 2, 173: 1, \
50: 2, 763: 3, 370: 1, 975: 2, 287: 1, 386: 1, 69: 1, 89: 1, 245: 3, 304: 3, \
656: 3, 167: 2, 1000: 2, 174: 1, 230: 1, 367: 1, 520: 2, 774: 2, 951: 1, \
820: 1, 71: 3, 613: 3, 778: 1, 94: 2, 74: 3, 296: 2, 799: 1, 879: 1, 170: 1, \
251: 1, 258: 2, 224: 3, 271: 1, 604: 1, 480: 2, 358: 1, 97: 1, 92: 4, 691: 5, \
332: 1, 1: 2, 447: 2, 649: 1, 537: 1, 16: 3, 697: 2, 683: 5, 936: 1, 9: 1, \
779: 2, 84: 3, 402: 2, 617: 1, 628: 2, 759: 1, 927: 6, 441: 2, 629: 1, 880: 2, \
345: 2, 45: 2, 154: 2, 551: 3, 232: 2, 564: 4, 204: 1, 4: 2, 114: 2, 851: 2, \
654: 1, 657: 2, 968: 2, 95: 1, 658: 1, 599: 3, 850: 1, 288: 3, 938: 1, 91: 4, \
203: 2, 752: 1, 966: 3, 885: 4, 516: 5, 333: 3, 963: 2, 285: 1, 453: 3, \
517: 1, 146: 2, 58: 1, 109: 1, 214: 3, 609: 1, 147: 2, 606: 1, 263: 1, 295: 2, \
73: 2, 823: 2, 372: 5, 196: 2, 33: 1, 25: 2, 767: 1, 898: 1, 948: 2, 533: 2, \
504: 4, 426: 2, 115: 2, 901: 1, 775: 2, 871: 1, 160: 1, 627: 1, 438: 2, \
758: 1, 900: 2, 950: 1, 804: 5, 351: 1, 133: 1, 455: 6, 856: 2, 707: 1, \
317: 3, 470: 2, 572: 1, 104: 2, 54: 1, 637: 1, 128: 1, 195: 2, 640: 1, 268: 1, \
342: 1, 928: 2, 878: 2, 847: 1, 616: 2, 837: 4, 838: 1, 693: 1, 36: 1, 626: 3, \
139: 2, 984: 2, 303: 2, 780: 1, 15: 1, 239: 2, 477: 1, 688: 1, 877: 1, 300: 1, \
335: 2, 423: 2, 979: 3, 409: 1, 886: 2, 559: 2, 893: 3, 560: 4, 17: 2, 954: 2, \
385: 2, 353: 4, 310: 2, 548: 1, 792: 1, 916: 2, 277: 1, 957: 1, 555: 1, 60: 2, \
157: 2, 165: 2, 10: 1, 207: 1, 721: 1, 666: 1, 590: 2, 689: 2, 694: 3, 406: 2, \
149: 2, 59: 1, 791: 2, 569: 2, 825: 2, 515: 2, 622: 2, 318: 2, 863: 3, 280: 2, \
545: 1, 868: 2, 744: 1, 567: 3, 944: 1, 603: 1, 508: 3, 327: 3, 266: 3, \
561: 2, 236: 1, 574: 1, 379: 1, 246: 1, 874: 5, 6: 1, 28: 3, 641: 2, 276: 4, \
264: 1, 395: 2, 731: 1, 47: 1, 772: 1, 790: 1, 708: 3, 924: 2, 981: 2, 762: 4, \
357: 2, 437: 2, 462: 1, 369: 1, 32: 1, 241: 1, 915: 2, 126: 3, 876: 3, 375: 1, \
746: 3, 684: 1, 40: 1, 747: 2, 206: 3, 434: 1, 737: 2, 238: 1, 902: 2, 855: 1, \
557: 1, 741: 1, 715: 2, 359: 3, 887: 1, 812: 3, 63: 2, 857: 2, 211: 2, 352: 3, \
624: 3, 250: 1, 79: 1, 286: 3, 278: 1, 646: 5, 907: 2, 316: 3, 986: 3, 179: 1, \
912: 2, 996: 1, 217: 2, 308: 1, 185: 1, 42: 2, 558: 1, 929: 4, 81: 2, 735: 2, \
695: 2, 487: 2, 389: 1, 425: 1, 983: 2, 321: 4, 733: 2, 144: 2, 53: 2, 870: 2, \
639: 2, 484: 1, 670: 2, 699: 1, 749: 2, 845: 5, 7: 2, 233: 2, 361: 1, 186: 1, \
151: 2, 655: 1, 593: 1, 408: 1, 98: 2, 382: 1, 446: 1, 14: 1, 800: 1, 680: 2, \
322: 2, 189: 1, 311: 1, 465: 1, 110: 3, 919: 3, 23: 1, 718: 1, 117: 3, 743: 1, \
797: 1, 166: 1, 665: 1, 685: 3, 648: 1, 400: 2, 281: 3, 168: 2, 910: 2, 30: 1, \
143: 1, 601: 2, 882: 2, 298: 3, 130: 2, 782: 2, 420: 1, 589: 1, 305: 1, \
895: 2, 101: 2, 77: 1, 507: 1, 765: 2, 760: 1, 894: 1, 538: 2, 570: 2, 283: 3, \
859: 1, 751: 2, 314: 2, 940: 3, 90: 1, 982: 1, 344: 3, 155: 3, 501: 2, 785: 1, \
191: 1, 973: 1, 911: 1, 598: 1, 457: 1, 993: 2, 897: 1, 786: 1, 489: 3, \
292: 1, 220: 1, 615: 1, 324: 2, 612: 2, 265: 1, 55: 1, 275: 3, 781: 2, 223: 1, \
836: 1, 644: 3, 376: 2, 808: 3, 953: 1, 676: 1, 315: 3, 784: 2, 675: 2, \
460: 1, 814: 1, 137: 2, 267: 3, 674: 1, 807: 1, 407: 2, 215: 2, 202: 2, \
580: 1, 662: 2, 248: 1, 841: 1, 862: 1, 829: 1, 410: 1, 769: 2, 925: 3, \
884: 2, 86: 1, 594: 1, 933: 1, 530: 3, 738: 1, 243: 1, 716: 1, 396: 1, 208: 2, \
832: 2, 209: 1, 634: 2, 795: 1, 413: 2, 709: 1, 125: 1, 103: 1, 661: 1, \
788: 1, 720: 1, 750: 1, 908: 3, 302: 2, 132: 1, 974: 1, 343: 1, 571: 1, \
123: 2, 87: 2, 822: 1, 272: 1, 566: 1, 183: 2, 947: 1, 608: 2, 18: 3, 997: 1, \
56: 4, 62: 2, 621: 1, 964: 1, 138: 1, 282: 1, 164: 1, 906: 1, 68: 1, 422: 2, \
182: 1, 565: 1, 987: 1, 764: 2, 307: 1, 134: 1, 150: 2, 980: 1, 889: 2, \
969: 2, 394: 1, 499: 2, 398: 1, 835: 1, 816: 1, 135: 1, 112: 2, 505: 2, \
412: 2, 525: 1, 810: 1, 430: 1, 190: 1, 881: 1, 26: 1, 888: 2, 194: 1, 692: 2, \
48: 1, 923: 3, 469: 2, 44: 1, 817: 1, 776: 2, 249: 1, 140: 1, 257: 1, 393: 2, \
630: 1, 261: 3, 492: 3, 496: 1, 931: 1, 131: 1, 710: 2, 839: 1, 219: 1, \
371: 1, 172: 2, 801: 1, 120: 2, 988: 1, 729: 1, 424: 1, 212: 1, 890: 1, \
864: 2, 549: 1, 11: 1, 592: 1, 935: 3, 473: 2, 100: 2, 811: 1, 390: 3, 338: 1, \
711: 1, 348: 1, 228: 1, 643: 1, 591: 1, 754: 1, 222: 1, 917: 1, 959: 2, \
442: 1, 113: 2, 436: 2, 726: 2, 892: 1, 635: 1, 419: 1, 583: 1, 22: 1, 768: 1, \
539: 1, 34: 1, 381: 2, 75: 1, 85: 1, 831: 1, 631: 1, 429: 1, 490: 1, 596: 1, \
990: 1, 512: 1, 8: 1, 529: 1, 918: 1, 677: 1, 610: 1, 96: 2, 328: 1, 840: 1, \
301: 1, 416: 1, 171: 1, 360: 1, 454: 1, 198: 1, 755: 1, 458: 1, 552: 1, \
313: 2, 581: 1, 377: 2, 921: 1, 899: 1, 384: 1, 531: 1, 118: 1, 904: 1, \
440: 1, 244: 2, 72: 1, 349: 1, 826: 1, 210: 1, 734: 2, 226: 1, 614: 1, 88: 1, \
740: 2, 242: 1, 225: 1, 698: 1, 896: 1, 218: 1, 290: 1, 415: 1, 459: 1, \
563: 1, 943: 1, 503: 1, 961: 2, 284: 1, 161: 1, 651: 1, 76: 1, 262: 1, 270: 1, \
474: 1, 625: 1, 577: 1, 414: 1, 19: 1}
    """
    count_dict = {}
    
    filehandle = open(filename, 'r')
    for num in filehandle:
        num = int(num.strip())
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
            
    filehandle.close()
    return count_dict

def most_freq_number(filename: str) -> list[int]:
    """ returns a sorted list of the numbers in filename
    that have the highest frequency.
    >>> most_freq_number('empty.txt')
    []
    >>> most_freq_number('numbers_small.txt')
    [200, 771]
    >>> most_freq_number('numbers.txt')
    [455, 927]
    """
    freq_dict = get_number_frequencies(filename)
    new_list = []
    prev = 0
    
    for key in freq_dict:
        if freq_dict[key] > prev:
            prev = freq_dict[key]
            new_list = [key]
        elif freq_dict[key] == prev:
            new_list.append(key)      
    
    return sorted(new_list)

def create_population_dictionaries(filename: str, granularity: int
                                   ) -> (dict[str, int], dict[int, list[str]]):
    """ read population counts from filename into dictionaries:
    - Dict[country name: population]
    - Dict[population granularity: country names with population granularity]
    Returns the 2 dictionaries as a tuple.

    Precondition: assumes filename contains only one entry for each country
    granularity > 0
    >>> create_population_dictionaries('empty.txt', 10000)
    ({}, {})
    >>> create_population_dictionaries('populations_small.csv', 10000)
    ({'St. Martin (French part)': 31949, 'Nauru': 13049, 'Palau': 21503, \
'British Virgin Islands': 30661, 'San Marino': 33203, 'Gibraltar': 34408, \
'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}, \
{3: ['St. Martin (French part)', 'British Virgin Islands', 'San Marino', \
'Gibraltar', 'Monaco', 'Turks and Caicos Islands', 'Liechtenstein'], \
1: ['Nauru'], \
2: ['Palau']})
    >>> create_population_dictionaries('populations_small.csv', 1000)
    ({'St. Martin (French part)': 31949, 'Nauru': 13049, 'Palau': 21503, \
'British Virgin Islands': 30661, 'San Marino': 33203, 'Gibraltar': 34408, \
'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}, \
{31: ['St. Martin (French part)'], \
13: ['Nauru'], 21: ['Palau'], \
30: ['British Virgin Islands'], \
33: ['San Marino'], \
34: ['Gibraltar', 'Turks and Caicos Islands'], \
38: ['Monaco'], \
37: ['Liechtenstein']})
    """
    population_dict = create_population_dict(filename)
    granularity_dict = create_granularity_dict(population_dict, granularity)
    return (population_dict, granularity_dict)
     

def create_population_dict(filename:str) -> PopulationDict:
    '''
    reads population counts from filename into Dict[country name: population] 
    and returns it
    
    Precondition: assumes filename contains only one entry for each country
    
    >>> create_population_dict('empty.txt')
    {}
    >>> create_population_dict('populations_small.csv')
    {'St. Martin (French part)': 31949, 'Nauru': 13049, 'Palau': 21503, \
'British Virgin Islands': 30661, 'San Marino': 33203, 'Gibraltar': 34408, \
'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}
    '''
    population_dict = {}
    
    filehandle = open(filename, 'r')
    for line in filehandle:
        line = line.strip()
        line = line.split(',')
        population_dict[line[COUNTRY]] = int(line[POPULATION])
    
    filehandle.close() 
    return population_dict
    
def create_granularity_dict(population_dict:PopulationDict,
                            granularity:int) -> dict[int,list[str]]:
    '''
    reads population counts from filename into Dict[population granularity: 
    country names with population granularity] and returns it

    Precondition: assumes filename contains only one entry for each country
    granularity > 0
    
    >>> dictionary = {}
    >>> create_granularity_dict(dictionary, 10000)
    {}
    
    >>> dictionary = {'St. Martin (French part)': 31949, 'Nauru': 13049, \
'Palau': 21503,'British Virgin Islands': 30661, 'San Marino': 33203, \
'Gibraltar': 34408, 'Monaco': 38499, 'Turks and Caicos Islands': 34900, 'Liechtenstein': 37666}
    >>> create_granularity_dict(dictionary, 10000)
    {3: ['St. Martin (French part)', 'British Virgin Islands', 'San Marino', \
'Gibraltar', 'Monaco', 'Turks and Caicos Islands', 'Liechtenstein'], \
1: ['Nauru'], \
2: ['Palau']}
    >>> create_granularity_dict(dictionary, 1000)
    {31: ['St. Martin (French part)'], \
13: ['Nauru'], 21: ['Palau'], \
30: ['British Virgin Islands'], \
33: ['San Marino'], \
34: ['Gibraltar', 'Turks and Caicos Islands'], \
38: ['Monaco'], \
37: ['Liechtenstein']}
    '''
    granularity_dict = {}
        
    for country in population_dict:
        population_bin = population_dict[country]//granularity
        if population_bin in granularity_dict:
            granularity_dict[population_bin].append(country)
        else:
            granularity_dict[population_bin] = [country]
        
    return granularity_dict  

def population_analysis(filename: str, country: str, granularity: int
                        ) -> list[PopulationInfo]:
    """  given the population counts in filename, calculates
    the population bin of the given country using the given granularity.
    Creates a returns a sorted list of PopulationInfo for all countries
    in the same population bin as the given country.

    Precondition: country must be in english with correct capitalization
    granularity > 0
    >>> population_analysis('empty.txt', 'Canada', 1000)
    []
    >>> population_analysis('populations_small.csv', 'Canada', 1000)
    []
    >>> population_analysis('populations_small.csv', 'monaco', 1000)
    []
    >>> population_analysis('populations_small.csv', 'San Marino', 1000)
    [(33203, 'San Marino')]
    >>> population_analysis('populations_small.csv', 'Monaco', 10000)
    [(30661, 'British Virgin Islands'), (31949, 'St. Martin (French part)'), \
(33203, 'San Marino'), (34408, 'Gibraltar'), \
(34900, 'Turks and Caicos Islands'), (37666, 'Liechtenstein'), \
(38499, 'Monaco')]
    >>> population_analysis('populations.csv', 'Canada', 1000000)
    [(36286425, 'Canada')]
    >>> population_analysis('populations.csv', 'Jamaica', 1000000)
    [(2064845, 'Slovenia'), (2203821, 'Lesotho'), (2250260, 'Botswana'), \
(2479713, 'Namibia'), (2569804, 'Qatar'), (2872298, 'Lithuania'), \
(2876101, 'Albania'), (2881355, 'Jamaica'), (2924816, 'Armenia')]
    """
    new_list = []
    
    population_tuple = create_population_dictionaries(filename, granularity)
    population_dict = population_tuple[POPULATION_DICT]
    granularity_dict = population_tuple[GRANULARITY_DICT]
    
    if not country in population_dict:
        return new_list
    
    population_bin = population_dict[country]//granularity
    
    for country in granularity_dict[population_bin]:
        population = population_dict[country]
        population_info_tuple = (population, country)
        new_list.append(population_info_tuple)
    
    return sorted(new_list)