import { HttpClient } from '@angular/common/http';
import { Inject, Injectable } from '@angular/core';
import { Observable, Subject, tap } from 'rxjs';
import { CreateTenantSpec, TenantInfo } from './tenant.model';
import { REFRESH_TRIGGER } from 'src/app/app.module';

@Injectable({ providedIn: 'root' })
export class TenantService {
  private readonly refresh = () => this.refreshTrigger.next();

  constructor(
    private http: HttpClient,
    @Inject(REFRESH_TRIGGER) private refreshTrigger: Subject<void>
  ) {}

  getTenantInfoList$(): Observable<TenantInfo[]> {
    return this.http.get<TenantInfo[]>('/api/tenant/list');
  }

  createTenant$(createSpec: CreateTenantSpec) {
    return this.http
      .post('/api/tenant/create', createSpec)
      .pipe(tap(this.refresh));
  }
}
