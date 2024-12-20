export enum AvailabilityLevel {
  DEFAULT = 'Default',
  CUSTOMER_SPECIFIC = 'Customer-Specific',
  EXPIRED = 'Expired',
  UNKNOWN = 'Unknwon',
}

export interface CreateAvailabilityLogMessageSpec {
  tenant_id: number;
  level: AvailabilityLevel;
}
