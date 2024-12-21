import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ReportItem } from './report.model';

@Injectable({ providedIn: 'root' })
export class ReportService {
  constructor(private http: HttpClient) {}

  getCustomersReport$(strict: boolean): Observable<ReportItem[]> {
    const params = new HttpParams().set('strict', strict);
    return this.http.get<ReportItem[]>('/api/sla/report', { params });
  }
}
