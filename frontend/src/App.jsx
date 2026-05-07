import React, { useState } from 'react';
import PromptForm from './components/PromptForm';
import ResultViewer from './components/ResultViewer';
import MetricsPanel from './components/MetricsPanel';
import ClarificationBox from './components/ClarificationBox';
import { generateBackend } from './services/api';

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [clarification, setClarification] = useState(null);

  const handleGenerate = async (prompt) => {
    setLoading(true);
    setError(null);
    setResult(null);
    setClarification(null);

    try {
      const data = await generateBackend(prompt);
      
      // Check if clarification is needed
      if (data.status === 'clarification_needed') {
        setClarification(data);
      } else {
        setResult(data);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            AI Software Compiler
          </h1>
          <p className="text-gray-600 mt-1">
            Generate complete backend applications from natural language prompts
          </p>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        {/* Prompt Form */}
        <div className="mb-8">
          <PromptForm onSubmit={handleGenerate} loading={loading} />
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="inline-block">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
              <p className="text-gray-600">Generating your application...</p>
              <p className="text-sm text-gray-400 mt-2">This may take a few moments</p>
            </div>
          </div>
        )}

        {/* Error State */}
        {error && !loading && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-6">
            <div className="flex">
              <div className="flex-shrink-0">
                <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="ml-3">
                <h3 className="text-sm font-medium text-red-800">Error</h3>
                <p className="text-sm text-red-700 mt-1">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Clarification Box */}
        {clarification && !loading && (
          <ClarificationBox questions={clarification.questions} />
        )}

        {/* Results */}
        {result && !loading && (
          <div className="space-y-6">
            {/* Metrics Panel */}
            {result.metrics && (
              <MetricsPanel metrics={result.metrics} repairApplied={result.repair_applied} />
            )}

            {/* Validation Errors */}
            {result.validation_errors && result.validation_errors.length > 0 && (
              <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                <h3 className="text-lg font-semibold text-yellow-800 mb-2">Validation Errors</h3>
                <div className="space-y-1">
                  {result.validation_errors.map((error, idx) => (
                    <p key={idx} className="text-sm text-yellow-700">• {error}</p>
                  ))}
                </div>
              </div>
            )}

            {/* Result Viewer */}
            <ResultViewer result={result} />
          </div>
        )}

        {/* No Results State */}
        {!loading && !result && !clarification && !error && (
          <div className="text-center py-12">
            <svg className="mx-auto h-24 w-24 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
            <p className="mt-4 text-gray-500">Enter a prompt above to generate your backend application</p>
            <p className="text-sm text-gray-400 mt-2">Example: "Build a CRM with login, contacts, dashboard, and analytics"</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;