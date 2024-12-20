import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ServiceName } from './service-name.model';

@Injectable({ providedIn: 'root' })
export class ServiceNameService {
  constructor(private http: HttpClient) {}

  getServiceNameList$(): Observable<ServiceName[]> {
    return this.http.get<ServiceName[]>('/api/service/list');
  }
}
