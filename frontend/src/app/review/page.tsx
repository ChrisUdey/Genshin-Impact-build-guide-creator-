'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { isAuthenticated } from '@/lib/auth';
import { BuildGuide } from '@/types';

export default function PendingReviewPage() {
    const router = useRouter();
    const [guides, setGuides] = useState<BuildGuide[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Check authentication and admin role
        if (!isAuthenticated()) {
            router.push('/login'); // redirect non-admins
            return;
        }

        // Fetch pending guides
        fetch('http://127.0.0.1:8000/api/guides/pending')
            .then((res) => res.json())
            .then((data) => {
                setGuides(data);
                setLoading(false);
            })
            .catch((err) => {
                console.error('Failed to fetch pending guides:', err);
                setLoading(false);
            });
    }, [router]);

    const handleApprove = async (id: number) => {
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/guides/${id}/approve`, {
                method: 'PATCH',
            });
            if (!res.ok) throw new Error('Failed to approve');
            setGuides((prev) => prev.filter((g) => g.id !== id));
        } catch (err) {
            console.error(err);
            alert('Error approving guide');
        }
    };

    const handleReject = async (id: number) => {
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/guides/${id}`, {
                method: 'DELETE',
            });
            if (!res.ok) throw new Error('Failed to delete');
            setGuides((prev) => prev.filter((g) => g.id !== id));
        } catch (err) {
            console.error(err);
            alert('Error rejecting guide');
        }
    };

    if (loading) return <div className="p-10 text-center">Loading pending guides...</div>;

    return (
        <div className="min-h-screen bg-gray-100 p-8">
            <h1 className="text-black text-3xl font-bold mb-6">Pending Build Guides</h1>
            {guides.length === 0 && <p className="text-gray-600">No pending guides at the moment.</p>}
            <div className="space-y-4">
                {guides.map((guide) => (
                    <div
                        key={guide.id}
                        className="border-2 border-gray-300 rounded-2xl p-6 hover:shadow-xl transition-all hover:scale-[1.02] bg-gradient-to-br from-gray-50 to-white"
                    >
                        <div className="flex items-center space-x-4">
                            <img
                                src={`http://127.0.0.1:8000/static/build_pics/default.jpg`}
                                alt="default"
                                className="w-16 h-16 object-cover rounded-full"
                            />
                            <div className="text-black font-semibold">{guide.username}</div>
                        </div>
                        <div>
                            <h2 className="text-black text-xl font-semibold mb-1">
                                {guide.title}
                            </h2>
                            <p className="text-gray-600">
                                Character: {guide.character_name || 'Unknown'}
                            </p>
                            <p className="text-gray-700 mt-1 line-clamp-3">{guide.description}</p>
                            {guide.picture_path && (
                                <img
                                    src={`http://127.0.0.1:8000/static/${guide.picture_path}`}
                                    alt={guide.title}
                                    className="w-full max-w-[512px] h-64 object-cover mt-3"
                                />
                            )}
                            <div className="mt-3 text-xs text-gray-400">
                                {new Date(guide.created_at).toLocaleDateString()}
                            </div>
                        </div>
                        <div className="flex gap-3">
                            <button
                                onClick={() => handleApprove(guide.id)}
                                className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600"
                            >
                                Approve
                            </button>
                            <button
                                onClick={() => handleReject(guide.id)}
                                className="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600"
                            >
                                Reject
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
