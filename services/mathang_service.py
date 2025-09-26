from datetime import datetime
from entities.mathang import MatHang
from repositories.mathang_repo_sqlite import MatHangRepository
from services.interfaces.i_mathang_service import IMatHangService

class MatHangService(IMatHangService):
    def __init__(self):
        self.repo = MatHangRepository()

    def validate_mat_hang(self, mat_hang: MatHang, ma_hang: int | None) -> None:        
        errors = []

        # ---- Tên hàng ----
        try:
            if(ma_hang):
                all_items = self.repo.get_all_not_id(ma_hang)
                if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() for item in all_items):
                    errors.append("Tên hàng đã tồn tại.")
            else:
                all_items = self.repo.get_all()
                if any(item.ten_hang.lower() == mat_hang.ten_hang.lower() for item in all_items):
                    errors.append("Tên hàng đã tồn tại.")
            if not mat_hang.ten_hang or not mat_hang.ten_hang.strip():
                errors.append("Tên hàng không được để trống.")
            elif len(mat_hang.ten_hang.strip()) < 2:
                errors.append("Tên hàng phải có ít nhất 2 ký tự.")
            elif len(mat_hang.ten_hang.strip()) > 100:
                errors.append("Tên hàng không được quá 100 ký tự.")
            elif any(char in mat_hang.ten_hang for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Tên hàng không được chứa ký tự đặc biệt.")
            elif mat_hang.ten_hang.isdigit():
                errors.append("Tên hàng không được là chuỗi số.")
        except Exception:
            errors.append("Tên hàng phải là chuỗi và không quá 100 ký tự.")

        # ---- Đơn vị tính ----
        try:
            if not mat_hang.don_vi or not mat_hang.don_vi.strip():
                errors.append("Đơn vị tính không được để trống.")
            elif len(mat_hang.don_vi.strip()) > 20:
                errors.append("Đơn vị tính không được quá 20 ký tự.")
        except Exception:
            errors.append("Lỗi xử lý đơn vị tính.")

        # ---- Loại hàng ----
        try:
            if not mat_hang.loai or not mat_hang.loai.strip():
                errors.append("Loại hàng không được để trống.")
            elif len(mat_hang.loai.strip()) > 50:
                errors.append("Loại hàng không được quá 50 ký tự.")
            elif any(char in mat_hang.loai for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Loại hàng không được chứa ký tự đặc biệt.")
            elif mat_hang.loai.isdigit():
                errors.append("Loại hàng không được là chuỗi số.")
        except Exception:
            errors.append("Loại hàng phải là chuỗi và không quá 50 ký tự.")

        # ---- Mô tả ----
        try:
            if len(mat_hang.mo_ta.strip()) > 200:
                errors.append("Mô tả không được quá 200 ký tự.")
            elif any(char in mat_hang.mo_ta for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Mô tả không được chứa ký tự đặc biệt.")
        except Exception:
            errors.append("Mô tả phải là chuỗi và không quá 200 ký tự.")

        # ---- Tồn tối thiểu ----
        try:
            ton = int(mat_hang.ton_toi_thieu)
            if ton < 5:
                errors.append("Tồn tối thiểu phải >= 5.")
            elif ton > 100:
                errors.append("Tồn tối thiểu không được quá 100.")
            elif not str(mat_hang.ton_toi_thieu).isdigit():
                errors.append("Tồn tối thiểu phải là số nguyên.")
            elif any(char in str(mat_hang.ton_toi_thieu) for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Tồn tối thiểu không được chứa ký tự đặc biệt.")            

        except Exception:
            errors.append("Tồn tối thiểu phải là số nguyên dương.")

        # ---- Trạng thái ----
        try:
            if mat_hang.trang_thai not in ["Hoạt động", "Ngừng kinh doanh"]:
                errors.append("Trạng thái không hợp lệ.")
        except Exception:
            errors.append("Lỗi xử lý trạng thái.")
        return errors

            
        
    def add_mat_hang(self, mat_hang: MatHang) -> bool:
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
