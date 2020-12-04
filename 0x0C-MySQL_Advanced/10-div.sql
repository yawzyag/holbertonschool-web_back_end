-- save divide
-- query
DELIMITER $$

DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(
	a INT,
    b INT
) 
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE returnVal FLOAT;

    IF b = 0 THEN
		SET returnVal = 0;
    ELSE
        SET returnVal = a / b;
    END IF;
	-- return the customer level
	RETURN (returnVal);
END$$
DELIMITER ;