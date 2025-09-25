from datetime import datetime
from entities.nhapkho import NhapKho
from repositories.nhapkho_repo_sqlite import NhapKhoRepository
from services.interfaces.i_nhapkho_service import INhapKhoService

class NhapKhoService(INhapKhoService):
    def __init__(self):
        self.repo = NhapKhoRepository()

    @staticmethod
    def validate_nhap_kho(data: NhapKho):
        errors = []

        # Mã hàng
        try:
            if not data.ma_hang or not str(data.ma_hang).strip():
                errors.append("Mã hàng không được để trống.")
        except Exception:
            errors.append("Lỗi xử lý mã hàng.")

        # Số lượng
        try:
            if not str(data.so_luong).strip():
                errors.append("Số lượng không được để trống.")
            else:
                data.so_luong = int(data.so_luong)
                if data.so_luong <= 0:
                    errors.append("Số lượng phải là số nguyên dương.")
                elif data.so_luong > 1000:
                    errors.append("Số lượng không được quá 1000.")
                elif not str(data.so_luong).isdigit():
                    errors.append("Số lượng là số nguyên dương.")
                elif any(char in str(data.so_luong) for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                    errors.append("Số lượng không được chứa ký tự đặc biệt.")
        except Exception:
            errors.append("Số lượng phải là số nguyên dương.")

        # Giá nhập
        try:
            if not str(data.gia_nhap).strip():
                errors.append("Giá nhập không được để trống.")
            else:
                data.gia_nhap = float(data.gia_nhap)
                if data.gia_nhap < 0:
                    errors.append("Giá nhập phải >= 0.")
                elif data.gia_nhap > 100000:
                    errors.append("Giá nhập không được quá 100000.")
                elif any(char in str(data.gia_nhap) for char in "!@#$%^&*()_+=[]{}|;:'\",<>?/\\`~"):
                    errors.append("Giá nhập không được chứa ký tự đặc biệt.")
                elif not str(data.gia_nhap).isdigit():
                    errors.append("Giá nhập là số dương.")
           
        except Exception:
            errors.append("Giá nhập phải là số thực.")

        # Số hóa đơn (bắt buộc, số nguyên dương)
        try:
            if not str(data.so_hoa_don).strip():
                errors.append("Số hóa đơn không được để trống.")
            else:
                data.so_hoa_don = int(data.so_hoa_don)
                if data.so_hoa_don <= 0:
                    errors.append("Số hóa đơn phải là số nguyên dương.")
                elif not str(data.so_hoa_don).isdigit():
                    errors.append("Số hóa đơn là số nguyên dương.")
                elif any(char in str(data.so_hoa_don) for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                    errors.append("Số hóa đơn không được chứa ký tự đặc biệt.")                
        except Exception:
            errors.append("Số hóa đơn phải là số nguyên.")


        # Nhà cung cấp
        try:
            if not data.nha_cung_cap.strip():
                errors.append("Nhà cung cấp không được để trống.")
            elif len(data.nha_cung_cap.strip()) < 2:
                errors.append("Tên nhà cung cấp phải có ít nhất 2 ký tự.")
            elif len(data.nha_cung_cap.strip()) > 100:
                errors.append("Tên nhà cung cấp không được quá 100 ký tự.")
            elif not all(c.isalpha() or c.isspace() for c in data.nha_cung_cap):
                errors.append("Tên nhà cung cấp chỉ được chứa chữ cái và khoảng trắng.")            
            elif data.nha_cung_cap.isdigit():
                errors.append("Tên nhà cung cấp không được là chuỗi số.")
            elif any(char in data.nha_cung_cap for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Tên nhà cung cấp không được chứa ký tự đặc biệt.")            
        except Exception:
            errors.append("Nhà cung cấp phải là chuỗi ký tự.")

        # Nhân viên nhập
        try:
            if not data.nhan_vien_nhap.strip():
                errors.append("Nhân viên nhập không được để trống.")
            elif len(data.nhan_vien_nhap.strip()) < 2:
                errors.append("Tên nhân viên phải có ít nhất 2 ký tự.")
            elif len(data.nhan_vien_nhap.strip()) > 50:
                errors.append("Tên nhân viên không được quá 50 ký tự.")
            elif not all(c.isalpha() or c.isspace() for c in data.nhan_vien_nhap):
                errors.append("Tên nhân viên chỉ được chứa chữ cái và khoảng trắng.")
            elif data.nhan_vien_nhap.isdigit():
                errors.append("Tên nhân viên không được là chuỗi số.")
            elif any(char in data.nhan_vien_nhap for char in "!@#$%^&*()_+=[]{}|;:'\",.<>?/\\`~"):
                errors.append("Tên nhân viên không được chứa ký tự đặc biệt.")
        except Exception:
            errors.append("Nhân viên nhập phải là chuỗi ký tự.")

        # Hạn sử dụng
        try:
            if data.han_su_dung:
                datetime.strptime(data.han_su_dung, "%m/%d/%Y")
                if datetime.strptime(data.han_su_dung, "%m/%d/%Y") <= datetime.now():
                    errors.append("Hạn sử dụng phải là ngày trong tương lai.")                
        except ValueError:
            errors.append("Hạn sử dụng phải theo định dạng mm/dd/yyyy.")
        except Exception:
            errors.append("Lỗi xử lý hạn sử dụng.")

        return errors

    
    def add_nhap_kho(self, nhap_kho: NhapKho) -> int:
        all_items = self.repo.get_all()
        for item in all_items:
            if (item.ma_hang == nhap_kho.ma_hang and
                item.gia_nhap == nhap_kho.gia_nhap and
                item.nha_cung_cap == nhap_kho.nha_cung_cap and
                item.han_su_dung == nhap_kho.han_su_dung):

                item.so_luong += nhap_kho.so_luong

                if item.nhan_vien_nhap:
                    item.nhan_vien_nhap += " | " + nhap_kho.nhan_vien_nhap
            
                if item.ghi_chu:
                    item.ghi_chu += " | " + nhap_kho.ghi_chu
                self.repo.update(item)
                return item.id

        # nếu không trùng, thêm mới
        return self.repo.add(nhap_kho)


    def get_all_nhap_kho(self) -> list[NhapKho]:
        return self.repo.get_all()

    def get_nhap_kho_by_id(self, id: int) -> NhapKho | None:
        return self.repo.get_by_id(id)

    def update_nhap_kho(self, id: int, nhap_kho: NhapKho) -> bool:
        existing_item = self.repo.get_by_id(id)
        if not existing_item:
            return False
        nhap_kho.id = id  
        self.repo.update(nhap_kho)
        return True

    def delete_nhap_kho(self, id: int) -> bool:
        item = self.repo.get_by_id(id)
        if not item:
            return False

        self.repo.soft_delete(id)
        return True

    def search_nhap_kho(self, keyword: str) -> list[NhapKho]:
        return self.repo.search_nhap_kho(keyword)