import { Component, Inject, OnDestroy, OnInit } from '@angular/core';
import { Subject, Subscription } from 'rxjs';
import { REFRESH_TRIGGER } from 'src/app/app.module';
import { ModalService } from 'src/app/modal/modal.service';
import { AvailabilityModalComponent } from '../availability-modal/availability-modal.component';
import { CreateTenantModalComponent } from '../create-tenant-modal/create-tenant-modal.component';
import { TenantInfo } from './tenant.model';
import { TenantService } from './tenant.service';

@Component({
  selector: 'tenant-list',
  templateUrl: 'tenant-list.component.html',
  styleUrls: ['tenant-list.component.scss'],
})
export class TenantListComponent implements OnInit, OnDestroy {
  tenantInfoList: TenantInfo[] = [];

  private subscriptions = new Subscription();

  constructor(
    private tenantService: TenantService,
    private modalService: ModalService,
    @Inject(REFRESH_TRIGGER) private refreshTrigger: Subject<void>
  ) {}

  ngOnInit(): void {
    this.getTenantInfoList();
    this.subscriptions.add(
      this.refreshTrigger.subscribe(() => this.getTenantInfoList())
    );
  }

  ngOnDestroy(): void {
    this.subscriptions.unsubscribe();
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
