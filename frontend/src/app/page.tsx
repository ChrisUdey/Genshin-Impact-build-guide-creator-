'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import api from '@/lib/api';
import { Character } from '@/types';

export default function HomePage() {
    const [characters, setCharacters] = useState<Character[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const charactersPerPage = 4;
    const router = useRouter();

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

    // Calculate pagination
    const indexOfLastChar = currentPage * charactersPerPage;
    const indexOfFirstChar = indexOfLastChar - charactersPerPage;
    const currentCharacters = characters.slice(indexOfFirstChar, indexOfLastChar);
    const totalPages = Math.ceil(characters.length / charactersPerPage);

    const handlePrevPage = () => {
        setCurrentPage((prev) => Math.max(prev - 1, 1));
    };

    const handleNextPage = () => {
        setCurrentPage((prev) => Math.min(prev + 1, totalPages));
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen">
                <div className="text-xl font-bold">Loading characters...</div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100">
            {/* Main Content Area */}
            <div className="container mx-auto p-8">
                <div className="bg-white rounded-3xl shadow-2xl p-8 min-h-[600px]">
                    {/* Character Grid - 2x2 */}
                    <div className="grid grid-cols-2 gap-6 mb-8">
                        {currentCharacters.map((character) => (
                            <Link
                                key={character.id}
                                href={`/characters/${character.id}`}
                                className="border-2 border-gray-300 rounded-2xl p-6 hover:shadow-xl transition-all hover:scale-105 bg-gradient-to-br from-gray-50 to-white"
                            >
                                {/* Character Image */}
                                <div className="flex justify-center items-center bg-gradient-to-br from-purple-200 to-blue-200 rounded-xl h-48 mb-4">
                                    <img
                                        src={`https://genshin.jmp.blue/characters/${character.key}/icon-big`}
                                        alt={character.name}
                                        className="h-full object-contain"
                                    />
                                </div>

                                {/* Character Name - DARKER */}
                                <h3 className="font-bold text-xl mb-1 text-gray-900">
                                    {character.name}
                                </h3>

                                {/* Character Title - DARKER */}
                                <p className="text-sm text-gray-700 italic mb-3 font-medium">
                                    {character.title}
                                </p>

                                {/* Character Description - DARKER */}
                                <p className="text-sm text-gray-800 line-clamp-4 leading-relaxed">
                                    {character.description ||
                                        `${character.vision} character wielding a ${character.weapon}. ` +
                                        `From ${character.nation}. ${character.affiliation}.`
                                    }
                                </p>

                                {/* Stats badges */}
                                <div className="mt-4 flex gap-2 flex-wrap">
                  <span className="text-xs font-semibold bg-blue-500 text-white px-3 py-1 rounded-full">
                    {character.vision}
                  </span>
                                    <span className="text-xs font-semibold bg-gray-700 text-white px-3 py-1 rounded-full">
                    {character.weapon}
                  </span>
                                    <span className="text-sm">
                    {'⭐'.repeat(character.rarity)}
                  </span>
                                </div>
                            </Link>
                        ))}
                    </div>

                    {/* Pagination */}
                    <div className="flex justify-center items-center gap-4 mt-8">
                        <button
                            onClick={handlePrevPage}
                            disabled={currentPage === 1}
                            className="px-6 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-300 transition"
                        >
                            ← Previous
                        </button>

                        <span className="text-lg font-bold text-gray-800">
              Page {currentPage} of {totalPages}
            </span>

                        <button
                            onClick={handleNextPage}
                            disabled={currentPage === totalPages}
                            className="px-6 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed disabled:bg-gray-300 transition"
                        >
                            Next →
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}