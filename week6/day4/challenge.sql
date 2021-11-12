--  create table items(
--  	item_id serial primary key,
--  	price decimal default 0,
--  	title varchar(50) not null
--  );

--  create table orders(
--  	orders_id serial primary key,
-- 	order_number bigint not null,
--  	item_id bigint references items (item_id),
--  	unique(item_id)
--  );

--  insert into items(price, title) 
--  	values (300, 'mouse'), (300, 'hdmi cable'),(250, 'keyboard');

-- insert into orders(order_number, item_id) 
-- 	values (1, 1), (1, 2),(2, 3);
-- DROP FUNCTION total_price(bigint);

-- CREATE or REPLACE FUNCTION total_price(x bigint) 
-- RETURNS decimal AS $total$
-- BEGIN
-- RETURN(
-- 	select sum(items.price) 
-- 	  from orders
-- 		  join items on items.item_id = orders.item_id 
-- 			where orders.order_number = x
-- );
-- END;
-- $total$ LANGUAGE plpgsql;

-- SELECT * FROM total_price(1);

-- bonus --------------------

-- create table users(
-- 	user_id serial primary key,
-- 	name varchar(50) not null
-- );

-- ALTER TABLE orders
--  	add column user_id bigint,
--  	add constraint user_id
--  	foreign key (user_id) 
--  	references users (user_id);

-- insert into users(name) values ('jack'),('jane'), ('tom');
-- insert into orders(order_number, item_id, user_id) 
-- 	values (3, 2, 1)

-- CREATE or REPLACE FUNCTION total_price_user(odr bigint, usr bigint)
-- RETURNS decimal AS $total$
-- BEGIN
-- RETURN(
-- 	select sum(items.price) 
-- 	  from orders
-- 		  join items on items.item_id = orders.item_id 
-- 			where orders.order_number = odr and orders.user_id = usr
-- );
-- END;
-- $total$ LANGUAGE plpgsql;

-- SELECT * FROM total_price_user(3, 1);