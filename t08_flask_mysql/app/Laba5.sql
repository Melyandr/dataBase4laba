
CREATE TABLE flight_services (
    id int not null auto_increment PRIMARY KEY,
    flight_id int not null,
    service_description varchar(100) not null,
    service_type varchar(50) not null,
    service_cost decimal(10,2) not null

) ENGINE=InnoDB;


use flight_radar_project;

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
 INSERT INTO `dispatcher`
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