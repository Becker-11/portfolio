// src/components/Hero.tsx
export default function Hero() {
    return (
      <section className="mx-auto w-full max-w-4xl text-center pt-10 sm:pt-14">
        <h1 className="text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight bg-gradient-to-r from-slate-200 to-slate-100 bg-clip-text text-transparent">
          Curious about how the world works — and how we make it better.
        </h1>
        <p className="mt-3 text-zinc-400 max-w-xl mx-auto text-base lg:text-lg">
          I studied physics, computer science, and math to get a clearer view of reality.
          Now exploring Physics and AI safety research.
        </p>
      </section>
    );
  }
  