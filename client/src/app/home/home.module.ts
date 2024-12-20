import { NgModule } from '@angular/core';

import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ClarityModule } from '@clr/angular';
import { CreateTenantModalComponent } from './create-tenant-modal/create-tenant-modal.component';
import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';
import { TenantListComponent } from './tenant-list/tenant-list.component';
import { AvailabilityModalComponent } from './availability-modal/availability-modal.component';
import { TenantSlaComponent } from './tenant-sla/tenant-sla.component';
import { AvailabilityLevelPipe } from './tenant-sla/availability-level.pipe';

const modals = [CreateTenantModalComponent, AvailabilityModalComponent];
const components = [HomeComponent, TenantListComponent, TenantSlaComponent];
const pipes = [AvailabilityLevelPipe];

@NgModule({
  declarations: [...components, ...modals, ...pipes],
  imports: [HomeRoutingModule, CommonModule, ClarityModule, FormsModule],
  entryComponents: [...modals],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
