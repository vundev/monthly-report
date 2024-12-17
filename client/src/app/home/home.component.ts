import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CustomerMe } from '../model/customer.model';
import { CustomerService } from './customer.service';
import { AuthenticationService } from '../services/authentication.service';
import { extractErrorMessage } from '../global';

@Component({
  selector: 'home',
  templateUrl: 'home.component.html',
  styleUrls: ['home.component.scss'],
})
export class HomeComponent implements OnInit {
  customer?: CustomerMe;
  errorMessage?: string;

  constructor(
    private router: Router,
    private customerService: CustomerService,
    private authenticationServie: AuthenticationService
  ) {}

  ngOnInit(): void {
    this.customerService.getCustomer$().subscribe(
      (customer) => (this.customer = customer),
      (error) => (this.errorMessage = extractErrorMessage(error))
    );
  }

  logout() {
    this.authenticationServie.logout();
    this.router.navigate(['login']);
  }
}
