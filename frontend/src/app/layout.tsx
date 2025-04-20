import "./globals.css";
import React, { ReactNode } from "react";

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <title>Rowan Becker • Portfolio</title>
        {/* meta / favicon */}
      </head>

      {/* 1) full‑height flex column keeps footer at bottom
          2) bg‑black guarantees no white flash anywhere */}
      <body className="min-h-screen flex flex-col bg-black text-zinc-50">

        {/* ----- global nav, banner, etc. could go here ----- */}

        {/* 3) this wrapper gets the scrolling, not <body> */}
        <div className="flex-1 overflow-y-auto">
          {children}
        </div>

        {/* ----- global footer can live here, if desired ----- */}
      </body>
    </html>
  );
}
