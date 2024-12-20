import { NgModule } from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from '@clr/angular';
import { CreateTenantComponent } from './create-tenant-modal/create-tenant-modal.component';
import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';
import { TenantListComponent } from './tenant-list/tenant-list.component';

@NgModule({
  declarations: [HomeComponent, TenantListComponent, CreateTenantComponent],
  imports: [HomeRoutingModule, CommonModule, ClarityModule, FormsModule],
  entryComponents: [CreateTenantComponent],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
