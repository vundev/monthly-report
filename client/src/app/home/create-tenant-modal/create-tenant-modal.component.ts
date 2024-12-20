import { Component, OnInit } from '@angular/core';
import { ModalService } from 'src/app/modal/modal.service';
import { ServiceName } from './service-name.model';
import { ServiceNameService } from './service-name.service';
import { listIcon } from '@cds/core/icon';
import { TenantService } from '../tenant-list/tenant.service';

@Component({
  selector: 'create-tenant-modal',
  templateUrl: 'create-tenant-modal.component.html',
  styleUrls: ['create-tenant-modal.component.scss'],
})
export class CreateTenantComponent implements OnInit {
  serviceNameList: ServiceName[] = [];
  selectedServiceId?: number;
  tenantEmail?: string;

  constructor(
    private modalService: ModalService,
    private serviceNameService: ServiceNameService,
    private tenantService: TenantService
  ) {}

  ngOnInit(): void {
    this.serviceNameService.getServiceNameList$().subscribe((list) => {
      this.serviceNameList = list;
      this.selectedServiceId = list[0].id;
    });
  }

  submit() {
    if (!this.tenantEmail || !this.selectedServiceId) {
      return;
    }
    this.tenantService
      .createTenant$({
        email: this.tenantEmail!,
        service_id: this.selectedServiceId!,
      })
      .subscribe(() => this.modalService.close());
  }

  close() {
    this.modalService.close();
  }
}
