CREATE DATABASE smart_parking_db;

use smart_parking_db;

CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'MySQL@Secure123!';
GRANT ALL PRIVILEGES ON smart_parking_db.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON *.* TO 'django_user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

DROP TABLE contact_contact;
DROP TABLE contact_customerenquiry;

SHOW TABLES;

USE smart_parking_db;
DELETE FROM django_migrations WHERE app = 'contact';

SET SQL_SAFE_UPDATES = 0;
DELETE FROM django_migrations WHERE app = 'contact';
SET SQL_SAFE_UPDATES = 1;

SET GLOBAL time_zone = '+05:30';
SET SESSION time_zone = '+05:30';

SELECT @@global.time_zone, @@session.time_zone;

INSERT INTO parking_slot (city, location, slot_number, status)
VALUES
('Mumbai', 'Andheri', 'P1', 'Available'),
('Mumbai', 'Bandra', 'P2', 'Occupied'),
('Delhi', 'Connaught Place', 'D1', 'Available'),
('Delhi', 'Karol Bagh', 'D2', 'Occupied'),
('Bangalore', 'MG Road', 'B1', 'Available'),
('Pune', 'Shivaji Nagar', 'P3', 'Occupied');

INSERT INTO traffic_status (city, location, congestion_level)
VALUES
('Mumbai', 'Andheri', 6),
('Delhi', 'Connaught Place', 3),
('Bangalore', 'MG Road', 8),
('Pune', 'Shivaji Nagar', 5);

SELECT * FROM smart_parking_db.traffic_status WHERE city = 'Mumbai' AND location = 'Andheri';
describe users;
ALTER TABLE users 
DROP COLUMN is_staff,
DROP COLUMN date_joined,
DROP COLUMN profile_picture;

ALTER TABLE users 
DROP COLUMN is_active,
DROP COLUMN is_superuser,
DROP COLUMN first_name,
DROP COLUMN last_name,
DROP COLUMN address;

ALTER TABLE users ADD COLUMN is_staff TINYINT NOT NULL DEFAULT 0;
ALTER TABLE users ADD COLUMN is_active TINYINT NOT NULL DEFAULT 1;
ALTER TABLE users ADD COLUMN is_superuser TINYINT NOT NULL DEFAULT 0;

ALTER TABLE users 
DROP COLUMN is_active,
DROP COLUMN is_superuser,
DROP COLUMN is_staff;

ALTER TABLE users ADD COLUMN first_name VARCHAR(150) NOT NULL;
ALTER TABLE users ADD COLUMN last_name VARCHAR(150) NOT NULL;
ALTER TABLE users ADD COLUMN email VARCHAR(254) NOT NULL;
ALTER TABLE users ADD COLUMN date_joined DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP;

ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users DROP COLUMN is_customer;
ALTER TABLE users DROP COLUMN is_admin;
ALTER TABLE users DROP COLUMN is_staff;
ALTER TABLE users DROP COLUMN is_active;
ALTER TABLE users DROP COLUMN is_superuser;
ALTER TABLE users DROP COLUMN first_name;
ALTER TABLE users DROP COLUMN last_name;

UPDATE parking_slot
SET status = CASE 
    WHEN status = 'Available' THEN 0
    ELSE status 
END
WHERE id IS NOT NULL;  -- Ensure it applies to all rows safely

UPDATE parking_slot
SET status = CASE 
    WHEN status = 'Available' THEN 0
    ELSE status 
END;

SET SQL_SAFE_UPDATES = 0;
SELECT * FROM parking_slot;
UPDATE parking_slot
SET status = CASE 
    WHEN status = 'Available' THEN 0
    WHEN status = 'Occupied' THEN 1
    ELSE status 
END
WHERE id IS NOT NULL;

UPDATE parking_slot 
SET status = 
    CASE 
        WHEN status = 'Available' THEN 0 
        WHEN status = 'Occupied' THEN 1 
        ELSE NULL 
    END;

UPDATE parking_slot 
SET status = 
    CASE 
        WHEN status = 'Available' THEN 0 
        WHEN status = 'Occupied' THEN 1 
        ELSE 2-- Set 'Unknown' as 2 instead of NULL
    END;
    
ALTER TABLE parking_slot MODIFY COLUMN status INT NULL;

UPDATE parking_slot 
SET status = 
    CASE 
        WHEN status = 'Available' THEN 0 
        WHEN status = 'Occupied' THEN 1 
        ELSE 2 -- Set 'Unknown' as 2
    END;

ALTER TABLE parking_slot 
MODIFY COLUMN status INT NOT NULL;
ALTER TABLE parking_slot 
MODIFY COLUMN status VARCHAR(20);

UPDATE parking_slot 
SET status = 
    CASE 
        WHEN status = 'Available' THEN '0' 
        WHEN status = 'Occupied' THEN '1' 
        ELSE '2'  -- Assign 'Unknown' as 2
    END;

ALTER TABLE parking_slot 
MODIFY COLUMN status INT NOT NULL;
SELECT * FROM parking_slot WHERE status NOT IN (0, 1);
UPDATE parking_slot SET status = 0 WHERE status IS NULL;
UPDATE parking_slot
SET status = 1
WHERE status = 'Occupied';

UPDATE parking_slot
SET status = 0
WHERE status = 'Available';

SELECT * FROM parking_slot INTO OUTFILE '/tmp/parking_slot_backup.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n';

UPDATE parking_slot SET status = 0 WHERE status = 'Available';
UPDATE parking_slot SET status = 1 WHERE status = 'Occupied';
ALTER TABLE parking_slot MODIFY COLUMN status INT;
UPDATE parking_slot SET status = 0 WHERE status = 'Available';
UPDATE parking_slot SET status = 1 WHERE status = 'Occupied';
SELECT * FROM parking_slot;

UPDATE parking_reservation SET slot_id = 1 WHERE slot_id IS NULL;
DESC parking_reservation;
SHOW CREATE TABLE parking_reservation;
DROP TABLE IF EXISTS parking_slot;