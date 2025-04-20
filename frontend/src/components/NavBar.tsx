// src/components/Navbar.tsx
"use client";

import Link from "next/link";
import { ArrowRight } from "lucide-react";

const navLinks = [
  { label: "Projects", href: "#projects" },
  { label: "AI Safety Research", href: "/research" },
  { label: "Content Recommendations", href: "#recommendations" },
  { label: "Get to know me", href: "#about" },
];

export default function Navbar() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 backdrop-blur bg-black/70 border-b border-zinc-800 h-14">
      <div className="mx-auto max-w-6xl h-full flex items-center justify-between px-4 sm:px-6">
        <Link href="/" className="text-lg font-medium">
          Rowan Becker
        </Link>
        <nav className="hidden md:flex gap-6 text-sm">
          {navLinks.map((l) => (
            <Link
              key={l.label}
              href={l.href}
              className="text-zinc-300 hover:text-zinc-100"
            >
              {l.label}
            </Link>
          ))}
        </nav>
        <Link
          href="mailto:rowan@example.com"
          className="inline-flex items-center gap-1 rounded-full border border-sky-500/40 px-4 py-1.5 text-sm text-sky-300 hover:bg-sky-500/10"
        >
          Get in touch <ArrowRight className="h-4 w-4" />
        </Link>
      </div>
    </header>
  );
}
