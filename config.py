import os


class Config:
    '''
    Main configurations class
    '''

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/{}?apiKey={}'


class ProdConfig(Config):
    '''
    Production configuration class that inherits from the main configurations class
    '''

    pass


class DevConfig(Config):
    '''
    Configuration class for development stage of the app
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
