import { NgModule } from '@angular/core';

import { HomeComponent } from './home.component';
import { HomeRoutingModule } from './home-routing.module';
import { CommonModule } from '@angular/common';
import { ClarityModule } from '@clr/angular';

@NgModule({
  declarations: [HomeComponent],
  imports: [HomeRoutingModule, CommonModule, ClarityModule],
  providers: [],
  bootstrap: [HomeComponent],
})
export class HomeModule {}
