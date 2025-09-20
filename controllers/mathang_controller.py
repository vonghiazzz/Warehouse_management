from repositories.mathang_repo_sqlite import MatHangRepository
from entities.mathang import MatHang

class MatHangController:
    def __init__(self):
        self.repo = MatHangRepository()

    def add_mat_hang(self, mat_hang: MatHang) -> bool:
        all_items = self.repo.get_all()
        if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() for item in all_items):
            return False
        self.repo.add(mat_hang)
        return True

    def get_all_mat_hang(self) -> list[MatHang]:
        return self.repo.get_all()

    def get_mat_hang_by_id(self, ma_hang: int) -> MatHang | None:
        return self.repo.get_by_id(ma_hang)

    def update_mat_hang(self, ma_hang: int, mat_hang: MatHang) -> bool:
        all_items = self.repo.get_all()
        if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() and item.ma_hang != ma_hang for item in all_items):
            return False

        self.repo.update(self, mat_hang)
        return True

    def delete_mat_hang(self, ma_hang: int) -> bool:
        item = self.repo.get_by_id(ma_hang)
        if not item:
            return False

        self.repo.soft_delete(ma_hang)
        return True
