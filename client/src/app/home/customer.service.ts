import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CustomerMe } from '../model/customer.model';

@Injectable({ providedIn: 'root' })
export class CustomerService {
  constructor(private http: HttpClient) {}

  getCustomer$(): Observable<CustomerMe> {
    return this.http.get<CustomerMe>('/api/customer/me');
  }
}
