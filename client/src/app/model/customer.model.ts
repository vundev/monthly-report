export interface CustomerCredentials {
  username: string;
  password: string;
}

export interface CustomerMe {
  customerName: string;
}

export interface Token {
  access_token: string;
  token_type: string;
}
