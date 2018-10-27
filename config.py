from datetime import timedelta
from redis import StrictRedis


# 配置类
class Config:
    DEBUG = True
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:1234qwer@127.0.0.1:3306/infonews"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session存储类型
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置sessionid 加密
    SESSION_USE_SIGNER = True
    SECRET_KEY = "21CZbnpBQG9psaugtjs"  # 设置应用秘钥
    PERMANENT_SESSION_LIFETIME = timedelta(days=15)  # 设置session过期时间 默认支持设置过期时间


# 针对不同的编程环境 定义配置子类
# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True


# 生产环境
class ProductConfig(Config):
    DEBUG = False


# 记录配置的对应关系
config_dict = {
    "dev": DevelopmentConfig,
    "pro": ProductConfig
}
