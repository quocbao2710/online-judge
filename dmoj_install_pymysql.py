try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass  # Bỏ qua nếu không có pymysql (khi dùng PostgreSQL)
