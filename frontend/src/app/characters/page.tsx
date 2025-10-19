'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function CharactersPage() {
    const router = useRouter();

    useEffect(() => {
        // Redirect to home page
        router.push('/');
    }, [router]);

    return (
        <div className="flex items-center justify-center min-h-screen">
            <div className="text-xl">Redirecting to home...</div>
        </div>
    );
}