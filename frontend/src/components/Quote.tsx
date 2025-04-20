// src/components/Quote.tsx
export function Quote() {
    return (
      <section>
        <div className="mx-auto max-w-2xl border border-zinc-800 rounded-lg bg-zinc-900/70 py-6 px-6 text-center">
          <blockquote className="text-base sm:text-lg italic font-light text-zinc-300 space-y-4">
            <p>Some say the world will end in fire,</p>
            <p>Some say in ice.</p>
            <p>From what I’ve tasted of desire</p>
            <p>I hold with those who favor fire.</p>
            <p>But if it had to perish twice,</p>
            <p>I think I know enough of hate</p>
            <p>To say that for destruction ice</p>
            <p>Is also great</p>
            <p>And would suffice.</p>
            <footer className="mt-4 text-sm not-italic text-zinc-500">
              — Robert Frost, <cite>“Fire and Ice”</cite>
            </footer>
          </blockquote>
        </div>
      </section>
    );
  }
  