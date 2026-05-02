"""Allow PyMySQL to satisfy Django's MySQL backend ("MySQLdb") interface."""

try:
    import pymysql  # noqa: F401

    pymysql.install_as_MySQLdb()
except ImportError:
    pass
