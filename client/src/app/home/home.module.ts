import { NgModule } from '@angular/core';

import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { CommonModule } from '@angular/common';
import { ClarityModule } from '@clr/angular';
import { TenantListComponent } from './tenant-list/tenant-list.component';
import { CreateTenantComponent } from './create-tenant-modal/create-tenant-modal.component';

@NgModule({
  declarations: [HomeComponent, TenantListComponent, CreateTenantComponent],
  imports: [HomeRoutingModule, CommonModule, ClarityModule],
  entryComponents: [CreateTenantComponent],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
