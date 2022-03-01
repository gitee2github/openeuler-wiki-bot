import os
import configparser

CONFIG_PATH_FILE = "/etc/openEuler-wiki-bot/wiki-bot.conf"

configParser = configparser.ConfigParser()
if not os.path.exists(CONFIG_PATH_FILE):
    CONFIG_PATH_FILE = "../wiki-bot.conf"

configParser.read(CONFIG_PATH_FILE, encoding="utf-8")

LOG_FILE_DIR = configParser.get("log", "log_file_dir", fallback='/var/log/openEuler-wiki-bot')
LOG_FILE_NAME = configParser.get("log", "log_file_name", fallback='openEuler-wiki-bot')
MAX_BYTES = configParser.get("log", "max_bytes", fallback=10 * 1024 * 1024)
BACKUP_COUNT = configParser.get("log", "backup_count", fallback=100)
