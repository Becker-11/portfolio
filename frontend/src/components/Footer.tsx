// src/components/Footer.tsx
import Link from "next/link";

export default function Footer() {
  return (
    <footer className="border-t border-zinc-800 bg-black py-6 text-sm text-zinc-400">
      <div className="mx-auto max-w-4xl px-6 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex gap-4">
          <Link href="https://github.com/rowan" target="_blank" className="hover:text-zinc-50">GitHub</Link>
          <Link href="https://twitter.com/rowan" target="_blank" className="hover:text-zinc-50">Twitter</Link>
          <Link href="https://www.linkedin.com/in/rowan" target="_blank" className="hover:text-zinc-50">LinkedIn</Link>
        </div>
        <Link
          href="/Rowan_Meronek_CV.pdf"
          target="_blank"
          rel="noopener noreferrer"
          className="rounded-full border border-zinc-700 px-4 py-1.5 hover:bg-zinc-800 hover:text-zinc-50 transition"
        >
          Résumé / CV
        </Link>
      </div>
    </footer>
  );
}