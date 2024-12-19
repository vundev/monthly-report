export function extractErrorMessage(error: any): string | undefined {
  const unknownErrorMessage = 'unknown error';
  if (Array.isArray(error.error?.detail)) {
    return (
      error.error?.detail
        .map((detailedError: any) => detailedError.msg)
        .filter((errorMessage: string) => !!errorMessage)
        .join('\n') || unknownErrorMessage
    );
  }
  return error.error?.detail || error.message || unknownErrorMessage;
}
