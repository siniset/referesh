CREATE TYPE reference_type AS ENUM ('book');

CREATE TABLE IF NOT EXISTS reference_entries (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  type reference_type NOT NULL,
  created_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS fields (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  content TEXT,
  reference_entry INTEGER NOT NULL,
  FOREIGN KEY (reference_entry) REFERENCES reference_entries(id) ON DELETE CASCADE
);
