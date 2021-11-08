-- select * from items order by price ;
-- select * from items where price >= 80 order by price desc;
-- select fname, lname from customers order by fname limit 3;
-- select lname from customers order by lname desc;

-- # exercise 1

-- # the instructions didn't mention foreign keys so i did without it
-- create table purchases(
-- 	customer_id integer REFERENCES customers,
-- 	item_id integer REFERENCES items
-- )

-- # i didnt set not null so this works
-- insert into purchases(customer_id)
-- values(1)

-- insert into purchases(customer_id, item_id)
-- values(1,2),(2, 3),(2, 1),(1, 2),(3, 3)

-- # we could use the id somehow to get the values
-- select * from purchases

-- select * from purchases inner join customers on purchases.customer_id = customers.customer_id
-- select * from purchases inner join customers on purchases.customer_id = customers.customer_id where purchases.customer_id = 4;

-- select * from purchases 
-- 	inner join items on purchases.item_id = items.item_id 
--   		where items.item_name in('Lage desk', 'Small desk')

-- insert into items(item_name, price)
-- values('hard_drive', 250);
-- insert into purchases(customer_id, item_id)
-- values(3, 4);

-- select fname, lname, item_name
-- 	from customers 
-- 		inner join purchases on (purchases.customer_id = customers.customer_id)
-- 		inner join items on (items.item_id = items.item_id);
		
-- # works for me
--  select fname, lname, item_name
--  	from customers 
--  		inner join purchases on (purchases.customer_id = customers.customer_id)
--  		inner join items on (items.item_id = purchases.item_id);

-- # exercise 2

-- select * from customer
-- select first_name ||' '|| last_name from customer as full_name
-- select distinct create_date from customer
-- select * from customer order by first_name desc
-- select film_id, release_year, title, description, rental_rate from film order by rental_rate asc;
-- select first_name, last_name, district 
-- 	from customer inner join address on customer.address_id = address.address_id 
-- 		where district = 'Texas';
-- select * from film where film_id in(15, 150);
-- select film_id, title, description, length, rating from film where title = 'Alien Center';
-- select film_id, title, description, length, rating from film where title ilike '%Al%';
-- select * from film order by rental_rate limit 10;
-- select * from film order by rental_rate offset 10 fetch first 10 row only;

-- select customer.customer_id, amount, payment_date
-- 	from customer inner join payment on customer.customer_id = payment.customer_id 
-- 		order by customer.customer_id

-- select customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date 
-- 	from customer inner join payment on payment.customer_id = customer.customer_id 
-- 			order by customer.customer_id asc;