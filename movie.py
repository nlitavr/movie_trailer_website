# Movie class to describe movie object attributes
class Movie(object):

    # Has 3 properties that are strings
    title = ''
    box_art_url = ''
    youtube_url = ''

    # Class is initialized with all three properties
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


