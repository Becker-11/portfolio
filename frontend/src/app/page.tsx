"use client";
import React from "react";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { Card, CardHeader, CardContent, CardTitle } from "@/components/ui/card";

/**
 * Fits in a single viewport (≈ 720‑900 px tall) on laptop screens:
 *  – slimmer paddings
 *  – hero, quote, projects stacked inside a CSS grid with fixed row sizes
 *  – footer always visible
 */

const navLinks = [
  { label: "Projects", href: "#projects" },
  { label: "AI Safety Research", href: "/research" },
  { label: "Content Recommendations", href: "#recommendations" },
  { label: "Get to know me", href: "#about" },
];

const projects = [
  {
    title: "AI‑Safety Research Aggregator",
    blurb: "Aggregates the latest alignment papers and surfaces them via a sleek Next.js interface.",
    href: "/research",
  },
  {
    title: "Niobium Heat Treatments",
    blurb: "Honours thesis on niobium heat treatments for superconducting radio frequency cavities.",
    href: "/projects/niobium-heat-treatments",
  },
  {
    title: "The Consilience Report",
    blurb: "Podcast exploring the ideas put forth by The Consilience Project.",
    href: "https://www.youtube.com/@theconsiliencereport990",
  },
];

export default function HomePage() {
  return (
    <main className="min-h-screen flex flex-col bg-black text-zinc-50">
      {/* Navbar */}
      <header className="sticky top-0 z-50 backdrop-blur bg-black/70 border-b border-zinc-800 h-14">
        <div className="mx-auto max-w-6xl h-full flex items-center justify-between px-4 sm:px-6">
          <Link href="/" className="text-lg font-medium">Rowan Becker</Link>
          <nav className="hidden md:flex gap-6 text-sm">
            {navLinks.map((l) => (
              <Link key={l.label} href={l.href} className="text-zinc-300 hover:text-zinc-100">
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

      {/* Content grid: 3 rows that fit typical laptop viewport */}
      <div className="flex-1 grid grid-rows-[auto_auto_1fr] gap-12 overflow-hidden px-6">
        {/* Hero */}
        <section className="mx-auto w-full max-w-4xl text-center pt-10 sm:pt-14">
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight bg-gradient-to-r from-slate-200 to-slate-100 bg-clip-text text-transparent">
            Building reliable AI & thoughtful software.
          </h1>
          <p className="mt-3 text-zinc-400 max-w-xl mx-auto text-base lg:text-lg">
            Full‑stack engineer focused on AI‑safety tooling, TypeScript, and developer experience.
          </p>
        </section>

        {/* Quote */}
        <section>
          <div className="mx-auto max-w-2xl border border-zinc-800 rounded-lg bg-zinc-900/70 py-6 px-6 text-center">
            <blockquote className="text-base sm:text-lg italic font-light text-zinc-300">
              tsx <blockquote>&ldquo;The unexamined algorithm is not worth deploying.&rdquo;</blockquote>
            </blockquote>
          </div>
        </section>

        {/* Projects */}
        <section id="projects" className="mx-auto w-full max-w-6xl pb-8 overflow-y-auto">
          <h2 className="text-lg font-semibold mb-6">Featured Projects</h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            {projects.map((p) => (
              <Card key={p.title} className="bg-zinc-900/70 border-zinc-800 hover:shadow-md transition h-full">
                <CardHeader>
                  <CardTitle className="text-base font-medium">{p.title}</CardTitle>
                </CardHeader>
                <CardContent className="text-sm text-zinc-400 flex flex-col h-full">
                  <p className="flex-1 mb-3 leading-relaxed">{p.blurb}</p>
                  <Link
                    href={p.href}
                    target={p.href.startsWith("http") ? "_blank" : undefined}
                    className="inline-flex items-center gap-1 text-sky-400 hover:text-sky-300"
                  >
                    View project <ArrowRight className="h-4 w-4" />
                  </Link>
                </CardContent>
              </Card>
            ))}
          </div>
        </section>
      </div>

      {/* Footer */}
      <footer className="border-t border-zinc-800 bg-black py-6 text-sm text-zinc-400">
        <div className="mx-auto max-w-4xl px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex gap-4">
            <Link href="https://github.com/rowan" target="_blank" className="hover:text-zinc-50">GitHub</Link>
            <Link href="https://twitter.com/rowan" target="_blank" className="hover:text-zinc-50">Twitter</Link>
            <Link href="https://www.linkedin.com/in/rowan" target="_blank" className="hover:text-zinc-50">LinkedIn</Link>
          </div>
          <Link
            href="/Rowan_Becker_CV.pdf"
            target="_blank"
            className="rounded-full border border-zinc-700 px-4 py-1.5 hover:bg-zinc-800 hover:text-zinc-50 transition"
          >
            Résumé / CV
          </Link>
        </div>
      </footer>
    </main>
  );
}