import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CreateAvailabilityLogMessageSpec } from './availability.model';

@Injectable({ providedIn: 'root' })
export class AvailabilityService {
  constructor(private http: HttpClient) {}

  logAvailabilityChangeMessage$(createSpec: CreateAvailabilityLogMessageSpec) {
    return this.http.post('/api/sla/log', createSpec);
  }
}
