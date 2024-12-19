from sqlmodel import text

query_tenant_sla = text(
    """
    WITH MonthlyData AS (
        SELECT 
            strftime('%Y-%m', al.log_date) AS month,
            al.tenant_id,
            t.email,
            s.service_name,
            MIN(CASE 
                WHEN al.availability_level = 'Default' THEN 1
                WHEN al.availability_level = 'Customer-Specific' THEN 2
                ELSE 3
            END) AS min_availability_level,
            COUNT(CASE WHEN al.availability_level = 'Expired' THEN 1 END) AS expired_count
        FROM 
            availabilitylogs al
        JOIN 
            tenant t ON t.id = al.tenant_id
        JOIN 
            service s ON t.service_id = s.id
        GROUP BY 
            al.tenant_id, strftime('%Y-%m', al.log_date), s.service_name
    )
    SELECT * FROM MonthlyData
    ORDER BY 
        month;
    """
)
