export function extractErrorMessage(error: any): string | undefined {
  return error.error?.detail || error.message || 'unknown error';
}
