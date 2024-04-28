Create database mall;
use mall;

create table store_dimension(
store_id int primary key,
store_name varchar(50),
location varchar(200),
manager_name varchar(30),
opening_date date
);

create table product_dimension (
product_id int primary key,
product_name varchar(30),
category varchar(30),
brand varchar(100),
quantity int,
price decimal(5,2));

drop table product_dimension;

create table date_dimension (
date_id int primary key,
date_actual date,
day_of_week int,
day_name varchar(20),
month_actual int,
month_name varchar(20));

insert into product_dimension values 
(101,'Smartphone','electronics','samsung',500.00,0.3),
(102,'Laptop','electronics','Dell',1000.00,2.3),
(103,'T-shirt','Clothing','Nike',20.00,0.2),
(104,'Jeans','Clothing','Levis',50.00,0.8),
(105,'Shoes','Footwear','Adidas',70.00,0.5);

insert into store_dimension (store_id,store_name,location,manager_name,opening_date)values
(1,'X-mart mall A','new delhi','rajesh sharma','2022-02-02'),
(2,'X-mart mall b','Mumbai','priya sharma','2022-02-15'),
(3,'X-mart mall c','Banglore','amit sharma','2022-03-20');

insert into date_dimension(date_id,date_actual,day_of_week,day_name,month_actual,month_name)
values(1,'2022-01-01',6,'saturday',1,'January'),
(2,'2022-01-02',7,'saturday',1,'January'),
(3,'2022-01-03',1,'monday',1,'January'),
(4,'2022-01-04',2,'tuesday',1,'January'),
(5,'2022-01-05',3,'wednesday',1,'January');

create table sales_fact (
trans_id int primary key,
store_id int,
product_id int,
date_id int,
quantity int,
amount decimal(10,2),
foreign key (store_id) references store_dimension(store_id),
foreign key (product_id) references store_dimension(product_id),
foreign key (date_id) references store_dimension(date_id));

insert into sales_fact (transaction_id,store_id,product_id,data_id,quantity,amount)values
(1,1,101,1,10,50000.00),
(2,1,102,1,5,50000.00),
(3,1,103,1,20,400.00),
(4,1,104,1,15,750.00),
(5,1,105,1,12,840.00);
