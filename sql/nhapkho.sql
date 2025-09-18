-- Tạo bảng Nhập Kho
CREATE TABLE IF NOT EXISTS NhapKho (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MaHang INTEGER,
    NgayNhap TEXT,
    SoLuong INTEGER,
    GiaNhap REAL,
    FOREIGN KEY (MaHang) REFERENCES MatHang(MaHang)
);

-- Insert nhập kho
INSERT INTO NhapKho (MaHang, NgayNhap, SoLuong, GiaNhap)
VALUES (?, ?, ?, ?);

-- Lấy danh sách nhập kho theo mã hàng
SELECT * FROM NhapKho WHERE MaHang = ?;

-- Tìm theo giá nhập
SELECT * FROM NhapKho WHERE GiaNhap = ?;
