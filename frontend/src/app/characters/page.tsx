'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import api from '@/lib/api';
import { Character } from '@/types';

export default function CharactersPage() {
    const [characters, setCharacters] = useState<Character[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchCharacters = async () => {
            try {
                const response = await api.get('/api/characters/');
                setCharacters(response.data);
            } catch (error) {
                console.error('Failed to fetch characters:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchCharacters();
    }, []);

    if (loading) return <div className="container mx-auto p-8">Loading...</div>;

    return (
        <main className="container mx-auto p-8">
            <h1 className="text-3xl font-bold mb-6">Characters</h1>
            <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
                {characters.map((character) => (
                    <Link
                        key={character.id}
                        href={`/characters/${character.id}`}
                        className="border p-4 rounded hover:shadow-lg transition"
                    >
                        <h2 className="text-xl font-bold">{character.name}</h2>
                        <p className="text-sm text-gray-600">{character.title}</p>
                        <p className="mt-2">
                            <span className="text-xs bg-blue-100 px-2 py-1 rounded">{character.vision}</span>
                            <span className="text-xs bg-gray-100 px-2 py-1 rounded ml-2">{character.weapon}</span>
                        </p>
                    </Link>
                ))}
            </div>
        </main>
    );
}