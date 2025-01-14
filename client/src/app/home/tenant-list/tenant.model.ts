export interface TenantInfo {
  service_name: string;
  email: string;
  date_of_expiration: string;
  tenant_id: number;
}

export interface CreateTenantSpec {
  email: string;
  service_id: number;
}
