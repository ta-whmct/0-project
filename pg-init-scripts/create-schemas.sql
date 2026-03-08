DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_namespace WHERE nspname = 'zero') THEN
        CREATE SCHEMA zero;
    END IF;
END $$;
