artistes = {
    'Boyz II Men': {
        'Cooleyhighharmony': {
            'songs': ['Please Dont Go', 'Motownphilly', 'Under Pressure', 'Little Things'],
            'year': 1991,
            'platinum': False },
        'Christmas Interpretations': {
            'songs': ['Silent Night', 'Let It Snow', 'Share Love', 'You are not Alone', 'Do They Know', 'Cold December Nights', 'A Joyous Song', 'Share Love'],
            'year': 1993,
            'platinum': True },
        'II': {
            'songs': ['Thank You', 'All Around the World', 'U Know', 'Vibin', 'I Sit Away', 'Jezzebel', 'Khalil', 'Trying Times', 'I ll Make Love to you', 'On Bended Knees', '50 Candles', 'Water Runs Dry', 'Yesterday'],
            'year': 1994,
            'platinum': True },
        'Evolution': {
            'songs': ['4 Seasons Of Loneliness', 'Doing Just Fine', 'Girl in the Life Magazine', 'A Song for Mama', 'End of the Road'],
            'year': 1997,
            'platinum': True }
    },
    'Phil Collins': {
        'Bad':{
            'songs': ['We Fly So Close', 'Survivors', 'Please Come Out Tonight', 'Everyday'],
            'year': 1994,
            'platinum': False }
    },
    'Adele': {
        '21':{
            'songs': ['Rolling In The Deep', 'Rumour Has It', 'Turning Tables', 'Dont You Remember', 'Set Fire To The Rain', 'Take It All', 'One And Only'],
            'year': 2011,
            'platinum': True }
    },
    'Michael Jackson': {
        'Thriller':{
            'songs': ['Wanna Be Starting Something', 'Baby Be Mine', 'The Girl is Mine', 'Thriller', 'Beat It', 'Billie Jean', 'Human Nature', 'The Lady in My Life'],
            'year': 1982,
            'platinum': True },
        'Bad':{
            'songs': ['Bad', 'The Way You Make Me Feel', 'Liberian Girl', 'Just Good Friends', 'Man In The Mirror', 'Dirty Diana', 'Smooth Criminal'],
            'year': 1987,
            'platinum': True },
        'Dangerous':{
            'songs': ['Why You Wanna Trip On Me', 'Jam', 'In The Closet', 'She Drives Me Wild', 'Remember The Time', 'Heal The World', 'Black Or White', 'Who Is It', 'Give In To Me', 'Will You Be There', 'Gone Too Soon', 'Dangerous'],
            'year': 1991,
            'platinum': True },
        'Forever, Michael':{
            'songs': ['We re Almost There', 'Take Me Back', 'One Day In Your Life', 'Cinderella Stay Awhile', 'Just A Little Bit Of You', 'You Are There', 'Dapper-Dan', 'Dear Michael'],
            'year': 1975,
            'platinum': False }
    },
    'Mariah Carey': {
        "Music Box": {
            'songs': ["Dreamlover", "Hero", "Anytime You Need a Friend", "Music Box", "Now That I Know", "Never Forget You", "Without You", "Just to Hold You Once Again", "I've Been Thinking About You", "All I've Ever Wanted"],
            'year': 1993,
            'platinum': True
        },
        "Butterfly" : {
            'songs': ["Honey", "Butterfly", "My All", "The Roof", "Fourth of July", "Breakdown", "Babydoll", "Close My Eyes", "Whenever You Call", 	"Fly Away", "The Beautiful Ones", "Outside"],
            'year': 1997,
            'platinum': True
        }
    }
}

for artiste, creation in artistes.items():
    print(f"\t+{artiste}")

    for album, title in creation.items():
        print(f"\t\t-{album}")
        print(f"\t\t\t>>>{title['songs']}")