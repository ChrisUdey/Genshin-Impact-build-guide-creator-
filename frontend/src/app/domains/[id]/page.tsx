'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import api from '@/lib/api';
import { Domain, Artifact } from '@/types';

export default function DomainPage() {
    const params = useParams();
    const id = params.id;

    const [domain, setDomain] = useState<Domain | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchDomain = async () => {
            try {
                const res = await api.get(`/api/domains/${id}`);
                setDomain(res.data);
            } catch (err) {
                console.error('Failed to fetch domain:', err);
            } finally {
                setLoading(false);
            }
        };

        fetchDomain();
    }, [id]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-screen">
                <div className="text-xl font-bold">Loading domain...</div>
            </div>
        );
    }

    if (!domain) {
        return <div className="p-10">Domain not found.</div>;
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100 p-10">
            <div className="bg-white p-10 rounded-3xl shadow-2xl max-w-6xl mx-auto">

                {/* Title Row */}
                <div className="flex justify-between items-start mb-10">
                    <h1 className="text-4xl font-bold text-gray-900">{domain.name}</h1>
                    <h2 className="text-2xl font-bold text-gray-800">Domain Artifacts</h2>
                </div>

                <div className="grid grid-cols-2 gap-10">

                    {/* LEFT — Domain Info */}
                    <div>
                        <div className="bg-gray-200 border rounded-xl h-60 flex justify-center items-center mb-6">
                            <img
                                src={`http://127.0.0.1:8000/static/nation_pics/${domain.nation}/icon.png`}
                                className="h-48 w-48"
                                alt="test"
                            />
                        </div>

                        <p><strong>Location:</strong> {domain.location}</p>
                        <p><strong>Nation:</strong> {domain.nation}</p>

                        <p className="mt-4 text-gray-800 leading-relaxed">
                            {domain.description}
                        </p>
                    </div>

                    {/* RIGHT — Artifacts */}
                    <div className="space-y-6">
                        {domain.artifacts.map((da) => (
                            <div key={da.artifact.id} className="border rounded-xl p-4 shadow bg-gray-50">
                                <div className="flex gap-4">
                                    <img
                                        src={`http://127.0.0.1:8000/static/artifacts/${da.artifact.id}.png`}
                                        className="h-20 w-20"
                                    />

                                    <div>
                                        <h3 className="text-xl font-bold">{da.artifact.name}</h3>
                                        <p><strong>2-Set:</strong> {da.artifact.two_set_bonus}</p>
                                        <p><strong>4-Set:</strong> {da.artifact.four_set_bonus}</p>
                                        <p><strong>Rarity:</strong> ⭐{da.artifact.max_rarity}</p>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>

                </div>
            </div>
        </div>
    );
}
