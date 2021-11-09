-- create table customer (
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR (50) NOT NULL,
-- 	last_name VARCHAR (100) NOT NULL
-- );

-- create table customer_profile (
-- 	customer_profile_id SERIAL PRIMARY KEY,
-- 	balance bigint default 0,
-- 	foreign key(customer_profile_id) REFERENCES customer(customer_id)
-- );

-- insert into customer(first_name,last_name)
-- 	values ('dave', 'jhonson'),('dan', 'smith'),('dana', 'madar');

-- insert into customer_profile(balance)
-- 	values (100),(3000),(-550);

-- select * from customer_profile join customer on customer_profile.customer_profile_id = customer.customer_id;
-- select * from customer_profile left join customer on customer_profile.customer_profile_id = customer.customer_id;
-- select * from customer_profile right join customer on customer_profile.customer_profile_id = customer.customer_id;
-- select * from customer_profile full join customer on customer_profile.customer_profile_id = customer.customer_id;

-- create table product(
-- 	product_id serial primary key,
-- 	price bigint not null,
-- 	title varchar(50)
-- );

-- create table product_order (
-- 	product_order_id serial primary key,
-- 	customer_id bigint not null,
-- 	foreign key(product_order_id) REFERENCES customer(customer_id),
-- 	product_id bigint not null,
-- 	foreign key(product_order_id) REFERENCES product(product_id)
-- );

-- insert into product (price, title) values (3000, 'table'), (1500, 'bag'), (200, 'shirt');

-- insert into product_order(customer_id, product_id) values (1,1), (1,2), (3,2)

-- select title, first_name ||' '|| last_name as full_name, price
-- 	from product_order
-- 	join product on product_order.product_id = product.product_id 
--  join customer on product_order.customer_id = customer.customer_id 