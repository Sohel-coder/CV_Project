// File: app/page.tsx (Home Page)
'use client';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-white p-6 text-gray-800">
      <section className="text-center py-12">
        <h1 className="text-5xl font-bold mb-4">Med VQA</h1>
        <p className="text-xl max-w-3xl mx-auto">
          Med VQA is a Medical Visual Question Answering system designed to assist in medical diagnostics. Provide an X-ray or pathology image along with a question, and receive an AI-generated answer.
        </p>
        <div className="mt-8">
          <Tabs defaultValue="radiology" className="flex justify-center">
            <TabsList>
              <Link href="/radiology"><TabsTrigger value="radiology">Radiology</TabsTrigger></Link>
              <Link href="/pathology"><TabsTrigger value="pathology">Pathology</TabsTrigger></Link>
            </TabsList>
          </Tabs>
        </div>
      </section>

      <section className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto mt-12">
        <div className="p-6 bg-white shadow rounded-2xl">
          <h2 className="text-2xl font-semibold mb-2">What is Med VQA?</h2>
          <p>
            Med VQA is an AI-driven system that combines medical imaging and NLP to answer questions about radiology and pathology images. Built using deep learning models trained on SLAKE and PathVQA datasets.
          </p>
        </div>
        <div className="p-6 bg-white shadow rounded-2xl">
          <h2 className="text-2xl font-semibold mb-2">Use Cases</h2>
          <ul className="list-disc pl-6">
            <li>Support radiologists in decision making</li>
            <li>Educational tool for medical students</li>
            <li>Assist remote diagnostics in under-resourced areas</li>
          </ul>
        </div>
        <div className="p-6 bg-white shadow rounded-2xl">
          <h2 className="text-2xl font-semibold mb-2">Datasets</h2>
          <p>
            Our models are trained on:
            <br />- SLAKE (radiology)
            <br />- PathVQA (pathology)
          </p>
        </div>
        <div className="p-6 bg-white shadow rounded-2xl">
          <h2 className="text-2xl font-semibold mb-2">Developers</h2>
          <p>
            Team of 6 researchers and engineers from IISc Bangalore working on medical AI solutions.
          </p>
        </div>
      </section>
    </main>
  );
}

// File: app/radiology/page.tsx
'use client';
import { useState } from 'react';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import Image from 'next/image';

export default function Radiology() {
  const [image, setImage] = useState<File | null>(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async () => {
    const formData = new FormData();
    if (image) formData.append('image', image);
    formData.append('question', question);

    const response = await fetch('/api/radiology', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    setAnswer(data.answer);
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Radiology VQA</h1>
      <Input type="file" accept="image/*" onChange={(e) => setImage(e.target.files?.[0] || null)} />
      <Textarea className="mt-4" placeholder="Ask your question..." value={question} onChange={(e) => setQuestion(e.target.value)} />
      <Button className="mt-4" onClick={handleSubmit}>Get Answer</Button>
      {answer && <div className="mt-6 p-4 bg-gray-100 rounded-xl">Answer: {answer}</div>}
    </div>
  );
}

// File: app/pathology/page.tsx
'use client';
import { useState } from 'react';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';

export default function Pathology() {
  const [image, setImage] = useState<File | null>(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async () => {
    const formData = new FormData();
    if (image) formData.append('image', image);
    formData.append('question', question);

    const response = await fetch('/api/pathology', {
      method: 'POST',
      body: formData,
    });
    const data = await response.json();
    setAnswer(data.answer);
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">Pathology VQA</h1>
      <Input type="file" accept="image/*" onChange={(e) => setImage(e.target.files?.[0] || null)} />
      <Textarea className="mt-4" placeholder="Ask your question..." value={question} onChange={(e) => setQuestion(e.target.value)} />
      <Button className="mt-4" onClick={handleSubmit}>Get Answer</Button>
      {answer && <div className="mt-6 p-4 bg-gray-100 rounded-xl">Answer: {answer}</div>}
    </div>
  );
}

// File: app/api/radiology/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const formData = await req.formData();
  const image = formData.get('image') as File;
  const question = formData.get('question');

  // TODO: Call your radiology VQA model backend API here
  const mockAnswer = 'This is a mock answer for Radiology.';
  return NextResponse.json({ answer: mockAnswer });
}

// File: app/api/pathology/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const formData = await req.formData();
  const image = formData.get('image') as File;
  const question = formData.get('question');

  // TODO: Call your pathology VQA model backend API here
  const mockAnswer = 'This is a mock answer for Pathology.';
  return NextResponse.json({ answer: mockAnswer });
}

// Optional: Add tailwind.config.js with custom theme, and components from shadcn/ui
// To deploy to Vercel:
// 1. Push this Next.js project to GitHub
// 2. Go to vercel.com, import the GitHub repo, and deploy
// 3. Add any environment variables needed for model API URLs
