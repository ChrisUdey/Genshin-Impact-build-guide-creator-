'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { login } from '@/lib/auth';

export default function LoginPage() {
    const [email, setEmail] = useState('test@t.ca');
    const [password, setPassword] = useState('123456Pw');
    const [error, setError] = useState('');
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            await login(email, password);
            router.push('/characters');
        } catch (err) {
            setError('Invalid credentials');
        }
    };

    return (
        <main className="container mx-auto p-8 max-w-md">
            <h1 className="text-3xl font-bold mb-6">Login</h1>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block mb-2">Email</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full border p-2 rounded"
                    />
                </div>
                <div>
                    <label className="block mb-2">Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full border p-2 rounded"
                    />
                </div>
                {error && <p className="text-red-500">{error}</p>}
                <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded w-full">
                    Login
                </button>
            </form>
        </main>
    );
}