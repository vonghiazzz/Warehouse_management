from database.database import get_connection
from entities.nhapkho import NhapKho
from repositories.interfaces.i_nhapkho_repo import INhapKhoRepository
from datetime import datetime

class NhapKhoRepository(INhapKhoRepository):
    def add(self, nhap_kho: NhapKho) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
                # self.id = id
                # self.ma_hang = ma_hang
                # self.ngay_nhap = ngay_nhap
                # self.so_luong = so_luong
                # self.gia_nhap = gia_nhap
                # self.nha_cung_cap = nha_cung_cap
                # self.nhan_vien_nhap = nhan__vien_nhap   
                # self.han_su_dung = han_su_dung
                # self.so_hoa_don = so_hoa_don
                # self.ghi_chu = ghi_chu
                # self.ngay_tao = ngay_tao
                # self.isDelete = isDelete
            cursor.execute(
                """
                INSERT INTO NhapKho 
                (MaHang, SoLuong, GiaNhap, NhaCungCap, NhanVienNhap, HanSuDung, SoHoaDon, GhiChu, NgayTao, IsDeleted) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    nhap_kho.ma_hang,
                    nhap_kho.so_luong,
                    nhap_kho.gia_nhap,
                    nhap_kho.nha_cung_cap,
                    nhap_kho.nhan_vien_nhap,
                    nhap_kho.han_su_dung,
                    nhap_kho.so_hoa_don,
                    nhap_kho.ghi_chu,                
                    nhap_kho.ngay_tao.strftime("%Y-%m-%d %H:%M:%S"),
                    nhap_kho.is_delete,
                ),
            )
            conn.commit()
            new_id = cursor.lastrowid              
            nhap_kho.id = new_id  
            return new_id



    def get_all(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT ID,MaHang, SoLuong, GiaNhap, NhaCungCap, NhanVienNhap, HanSuDung, SoHoaDon, GhiChu, NgayTao, IsDeleted
                FROM NhapKho 
                WHERE IsDeleted = 0
                """
            )
            rows = cursor.fetchall()
            return [
                NhapKho(
                    id = row[0],
                    ma_hang=row[1],
                    so_luong=row[2],
                    gia_nhap=row[3],
                    nha_cung_cap=row[4],
                    nhan_vien_nhap=row[5],
                    han_su_dung=row[6],
                    so_hoa_don=row[7],
                    ghi_chu=row[8],
                    ngay_tao=row[9],
                    is_delete=row[10],                    
                )
                for row in rows
            ]

    def get_by_id(self, nhap_kho: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT ID,MaHang, SoLuong, GiaNhap, NhaCungCap, NhanVienNhap, HanSuDung, SoHoaDon, GhiChu, NgayTao, IsDeleted
                FROM NhapKho 
                WHERE ID = ? AND IsDeleted = 0
                """,
                (nhap_kho,),
            )
            row = cursor.fetchone()
            if row:
                return NhapKho(
                    id = row[0],
                    ma_hang=row[1],
                    so_luong=row[2],
                    gia_nhap=row[3],
                    nha_cung_cap=row[4],
                    nhan_vien_nhap=row[5],
                    han_su_dung=row[6],
                    so_hoa_don=row[7],
                    ghi_chu=row[8],
                    ngay_tao=row[9],
                    is_delete=row[10],                    
                )
            return None

    def update(self, nhap_kho: NhapKho):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE NhapKho 
                SET MaHang=?, SoLuong=?, GiaNhap=?, NhaCungCap=?, NhanVienNhap=?, HanSuDung=?, SoHoaDon=?, GhiChu=?
                WHERE ID=? AND IsDeleted=0
                """,
                (
                    nhap_kho.ma_hang,
                    nhap_kho.so_luong,
                    nhap_kho.gia_nhap,
                    nhap_kho.nha_cung_cap,
                    nhap_kho.nhan_vien_nhap,
                    nhap_kho.han_su_dung,
                    nhap_kho.so_hoa_don,
                    nhap_kho.ghi_chu,                
                    nhap_kho.id,
                ),
            )
            conn.commit()

    def soft_delete(self, id: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE NhapKho SET IsDeleted = 1 WHERE ID = ?",
                (id,),
            )
            conn.commit()

    def search_nhap_kho(self, keyword: str) -> list[NhapKho]:
        with get_connection() as conn:
            cursor = conn.cursor()
            like_keyword = f"%{keyword}%"
            cursor.execute(
                """
                SELECT ID,MaHang, SoLuong, GiaNhap, NhaCungCap, NhanVienNhap, HanSuDung, SoHoaDon, GhiChu, NgayTao, IsDeleted
                FROM NhapKho 
                WHERE (NhaCungCap LIKE ? OR NhanVienNhap LIKE ? OR SoHoaDon LIKE ? OR GhiChu LIKE ?) AND IsDeleted = 0
                """,
                (like_keyword, like_keyword, like_keyword, like_keyword),
            )
            rows = cursor.fetchall()
            return [
                NhapKho(
                    id = row[0],
                    ma_hang=row[1],
                    so_luong=row[2],
                    gia_nhap=row[3],
                    nha_cung_cap=row[4],
                    nhan_vien_nhap=row[5],
                    han_su_dung=row[6],
                    so_hoa_don=row[7],
                    ghi_chu=row[8],
                    ngay_tao=row[9],
                    is_delete=row[10],                    
                )
                for row in rows
            ]
        
    def validate_nhap_kho(self, data: NhapKho):
        errors = []

        if data.so_luong <= 0:
            errors.append("Số lượng phải lớn hơn 0.")

        if data.gia_nhap <= 0:
            errors.append("Giá nhập phải lớn hơn 0.")

        if not data.ma_hang:
            errors.append("Mã hàng không được để trống.")

        if not data.so_hoa_don.strip():
            errors.append("Số hóa đơn không được để trống.")

        if len(data.so_hoa_don) > 50:
            errors.append("Số hóa đơn không được vượt quá 50 ký tự.")

        if len(data.ghi_chu) > 200:
            errors.append("Ghi chú không được vượt quá 200 ký tự.")

        if len(data.nha_cung_cap) > 100:
            errors.append("Nhà cung cấp không được vượt quá 100 ký tự.")

        if len(data.nhan_vien_nhap) > 100:
            errors.append("Nhân viên nhập không được vượt quá 100 ký tự.")

        if not data.nha_cung_cap.strip():
            errors.append("Nhà cung cấp không được để trống.")

        if not data.nhan_vien_nhap.strip():
            errors.append("Nhân viên nhập không được để trống.")

        # Check hạn sử dụng (nếu có)
        if data.han_su_dung:
            try:
                datetime.strptime(data.han_su_dung, "%Y-%m-%d")
            except ValueError:
                errors.append("Hạn sử dụng phải theo định dạng YYYY-MM-DD.")

        return errors