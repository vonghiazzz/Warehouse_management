-- Tạo bảng Mặt Hàng
CREATE TABLE IF NOT EXISTS MatHang (
    MaHang INTEGER PRIMARY KEY AUTOINCREMENT,
    TenHang TEXT UNIQUE NOT NULL
);

ALTER TABLE MatHang ADD COLUMN DonViTinh TEXT;       -- Ví dụ: cái, hộp, kg
ALTER TABLE MatHang ADD COLUMN LoaiHang TEXT;        -- Nhóm hàng (điện tử, thực phẩm, v.v.)
ALTER TABLE MatHang ADD COLUMN MoTa TEXT;            -- Mô tả chi tiết sản phẩm
ALTER TABLE MatHang ADD COLUMN TonToiThieu INTEGER;  -- Số lượng tồn tối thiểu để cảnh báo
ALTER TABLE MatHang ADD COLUMN NgayTao TEXT;         -- Ngày tạo mặt hàng
ALTER TABLE MatHang ADD COLUMN TrangThai TEXT;       -- Hoạt động / Ngưng kinh doanh


-- Insert mặt hàng
INSERT INTO MatHang (TenHang) VALUES (?);

-- Lấy toàn bộ mặt hàng
SELECT * FROM MatHang;

-- Tìm mặt hàng theo tên
SELECT * FROM MatHang WHERE TenHang = ?;
