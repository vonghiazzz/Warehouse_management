from database import get_connection
from repositories.interfaces.i_mathang_repo import IMatHangRepo
from entities.mathang import MatHang

class MatHangRepoSQLite(IMatHangRepo):
    def add(self, item: MatHang) -> MatHang:
        item.validate()
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO MatHang (TenHang) VALUES (?)", item.to_row_insert())
        item.mahang = cur.lastrowid
        conn.commit()
        conn.close()
        return item

    def get_all(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT MaHang, TenHang FROM MatHang")
        rows = cur.fetchall()
        conn.close()
        return [MatHang.from_row(r) for r in rows]

    def get_by_name(self, tenhang: str):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT MaHang, TenHang FROM MatHang WHERE TenHang=?", (tenhang,))
        row = cur.fetchone()
        conn.close()
        return MatHang.from_row(row) if row else None

class MatHangRepository:
    @staticmethod
    def add(MatHang: MatHang):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MatHang (TenHang) VALUES (?)", (MatHang.ten_hang,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MaHang, TenHang FROM MatHang")
        rows = cursor.fetchall()
        conn.close()
        return [MatHang(ma_hang=row[0], ten_hang=row[1]) for row in rows]