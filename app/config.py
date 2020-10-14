class Config:
    '''
    General configuration parent class
    '''
    #https://api.themoviedb.org/3/movie/550?api_key=977c9fd7d952560acf0046a1cb92b01a
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args: 
    Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
