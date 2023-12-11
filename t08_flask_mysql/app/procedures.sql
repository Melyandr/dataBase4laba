
-- second task(a)

DELIMITER // 
create  procedure insert_with_params_route(in start_country_params varchar(30),
in last_country_params varchar(30),
in marshrut_id_params int,

in max_price_param int)
begin 
insert into route(start_country,last_country,marshrut_id,price)
values(start_country_params,last_country_params,marshrut_id_params,max_price_param);
end //
DELIMITER ;



-- call insert_with_params_route("Ukraine", "France", 2,200,400);


 -- second b  

DELIMITER //
create procedure insert_in_pilot_has_flight(in pilot_id int, in flight_id int)
begin
declare pilot_calling varchar(30);
declare flight_start_time varchar(30);
select calling into pilot_calling from pilot where id = pilot_id;
select start_time into flight_start_time from flight where id = flight_id;
if (pilot_calling is not null and flight_start_time is not null)then
insert into pilot_has_flight (pilot_id, flight_id, pilot_calling, flight_start_time)
values (pilot_id, flight_id, pilot_calling, flight_start_time);
end if;
end //
DELIMITER ;

-- call insert_in_pilot_has_flight(4, 2);








-- second c
DELIMITER //
create  procedure ten_inserts_in_pilot()
begin
declare counter int default 1;
while counter <11 do
insert into pilot(calling, age, experience)
value(concat('him calling is ', counter), 18,1);
set counter= counter+1;
end while;
end//
DELIMITER ;

-- call ten_inserts_in_pilot();


-- second d

DELIMITER //
create procedure finding_max_price_in_route()
begin 
declare max_price_routes int;

  set max_price_routes = max_price_route();
   select max_price_routes;
end //
DELIMITER ;


DELIMITER //
create function max_price_route() returns int DETERMINISTIC
begin
declare max_price_r int;
select Max(price)into max_price_r from route;
return max_price_r;
end//
DELIMITER ;

call finding_max_price_in_route();


-- second e 

DELIMITER //
create procedure create_database()
begin
declare done int default false;
declare NameT char(30);
declare i int;
declare st_cursor cursor for select name from aviacompany;
declare continue handler for not found set done = true;

open st_cursor;

myLoop: LOOP
fetch st_cursor into nameT;
if done = true then leave myLoop;
END IF;

set @temp_query = concat('CREATE DATABASE `', nameT, '`');
prepare myquery from @temp_query;
execute myquery;
deallocate prepare myquery;

set i = 1;
while i <= FLOOR(1 + RAND() * 9) do
set @temp_query = CONCAT('CREATE TABLE `', nameT, '`.`', nameT, i, '` (id INT)');
prepare myquery from   @temp_query;
execute myquery;
deallocate prepare myquery;
set i = i + 1;
end while;
end LOOP;
close st_cursor;
end  //
DELIMITER ;

-- call create_database();