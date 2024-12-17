import { Component } from '@angular/core';
import { CustomerCredentials, Token } from '../model/customer.model';
import { AuthenticationService } from '../services/authentication.service';
import { Observable, switchMap } from 'rxjs';
import { Router } from '@angular/router';
import { extractErrorMessage } from '../global';

@Component({
  selector: 'login',
  templateUrl: 'login.component.html',
  styleUrls: ['login.component.sass'],
})
export class LoginComponent {
  credentials: CustomerCredentials = {
    username: '',
    password: '',
  };

  isRegisterPath = false;
  errorMessage?: string;

  constructor(
    private authenticationService: AuthenticationService,
    private router: Router
  ) {}

  submit() {
    this.aunthenticate$().subscribe(
      () => this.gotoHomePage(),
      (error) => (this.errorMessage = extractErrorMessage(error))
    );
  }

  changeAuthenticationPath() {
    this.isRegisterPath = !this.isRegisterPath;
  }

  private aunthenticate$(): Observable<Token> {
    if (this.isRegisterPath) {
      return this.authenticationService.register$(this.credentials);
    } else {
      return this.authenticationService.login$(this.credentials);
    }
  }

  private gotoHomePage() {
    this.router.navigate(['home']);
  }
}
