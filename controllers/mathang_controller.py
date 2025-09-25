from repositories.mathang_repo_sqlite import MatHangRepository
from entities.mathang import MatHang
from services.mathang_service import MatHangService
class MatHangController:
    def __init__(self):
        self.repo = MatHangRepository()
        self.service = MatHangService()

    def add_mat_hang(self, mat_hang: MatHang) -> int | None:
        try:
            all_items = self.repo.get_all()
            if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() for item in all_items):
                return -1
            return self.repo.add(mat_hang)
        except Exception as e:
            print(f"Lỗi SQL khi thêm mặt hàng: {e}")
            return None
        

    def get_all_mat_hang(self) -> list[MatHang] | None:
        try:
            return self.repo.get_all()
        except Exception as e:
            print(f"Lỗi SQL khi lấy danh sách mặt hàng: {e}")
            return None

    def get_mat_hang_by_id(self, ma_hang: int) -> MatHang | None:
        try:
            return self.repo.get_by_id(ma_hang)
        except Exception as e:
            print(f"Lỗi SQL khi lấy mặt hàng theo ID {ma_hang}: {e}")
            return None

    def update_mat_hang(self, ma_hang: int, mat_hang: MatHang) -> bool:
        try:
            all_items = self.repo.get_all()
            if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() and item.ma_hang != ma_hang for item in all_items):
                return False

            self.repo.update(mat_hang)
            return True
        except Exception as e:
            print(f"Lỗi SQL khi cập nhật mặt hàng {ma_hang}: {e}")
            return False

    def delete_mat_hang(self, ma_hang: int) -> bool:
        try:
            item = self.repo.get_by_id(ma_hang)
            if not item:
                return False

            self.repo.soft_delete(ma_hang)
            return True
        except Exception as e:
            print(f"Lỗi SQL khi xóa mặt hàng {ma_hang}: {e}")
            return False
        self.repo.soft_delete(ma_hang)
        return True
    
    def validate_mat_hang(self, data: MatHang) -> list[str]:
        return self.service.validate_mat_hang(data)
