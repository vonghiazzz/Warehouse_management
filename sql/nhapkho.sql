-- Tạo bảng Nhập Kho
CREATE TABLE IF NOT EXISTS NhapKho (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MaHang INTEGER,
    SoLuong INTEGER,
    GiaNhap REAL,
    FOREIGN KEY (MaHang) REFERENCES MatHang(MaHang)
);

ALTER TABLE NhapKho ADD COLUMN NhaCungCap TEXT;      
ALTER TABLE NhapKho ADD COLUMN NhanVienNhap TEXT;    
ALTER TABLE NhapKho ADD COLUMN HanSuDung TEXT;       
ALTER TABLE NhapKho ADD COLUMN SoHoaDon TEXT;        
ALTER TABLE NhapKho ADD COLUMN GhiChu TEXT;          
ALTER TABLE NhapKho ADD COLUMN NgayTao TEXT DEFAULT (datetime('now'));  
ALTER TABLE NhapKho ADD COLUMN IsDeleted INTEGER DEFAULT 0;  


-- Insert nhập kho
INSERT INTO NhapKho (ID,MaHang, SoLuong, GiaNhap, NhaCungCap, NhanVienNhap, HanSuDung, SoHoaDon, GhiChu)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);

-- Lấy danh sách nhập kho theo mã hàng
SELECT * FROM NhapKho WHERE ID = ?;

-- Tìm theo giá nhập
SELECT * FROM NhapKho WHERE GiaNhap = ?;
