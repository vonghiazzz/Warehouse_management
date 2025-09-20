-- Tạo bảng Mặt Hàng
CREATE TABLE IF NOT EXISTS MatHang (
    MaHang INTEGER PRIMARY KEY AUTOINCREMENT,
    TenHang TEXT UNIQUE NOT NULL,
    DonVi TEXT,
    Loai TEXT,
    MoTa TEXT,
    TonToiThieu INTEGER DEFAULT 0,
    TrangThai TEXT,
    NgayTao TEXT DEFAULT (datetime('now')), 
    IsDeleted INTEGER DEFAULT 0
);

-- Insert mặt hàng
INSERT INTO MatHang (TenHang, DonVi, Loai, MoTa, TonToiThieu, TrangThai) VALUES (?, ?, ?, ?, ?, ?);

-- Lấy toàn bộ mặt hàng
SELECT * FROM MatHang;

-- Tìm mặt hàng theo tên
SELECT * FROM MatHang WHERE TenHang = ?;
