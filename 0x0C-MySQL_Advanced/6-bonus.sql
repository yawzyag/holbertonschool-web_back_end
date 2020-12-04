-- store values
-- email procedure
DELIMITER //
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (IN user_id int, IN project_name varchar(255), IN score int)
BEGIN
   INSERT INTO projects (name)
    SELECT * FROM (SELECT project_name) AS tmp
    WHERE NOT EXISTS (
        SELECT name FROM projects WHERE name = project_name
    ) LIMIT 1;
    
   INSERT INTO corrections SET user_id = user_id, score = score,
   project_id = (select id from projects where projects. name = project_name);
END //
DELIMITER ;