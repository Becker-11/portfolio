// frontend/src/app/page.tsx

import Link from 'next/link';

export default function HomePage() {
  return (
    <main
      className="
        flex flex-col items-center justify-center
        min-h-screen p-8
        bg-gradient-to-r from-indigo-600 to-blue-500
        text-white
      "
    >
      <h1 className="text-5xl font-bold mb-4">Rowan Becker</h1>
      <p className="text-lg max-w-2xl text-center mb-6">
        Software engineer &amp; AI Safety researcher building tools to track the
        latest advances in AI alignment.
      </p>
      <Link
        href="/research"
        className="
          px-6 py-3
          bg-white text-indigo-700
          rounded-lg font-semibold
        "
      >
        View AI Safety Research
      </Link>
    </main>
  );
}
