import os
import dj_database_url
import pymysql
import ssl

# Đăng ký pymysql làm driver MySQL cho Django
pymysql.install_as_MySQLdb()

DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    db_config = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
    
    # FIX LỖI SSL CHO TIDB CLOUD
    # TiDB bắt buộc SSL. Chúng ta trỏ đến chứng chỉ bảo mật có sẵn trên hệ thống Render (Ubuntu)
    db_config['OPTIONS'] = {
        'ssl': {
            'ca': '/etc/ssl/certs/ca-certificates.crt',
            'check_hostname': True,
            'cert_reqs': ssl.CERT_REQUIRED
        }
    }
    
    DATABASES = {
        'default': db_config
    }
else:
    # Fallback về SQLite nếu chạy local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db.sqlite3'),
        }
    }

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static_collected')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'primary': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
