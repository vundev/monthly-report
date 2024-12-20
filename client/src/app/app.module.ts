import { InjectionToken, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ClarityModule } from '@clr/angular';
import { FormsModule } from '@angular/forms';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './login/login.component';
import { BearerInterceptor } from './interceptors/bearer.interceptor';
import { ModalWrapperComponent } from './modal/modal-wrapper.component';
import { Subject } from 'rxjs';

export const REFRESH_TRIGGER = new InjectionToken<Subject<void>>(
  'REFRESH_TRIGGER'
);

@NgModule({
  declarations: [AppComponent, LoginComponent, ModalWrapperComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserModule,
    BrowserAnimationsModule,
    ClarityModule,
    FormsModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: BearerInterceptor,
      multi: true,
    },
    {
      provide: REFRESH_TRIGGER,
      useValue: new Subject<void>(),
    },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
