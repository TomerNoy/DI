-- select * from language;
-- select title, description, language.name from film inner join language on film.language_id = language.language_id;
-- select title, description, language.name from film left join language on film.language_id = language.language_id;
-- select title, description, language.name from film right join language on film.language_id = language.language_id;
--  select title, description, language.name from film full join language on film.language_id = language.language_id;
--  create table new_film (
--  	id serial primary key,
--  	name varchar(50)
--  )

--   insert into new_film(name) values('godfather'), ('dune'), ('eternals'), ('seven samurai'), ('city lights');

-- create table customer_review(
--  	review_id serial primary key not null,
--  	film_id int references new_film(id) not null,
--  	language_id int references language(language_id) not null,
--  	title varchar(50) not null,
--  	score smallint,
--  	review_text text,
--  	last_update date
-- );

-- insert into customer_review(film_id,language_id,title,score,review_text,last_update) 
--    values (3,1,'review by admin',8,'this film is awesome bro','2021-01-01'),
--    		(4,1,'review by admin 2',8,'this film is cool bro','2021-01-01');

-- delete from new_film where id = 3

-- output err = ERROR:  update or delete on table "new_film" violates foreign key constraint "customer_review_film_id_fkey" on table "customer_review"


----------------------------------------------------------------------------------------------------------------------------

-- update film set language_id = 3 where title = 'Academy Dinosaur';
-- customer table has references for store id and adress id of which both are required (not null)
-- drop table customer_review; -- we could delete also the references
-- select count(*) from rental where return_date is null;
-- select amount, title
-- 	from rental 
-- 		inner join payment ON rental.rental_id = payment.rental_id
-- 		inner join inventory ON rental.inventory_id = inventory.inventory_id
-- 		inner join film ON inventory.film_id = film.film_id
-- where return_date is null order by amount desc limit 30;

-- select film.title, film.description
-- 	from film
-- 		join film_actor on film_actor.film_id = film.film_id
-- 		join actor on actor.actor_id = film_actor.actor_id
-- where film.description like '%Sumo Wrestler%' and actor.first_name like 'Penelope' and actor.last_name like 'Monroe';
