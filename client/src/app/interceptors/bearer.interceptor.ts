import {
    HttpHandler,
    HttpInterceptor,
    HttpRequest,
} from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthenticationService } from '../services/authentication.service';

@Injectable()
export class BearerInterceptor implements HttpInterceptor {
  private readonly authenticationEndpoints = [
    'api/customer/access-token',
    'api/customer/register',
  ];

  constructor(private authenticationService: AuthenticationService) {}

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<any> {
    const token = this.authenticationService.getAccessToken();

    if (token && !this.isAuthenticationRequest(request.url)) {
      const clonedRequest = request.clone({
        setHeaders: {
          Authorization: `Bearer ${token}`,
        },
      });
      return next.handle(clonedRequest);
    }

    return next.handle(request);
  }

  private isAuthenticationRequest(url: string): boolean {
    return this.authenticationEndpoints.includes(url);
  }
}
