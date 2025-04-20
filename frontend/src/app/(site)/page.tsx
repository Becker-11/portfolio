// src/app/page.tsx
"use client";

import Hero from "@/components/Hero";
import { Quote } from "@/components/Quote";
import { Projects } from "@/components/Projects";

export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col bg-black text-zinc-50 pt-14">
      <div className="flex-1 grid grid-rows-[auto_auto_1fr] gap-12 overflow-auto px-6">
        <Hero />
        <Quote />
        <Projects />
      </div>
    </main>
  );
}
