# create database gjg_lorraine;

DROP TABLE IF EXISTS gjg_lorraine.users;

CREATE TABLE gjg_lorraine.users (
  user varchar(32) NOT NULL,
  passw varchar(32) NOT NULL,
  name varchar(32) NOT NULL,
  PRIMARY KEY (`user`),
  UNIQUE KEY user (user),
  UNIQUE KEY passw (passw)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS gjg_lorraine.blogs;

CREATE TABLE gjg_lorraine.blogs (
  title varchar(32) NOT NULL,
  content text NOT NULL,
  user varchar(32) NOT NULL,
  PRIMARY KEY (title),
  KEY user (user),
  CONSTRAINT user FOREIGN KEY (user) REFERENCES users (user)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
