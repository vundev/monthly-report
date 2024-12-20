import { NgModule } from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from '@clr/angular';
import { CreateTenantModalComponent } from './create-tenant-modal/create-tenant-modal.component';
import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';
import { TenantListComponent } from './tenant-list/tenant-list.component';
import { AvailabilityModalComponent } from './availability-modal/availability-modal.component';

const modals = [CreateTenantModalComponent, AvailabilityModalComponent];

@NgModule({
  declarations: [HomeComponent, TenantListComponent, ...modals],
  imports: [HomeRoutingModule, CommonModule, ClarityModule, FormsModule],
  entryComponents: [...modals],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
