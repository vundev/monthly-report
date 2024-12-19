import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { CustomerCredentials, Token } from '../model/customer.model';
import { CookieService } from 'ngx-cookie-service';

@Injectable({ providedIn: 'root' })
export class AuthenticationService {
  private readonly accessTokenCookieName = 'access-token';

  private readonly storeAccessToken = (token: Token) =>
    this.cookieService.set(
      this.accessTokenCookieName,
      token.access_token,
      1,
      undefined,
      undefined,
      true,
      'Strict'
    );

  constructor(private http: HttpClient, private cookieService: CookieService) {}

  register$(credentials: CustomerCredentials): Observable<Token> {
    return this.http
      .post<Token>('/api/customer/register', credentials)
      .pipe(tap(this.storeAccessToken));
  }

  login$(credentials: CustomerCredentials): Observable<Token> {
    // By oauth2 policy credentials names must be username & password.
    const body = new HttpParams()
      .set('username', credentials.username)
      .set('password', credentials.password);

    const headers = new HttpHeaders().set(
      'Content-Type',
      'application/x-www-form-urlencoded'
    );

    return this.http
      .post<Token>('/api/customer/access-token', body, {
        headers,
      })
      .pipe(tap(this.storeAccessToken));
  }

  logout() {
    this.cookieService.delete(this.accessTokenCookieName);
  }

  isAuthenticated(): boolean {
    return !!this.getAccessToken();
  }

  getAccessToken(): string {
    return this.cookieService.get(this.accessTokenCookieName);
  }
}
