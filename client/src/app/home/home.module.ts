import { NgModule } from '@angular/core';

import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { CommonModule } from '@angular/common';
import { ClarityModule } from '@clr/angular';
import { TenantListComponent } from './tenant-list/tenant-list.component';

@NgModule({
  declarations: [HomeComponent, TenantListComponent],
  imports: [HomeRoutingModule, CommonModule, ClarityModule],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
