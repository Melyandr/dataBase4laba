CREATE DATABASE IF NOT EXISTS flight_radar_lab5;
USE flight_radar_lab5;



drop table if exists pilot_has_flight, air_hostess_has_flight, dispatcher_has_flight, flight, airplane, registration, aviacompany, route, marshrut, aeroport, pilot, dispatcher, air_hostess, flight_services;



CREATE TABLE aeroport (
id int not null auto_increment PRIMARY KEY,
country varchar(50) not null,
city varchar(50) not null,
name varchar(50) not null,
num_run_lines int not null,
run_line_metres int not null
) ENGINE = INNODB;

create index situated_aeroport
on aeroport(country, city);

create index data_run_lines
on aeroport (num_run_lines,run_line_metres);


Create table marshrut(
id int not null auto_increment PRIMARY KEY,
country varchar(50) not null,
city varchar(50) not null,
aeroport_id1 int not null,
aeroport_id2 int not null,
distance_km int not null,
marshrut_status varchar(20) not null
)engine= innodb;

create index situated_marshrut
on marshrut(country,city);

create index extra_info_marshrut
on marshrut(distance_km,marshrut_status);

ALTER TABLE marshrut
ADD CONSTRAINT FK_marshrut_aeroport1
FOREIGN KEY (aeroport_id1)
REFERENCES aeroport (id);


ALTER TABLE marshrut
ADD CONSTRAINT FK_marshrut_aeroport2
FOREIGN KEY (aeroport_id2)
REFERENCES aeroport (id);

create table route(
id int not null auto_increment PRIMARY KEY,
start_country varchar(50) not null,
last_country varchar(50) not null,
marshrut_id int not null,
average_ticket_price int not null,
max_price int not null 
)engine innodb;

Alter table  route
add constraint FK_route_marshrut
foreign key(marshrut_id)
references marshrut(id);

create index route_countries
on route (start_country, last_country);

create index route_prices
on route(average_ticket_price,max_price);




create table aviacompany(
id int not null auto_increment PRIMARY KEY,
name varchar(50) not null,
country_of_company varchar(50) not null,
city_of_company varchar(50) not null,
website varchar(100) null,
phone_number varchar(20) null
)engine=innodb;

create index situated_aviacompany
on aviacompany(country_of_company,city_of_company);

create index contact_info_aviacompany
on aviacompany(website,phone_number);


create table registration(
id int not null auto_increment PRIMARY KEY,
owner varchar(50) not null,
country_of_registration varchar(50) not null,
city_of_registration varchar(50) not null,
registration_date date not null,
expiration_date date not null
)engine=innodb;


create index record_dates_registration
on registration(registration_date,expiration_date);

create index place_registration 
on registration(city_of_registration,country_of_registration);


create table airplane(
id int not null auto_increment PRIMARY KEY,
lift_weight int not null,
number_of_passenger int not null,
plain_mileage varchar(50) not null,
average_speed varchar(50) not null,
aviacompany_id int not null,
registration_id int not null,
plane_model varchar(50) not null,
plane_maker varchar(50) not null
)engine=innodb;


create index about_model_airplane
on airplane(plane_model,plane_maker);

create index features_airplane
on airplane(lift_weight,number_of_passenger,plain_mileage,average_speed);


alter table airplane
add constraint FK_airplane_aviacompany1
foreign key (aviacompany_id)
references aviacompany (id);

alter table airplane
add constraint FK_airplane_registration1
foreign key (registration_id)
references registration (id);

create table flight(
id int not null auto_increment PRIMARY KEY,
start_time datetime not null,
end_time datetime not null,
route_id int not null,
airplane_id int not null,
departure_gate varchar(10) not null,
arrival_gate varchar(10) not null
)engine=innodb;


CREATE INDEX fligh_times
ON flight (start_time,end_time);

create index flight_gates
on flight (departure_gate,arrival_gate);


alter table flight
add constraint FK_flight_route
foreign key (route_id)
references route(id);

alter table flight
add constraint FK_flight_airplane
foreign key (airplane_id)
references airplane(id);


create table pilot(
id int not null auto_increment PRIMARY KEY,
calling varchar(50) not null,
age int not null,
experience int null,
license_number varchar(20) not null,
current_rank varchar(20) not null
)engine= innodb;

create index proffessional_data_pilot
on pilot (calling,current_rank);


create index allowing_data_pilot
on pilot (license_number,experience);



create table dispatcher(
id int not null auto_increment PRIMARY KEY,
calling varchar(50) not null,
age int not null,
aeroport_id int not null,
dispatcher_license_number varchar(20) not null,
contact_number varchar(15) null
)engine= innodb;

create index personal_data_dispatcher
on dispatcher(age,contact_number);

create index proff_data_dispatcher
on dispatcher(calling, dispatcher_license_number);

alter table dispatcher
add constraint FK_dispatcher_aeroport1
foreign key (aeroport_id)
references aeroport(id);

create table air_hostess(
id int not null auto_increment PRIMARY KEY,
gender varchar(50) not null,
age int null,
email varchar (50) null,
languages_spoken varchar(100) null,
language_nature varchar(30)
)engine=innodb; 

create index personal_data_air_hostess
on air_hostess(gender, email,age);

create index languages_air_hostess
on air_hostess(languages_spoken, language_nature);



create table pilot_has_flight(
pilot_id int not null auto_increment ,
flight_id int not null,
PRIMARY KEY (pilot_id, flight_id)
)engine=innodb;

alter table pilot_has_flight
add constraint FK_pilot_has_flight_pilot1
foreign key (pilot_id)
references pilot (id);


alter table pilot_has_flight
add constraint fk_pilot_has_flight_flight1
foreign key (flight_id)
references flight (id);

create table air_hostess_has_flight(
air_hostess_id int not null ,
flight_id int not null,
PRIMARY KEY (air_hostess_id, flight_id)
)engine=innodb;

alter table air_hostess_has_flight
add constraint fk_air_hostess_has_flight_air_hostess1
foreign key (air_hostess_id)
references air_hostess (id);

alter table air_hostess_has_flight
add constraint fk_air_hostess_has_flight_flight1
foreign key (flight_id)
references flight (id);

create table dispatcher_has_flight(
dispatcher_id int not null,
flight_id int not null,
PRIMARY KEY (dispatcher_id, flight_id)
)engine=innodb;


alter table dispatcher_has_flight
add constraint fk_dispatcher_has_flight_dispatcher1
foreign key (dispatcher_id)
references dispatcher (id);

alter table dispatcher_has_flight
add constraint fk_dispatcher_has_flight_flight1
foreign key (flight_id)
references flight (id);

CREATE TABLE flight_services (
    id int not null auto_increment PRIMARY KEY,
    flight_id int not null,
    service_description varchar(100) not null,
    service_type varchar(50) not null,
    service_cost decimal(10,2) not null
    
) ENGINE=InnoDB;

INSERT INTO aeroport (country, city, name, num_run_lines, run_line_metres) VALUES
('Україна', 'Київ', 'Бориспіль', 4, 3000),
('США', 'Лос-Анджелес', 'Ейрпорт', 5, 4000),
('Франція', 'Париж', 'Паризький', 3, 2500),
('Велика Британія', 'Лондон', 'Лондонський', 4, 3200),
('Іспанія', 'Мадрид', 'Мадридський', 3, 2700),
('Німеччина', 'Франкфурт', 'Франкфуртський', 4, 3500),
('Китай', 'Пекін', 'Пекінський', 5, 4000),
('Японія', 'Токіо', 'Токіо аеропорт', 3, 2500),
('Канада', 'Оттава', 'Оттавський  Аеропорт', 4, 3300),
('Австралія', 'Сідней', 'Сіднейський', 5, 4200);


INSERT INTO marshrut (country, city, aeroport_id1, aeroport_id2, distance_km, marshrut_status) VALUES
('Україна', 'Київ', 1, 2, 1200, 'Активний'),
('Сполучені Штати', 'Лос-Анджелес', 2, 3, 2500, 'Активний'),
('Франція', 'Париж', 3, 4, 3000, 'Активний'),
('Велика Британія', 'Лондон', 4, 5, 2000, 'Активний'),
('Іспанія', 'Мадрид', 5, 6, 2200, 'Активний'),
('Німеччина', 'Франкфурт', 6, 7, 2800, 'Активний'),
('Китай', 'Пекін', 7, 8, 3500, 'Активний'),
('Японія', 'Токіо', 8, 9, 3000, 'Активний'),
('Канада', 'Оттава', 9, 10, 2700, 'Активний'),
('Австралія', 'Сідней', 10, 1, 3200, 'Активний');


INSERT INTO route (start_country, last_country, marshrut_id, average_ticket_price, max_price) VALUES
('Україна', 'Сполучені Штати', 1, 500, 800),
('Сполучені Штати', 'Франція', 2, 700, 1000),
('Франція', 'Велика Британія', 3, 450, 750),
('Велика Британія', 'Іспанія', 4, 550, 900),
('Іспанія', 'Німеччина', 5, 600, 950),
('Німеччина', 'Китай', 6, 800, 1200),
('Китай', 'Японія', 7, 650, 1100),
('Японія', 'Канада', 8, 750, 1250),
('Канада', 'Австралія', 9, 900, 1500),
('Австралія', 'Україна', 10, 1000, 1800);

INSERT INTO aviacompany (name, country_of_company, city_of_company, website, phone_number) VALUES
('Український авіаперевізник', 'Україна', 'Київ', 'www.ukravia.com', '+380123456789'),
('Французький перевізник', 'Франція', 'Париж', 'www.frenchairlines.com', '+33123456789'),
('Американський перевізник', 'США', 'Лос-Анджелес', 'www.usaairlines.com', '+1323456789'),
('Британський перевізник', 'Велика Британія', 'Лондон', 'www.britishairlines.com', '+4423456789'),
('Іспанський перевізник', 'Іспанія', 'Мадрид', 'www.spanishairlines.com', '+3423456789'),
('Люфтганза', 'Німеччина', 'Франкфурт', 'www.lufthansa.com', '+4923456789'),
('Китайські авіалінії', 'Китай', 'Пекін', 'www.chinaairlines.com', '+8623456789'),
('Японські польоти', 'Японія', 'Токіо', 'www.japanairlines.com', '+8123456789'),
('Канадські польоти', 'Канада', 'Оттава', 'www.canadianairlines.com', '+1123456789'),
('Австралійський авіаперевізник', 'Австралія', 'Сідней', 'www.australianairlines.com', '+6123456789');

INSERT INTO registration (owner, country_of_registration, city_of_registration, registration_date, expiration_date) VALUES
('Українська компанія', 'Україна', 'Київ', '2023-01-15', '2024-01-15'),
('Французька компанія', 'Франція', 'Париж', '2023-02-20', '2024-02-20'),
('Американська компанія', 'США', 'Лос-Анджелес', '2023-03-25', '2024-03-25'),
('Британська компанія', 'Велика Британія', 'Лондон', '2023-04-30', '2024-04-30'),
('Іспанська компанія', 'Іспанія', 'Мадрид', '2023-05-10', '2024-05-10'),
('Люфтганза', 'Німеччина', 'Франкфурт', '2023-06-15', '2024-06-15'),
('Китайські авіалінії', 'Китай', 'Пекін', '2023-07-20', '2024-07-20'),
('Японські польоти', 'Японія', 'Токіо', '2023-08-25', '2024-08-25'),
('Канадські польоти', 'Канада', 'Оттава', '2023-09-30', '2024-09-30'),
('Австралійська компанія', 'Австралія', 'Сідней', '2023-10-05', '2024-10-05');

INSERT INTO airplane (lift_weight, number_of_passenger, plain_mileage, average_speed, aviacompany_id, registration_id, plane_model, plane_maker) VALUES
(150000, 180, '5000', '900', 1, 1, 'Model-1', 'Maker-1'),
(200000, 220, '5500', '950', 2, 2, 'Model-2', 'Maker-2'),
(180000, 200, '5200', '920', 3, 3, 'Model-3', 'Maker-3'),
(160000, 190, '5100', '910', 4, 4, 'Model-4', 'Maker-4'),
(170000, 195, '5250', '930', 5, 5, 'Model-5', 'Maker-5'),
(190000, 205, '5350', '940', 6, 6, 'Model-6', 'Maker-6'),
(210000, 230, '5800', '970', 7, 7, 'Model-7', 'Maker-7'),
(180000, 200, '5100', '900', 8, 8, 'Model-8', 'Maker-8'),
(220000, 240, '6000', '980', 9, 9, 'Model-9', 'Maker-9'),
(160000, 190, '5150', '910', 10, 10, 'Model-10', 'Maker-10');

INSERT INTO flight (start_time, end_time, route_id, airplane_id, departure_gate, arrival_gate) VALUES
('2023-10-23 08:00:00', '2023-10-23 14:30:00', 1, 1, 'A1', 'B2'),
('2023-10-23 10:30:00', '2023-10-23 18:00:00', 2, 2, 'C3', 'D4'),
('2023-10-23 09:45:00', '2023-10-23 17:30:00', 3, 3, 'E5', 'F6'),
('2023-10-23 12:15:00', '2023-10-23 20:45:00', 4, 4, 'G7', 'H8'),
('2023-10-23 11:30:00', '2023-10-23 19:15:00', 5, 5, 'I9', 'J10'),
('2023-10-23 07:00:00', '2023-10-23 14:30:00', 6, 6, 'K11', 'L12'),
('2023-10-23 13:45:00', '2023-10-23 22:15:00', 7, 7, 'M13', 'N14'),
('2023-10-23 15:20:00', '2023-10-23 23:45:00', 8, 8, 'O15', 'P16'),
('2023-10-23 14:00:00', '2023-10-23 22:30:00', 9, 9, 'Q17', 'R18'),
('2023-10-23 08:45:00', '2023-10-23 17:15:00', 10, 10, 'S19', 'T20');

INSERT INTO pilot (calling, age, experience, license_number, current_rank) VALUES
('рев', 35, 10, 'P-111', 'Капітан'),
('борсук', 40, 15, 'P-222', 'Капітан'),
('хорнет', 32, 8, 'P-333', 'Капітан'),
('сокіл', 38, 12, 'P-444', 'Капітан'),
('дикий', 29, 6, 'P-555', 'Капітан'),
('олень', 45, 20, 'P-666', 'Капітан'),
('бобер', 34, 9, 'P-777', 'Капітан'),
('дикий-8.4', 39, 14, 'P-888', 'Капітан'),
('сокіл', 31, 7, 'P-999', 'Капітан'),
('рев', 37, 11, 'P-1010', 'Капітан');


INSERT INTO dispatcher (calling, age, aeroport_id, dispatcher_license_number, contact_number) VALUES
('рись', 30, 1, 'D-111', '+380111111111'),
('хорнет', 35, 2, 'D-222', '+331111111111'),
('хорнет-3.1', 28, 3, 'D-333', '+132111111111'),
('шкіпер', 33, 4, 'D-444', '+442111111111'),
('ротор', 26, 5, 'D-555', '+342111111111'),
('прайс', 37, 6, 'D-666', '+492111111111'),
('озон', 29, 7, 'D-777', '+862111111111'),
('скерк-8.3', 32, 8, 'D-888', '+812111111111'),
('мактавіш', 36, 9, 'D-999', '+112111111111'),
('шепард', 31, 10, 'D-1010', '+612111111111');

INSERT INTO air_hostess (gender, age, email, languages_spoken, language_nature) VALUES
('Жінка', 28, 'wew@gmail.com', 'Англійська, Французька', 'Французька'),
('Жінка', 26, 'gtg@gmail.com', 'Англійська, Іспанська', 'Іспанська'),
('Чоловік', 31, 'bf@gmail.com', 'Англійська, Китайська', 'Китайська'),
('Жінка', 29, 'uu@gmail.com', 'Англійська, Японська', 'Японська'),
('Чоловік', 30, 'gg@gmail.com', 'Англійська, Німецька', 'Німецька'),
('Жінка', 28, 'pp@gmail.com', 'Англійська, Корейська', 'Англійська'),
('Жінка', 27, 'mm@gmail.com', 'Англійська, Французька', 'Англійська'),
('Чоловік', 30, 'qq@gmail.com', 'Англійська, Чеська', 'Англійська'),
('Жінка', 32, 'ee@gmail.com', 'Англійська, Німецька', 'Німецька'),
('Чоловік', 27, 'ww@gmail.com', 'Англійська, Італійська', 'Італійська');

INSERT INTO pilot_has_flight (pilot_id, flight_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);


INSERT INTO air_hostess_has_flight (air_hostess_id, flight_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO dispatcher_has_flight (dispatcher_id, flight_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);

INSERT INTO flight_services (flight_id, service_description, service_type, service_cost)
VALUES (1, 'Обід', 'Харчування', 25.00),
 (2, 'Додатковий багаж', 'Послуги', 50.00)
 ;
 
 INSERT INTO flight_services (flight_id, service_description, service_type, service_cost)
VALUES (3, 'Обід', 'Харчування', 150.00);
 DROP TRIGGER IF EXISTS before_insert_flight_services;
DELIMITER //

CREATE TRIGGER before_insert_flight_services
BEFORE INSERT ON flight_services
FOR EACH ROW
BEGIN
    IF NOT EXISTS (SELECT 1 FROM flight WHERE id = NEW.flight_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Недійсний flight_id, рейсу не існу';
    END IF;
END //

DELIMITER ;

DROP TRIGGER IF EXISTS prevent_double_zero;
DELIMITER //
CREATE TRIGGER prevent_double_zero
BEFORE INSERT ON aviacompany
FOR EACH ROW
BEGIN
    IF NEW.name LIKE '%00' THEN 
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Значення name не може закінчуватися двома нулями';
    END IF;
END;
//
DELIMITER ;


DROP TRIGGER IF EXISTS check_allowed_names;
DELIMITER //
CREATE TRIGGER check_allowed_names
BEFORE INSERT ON air_hostess
FOR EACH ROW
BEGIN
    IF NEW.gender NOT IN ('Svitlana', 'Petro', 'Olha', 'Taras') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Неможна використовувати таке імя ';
    END IF;
END;
//

DELIMITER ;






DROP TRIGGER IF EXISTS check_row_cardinality;
DELIMITER //
CREATE TRIGGER check_row_cardinality
BEFORE INSERT ON flight
FOR EACH row
BEGIN
    DECLARE row_count INT;
    SELECT COUNT(*) INTO row_count FROM flight;
    
    IF row_count >= 6 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Досягнуто максимальну кардинальність (6)';
    END IF;
END;
//
DELIMITER ;


-- INSERT INTO air_hostess (gender, age, email) VALUES
-- ('nnnnn', '25', 'nastya@gmail.com');


-- INSERT INTO flight (start_time, end_time, route_id, airplane_id) VALUES
-- ('2023-09-28 08:00:00', '2023-09-28 10:00:00', 1, 1);

-- INSERT INTO aviacompany (name, country_of_company) VALUES
-- ('Germany avia00', 'Germany');







-- second task(a)
DROP PROCEDURE IF EXISTS insert_dispatcher;

DELIMITER $$

CREATE PROCEDURE insert_dispatcher(
 IN calling VARCHAR(50),
 IN age INT,
 IN aeroport_id INT,
 IN dispatcher_license_number VARCHAR(20),
 IN contact_number VARCHAR(15)
)
BEGIN

 -- Вставка нового рядка
 INSERT INTO `flight_radar_lab5`.`dispatcher`
 (`calling`, `age`, `aeroport_id`, `dispatcher_license_number`, `contact_number`)
 VALUES
 (calling, age, aeroport_id, dispatcher_license_number, contact_number);

END $$

DELIMITER ;


-- CALL insert_dispatcher(
--  'Maria Petrivna',
--  40,
--  7,
--  '38573984',
--  '+380000000'
-- );


 -- second task(C)
 DROP PROCEDURE IF EXISTS insert_noname_in_marshrut;
DELIMITER $$
CREATE PROCEDURE insert_noname_in_marshrut(
  IN city VARCHAR(50),
  IN airport_id1 INT,
  IN airport_id2 INT
)
BEGIN
  DECLARE i INT DEFAULT 5;

  WHILE i <= 10 DO
    INSERT INTO marshrut (country, city, aeroport_id1, aeroport_id2, distance_km, marshrut_status)
    VALUES (CONCAT('country', i), city, aeroport_id1, aeroport_id2, distance_km, marshrut_status);
    SET i = i + 1;
  END WHILE;
END$$
DELIMITER ;


CALL insert_noname_in_marshrut('Sambir', 1, 2 , 1111,'Active');







 DROP PROCEDURE IF EXISTS get_statistic;
 
 DELIMITER $$
CREATE FUNCTION get_statistic(
  table_name VARCHAR(50),
  column_name VARCHAR(50),
  statistic_type VARCHAR(50)
)
RETURNS DECIMAL(10,2)
BEGIN
  DECLARE result DECIMAL(10,2);

  CASE statistic_type
    WHEN 'MAX' THEN
      SELECT MAX(column_name) INTO result
      FROM table_name;
    WHEN 'MIN' THEN
      SELECT MIN(column_name) INTO result
      FROM table_name;
    WHEN 'SUM' THEN
      SELECT SUM(column_name) INTO result
      FROM table_name;
    WHEN 'AVG' THEN
      SELECT AVG(column_name) INTO result
      FROM table_name;
    ELSE
      RETURN NULL;
  END CASE;

  RETURN result;
END$$
DELIMITER ;








DELIMITER $$
CREATE FUNCTION get_statistic(
  table_name VARCHAR(50),
  column_name VARCHAR(50),
  statistic_type VARCHAR(50)
)
RETURNS DECIMAL(10,2)
BEGIN
  DECLARE result DECIMAL(10,2);

  IF statistic_type = 'MAX' THEN
    SELECT MAX(column_name) INTO result
    FROM table_name;
  ELSIF statistic_type = 'MIN' THEN
    SELECT MIN(column_name) INTO result
    FROM table_name;
  ELSIF statistic_type = 'SUM' THEN
    SELECT SUM(column_name) INTO result
    FROM table_name;
  ELSIF statistic_type = 'AVG' THEN
    SELECT AVG(column_name) INTO result
    FROM table_name;
  ELSE
    RETURN NULL;
  END IF;

  RETURN result;
END$$
DELIMITER ;

CALL get_statistic_in_select('marshrut', 'distance_km', 'AVG');