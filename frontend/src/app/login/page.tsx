tsx
import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import LoginForm from '@/components/LoginForm';

export default function LoginPage() {
  const [isLoggingIn, setIsLoggingIn] = useState(false);
  const [loginError, setLoginError] = useState<string | null>(null);
  const router = useRouter();

  const handleLogin = async (email: string, password: string) => {
    setIsLoggingIn(true);
    setLoginError(null);
    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        setLoginError(errorData.message || 'Login failed');
        return;
      }

      const data = await response.json();
      localStorage.setItem('jwt', data.token);
      router.push('/');
    } catch (error) {
      setLoginError('An unexpected error occurred');
    } finally {
      setIsLoggingIn(false);
    }
  };

  return (
    <div>
      <LoginForm onLogin={handleLogin} isLoading={isLoggingIn} />
      {loginError && <p style={{ color: 'red' }}>{loginError}</p>}
    </div>
  );
}