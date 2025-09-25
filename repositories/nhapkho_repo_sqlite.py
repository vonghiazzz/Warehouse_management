from CTO.nhapkho_history_dto import NhapKhoHistoryDTO
from database.database import get_connection
from entities.nhapkho import NhapKho
from repositories.interfaces.i_nhapkho_repo import INhapKhoRepository
from datetime import datetime

class NhapKhoRepository(INhapKhoRepository):
    def add(self, nhap_kho: NhapKho) -> int:
        with get_connection() as conn:
            cursor = conn.cursor()
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

    def get_history_by_mat_hang(self, ma_hang: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT 
                    nk.ID, mh.TenHang, nk.SoLuong, nk.GiaNhap, nk.NhaCungCap, 
                    nk.NhanVienNhap, nk.HanSuDung, nk.SoHoaDon, nk.GhiChu, nk.NgayTao, nk.IsDeleted
                FROM NhapKho nk
                JOIN MatHang mh ON nk.MaHang = mh.MaHang
                WHERE nk.MaHang = ? AND nk.IsDeleted = 0
                """,
                (ma_hang,),
            )
            rows = cursor.fetchall()
            return [
                NhapKhoHistoryDTO(
                    id = row[0],
                    ten_hang=row[1],
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
        