import { useState } from 'react';

export default function Pathology() {
  const [image, setImage] = useState(null);
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleSubmit = async () => {
    const form = new FormData();
    form.append('image', image);
    form.append('question', question);

    const res = await fetch('/api/get_answer', {
      method: 'POST',
      body: form,
    });
    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl mb-4">Pathology VQA</h1>
      <input type="file" onChange={(e) => setImage(e.target.files[0])} />
      <input
        className="border p-2 block my-2"
        type="text"
        placeholder="Enter your question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button className="bg-green-600 text-white px-4 py-2 rounded" onClick={handleSubmit}>
        Get Answer
      </button>
      {answer && <p className="mt-4 text-lg">Answer: <strong>{answer}</strong></p>}
    </div>
  );
}