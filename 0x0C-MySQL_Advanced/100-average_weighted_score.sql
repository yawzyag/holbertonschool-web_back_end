-- store values
-- average score
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id int)
BEGIN
    UPDATE users set average_score = (SELECT 
    SUM((c.score) * p.weight) / (SUM(p.weight)) 'avg'
    FROM corrections as c
    INNER JOIN projects AS p 
    ON p.id = c.project_id 
    where c.user_id = user_id)
    where users.id = user_id;
END //
DELIMITER ;
