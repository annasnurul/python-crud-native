from database.db import MySQLDatabase
from repository.mahasiswa import MahasiswaRepo
from logic.mahasiswa import MahasiswaLogic
from entity.mahasiswa import MahasiswaEntity
import config

# Configuration
mysql_config = {
    "host": config.DB_HOST,
    "user": config.DB_USER,
    "password": config.DB_PASSWORD,
    "database": config.DB_DATABASE,
}

# Initialization
mysql_db = MySQLDatabase(**mysql_config)
mhs_repo = MahasiswaRepo(db=mysql_db)
mhs_logic = MahasiswaLogic(repo=mhs_repo)

# Usage
mhs = [
    MahasiswaEntity("2207004", "Annas Nurul Hakim", "Garut"),
    MahasiswaEntity("2207009", "ilham", "Garut"),
    MahasiswaEntity("2207010", "daffa", "Garut"),
    MahasiswaEntity("220795", "duka", "Garut"),
    ]
# mhs_logic.creates(mhs)
mhs_logic.delete(mhs[3].nim)
