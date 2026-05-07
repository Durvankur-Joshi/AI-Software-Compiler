import React, { useState } from 'react';

const PromptForm = ({ onSubmit, loading }) => {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (prompt.trim() && !loading) {
      onSubmit(prompt.trim());
    }
  };

  const examples = [
    "Build a CRM with login, contacts, dashboard, analytics, and subscriptions",
    "Create an e-commerce platform with products, cart, checkout, and payments",
    "Build a hospital management system with doctors, patients, and appointments"
  ];

  const handleExampleClick = (example) => {
    setPrompt(example);
  };

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="prompt" className="block text-sm font-medium text-gray-700 mb-2">
            Application Description
          </label>
          <textarea
            id="prompt"
            rows="4"
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none font-mono text-sm"
            placeholder="Describe the application you want to build... (e.g., Build a CRM with user authentication, contact management, dashboard, and reporting)"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            disabled={loading}
          />
        </div>

        <div className="mb-4">
          <p className="text-sm text-gray-600 mb-2">Examples:</p>
          <div className="flex flex-wrap gap-2">
            {examples.map((example, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => handleExampleClick(example)}
                className="text-xs bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-1 rounded-full transition"
                disabled={loading}
              >
                {example.substring(0, 50)}...
              </button>
            ))}
          </div>
        </div>

        <button
          type="submit"
          disabled={!prompt.trim() || loading}
          className="w-full bg-gradient-to-r from-blue-600 to-purple-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-blue-700 hover:to-purple-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Generating...' : 'Generate Application'}
        </button>
      </form>
    </div>
  );
};

export default PromptForm;