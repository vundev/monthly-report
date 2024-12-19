import { Component, OnInit } from '@angular/core';
import { TenantService } from '../shared/services/tenant.service';
import { TenantInfo } from '../shared/model/tenant.model';

@Component({
  selector: 'tenant-list',
  templateUrl: 'tenant-list.component.html',
  styleUrls: ['tenant-list.component.scss'],
})
export class TenantListComponent implements OnInit {
  tenantInfoList: TenantInfo[] = [];

  constructor(private tenantService: TenantService) {}

  ngOnInit(): void {
    this.tenantService
      .getTenantInfoList$()
      .subscribe((list) => (this.tenantInfoList = list));
  }
}
