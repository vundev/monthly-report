import { Pipe, PipeTransform } from '@angular/core';
import { AvailabilityLevel } from '../availability-modal/availability.model';

@Pipe({
  name: 'availabilityLevel',
})
export class AvailabilityLevelPipe implements PipeTransform {
  transform(value: number): AvailabilityLevel {
    const nameByLevel: Record<number, AvailabilityLevel> = {
      1: AvailabilityLevel.DEFAULT,
      2: AvailabilityLevel.CUSTOMER_SPECIFIC,
      3: AvailabilityLevel.EXPIRED,
    };
    return nameByLevel[value] || AvailabilityLevel.UNKNOWN;
  }
}
