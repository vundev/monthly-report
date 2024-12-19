from sqlmodel import text

# Used for debug purpose.
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

query_report = text(
    """
    WITH MonthlyData AS (
        SELECT 
            al.tenant_id,
            strftime('%Y-%m', al.log_date) AS month,
            MIN(CASE 
                WHEN al.availability_level = 'Default' THEN 1
                WHEN al.availability_level = 'Customer-Specific' THEN 2
                -- For Expired level we return the highest value.
                ELSE 3
            END) AS min_availability_level,
            -- Count the number of AvailabilityLevel entries with level Expired.
            COUNT(CASE WHEN al.availability_level = 'Expired' THEN 1 END) AS expired_count
        FROM 
            availabilitylogs al
        GROUP BY 
            al.tenant_id, strftime('%Y-%m', al.log_date)
    ),
    FilteredData AS (
        SELECT 
            md.tenant_id,
            md.month,
            CASE md.min_availability_level
                WHEN 1 THEN 'Default'
                WHEN 2 THEN 'Customer-Specific'
            END AS availability_level
        FROM 
            MonthlyData md
        WHERE 
            -- Exclude tenants which were in state Expired during some period in the month.
            md.expired_count = 0
    )
    SELECT 
        fd.month,
        c.customer_name,
        fd.tenant_id,
        t.email,
        s.service_name,
        fd.availability_level
    FROM 
        FilteredData fd
    JOIN 
        tenant t ON t.id = fd.tenant_id
    JOIN 
        service s ON t.service_id = s.id
    JOIN
        customer c ON t.customer_id = c.id
    ORDER BY 
        fd.month;
    """
)
