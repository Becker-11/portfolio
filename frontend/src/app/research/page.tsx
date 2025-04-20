// frontend/src/app/research/page.tsx

import { supabase } from '@/lib/supabaseClient'
import { Paper } from '@/types'

export default async function ResearchPage() {
  const { data: papers } = await supabase
    .from('papers')       // Database types are now inferred
    .select('*')
    .order('published', { ascending: false })

  return (
    <main className="min-h-screen p-8 bg-gray-50">
      <h1 className="text-4xl font-bold mb-6">AI Safety Research</h1>
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {papers?.map((p: Paper) => (
          <article key={p.id} className="bg-white p-4 rounded-lg shadow">
            <h2 className="text-xl font-semibold">
              <a href={p.url} target="_blank" rel="noopener noreferrer">
                {p.id} — {p.title}
              </a>
            </h2>
            <p className="text-sm text-gray-500">{new Date(p.published).toDateString()}</p>
            <p className="mt-2 text-gray-700">{p.summary}</p>
            <p className="mt-2 text-sm text-indigo-600">Keywords: {p.keywords}</p>
          </article>
        ))}
      </div>
    </main>
  )
}
