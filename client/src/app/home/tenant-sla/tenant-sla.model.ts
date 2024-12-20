export interface TenantSlaInfo {
  month: string;
  tenant_id: number;
  email: string;
  service_name: string;
  min_availability_level: number;
  expired_count: number;
}
