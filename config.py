from dotenv import dotenv_values

from sqlalchemy import create_engine

config_env = dict(dotenv_values(".env"))

config_mysql = {
    "mysql_usr": config_env.get("MYSQL_USER"),
    "mysql_pass": config_env.get("MYSQL_PASS"),
    "mysql_host": config_env.get("MYSQL_HOST"),
    "mysql_port": config_env.get("MYSQL_PORT"),
    "mysql_db": config_env.get("MYSQL_DB"),
}