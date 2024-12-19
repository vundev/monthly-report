import { Component, OnInit } from '@angular/core';
import { TenantService } from './tenant.service';
import { TenantInfo } from './tenant.model';
import { ModalService } from 'src/app/modal/modal.service';
import { CreateTenantComponent } from '../create-tenant-modal/create-tenant-modal.component';

@Component({
  selector: 'tenant-list',
  templateUrl: 'tenant-list.component.html',
  styleUrls: ['tenant-list.component.scss'],
})
export class TenantListComponent implements OnInit {
  tenantInfoList: TenantInfo[] = [];

  constructor(
    private tenantService: TenantService,
    private modalService: ModalService
  ) {}

  ngOnInit(): void {
    this.tenantService
      .getTenantInfoList$()
      .subscribe((list) => (this.tenantInfoList = list));
  }

  openCreateTenantModal() {
    this.modalService.open(CreateTenantComponent);
  }
}
