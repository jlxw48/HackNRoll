DROP SCHEMA IF EXISTS soscoders CASCADE;

CREATE SCHEMA soscoders;

SET search_path TO soscoders;

--Tables
CREATE TYPE gender AS enum ('male', 'female');
CREATE TYPE faculty AS enum ('FASS', 'Business', 'Engineering', 'Computing', 'Science', 'SDE', 'Music');

CREATE TABLE users (
    telegram_id INTEGER PRIMARY KEY,
    telegram_username VARCHAR,
    faculty faculty NOT NULL,
    study_year INTEGER NOT NULL,
    gender gender NOT NULL
);

CREATE TABLE request (
    id INTEGER references users (telegram_id),
    module VARCHAR NOT NULL,
    PRIMARY KEY(id, module)
);