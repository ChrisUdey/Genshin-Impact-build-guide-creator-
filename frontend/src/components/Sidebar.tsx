'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

export default function Sidebar() {
    const pathname = usePathname();

    const isActive = (path: string) => {
        return pathname === path;
    };

    return (
        <aside className="w-32 bg-white border-r-2 border-gray-200 p-4">
            <nav className="space-y-4">
                <Link
                    href="/"
                    className={`block text-center py-3 px-4 rounded-lg font-semibold transition-colors ${
                        isActive('/')
                            ? 'bg-blue-500 text-white'
                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                >
                    Home
                </Link>

                <Link
                    href="/guides"
                    className={`block text-center py-3 px-4 rounded-lg font-semibold transition-colors ${
                        isActive('/guides')
                            ? 'bg-blue-500 text-white'
                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                >
                    Guides
                </Link>
            </nav>
        </aside>
    );
}