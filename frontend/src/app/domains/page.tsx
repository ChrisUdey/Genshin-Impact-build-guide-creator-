'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import api from '@/lib/api';
import { Domain } from '@/types';

export default function Domains() {
    const [domains, setDomains] = useState<Domain[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const domainsPerPage = 4;
    const router = useRouter();

    useEffect(() => {
        const fetchDomains = async () => {
            try {
                const response = await api.get('/api/domains/');
                setDomains(response.data);
            } catch (error) {
                console.error('Failed to fetch domains:', error);
            } finally {
                setLoading(false);
            }
        };

        fetchDomains();
    }, []);

    // Pagination
    const indexOfLast = currentPage * domainsPerPage;
    const indexOfFirst = indexOfLast - domainsPerPage;
    const currentDomains = domains.slice(indexOfFirst, indexOfLast);
    const totalPages = Math.ceil(domains.length / domainsPerPage);

    const handlePrevPage = () => {
        setCurrentPage((prev) => Math.max(prev - 1, 1));
    };
    const handleNextPage = () => {
        setCurrentPage((prev) => Math.min(prev + 1, totalPages));
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen">
                <div className="text-xl font-bold">Loading domains...</div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100">
            <div className="container mx-auto p-8">
                <div className="bg-white rounded-3xl shadow-2xl p-8 min-h-[600px]">

                    {/* Domain Grid (2x2) */}
                    <div className="grid grid-cols-2 gap-6 mb-8">
                        {currentDomains.map((domain) => (

                            <div
                                key={domain.id}
                                onClick={() => router.push(`/domains/${domain.id}`)}
                                className="cursor-pointer border-2 border-gray-300 rounded-2xl p-6 hover:shadow-xl transition-all hover:scale-105 bg-gradient-to-br from-gray-50 to-white"
                            >

                            {/* Domain Image */}
                                <div className="flex justify-center items-center bg-gradient-to-br from-purple-200 to-blue-200 rounded-xl h-48 mb-4">
                                    <img
                                        src={`http://127.0.0.1:8000/static/nation_pics/${domain.nation}/icon.png`}
                                        className="h-48 w-48"
                                        alt="test"
                                    />

                                </div>

                                {/* Domain Name */}
                                <h3 className="font-bold text-xl mb-1 text-gray-900">
                                    {domain.name}
                                </h3>

                                {/* Domain Type */}
                                <p className="text-sm text-gray-700 italic mb-3 font-medium">
                                    {domain.type}
                                </p>

                                {/* Domain Description */}
                                <p className="text-sm text-gray-800 line-clamp-4 leading-relaxed">
                                    {domain.description}
                                </p>

                                {/* Badges */}
                                <div className="mt-4 flex justify-between items-center w-full">

                                    {/* Badges */}
                                    <div className="flex gap-2 flex-wrap">
                                    <span className="text-xs font-semibold bg-blue-500 text-white px-3 py-1 rounded-full">
                                        {domain.location}
                                    </span>
                                                                    <span className="text-xs font-semibold bg-gray-700 text-white px-3 py-1 rounded-full">
                                        {domain.nation}
                                    </span>
                                    </div>

                                    {/* Reload Button */}
                                    <button
                                        onClick={async (e) => {
                                            e.stopPropagation();
                                            try {
                                                // Remove the domain locally
                                                setDomains(prev => prev.filter(d => d.id !== domain.id));

                                                // Re-fetch the list (optional)
                                                const res = await api.get('/api/domains/');
                                                setDomains(res.data);

                                            } catch (err) {
                                                console.error("Failed to reload domain:", err);
                                            }
                                        }}
                                        className="bg-red-600 text-white text-xs font-semibold px-3 py-1 rounded-full
                                                hover:bg-red-700 transition
                                                shadow-sm
                                            ">Reload
                                    </button>
                                </div>

                            </div>

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
