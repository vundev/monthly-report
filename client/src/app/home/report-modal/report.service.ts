import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ReportItem } from './report.model';

@Injectable({ providedIn: 'root' })
export class ReportService {
  constructor(private http: HttpClient) {}

  getCustomersReport$(strict: boolean): Observable<ReportItem[]> {
    return this.http.get<ReportItem[]>(
      strict ? '/api/sla/report-strict' : '/api/sla/report'
    );
  }
}
