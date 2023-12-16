from interface import MahasiswaAbstract
from entity.mahasiswa import MahasiswaEntity

class MahasiswaLogic:
    def __init__(self, repo: MahasiswaAbstract):
        self.repo = repo

    def create(self, entity: MahasiswaEntity):
        self.repo.create_mahasiswa(entity)

    def creates(self, entities: list[MahasiswaEntity]):
        for ent in entities:
            self.repo.create_mahasiswa(ent)
            
    def delete(self, nim: str):
        self.repo.delete_mahasiswa(nim)

    def deletes(self, entities: list[MahasiswaEntity]):
        for ent in entities:
            self.repo.delete_mahasiswa(ent.nim)