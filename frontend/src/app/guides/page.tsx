"use client";

import { useEffect, useState } from "react";
import { BuildGuide, Character } from "@/types";

export default function BuildGuides() {
    const [guides, setGuides] = useState<BuildGuide[]>([]);
    const [characters, setCharacters] = useState<Character[]>([]);
    const [loading, setLoading] = useState(true);
    const [currentPage, setCurrentPage] = useState(1);
    const guidesPerPage = 4;

    // New post state
    const [newGuide, setNewGuide] = useState({
        username: "",
        character_name: "",
        title: "",
        description: "",
        picture: null as File | null,
    });

    // Fetch characters and guides
    useEffect(() => {
        Promise.all([
            fetch("http://127.0.0.1:8000/api/characters").then((r) => r.json()),
            fetch("http://127.0.0.1:8000/api/guides").then((r) => r.json()),
        ])
            .then(([chars, gds]) => {
                setCharacters(chars);
                const sortedGuides = gds.sort((a: BuildGuide, b: BuildGuide) => b.id - a.id);
                setGuides(sortedGuides);
                setLoading(false);
            })
            .catch((err) => {
                console.error("Error loading data:", err);
                setLoading(false);
            });
    }, []);

    const getCharacter = (id: number | string) =>
        characters.find((c) => String(c.id) === String(id));

    // Pagination
    const indexOfLast = currentPage * guidesPerPage;
    const indexOfFirst = indexOfLast - guidesPerPage;
    const currentGuides = guides.slice(indexOfFirst, indexOfLast);
    const totalPages = Math.ceil(guides.length / guidesPerPage);
    const handlePrevPage = () => setCurrentPage((p) => Math.max(p - 1, 1));
    const handleNextPage = () => setCurrentPage((p) => Math.min(p + 1, totalPages));

    //Handle new guide form input
    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setNewGuide((prev) => ({ ...prev, [name]: value }));
    };

    //  Handle file upload (block .webp)
    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (!file) return;

        if (file.type === "image/webp") {
            alert("WebP images are not supported. Please upload PNG, JPG, or JPEG.");
            e.target.value = "";
            return;
        }

        setNewGuide((prev) => ({ ...prev, picture: file }));
    };

    //  Submit new guide
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!newGuide.username || !newGuide.character_name || !newGuide.title || !newGuide.description) {
            alert("Please fill in all fields.");
            return;
        }

        try {
            const formData = new FormData();
            formData.append("username", newGuide.username);
            formData.append("character_name", newGuide.character_name);
            formData.append("title", newGuide.title);
            formData.append("description", newGuide.description);
            if (newGuide.picture) formData.append("picture", newGuide.picture);

            const res = await fetch("http://127.0.0.1:8000/api/guides/", {
                method: "POST",
                body: formData,
            });

            if (!res.ok) {
                const text = await res.text();
                console.error("Create failed:", res.status, text);
                alert(`Failed to submit: ${res.status}`);
                return;
            }

            alert("Submitted for approval");
        } catch (err) {
            console.error("Network error:", err);
            alert("Failed to reach the server. Is backend running?");
        }
    };


    if (loading) return <div className="p-10 text-center">Loading...</div>;

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-100 to-blue-100">
            <div className="container mx-auto p-8">

                {/* Add New Guide Section */}
                {/* Existing Guides Section */}
                <div className="bg-white rounded-3xl shadow-2xl p-8">
                    <div className="border-2 border-gray-300 rounded-2xl p-6 hover:shadow-xl bg-gradient-to-br from-gray-50 to-white">
                        <h2 className="text-2xl font-bold mb-6 text-gray-900">Create a New Build Guide</h2>
                        <form onSubmit={handleSubmit} className="space-y-5 text-gray-900">

                            {/* Top row: username, character, title */}
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                <div>
                                    <label className="block text-sm font-semibold mb-1">Username</label>
                                    <input
                                        type="text"
                                        name="username"
                                        minLength={4}
                                        maxLength={20}
                                        placeholder="Your Username"
                                        value={newGuide.username}
                                        onChange={handleChange}
                                        className="w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 text-gray-900"
                                        required
                                    />
                                    <div className="text-right text-sm text-gray-500">
                                        must be 4-20 characters
                                    </div>
                                </div>

                                <div>
                                    <label className="block text-sm font-semibold mb-1">Character</label>
                                    <select
                                        name="character_name"
                                        value={newGuide.character_name}
                                        aria-valuemin={1}
                                        onChange={handleChange}
                                        className="w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 text-gray-900"
                                        required
                                    >
                                        <option disabled={true} value="">Select Character</option>
                                        {characters.map((char) => (
                                            <option key={char.id} value={char.name}>
                                                {char.name}
                                            </option>
                                        ))}
                                    </select>
                                </div>

                                <div>
                                    <label className="block text-sm font-semibold mb-1">Build Title</label>
                                    <input
                                        type="text"
                                        name="title"
                                        minLength={4}
                                        maxLength={20}
                                        placeholder="Build Title"
                                        value={newGuide.title}
                                        onChange={handleChange}
                                        className="w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 text-gray-900"
                                        required
                                    />
                                    <div className="text-right text-sm text-gray-500">
                                        must be 4-30 characters
                                    </div>
                                </div>
                            </div>

                            {/* Description */}
                            <div>
                                <label className="block text-sm font-semibold mb-1 text-gray-900">Description</label>
                                <textarea
                                    name="description"
                                    placeholder="Write a description (10-350 characters)..."
                                    value={newGuide.description}
                                    onChange={handleChange}
                                    minLength={10}
                                    maxLength={350}
                                    className="w-full p-3 border border-gray-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400 text-gray-900 h-24 resize-none"
                                    required
                                />
                                <div className="text-right text-sm text-gray-500">
                                    {newGuide.description.length}/350
                                </div>
                            </div>

                            {/* Picture upload */}
                            <div>
                                <label className="block text-sm font-semibold mb-1">Upload Picture</label>
                                <input
                                    type="file"
                                    accept="image/*"
                                    onChange={handleFileChange}
                                    className="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
                                />
                                <p className="text-xs text-gray-500 mt-1">Supported formats: PNG, JPG, JPEG</p>
                            </div>

                            {/* Submit button */}
                            <button
                                type="submit"
                                className="px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition"
                            >
                                Post Guide
                            </button>
                        </form>
                    </div>
                    <div className="flex flex-col gap-6">
                        {currentGuides.map((guide) => {
                            const character = getCharacter(guide.character_id);
                            return (
                                <div
                                    key={guide.id}
                                    className="border-2 border-gray-300 rounded-2xl p-6 hover:shadow-xl transition-all hover:scale-[1.02] bg-gradient-to-br from-gray-50 to-white"
                                >
                                    {/* User Picture */}
                                    <div className="flex items-center space-x-4">
                                        <img
                                            src={`http://127.0.0.1:8000/static/build_pics/default.jpg`}
                                            alt="default"
                                            className="w-16 h-16 object-cover rounded-full"
                                        />
                                        <div className="text-black font-semibold">{guide.username}</div>
                                    </div>

                                    <div className="p-5 flex-1">
                                        <h2 className="text-black text-xl font-semibold mb-1">
                                            {guide.title}
                                        </h2>
                                        <p className="text-sm text-gray-500 mb-2">
                                            Character: {character?.name || guide.character_name || "Unknown Character"}
                                        </p>
                                        <p className="text-gray-700 text-sm leading-snug line-clamp-4">
                                            {guide.description}
                                        </p>

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
                                </div>
                            );
                        })}
                    </div>

                    {/* Pagination */}
                    <div className="flex justify-center items-center gap-4 mt-8">
                        <button
                            onClick={handlePrevPage}
                            disabled={currentPage === 1}
                            className="px-6 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 disabled:opacity-50"
                        >
                            ← Previous
                        </button>

                        <span className="text-lg font-bold text-gray-800">
              Page {currentPage} of {totalPages}
            </span>

                        <button
                            onClick={handleNextPage}
                            disabled={currentPage === totalPages}
                            className="px-6 py-3 bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 disabled:opacity-50"
                        >
                            Next →
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}
