-- store values
-- average score
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id int)
BEGIN
    UPDATE users set average_score = (SELECT 
    Sum(score) / COUNT(DISTINCT project_id) AS 'avg'
    from corrections where corrections.user_id = user_id)
    where users.id = user_id;
END //
DELIMITER ;