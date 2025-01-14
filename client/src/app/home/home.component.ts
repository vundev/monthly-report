import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CustomerMe } from '../model/customer.model';
import { CustomerService } from './customer.service';
import { AuthenticationService } from '../services/authentication.service';
import { extractErrorMessage } from '../global';
import { ReportModalComponent } from './report-modal/report-modal.component';
import { ModalService } from '../modal/modal.service';

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
    private authenticationServie: AuthenticationService,
    private modalService: ModalService
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

  openReportModal(strict: boolean = false) {
    this.modalService.open(
      ReportModalComponent,
      { strict },
      {
        title: strict ? 'Report strict' : 'Report',
        size: 'xl',
      }
    );
  }
}
