export interface CustomerCredentials {
  username: string;
  password: string;
}

export interface CustomerMe {
  customerName: string;
}

export interface Token {
  accessToken: string;
  tokenType: string;
}
