CREATE TABLE album
(
    album_id INT NOT NULL,
    title VARCHAR(160) NOT NULL,
    artist_id INT NOT NULL,
    CONSTRAINT album_pkey PRIMARY KEY  (album_id)
);

CREATE TABLE artist
(
    artist_id INT NOT NULL,
    name VARCHAR(120),
    CONSTRAINT artist_pkey PRIMARY KEY  (artist_id)
);

CREATE TABLE customer
(
    customer_id INT NOT NULL,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(60) NOT NULL,
    CONSTRAINT customer_pkey PRIMARY KEY  (customer_id)
);

CREATE TABLE invoice
(
    invoice_id INT NOT NULL,
    customer_id INT NOT NULL,
    invoice_date TIMESTAMP NOT NULL,
    total NUMERIC(10,2) NOT NULL,
    CONSTRAINT invoice_pkey PRIMARY KEY  (invoice_id)
);

CREATE TABLE invoice_line
(
    invoice_line_id INT NOT NULL,
    invoice_id INT NOT NULL,
    track_id INT NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    quantity INT NOT NULL,
    CONSTRAINT invoice_line_pkey PRIMARY KEY  (invoice_line_id)
);

CREATE TABLE track
(
    track_id INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    album_id INT,
    unit_price NUMERIC(10,2) NOT NULL,
    CONSTRAINT track_pkey PRIMARY KEY  (track_id)
);

ALTER TABLE album ADD CONSTRAINT album_artist_id_fkey
    FOREIGN KEY (artist_id) REFERENCES artist (artist_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE invoice ADD CONSTRAINT invoice_customer_id_fkey
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE invoice_line ADD CONSTRAINT invoice_line_invoice_id_fkey
    FOREIGN KEY (invoice_id) REFERENCES invoice (invoice_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE invoice_line ADD CONSTRAINT invoice_line_track_id_fkey
    FOREIGN KEY (track_id) REFERENCES track (track_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE track ADD CONSTRAINT track_album_id_fkey
    FOREIGN KEY (album_id) REFERENCES album (album_id) ON DELETE NO ACTION ON UPDATE NO ACTION;