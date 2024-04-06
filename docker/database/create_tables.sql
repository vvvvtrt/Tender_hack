create table if not exists products(
    id BIGINT primary key,
    standart_unit text not null,
    type text,
    model text,
    producer text,
    units text,
--     created_at bool
);