export enum AvailabilityLevel {
  DEFAULT = 'Default',
  CUSTOMER_SPECIFIC = 'Customer-Specific',
  EXPIRED = 'Expired',
}

export interface CreateAvailabilityLogMessageSpec {
  tenant_id: number;
  level: AvailabilityLevel;
}
