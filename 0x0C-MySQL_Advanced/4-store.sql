-- store values
-- create triggers
DELIMITER $$

CREATE TRIGGER after_new_order
BEFORE INSERT
ON orders FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;