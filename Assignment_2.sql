use students;
-- Que 1] a}
create table test_table(RecordNumber INT(3),CurrentDate Date);
desc test_table;
insert into test_table values('1',curdate());
select * from test_table;

DELIMITER //
CREATE PROCEDURE InsertRecords()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 50 DO
        INSERT INTO test_table (RecordNumber, CurrentDate) VALUES (i, CURDATE()); -- CURDATE() returns the current dat
        SET i = i + 1;
    END WHILE;
END //
DELIMITER ;

call InsertRecords();


-- QUe 1] b}
drop table products;
Create table products(ProductID INT(4) NOT NULL,category varchar(10),detail varchar(30),price decimal(10,2),stock INT(5));
insert into products values(114,'Laptop','HP RYZEN 5 Octacore',46500.25,200);
insert into products values(142,'Phone','Samsung galaxy F62',25000.0,200);
insert into products values(124,'Laptop','HP Intel I5 Octacore',50000.25,200);
insert into products values(134,'Phone','Oppo v6',18000.25,200);
insert into products values(154,'Laptop','Dell inspiron Octacore',80000.25,200);
select * from products;

-- Create a stored procedure
DELIMITER //
CREATE PROCEDURE IncreasePriceByCategory(IN X DECIMAL(5,2), IN Y VARCHAR(10))
BEGIN
    -- Update the price for products in the specified category
    UPDATE products SET Price = Price * (1 + X / 100) WHERE Category = Y;
END //
DELIMITER ;
-- Drop the stored procedure
DROP PROCEDURE IF EXISTS IncreasePriceByCategory;

call IncreasePriceByCategory(5.4,'Laptop');
select * from products;





-- Que2] 
commit;


