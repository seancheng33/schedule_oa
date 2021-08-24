# 图片字母验证码的配置
CAPTCHA_IMAGE_SIZE = (80,45)    # 设置图片大小
CAPTCHA_LENGTH = 4              # 字符个数
CAPTCHA_TIMEOUT = 1             # 超时（单位：分钟）

# 输出格式：输入框 验证码图片 隐藏域
CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(image)s %(hidden_field)s'
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_null',
    # 'captcha.helpers.noise_arcs',
    'captcha.helpers.noise_dots',
)

# 随机字符验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

# django连接redis的配置（使用django-redis）
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.7:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": "utf-8"
            },
            "PASSWORD": "123456789"
        }
    }
}
