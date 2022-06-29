CREATE TABLE IF NOT EXISTS Pages (
    id INTEGER PRIMARY KEY, 
    url TEXT UNIQUE, 
    html TEXT,
    error INTEGER, 
    old_rank REAL, 
    new_rank REAL
);

CREATE TABLE IF NOT EXISTS Links (
    from_id INTEGER, 
    to_id INTEGER, 
    UNIQUE(from_id, to_id)
);

CREATE TABLE IF NOT EXISTS Webs (
    url TEXT UNIQUE
);

SELECT 
    id,url 
FROM 
    Pages 
WHERE 
    html is NULL 
    and 
    error is NULL 
ORDER BY 
    RANDOM() LIMIT 1
;