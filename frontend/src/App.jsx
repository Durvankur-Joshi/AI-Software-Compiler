import React, { useState, useEffect } from 'react';
import PromptForm from './components/PromptForm';
import ResultViewer from './components/ResultViewer';
import MetricsPanel from './components/MetricsPanel';
import ClarificationBox from './components/ClarificationBox';
import { generateBackend } from './services/api';
import { Terminal, Zap,Moon, Sun, Sparkles, Loader2 } from 'lucide-react';

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [clarification, setClarification] = useState(null);
  const [darkMode, setDarkMode] = useState(true);
  const [typedText, setTypedText] = useState('');
  const fullText = 'Generate production-ready backend code from natural language';

  useEffect(() => {
    let i = 0;
    const typing = setInterval(() => {
      if (i < fullText.length) {
        setTypedText(fullText.slice(0, i + 1));
        i++;
      } else {
        clearInterval(typing);
      }
    }, 50);
    return () => clearInterval(typing);
  }, []);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  const handleGenerate = async (prompt) => {
    setLoading(true);
    setError(null);
    setResult(null);
    setClarification(null);

    try {
      const data = await generateBackend(prompt);
      
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
    <div className="min-h-screen bg-dark-bg transition-colors duration-300">
      {/* Animated Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-primary-600/20 rounded-full blur-3xl animate-float"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-purple-600/20 rounded-full blur-3xl animate-float" style={{ animationDelay: '2s' }}></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-cyan-600/10 rounded-full blur-3xl"></div>
      </div>

      {/* Header */}
      <header className="relative bg-dark-surface/80 backdrop-blur-sm border-b border-dark-border">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <div className="gradient-border">
                <div className="p-2 rounded-lg bg-dark-surface">
                  <Terminal className="w-6 h-6 text-primary-500" />
                </div>
              </div>
              <div>
                <h1 className="text-2xl font-bold bg-gradient-to-r from-primary-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                  AI Compiler
                </h1>
                <p className="text-xs text-dark-text-secondary hidden sm:block">
                  Intelligent Code Generation System
                </p>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="hidden md:flex items-center space-x-2 text-xs text-dark-text-secondary">
                <Zap className="w-4 h-4 text-primary-500" />
                <span>Powered by Gemini AI</span>
              </div>
              
              <button
                onClick={() => setDarkMode(!darkMode)}
                className="p-2 rounded-lg bg-dark-surface border border-dark-border hover:bg-dark-secondary transition-all duration-300 transform hover:scale-105"
              >
                {darkMode ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
              </button>
              
              <a
                href="#"
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded-lg bg-dark-surface border border-dark-border hover:bg-dark-secondary transition-all duration-300"
              >
                
              </a>
            </div>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <div className="relative max-w-7xl mx-auto px-4 pt-12 pb-8 text-center">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-primary-600/10 border border-primary-500/20 mb-6">
          <Sparkles className="w-4 h-4 text-primary-500 animate-pulse" />
          <span className="text-xs text-primary-400 font-mono">AI-POWERED DEVELOPMENT</span>
        </div>
        
        <h2 className="text-5xl md:text-6xl font-bold mb-4 bg-gradient-to-r from-primary-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
          Create Apps with AI
        </h2>
        
        <p className="text-base md:text-lg text-dark-text-secondary max-w-2xl mx-auto">
          {typedText}
          <span className="inline-block w-0.5 h-4 bg-primary-500 ml-1 animate-pulse"></span>
        </p>
      </div>

      {/* Main Content */}
      <main className="relative max-w-7xl mx-auto px-4 pb-12">
        {/* Prompt Form */}
        <div className="mb-8 animate-slide-up">
          <PromptForm onSubmit={handleGenerate} loading={loading} />
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-16 animate-fade-in">
            <div className="inline-block relative">
              <div className="w-20 h-20 border-4 border-dark-border border-t-primary-500 rounded-full animate-spin"></div>
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="w-10 h-10 border-4 border-dark-border border-b-purple-500 rounded-full animate-spin" style={{ animationDirection: 'reverse' }}></div>
              </div>
            </div>
            <p className="text-dark-text-secondary mt-4 font-mono">Generating your application...</p>
            <div className="mt-2 w-48 h-1 bg-dark-surface rounded-full overflow-hidden mx-auto">
              <div className="h-full bg-gradient-to-r from-primary-500 to-purple-500 rounded-full animate-shimmer w-3/4"></div>
            </div>
          </div>
        )}

        {/* Error State */}
        {error && !loading && (
          <div className="bg-red-900/20 border border-red-700 rounded-xl p-4 mb-6 animate-slide-down">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <svg className="h-5 w-5 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="ml-3">
                <h3 className="text-sm font-medium text-red-400">Generation Failed</h3>
                <p className="text-sm text-red-300 mt-1">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* Clarification Box */}
        {clarification && !loading && (
          <div className="animate-scale-up">
            <ClarificationBox questions={clarification.questions} />
          </div>
        )}

        {/* Results */}
        {result && !loading && (
          <div className="space-y-6 animate-fade-in">
            {/* Metrics Panel */}
            {result.metrics && (
              <MetricsPanel metrics={result.metrics} repairApplied={result.repair_applied} />
            )}

            {/* Validation Errors */}
            {result.validation_errors && result.validation_errors.length > 0 && (
              <div className="bg-yellow-900/20 border border-yellow-700 rounded-xl p-4 animate-slide-down">
                <div className="flex items-start">
                  <div className="flex-shrink-0">
                    <svg className="h-5 w-5 text-yellow-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
                    </svg>
                  </div>
                  <div className="ml-3 flex-1">
                    <h3 className="text-sm font-medium text-yellow-400">Validation Issues Detected</h3>
                    <ul className="mt-2 text-sm text-yellow-300 space-y-1">
                      {result.validation_errors.map((error, idx) => (
                        <li key={idx} className="flex items-start">
                          <span className="mr-2">•</span>
                          {error}
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>
              </div>
            )}

            {/* Result Viewer */}
            <ResultViewer result={result} />
          </div>
        )}

        {/* No Results State */}
        {!loading && !result && !clarification && !error && (
          <div className="text-center py-16 animate-fade-in">
            <div className="gradient-border w-32 h-32 mx-auto mb-6">
              <div className="w-full h-full rounded-xl bg-dark-surface flex items-center justify-center">
                <Terminal className="w-16 h-16 text-dark-text-secondary" />
              </div>
            </div>
            <p className="text-dark-text-secondary font-mono">Ready to create something amazing</p>
            <p className="text-sm text-dark-text-secondary/60 mt-2">Enter a prompt above to start generating</p>
            
            <div className="mt-8 flex flex-wrap justify-center gap-3">
              <div className="px-3 py-1.5 rounded-lg bg-dark-surface border border-dark-border text-xs text-dark-text-secondary">
                🚀 CRM Systems
              </div>
              <div className="px-3 py-1.5 rounded-lg bg-dark-surface border border-dark-border text-xs text-dark-text-secondary">
                📊 Analytics Dashboards
              </div>
              <div className="px-3 py-1.5 rounded-lg bg-dark-surface border border-dark-border text-xs text-dark-text-secondary">
                🏥 Healthcare Apps
              </div>
              <div className="px-3 py-1.5 rounded-lg bg-dark-surface border border-dark-border text-xs text-dark-text-secondary">
                💳 E-commerce Platforms
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="border-t border-dark-border mt-12 py-6">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p className="text-xs text-dark-text-secondary">
            AI Software Compiler • Real-time backend generation • Powered by Google Gemini AI
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;