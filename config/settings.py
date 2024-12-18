# config/settings.py
import os
import logging
from dotenv import load_dotenv

load_dotenv()


class Config:
  # MT5 settings
    MT5_LOGIN = os.getenv('MT5_LOGIN')
    MT5_PASSWORD = os.getenv('MT5_PASSWORD')
    MT5_SERVER = os.getenv('MT5_SERVER')
    MODE = os.getenv('MODE', 'demo')
    
    # Trading settings
    SYMBOL = os.getenv('SYMBOL', 'EURUSD')
    TIMEFRAME = os.getenv('TIMEFRAME', 'H1')  # M1, M5, M15, M30, H1, H4, D1, W1, MN1
    LOT_SIZE = float(os.getenv('LOT_SIZE', '0.01'))
    
    # API kalitlari
    ECONOMIC_API_KEY = os.getenv('ECONOMIC_API_KEY')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    CRYPTO_API_KEY = os.getenv('CRYPTO_API_KEY')
    
    # Fundamental analiz
    USE_FUNDAMENTAL_ANALYSIS = os.getenv('USE_FUNDAMENTAL_ANALYSIS', 'true').lower() == 'true'
    MACRO_ANALYSIS = os.getenv('MACRO_ANALYSIS', 'true').lower() == 'true'
    COMPANY_ANALYSIS = os.getenv('COMPANY_ANALYSIS', 'true').lower() == 'true'
    SECTOR_ANALYSIS = os.getenv('SECTOR_ANALYSIS', 'true').lower() == 'true'
    
    # Risk management
    USE_RISK_MANAGEMENT = os.getenv('USE_RISK_MANAGEMENT', 'true').lower() == 'true'
    MAX_DAILY_LOSS = float(os.getenv('MAX_DAILY_LOSS', '-2.0'))
    MAX_POSITION_SIZE = float(os.getenv('MAX_POSITION_SIZE', '0.1'))
    
    # AI model parametrlari
    MODEL_UPDATE_INTERVAL = int(os.getenv('MODEL_UPDATE_INTERVAL', '168'))
    FEATURE_ENGINEERING = os.getenv('FEATURE_ENGINEERING', 'true').lower() == 'true'
    DEEP_LEARNING = os.getenv('DEEP_LEARNING', 'false').lower() == 'true'
    
    # Signal weights
    SIGNAL_WEIGHTS = {
        'technical': float(os.getenv('TECHNICAL_WEIGHT', '0.4')),
        'fundamental': float(os.getenv('FUNDAMENTAL_WEIGHT', '0.4')),
        'sentiment': float(os.getenv('SENTIMENT_WEIGHT', '0.2'))
    }
