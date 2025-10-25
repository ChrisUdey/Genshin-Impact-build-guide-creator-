'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { isAuthenticated, logout, getUser } from '@/lib/auth';

export default function Header() {
    const [mounted, setMounted] = useState(false);
    const [loggedIn, setLoggedIn] = useState(false);
    const [user, setUser] = useState<any>(null);
    const [searchQuery, setSearchQuery] = useState('');
    const router = useRouter();

    useEffect(() => {
        setMounted(true);
        setLoggedIn(isAuthenticated());
        setUser(getUser());

    }, []);

    const handleLogout = () => {
        logout();
        setLoggedIn(false);
        setUser(null);
        window.location.href = '/';
    };

    const handleSearch = (e: React.FormEvent) => {
        e.preventDefault();
        if (searchQuery.trim()) {
            router.push(`/guides?search=${searchQuery}`);
        }
    };

    // Don't show auth state until mounted (prevents hydration mismatch)
    if (!mounted) {
        return (
            <header className="bg-gradient-to-r from-cyan-400 to-blue-400 p-4 shadow-lg">
                <div className="container mx-auto flex items-center justify-between">
                    {/* App Name */}
                    <div className="text-2xl font-bold text-white px-4 py-2 bg-white/20 rounded-lg">
                        Genshin Guides
                    </div>

                    {/* Search Bar */}
                    <form onSubmit={handleSearch} className="flex-1 max-w-2xl mx-8">
                        <input
                            type="text"
                            placeholder="Search for character guides..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="w-full px-6 py-3 rounded-full bg-white border-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 shadow-md text-gray-800 placeholder-gray-500 font-medium"
                        />
                    </form>

                    {/* Placeholder for auth button (prevents layout shift) */}
                    <div className="w-24 h-10"></div>
                </div>
            </header>
        );
    }

    return (
        <header className="bg-gradient-to-r from-cyan-400 to-blue-400 p-4 shadow-lg">
            <div className="container mx-auto flex items-center justify-between">
                {/* App Name */}
                <div className="text-2xl font-bold text-white px-4 py-2 bg-white/20 rounded-lg">
                    Genshin Guides
                </div>

                {/* Search Bar */}
                <form onSubmit={handleSearch} className="flex-1 max-w-2xl mx-8">
                    <input
                        type="text"
                        placeholder="Search for character guides..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        className="w-full px-6 py-3 rounded-full bg-white border-2 border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 shadow-md text-gray-800 placeholder-gray-500 font-medium"
                    />
                </form>

                {/* Login/Logout Button */}

                <div className="flex items-center gap-3">
                    {loggedIn && user?.email === 'test@t.ca' && (
                        <button
                            onClick={() => router.push('/review')}
                            className="px-6 py-2 bg-yellow-400 text-white font-semibold rounded-lg hover:bg-yellow-500 shadow-md"
                        >
                            Review Pending
                        </button>
                    )}

                    {loggedIn ? (
                        <>
                            <span className="text-white font-semibold">{user?.email}</span>
                            <button
                                onClick={handleLogout}
                                className="px-6 py-2 bg-white text-blue-600 font-semibold rounded-lg hover:bg-gray-100 shadow-md"
                            >
                                Logout
                            </button>
                        </>
                    ) : (
                        <button
                            onClick={() => router.push('/login')}
                            className="px-6 py-2 bg-white text-blue-600 font-semibold rounded-lg hover:bg-gray-100 shadow-md"
                        >
                            Log In
                        </button>
                    )}
                </div>
            </div>
        </header>
    );
}