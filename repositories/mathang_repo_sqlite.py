from database.database import get_connection
from entities.mathang import MatHang
from repositories.interfaces.i_mathang_repo import IMatHangRepository
from datetime import datetime

class MatHangRepository(IMatHangRepository):
    def add(self, mat_hang: MatHang):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO MatHang 
            (TenHang, DonViTinh, LoaiHang, MoTa, TonToiThieu, TrangThai, NgayTao, IsDeleted) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                mat_hang.ten_hang,
                mat_hang.don_vi,
                mat_hang.loai,
                mat_hang.mo_ta,
                mat_hang.ton_toi_thieu,
                mat_hang.trang_thai,
                mat_hang.ngay_tao if mat_hang.ngay_tao else datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                mat_hang.is_deleted,
            ),
        )
        conn.commit()
        conn.close()

    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT MaHang, TenHang, DonViTinh, LoaiHang, MoTa, TonToiThieu, TrangThai, NgayTao, IsDeleted
            FROM MatHang 
            WHERE IsDeleted = 0
            """
        )
        rows = cursor.fetchall()
        conn.close()
        return [
            MatHang(
                ma_hang=row[0],
                ten_hang=row[1],
                don_vi=row[2],
                loai=row[3],
                mo_ta=row[4],
                ton_toi_thieu=row[5],
                trang_thai=row[6],
                ngay_tao=row[7],
                is_deleted=row[8],
            )
            for row in rows
        ]

    def get_by_id(self, ma_hang: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT MaHang, TenHang, DonViTinh, LoaiHang, MoTa, TonToiThieu, TrangThai, NgayTao, IsDeleted
            FROM MatHang 
            WHERE MaHang = ? AND IsDeleted = 0
            """,
            (ma_hang,),
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return MatHang(
                ma_hang=row[0],
                ten_hang=row[1],
                don_vi=row[2],
                loai=row[3],
                mo_ta=row[4],
                ton_toi_thieu=row[5],
                trang_thai=row[6],
                ngay_tao=row[7],
                is_deleted=row[8],
            )
        return None

    def update(self, mat_hang: MatHang):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE MatHang 
            SET TenHang=?, DonVi=?, Loai=?, MoTa=?, TonToiThieu=?, TrangThai=? 
            WHERE MaHang=? AND IsDeleted=0
            """,
            (
                mat_hang.ten_hang,
                mat_hang.don_vi,
                mat_hang.loai,
                mat_hang.mo_ta,
                mat_hang.ton_toi_thieu,
                mat_hang.trang_thai,
                mat_hang.ma_hang,
            ),
        )
        conn.commit()
        conn.close()

    def soft_delete(self, ma_hang: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE MatHang SET IsDeleted = 1 WHERE MaHang = ?",
            (ma_hang,),
        )
        conn.commit()
        conn.close()