-- index
-- create index on table names
-- CREATE INDEX idx_name_first ON names (name(1));
ALTER TABLE `names`
ADD INDEX `idx_name_first` (`name`(1));