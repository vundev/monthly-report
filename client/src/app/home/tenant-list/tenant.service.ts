import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { TenantInfo } from './tenant.model';

@Injectable({ providedIn: 'root' })
export class TenantService {
  constructor(private http: HttpClient) {}

  getTenantInfoList$(): Observable<TenantInfo[]> {
    return this.http.get<TenantInfo[]>('/api/tenant/list');
  }
}
