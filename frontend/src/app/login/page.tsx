'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { login } from '@/lib/auth';

export default function LoginPage() {
    const [email, setEmail] = useState('test@t.ca');
    const [password, setPassword] = useState('123456Pw');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const router = useRouter();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            await login(email, password);
            // Redirect to HOME page after successful login
            window.location.href = '/';
        } catch (err: any) {
            console.error('Login error:', err);
            // Set error message
            const errorMessage = err.response?.data?.detail || err.message || 'Invalid credentials';
            setError(errorMessage);
            // Don't redirect on error - stay on login page
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="container mx-auto p-8 max-w-md">
            <div className="bg-white p-8 rounded-lg shadow-lg">
                <h1 className=" text-black text-3xl font-bold mb-6">Login</h1>

                <form onSubmit={handleSubmit} className="space-y-4">
                    <div>
                        <label className="text-black block mb-2 font-semibold">Email</label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                            required
                        />
                    </div>

                    <div>
                        <label className="text-black block mb-2 font-semibold">Password</label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                            required
                        />
                    </div>

                    {error && (
                        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
                            {error}
                        </div>
                    )}

                    <button
                        type="submit"
                        disabled={loading}
                        className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-3 rounded w-full font-semibold disabled:bg-gray-400"
                    >
                        {loading ? 'Logging in...' : 'Login'}
                    </button>
                </form>

                <div className="mt-4 p-4 bg-gray-100 rounded">
                    <p className=" text-black text-sm font-semibold mb-2">Test Credentials:</p>
                    <p className="text-black text-sm">Email: test@t.ca</p>
                    <p className="text-black text-sm">Password: 123456Pw</p>
                </div>
            </div>
        </main>
    );
}