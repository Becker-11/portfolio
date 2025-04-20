// frontend/src/app/(site)/about/page.tsx
export default function AboutPage() {
    return (
      <div className="max-w-3xl mx-auto p-6 space-y-6">
        <h1 className="text-3xl font-bold text-zinc-100">Get to Know Me</h1>
  
        <p className="text-zinc-400 text-base leading-relaxed">
          I&apos;m Rowan, a curious and detail-oriented engineer with a background in physics, computer science, and mathematics. 
          I thrive on exploring deep questions about how the world works&mdash;and how we can build systems that make it better.
        </p>
  
        <p className="text-zinc-400 text-base leading-relaxed">
          My recent work focuses on <strong>AI safety</strong>, where I combine technical skills with a philosophical mindset to 
          help ensure powerful systems are aligned with human values. I&apos;ve also worked on problems in scientific computing, 
          knowledge organization, and developer experience.
        </p>
  
        <p className="text-zinc-400 text-base leading-relaxed">
          Outside of work, I host a podcast exploring high-context ideas, and I&apos;m always up for a conversation about 
          epistemology, systems thinking, or the best way to make a portfolio website not suck.
        </p>
  
        <p className="text-zinc-400 text-base leading-relaxed">
          If you&apos;re working on hard problems&mdash;or just want to chat&mdash;feel free to <a 
          href="mailto:rowan@example.com" className="text-sky-400 hover:underline">get in touch</a>.
        </p>
      </div>
    );
  }
  