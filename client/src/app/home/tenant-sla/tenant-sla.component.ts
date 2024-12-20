import { Component, OnInit } from '@angular/core';
import { TenantSlaService } from './tenant-sla.service';
import { TenantSlaInfo } from './tenant-sla.model';

@Component({
  selector: 'tenant-sla',
  templateUrl: 'tenant-sla.component.html',
  styleUrls: ['tenant-sla.component.scss'],
})
export class TenantSlaComponent implements OnInit {
  tenantSlaInfoList: TenantSlaInfo[] = [];

  constructor(private tenantSlaService: TenantSlaService) {}

  ngOnInit(): void {
    this.tenantSlaService
      .getTenantSla$()
      .subscribe((list) => (this.tenantSlaInfoList = list));
  }
}
