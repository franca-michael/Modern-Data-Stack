with source as (
    select * from {{ source('raw_ecommerce', 'olist_orders_dataset') }}
),

renamed as (
    select
        order_id,
        customer_id,
        order_status,
        -- Convertendo strings para formato de data/hora (Timestamp) no Postgres
        order_purchase_timestamp::timestamp as purchased_at,
        order_delivered_customer_date::timestamp as delivered_at
    from source
)

select * from renamed