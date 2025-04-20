// frontend/src/app/(site)/recommendations/page.tsx
export default function RecommendationsPage() {
    return (
      <div className="max-w-3xl mx-auto p-6 space-y-10">
        <h1 className="text-3xl font-bold text-zinc-100">Content Recommendations</h1>
  
        {/* Book Recommendations */}
        <section>
          <h2 className="text-xl font-semibold text-zinc-200 mb-3">📚 Books</h2>
          <ul className="space-y-2 text-zinc-400 list-disc list-inside">
            <li>
              <span className="text-zinc-100 font-medium">Gödel, Escher, Bach</span> — Douglas Hofstadter
            </li>
            <li>
              <span className="text-zinc-100 font-medium">The Alignment Problem</span> — Brian Christian
            </li>
            <li>
              <span className="text-zinc-100 font-medium">Surely You’re Joking, Mr. Feynman!</span> — Richard Feynman
            </li>
            <li>
              <span className="text-zinc-100 font-medium">The Beginning of Infinity</span> — David Deutsch
            </li>
          </ul>
        </section>
  
        {/* Podcast Recommendations */}
        <section>
          <h2 className="text-xl font-semibold text-zinc-200 mb-3">🎙️ Podcasts</h2>
          <ul className="space-y-2 text-zinc-400 list-disc list-inside">
            <li>
              <span className="text-zinc-100 font-medium">The 80,000 Hours Podcast</span> — long-form interviews on impactful careers
            </li>
            <li>
              <span className="text-zinc-100 font-medium">AXRP</span> — the AI X-risk Research Podcast
            </li>
            <li>
              <span className="text-zinc-100 font-medium">The Lunar Society</span> — deep dives into science, tech, and philosophy
            </li>
            <li>
              <span className="text-zinc-100 font-medium">EconTalk</span> — conversations on economics, ideas, and moral frameworks
            </li>
          </ul>
        </section>
  
        {/* Future Expansion */}
        <section className="pt-2 text-sm text-zinc-500 italic">
          More coming soon — including articles, videos, and tools.
        </section>
      </div>
    );
  }
  