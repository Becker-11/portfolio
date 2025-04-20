// src/components/Projects.tsx
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { Card, CardHeader, CardContent, CardTitle } from "@/components/ui/card";

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

export function Projects() {
  return (
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
  );
}