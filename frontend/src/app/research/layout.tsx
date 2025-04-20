// frontend/src/app/research/layout.tsx
import "../globals.css";
import React from "react"
import Link from "next/link";

export default function ResearchLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50 text-gray-900">
        <header className="w-full border-b border-gray-200 bg-white p-6 shadow-sm">
          <div className="mx-auto max-w-6xl flex justify-between items-center">
            <h1 className="text-2xl font-bold text-indigo-600">AI Safety Research</h1>
            <Link href="/" className="text-blue-500 hover:underline">Back to portfolio</Link>
          </div>
        </header>

        <main className="max-w-6xl mx-auto p-6">{children}</main>

        {/* Optional: add a small footer or leave it clean */}
      </body>
    </html>
  );
}
