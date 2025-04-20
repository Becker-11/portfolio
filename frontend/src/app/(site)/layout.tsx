// src/app/(site)/layout.tsx
import "@/app/globals.css";
import React, { ReactNode } from "react";
import NavBar from "@/components/NavBar";
import Footer from "@/components/Footer";

export default function SiteLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <title>Rowan Becker • Portfolio</title>
        {/* Add any meta tags or favicons here */}
      </head>
      <body className="min-h-screen flex flex-col bg-black text-zinc-50">
        {/* Global Header */}
        <NavBar />

        {/* Main content area */}
        <div className="flex-1 overflow-y-auto pt-14">
          {children}
        </div>

        {/* Global Footer */}
        <Footer />
      </body>
    </html>
  );
}
