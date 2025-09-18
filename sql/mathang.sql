-- Tạo bảng Mặt Hàng
CREATE TABLE IF NOT EXISTS MatHang (
    MaHang INTEGER PRIMARY KEY AUTOINCREMENT,
    TenHang TEXT UNIQUE NOT NULL
);

-- Insert mặt hàng
INSERT INTO MatHang (TenHang) VALUES (?);

-- Lấy toàn bộ mặt hàng
SELECT * FROM MatHang;

-- Tìm mặt hàng theo tên
SELECT * FROM MatHang WHERE TenHang = ?;
