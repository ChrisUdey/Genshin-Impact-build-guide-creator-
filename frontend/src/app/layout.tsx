import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import Header from "@/components/Header";
import { GoogleOAuthProvider } from "@react-oauth/google";

const geistSans = Geist({
    variable: "--font-geist-sans",
    subsets: ["latin"],
});

const geistMono = Geist_Mono({
    variable: "--font-geist-mono",
    subsets: ["latin"],
});

export const metadata: Metadata = {
    title: "Genshin Build Guide Creator",
    description: "Create and share Genshin Impact character build guides",
};

export default function RootLayout({
                                       children,
                                   }: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
        <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <GoogleOAuthProvider clientId={process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID!}>
            <div className="flex flex-col min-h-screen">
                <Header />
                <div className="flex flex-1">
                    <Sidebar />

                    {/* Only place children HERE */}
                    <main className="flex-1">
                        {children}
                    </main>
                </div>
            </div>
        </GoogleOAuthProvider>
        </body>
        </html>
    );
}
