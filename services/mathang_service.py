from data.repositories.interfaces.i_mathang_repo import IMatHangRepo
from core.entities.mathang import MatHang

class MatHangService:
    def __init__(self, repo: IMatHangRepo):
        self.repo = repo

    def them_mat_hang(self, tenhang: str):
        mh = MatHang(tenhang=tenhang)
        return self.repo.add(mh)

    def danh_sach(self):
        return self.repo.get_all()

    def tim_theo_ten(self, tenhang: str):
        return self.repo.get_by_name(tenhang)
