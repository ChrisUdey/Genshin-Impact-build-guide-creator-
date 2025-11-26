'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { login } from '@/lib/auth';
import { GoogleLogin } from '@react-oauth/google';
import api from '@/lib/api';

export default function LoginPage() {
    const [email, setEmail] = useState('test@t.ca');
    const [reEmail, setReEmail] = useState('');
    const [password, setPassword] = useState('123456Pw');
    const [rePassword, setRePassword] = useState('');
    const [username, setUsername] = useState('');
    const [isRegistering, setIsRegistering] = useState(false);

    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const router = useRouter();

    // ---------------------- LOGIN ----------------------
    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');
        setLoading(true);

        try {
            await login(email, password);
            window.location.href = '/';
        } catch (err: any) {
            const message = err.response?.data?.detail || 'Invalid credentials';
            setError(message);
        } finally {
            setLoading(false);
        }
    };

    // ------------------- VALIDATION --------------------
    const validateRegistration = () => {
        // Username validation
        if (username.length < 4) return "Username must be at least 5 characters long";
        // Email format validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) return "Invalid email format.";
        if (email !== reEmail) return "Emails do not match.";

        // Password validation
        if (password.length < 5) return "Password must be at least 5 characters long.";
        const special = /[!@#$%^&]/;
        if (!special.test(password)) return "Password must include at least one special character (!@#$%^&).";
        if (password !== rePassword) return "Passwords do not match.";

        return null; // No errors
    };

    // ---------------- REGISTER -------------------------
    const handleRegister = async (e: React.FormEvent) => {
        e.preventDefault();
        setError('');

        const validationError = validateRegistration();
        if (validationError) {
            setError(validationError);
            return;
        }

        // BACKEND NOT IMPLEMENTED YET
        alert("Registration backend not implemented yet.\n\nValidated successfully!");
    };

    return (
        <main className="container mx-auto p-8 max-w-md">
            <div className="bg-white p-8 rounded-lg shadow-lg">
                <h1 className="text-black text-3xl font-bold mb-6">
                    {isRegistering ? "Create Account" : "Login"}
                </h1>

                {/* ------------------- LOGIN FORM ------------------- */}
                {!isRegistering && (
                    <form onSubmit={handleLogin} className="space-y-4">
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

                        <p className="text-center text-black mt-4">
                            Dont have an account?{" "}
                            <button
                                type="button"
                                className="text-blue-600 underline"
                                onClick={() => setIsRegistering(true)}
                            >
                                Create Account
                            </button>
                        </p>

                        <div className="mt-6">
                            <GoogleLogin
                                onSuccess={async (response) => {
                                    try {
                                        const idToken = response.credential;

                                        const res = await api.post("/api/auth/google", {
                                            token: idToken
                                        });

                                        localStorage.setItem("access_token", res.data.access_token);
                                        window.location.href = "/";
                                    } catch (err) {
                                        console.error("Google login failed:", err);
                                    }
                                }}
                                onError={() => {
                                    console.log("Google Login Failed");
                                }}
                            />
                        </div>
                    </form>
                )}

                {/* ------------------- REGISTER FORM ------------------- */}
                {isRegistering && (
                    <form onSubmit={handleRegister} className="space-y-4">

                        {/* USERNAME */}
                        <div>
                            <label className="text-black block mb-2 font-semibold">Username</label>
                            <input
                                type="text"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                                required
                            />
                            <div className="text-right text-sm text-gray-500">
                                Username must be at least 5 characters long.
                            </div>
                        </div>

                        {/* EMAIL */}
                        <div>
                            <label className="text-black block mb-2 font-semibold">Email</label>
                            <input
                                type="email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                                required
                            />
                            <div className="text-right text-sm text-gray-500">
                                Email must be in the nnn@nn.nn format
                            </div>
                        </div>

                        {/* RE-EMAIL */}
                        <div>
                            <label className="text-black block mb-2 font-semibold">Re-enter Email</label>
                            <input
                                type="email"
                                value={reEmail}
                                onChange={(e) => setReEmail(e.target.value)}
                                className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                                required
                            />
                        </div>

                        {/* PASSWORD */}
                        <div>
                            <label className="text-black block mb-2 font-semibold">Password</label>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                                required
                            />
                            <div className="text-right text-sm text-gray-500">
                                Must include at least one (!@#$%^&)
                            </div>
                        </div>

                        {/* RE-PASSWORD */}
                        <div>
                            <label className="text-black block mb-2 font-semibold">Re-enter Password</label>
                            <input
                                type="password"
                                value={rePassword}
                                onChange={(e) => setRePassword(e.target.value)}
                                className="w-full border border-gray-300 p-3 rounded bg-white text-gray-900"
                                required
                            />
                        </div>

                        {/* ERRORS */}
                        {error && (
                            <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
                                {error}
                            </div>
                        )}

                        {/* REGISTER BUTTON */}
                        <button
                            type="submit"
                            className="bg-green-500 hover:bg-green-600 text-white px-4 py-3 rounded w-full font-semibold"
                        >
                            Create Account
                        </button>

                        {/* Back to login */}
                        <p className="text-center text-black mt-4">
                            Already have an account?{" "}
                            <button
                                type="button"
                                className="text-blue-600 underline"
                                onClick={() => setIsRegistering(false)}
                            >
                                Login
                            </button>
                        </p>
                    </form>
                )}

                {!isRegistering && (
                    <div className="mt-4 p-4 bg-gray-100 rounded">
                        <p className="text-black text-sm font-semibold mb-2">Test Credentials:</p>
                        <p className="text-black text-sm">Email: test@t.ca</p>
                        <p className="text-black text-sm">Password: 123456Pw</p>
                    </div>
                )}
            </div>
        </main>
    );
}
