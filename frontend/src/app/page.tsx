import Link from 'next/link';

export default function Home() {
  return (
      <main className="container mx-auto p-8">
        <h1 className="text-4xl font-bold mb-4">Genshin Build Guide Creator</h1>
        <p className="mb-4">Create and share character build guides</p>
        <div className="space-x-4">
          <Link href="/characters" className="bg-blue-500 text-white px-4 py-2 rounded">
            Browse Characters
          </Link>
          <Link href="/login" className="bg-green-500 text-white px-4 py-2 rounded">
            Login
          </Link>
        </div>
      </main>
  );
}