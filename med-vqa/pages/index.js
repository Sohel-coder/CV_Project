import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 p-6 text-center">
      <h1 className="text-4xl font-bold mb-4">Med VQA</h1>
      <p className="text-lg mb-6">Medical Visual Question Answering using X-ray and Pathology images.</p>
      <div className="grid gap-6 grid-cols-1 md:grid-cols-2">
        <Link href="/radiology" className="bg-blue-500 text-white py-4 rounded-lg hover:bg-blue-700 transition">
          Radiology VQA
        </Link>
        <Link href="/pathology" className="bg-green-500 text-white py-4 rounded-lg hover:bg-green-700 transition">
          Pathology VQA
        </Link>
      </div>
      <div className="mt-10 text-left max-w-3xl mx-auto">
        <h2 className="text-2xl font-semibold">About the Project</h2>
        <p>Med VQA uses deep learning to answer questions related to medical images. Models trained on SLAKE (radiology) and PathVQA (pathology).</p>
        <h3 className="text-xl mt-4 font-semibold">Use Cases</h3>
        <ul className="list-disc pl-6">
          <li>Medical education</li>
          <li>AI-assisted diagnosis</li>
          <li>Research in multimodal learning</li>
        </ul>
        <h3 className="text-xl mt-4 font-semibold">Developers</h3>
        <p>Team of 6 members from IISc Bangalore</p>
      </div>
    </div>
  );
}