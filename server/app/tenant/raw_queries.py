from sqlmodel import text

query_tenant_infos = text(
    """
    SELECT service.service_name AS service_name,
            tenant.email AS email,
            tenant.date_of_expiration AS date_of_expiration
    FROM tenant
    JOIN service ON tenant.service_id = service.id
    WHERE tenant.customer_id = :customer_id
    """
)
