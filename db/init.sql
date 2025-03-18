-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create database (if not already created by POSTGRES_DB)
SELECT 'CREATE DATABASE :' || :'POSTGRES_DB' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = :'POSTGRES_DB')\gexec

-- Switch to the database
\c :POSTGRES_DB;

-- Create user and grant privileges dynamically
DO $$
DECLARE
    chatbot_user TEXT := :'POSTGRES_USER';
    chatbot_password TEXT := :'POSTGRES_PASSWORD';
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = chatbot_user) THEN
        EXECUTE format('CREATE USER %I WITH ENCRYPTED PASSWORD %L', chatbot_user, chatbot_password);
    END IF;
END $$;

GRANT ALL PRIVILEGES ON DATABASE :POSTGRES_DB TO :CHATBOT_DB_USER;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) CHECK (role IN ('admin', 'support')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chatbot_queries (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ticket_responses (
    id SERIAL PRIMARY KEY,
    ticket_id INT NOT NULL,
    user_id INT REFERENCES users(id) ON DELETE SET NULL,
    ai_response TEXT NOT NULL,
    status VARCHAR(20) CHECK (status IN ('pending', 'approved', 'sent')) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE knowledge_base (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    file_url TEXT,  -- Stores document location (Hetzner S3)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vector_index (
    id SERIAL PRIMARY KEY,
    knowledge_id INT REFERENCES knowledge_base(id) ON DELETE CASCADE,
    embedding_vector VECTOR(1536), -- Using OpenAI's embedding size
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chatbot_settings (
    id SERIAL PRIMARY KEY,
    setting_key VARCHAR(255) UNIQUE NOT NULL,
    setting_value TEXT NOT NULL
);