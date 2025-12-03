CREATE DATABASE IF NOT EXISTS quanly_xe;
USE quanly_xe;

-- Xóa từng bảng nếu tồn tại, theo thứ tự tránh FK
DROP TABLE IF EXISTS phancong;
DROP TABLE IF EXISTS xe;
DROP TABLE IF EXISTS laixe;
DROP TABLE IF EXISTS chucvu;
DROP TABLE IF EXISTS phongban;

-- BẢNG PHÒNG BAN
CREATE TABLE IF NOT EXISTS phongban (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_phongban VARCHAR(100) NOT NULL,
    mota VARCHAR(255) DEFAULT ''
);
-- coi dư liệu bảng
SELECT * FROM phongban;

-- Thêm xe mẫu
INSERT INTO xe (id, bien_so, ten_xe) VALUES (1, '51A-12345', 'Xe A');
INSERT INTO xe (id, bien_so, ten_xe) VALUES (2, '51B-54321', 'Xe B');

-- Thêm lái xe mẫu
INSERT INTO laixe (id, ho_ten) VALUES (1, 'Nguyen Van A');
INSERT INTO laixe (id, ho_ten) VALUES (2, 'Tran Thi B');

DESCRIBE xe;

CREATE TABLE chucvu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    phongban_id INT NOT NULL,
    ten_cv VARCHAR(100) NOT NULL,
    mota_cv VARCHAR(255),
    FOREIGN KEY (phongban_id) REFERENCES phongban(id) ON DELETE CASCADE
);
DROP TABLE chucvu;
SHOW TABLES LIKE 'chucvu';
SELECT * FROM chucvu;
DELETE FROM chucvu WHERE id=7;

DESCRIBE chucvu;
SELECT * FROM laixe;

ALTER TABLE chucvu
INSERT INTO laixe (id, ten, cmnd, sdt)
VALUES (1, 'Tài xế A', '123456789', '0909000000');

DESCRIBE laixe;

CREATE TABLE IF NOT EXISTS chuyendi (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_xe INT NOT NULL,
    id_laixe INT NOT NULL,
    ngay_di DATE NOT NULL,
    noi_di VARCHAR(255),
    noi_den VARCHAR(255),
    tinh_trang VARCHAR(50) DEFAULT 'Hoàn thành',
    FOREIGN KEY (id_xe) REFERENCES xe(id) ON DELETE CASCADE,
    FOREIGN KEY (id_laixe) REFERENCES laixe(id) ON DELETE CASCADE
);
SET SQL_SAFE_UPDATES = 0;
INSERT INTO laixe (ho_ten, gioi_tinh, ngay_sinh, id_phongban, id_chucvu, sdt, bang_lai)
VALUES ('Tài xế A', 'Nam', '1990-01-01', 1, 1, '0909000000', 'B2');
SELECT * FROM laixe;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE laixe;
SET FOREIGN_KEY_CHECKS = 1;
CREATE TABLE laixe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(100),
    gioi_tinh VARCHAR(10),
    ngay_sinh DATE,
    id_phongban INT,
    id_chucvu INT,
    sdt VARCHAR(15),
    bang_lai VARCHAR(10)
);
INSERT INTO laixe (ho_ten, gioi_tinh, ngay_sinh, id_phongban, id_chucvu, sdt, bang_lai)
VALUES ('Tài xế A', 'Nam', '1990-01-01', 1, 1, '0909000000', 'B2');

SELECT * FROM laixe;
INSERT INTO laixe (ho_ten, gioi_tinh, ngay_sinh, id_phongban, id_chucvu, sdt, bang_lai)
VALUES ('Tài xế B', 'Nam', '1992-05-10', 1, 1, '0909000001', 'B2');


DELETE FROM chucvu WHERE ten_chucvu IN ('Nhân viên','Tài xế','Quản lý');
DELETE FROM phongban WHERE ten_phongban IN ('Hành chính','Kế toán','Nhân sự');


-- BẢNG CHỨC VỤ
CREATE TABLE IF NOT EXISTS chucvu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ten_chucvu VARCHAR(100) NOT NULL,
    mota VARCHAR(255) DEFAULT ''
);

CREATE TABLE laixe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(100),
    gioi_tinh VARCHAR(10),
    ngay_sinh DATE,
    id_phongban INT,
    id_chucvu INT,
    sdt VARCHAR(15),
    bang_lai VARCHAR(10)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dữ liệu mặc định
INSERT IGNORE INTO chucvu (ten_chucvu) VALUES 
('Nhân viên'), ('Tài xế'), ('Quản lý');

-- BẢNG XE
CREATE TABLE IF NOT EXISTS xe (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Khóa chính
    bien_so VARCHAR(20) NOT NULL,             -- Biển số xe
    loai_xe VARCHAR(50),                       -- Loại xe
    suc_chua INT,                              -- Sức chứa (nếu cần)
    nam_sx YEAR,                               -- Năm sản xuất
    tinh_trang VARCHAR(50) DEFAULT 'Tốt'      -- Tình trạng xe
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS xe;

-- BẢNG PHÂN CÔNG
CREATE TABLE IF NOT EXISTS phancong (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_nhanvien INT,
    id_xe INT,
    ngay DATE,
    FOREIGN KEY (id_nhanvien) REFERENCES laixe(id),
    FOREIGN KEY (id_xe) REFERENCES xe(id)
);
