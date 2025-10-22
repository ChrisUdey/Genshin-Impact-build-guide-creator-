"use client";

import { useEffect, useState } from "react";
import {BuildGuide, Character} from "@/types";

export default function BuildGuides() {
    const [guides, setGuides] = useState<BuildGuide[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const guidesPerPage = 4;

    const [characters, setCharacters] = useState<Character[]>([]);

    useEffect(() => {
        fetch("/api/characters")
            .then(res => res.json())
            .then(setCharacters);
    }, []);

    const getCharacter = (id: number) =>
        characters.find(c => c.id === id);

    guides.map(guide => {
        const character = getCharacter(guide.character_id);
        return (
            <div key={guide.id}>
                <h2>{character?.name || "Unknown Character"}</h2>
                <p>{guide.title}</p>
            </div>
        );
    });

    useEffect(() => {
        fetch("http://127.0.0.1:8000/api/guides")
            .then((res) => res.json())
            .then((data) => {
                console.log("Guides from backend:", data);
                setGuides(Array.isArray(data) ? data : []);
                setLoading(false);
            })
            .catch((err) => {
                console.error(err);
                setGuides([]);
                setLoading(false);
            });
    }, []);


    if (loading) return <div className="p-10 text-center">Loading...</div>;
    if (guides.length === 0) return <div className="p-10 text-center">No build guides available.</div>;

    // Pagination calculation
    const indexOfLast = currentPage * guidesPerPage;
    const indexOfFirst = indexOfLast - guidesPerPage;
    const currentGuides = guides.slice(indexOfFirst, indexOfLast);
    const totalPages = Math.ceil(guides.length / guidesPerPage);

    return (
        <div className="min-h-screen bg-gray-100 py-10">
            <div className="max-w-3xl mx-auto px-4">
                <h1 className="text-3xl font-bold mb-8 text-center">Genshin Build Guides</h1>

                <div className="flex flex-col gap-6">
                    {currentGuides.map((guide) => (
                        <div
                            key={guide.id}
                            className="bg-white rounded-2xl shadow hover:shadow-lg transition duration-200 overflow-hidden flex"
                        >
                            <img
                                src={`http://127.0.0.1:8000/static/${guide.picture_path}`}
                                alt={guide.title}
                                className="w-64 h-64 object-cover"
                            />


                            {/* Text content */}
                            <div className="p-5 flex-1">
                                <h2 className="text-xl font-semibold mb-1">{guide.title}</h2>
                                <p className="text-sm text-gray-500 mb-2">
                                    Character: {guide.character?.name ?? "Unknown"}
                                </p>
                                <p className="text-gray-700 text-sm leading-snug line-clamp-4">
                                    {guide.description}
                                </p>
                                <div className="mt-3 text-xs text-gray-400">
                                    {new Date(guide.created_at).toLocaleDateString()}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>

            </div>
        </div>
    );
}