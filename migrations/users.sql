CREATE TABLE public.users
(
    username character varying(10) NOT NULL,
    email character varying(50),
    password character varying(10) NOT NULL,
    CONSTRAINT username PRIMARY KEY (username)
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public.users
    OWNER to postgres;
COMMENT ON TABLE public.users
    IS 'user information';
