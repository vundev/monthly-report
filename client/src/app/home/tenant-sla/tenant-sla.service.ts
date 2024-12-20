import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { TenantSlaInfo } from './tenant-sla.model';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class TenantSlaService {
  constructor(private http: HttpClient) {}

  getTenantSla$(): Observable<TenantSlaInfo[]> {
    return this.http.get<TenantSlaInfo[]>('/api/sla/tenant-sla');
  }
}
