import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration class"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    # IBM Watson ML configuration
    IBM_WATSON_ML_API_KEY = os.environ.get('IBM_WATSON_ML_API_KEY')
    IBM_WATSON_ML_URL = os.environ.get('IBM_WATSON_ML_URL', 'https://us-south.ml.cloud.ibm.com')
    IBM_WATSON_ML_PROJECT_ID = os.environ.get('IBM_WATSON_ML_PROJECT_ID')
    
    # Model configuration
    DEFAULT_MODEL_ID = 'ibm/granite-13b-chat-v2'
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    TOP_P = 0.9
    REPETITION_PENALTY = 1.1
    
    @staticmethod
    def validate_config():
        """Validate that all required configuration is present"""
        required_vars = [
            'IBM_WATSON_ML_API_KEY',
            'IBM_WATSON_ML_PROJECT_ID'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY must be set in production")

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}