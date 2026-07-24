-- Improving Parts Tracking
SELECT *
FROM parts
LIMIT 10;

ALTER TABLE parts
ALTER COLUMN code SET NOT NULL;

ALTER TABLE parts
ADD UNIQUE(code);

UPDATE parts
SET description = 'Not Available'
WHERE description IS NULL;

CREATE TABLE part_descriptions (
  id INTEGER PRIMARY KEY,
  description TEXT
);

INSERT INTO part_descriptions VALUES (
  1,
  '5V resistor'
), (
  2,
  '3V resistor'
);

UPDATE parts
SET description = part_descriptions.description
FROM part_descriptions
WHERE part_descriptions.id = parts.id
  AND parts.description IS NULL;

ALTER TABLE parts
ALTER COLUMN description SET NOT NULL;

INSERT INTO parts (
  id,
  description,
  code,
  manufacturer_id
) VALUES (
  54,
  'Passive Buzzer',
  'V1-009',
  9
);

ALTER TABLE reorder_options
ALTER COLUMN price_usd SET NOT NULL;

ALTER TABLE reorder_options
ALTER COLUMN quantity SET NOT NULL;

ALTER TABLE reorder_options
ADD CHECK (price_usd > 0 AND quantity > 0);

ALTER TABLE reorder_options
ADD CHECK (price_usd/quantity > 0.02 AND price_usd/quantity < 25.00);

ALTER TABLE parts
ADD PRIMARY KEY (id);

ALTER TABLE reorder_options
ADD FOREIGN KEY (part_id) REFERENCES parts (id);

-- Improving Location Tracking
ALTER TABLE locations
ADD CHECK (qty > 0);

ALTER TABLE locations
ADD UNIQUE (part_id, location);

ALTER TABLE locations
ADD FOREIGN KEY (part_id) 
REFERENCES parts(id);

-- Improving Manufacturer Tracking
ALTER TABLE parts
ADD FOREIGN KEY (manufacturer_id)
REFERENCES manufacturers (id);

INSERT INTO manufacturers (
  name,
  id
)
VALUES (
  'Pip-NNC Industrial',
  11
);

UPDATE parts
SET manufacturer_id = 11
WHERE manufacturer_id = 1
  OR manufacturer_id = 2;
