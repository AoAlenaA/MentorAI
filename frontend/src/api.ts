const API_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000';

export interface LoginPayload {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: 'bearer';
  user: {
    id: number;
    email: string;
    name: string;
    role: string;
  };
}

export async function login(payload: LoginPayload): Promise<LoginResponse> {
  const response = await fetch(`${API_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Ошибка авторизации' }));
    throw new Error(error.detail ?? 'Ошибка авторизации');
  }

  return response.json();
}
