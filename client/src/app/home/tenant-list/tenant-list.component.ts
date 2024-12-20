import { Component, Inject, OnInit } from '@angular/core';
import { TenantService } from './tenant.service';
import { TenantInfo } from './tenant.model';
import { ModalService } from 'src/app/modal/modal.service';
import { CreateTenantModalComponent } from '../create-tenant-modal/create-tenant-modal.component';
import { Subject } from 'rxjs';
import { REFRESH_TRIGGER } from 'src/app/app.module';
import { AvailabilityModalComponent } from '../availability-modal/availability-modal.component';

@Component({
  selector: 'tenant-list',
  templateUrl: 'tenant-list.component.html',
  styleUrls: ['tenant-list.component.scss'],
})
export class TenantListComponent implements OnInit {
  tenantInfoList: TenantInfo[] = [];

  constructor(
    private tenantService: TenantService,
    private modalService: ModalService,
    @Inject(REFRESH_TRIGGER) private refreshTrigger: Subject<void>
  ) {}

  ngOnInit(): void {
    this.getTenantInfoList();
    this.refreshTrigger.subscribe(() => this.getTenantInfoList());
  }

  openCreateTenantModal() {
    this.modalService.open(CreateTenantModalComponent, undefined, {
      title: 'Add tenant',
    });
  }

  manageAvailability(tenantInfo: TenantInfo) {
    this.modalService.open(
      AvailabilityModalComponent,
      {
        tenant_id: tenantInfo.tenant_id,
        tenant_email: tenantInfo.email,
      },
      { title: 'Manage availability' }
    );
  }

  private getTenantInfoList() {
    this.tenantService
      .getTenantInfoList$()
      .subscribe((list) => (this.tenantInfoList = list));
  }
}
