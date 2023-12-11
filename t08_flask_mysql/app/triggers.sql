-- first task
DELIMITER //
create trigger insert_flight_services before insert on flight_services
for each row  begin
if  not exists(select * from flight where id = new.flight_id) then
signal sqlstate '45000'
set message_text='there is none flight with such id';
end if;
end //
DELIMITER ;


-- trigger e with not

DELIMITER //
create trigger not_equal_letters  before insert on route
for each row 
begin 
declare first_letter_start_country varchar(1);
declare first_letter_last_country varchar(1);
set first_letter_start_country =  left(new.start_country ,1); 
set first_letter_last_country = left(new.last_country,1);
if first_letter_start_country=first_letter_last_country then
signal sqlstate "45000"
set message_text = "two first letters are equal";
end if;


end //
DELIMITER ;

-- INSERT INTO route (start_country, last_country, marshrut_id, average_ticket_price, max_price) VALUES
-- ('Україна', 'Уполучені Штати', 1, 500, 800);



DELIMITER //
create trigger forbid_on_changing before update on  pilot
for each row begin 
if old.age > new.age and old.experience> new.experience then
signal sqlstate "45000"
set message_text = "Age and experience must be bigger tnan were";
end if;
end //
DELIMITER ;


-- UPDATE pilot
-- SET age =30, experience=10
-- WHERE id=4; 


-- forbid delete trigger

DELIMITER //
create trigger forbid_to_delete before delete on registration
for each row 
signal sqlstate '45000'
set message_text = 'You cant delete in registration table'
//
DELIMITER ; 

-- delete from registration where id =10;
