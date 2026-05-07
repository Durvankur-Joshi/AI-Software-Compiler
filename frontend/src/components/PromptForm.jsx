import React, { useState } from 'react';
import { Send, Loader2, Lightbulb, Code, Zap } from 'lucide-react';

const PromptForm = ({ onSubmit, loading }) => {
  const [prompt, setPrompt] = useState('');
  const [focused, setFocused] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (prompt.trim() && !loading) {
      onSubmit(prompt.trim());
    }
  };

  const examples = [
    { text: "Build a CRM with login, contacts, dashboard, analytics, and subscriptions", icon: "📊" },
    { text: "Create an e-commerce platform with products, cart, checkout, and payments", icon: "🛒" },
    { text: "Build a hospital management system with doctors, patients, and appointments", icon: "🏥" },
    { text: "Create a task management tool with teams, projects, and deadlines", icon: "✅" }
  ];

  const handleExampleClick = (example) => {
    setPrompt(example);
  };

  const getCharacterCount = () => {
    const count = prompt.length;
    if (count === 0) return '';
    if (count < 50) return 'short';
    if (count < 200) return 'good';
    return 'excellent';
  };

  return (
    <div className="gradient-border">
      <div className="gradient-border-inner p-6">
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <div className={`flex items-center justify-between mb-2 transition-all duration-300 ${focused ? 'text-primary-400' : 'text-dark-text-secondary'}`}>
              <label className="text-sm font-medium flex items-center gap-2">
                <Code className="w-4 h-4" />
                Describe Your Application
              </label>
              {prompt && (
                <div className="flex items-center gap-1 text-xs">
                  <Zap className="w-3 h-3" />
                  <span className={`${
                    getCharacterCount() === 'short' ? 'text-yellow-500' :
                    getCharacterCount() === 'good' ? 'text-green-500' : 'text-primary-500'
                  }`}>
                    {prompt.length} characters
                  </span>
                </div>
              )}
            </div>
            
            <textarea
              id="prompt"
              rows="5"
              className={`w-full px-4 py-3 bg-dark-secondary border rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent resize-none font-mono text-sm transition-all duration-300 ${
                focused ? 'border-primary-500/50' : 'border-dark-border'
              }`}
              placeholder="Example: Build a modern CRM with user authentication, contact management, activity tracking, analytics dashboard, and subscription billing..."
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              onFocus={() => setFocused(true)}
              onBlur={() => setFocused(false)}
              disabled={loading}
            />
          </div>

          {/* Quick Tips */}
          <div className="mb-4 p-3 rounded-lg bg-dark-secondary/50 border border-dark-border">
            <div className="flex items-center gap-2 mb-2">
              <Lightbulb className="w-4 h-4 text-primary-500" />
              <span className="text-xs font-medium text-dark-text-secondary">Pro Tips</span>
            </div>
            <div className="flex flex-wrap gap-2 text-xs text-dark-text-secondary">
              <span className="px-2 py-1 rounded bg-dark-surface">✅ Be specific about features</span>
              <span className="px-2 py-1 rounded bg-dark-surface">👥 Mention user roles</span>
              <span className="px-2 py-1 rounded bg-dark-surface">📊 Include data requirements</span>
              <span className="px-2 py-1 rounded bg-dark-surface">🔐 Specify auth needs</span>
            </div>
          </div>

          {/* Example Prompts */}
          <div className="mb-4">
            <p className="text-xs text-dark-text-secondary mb-2 flex items-center gap-1">
              <Zap className="w-3 h-3" />
              Quick Examples
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              {examples.map((example, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => handleExampleClick(example.text)}
                  className="text-left text-xs bg-dark-secondary hover:bg-dark-border border border-dark-border rounded-lg px-3 py-2 transition-all duration-300 hover:scale-[1.02] hover:border-primary-500/50 group"
                  disabled={loading}
                >
                  <span className="mr-2">{example.icon}</span>
                  <span className="text-dark-text-secondary group-hover:text-dark-text transition">
                    {example.text.substring(0, 60)}...
                  </span>
                </button>
              ))}
            </div>
          </div>

          <button
            type="submit"
            disabled={!prompt.trim() || loading}
            className="relative w-full bg-gradient-to-r from-primary-600 to-accent-purple text-white font-semibold py-3 px-4 rounded-xl hover:shadow-lg hover:shadow-primary-500/25 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed group overflow-hidden"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000"></div>
            <div className="relative flex items-center justify-center gap-2">
              {loading ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Generating...</span>
                </>
              ) : (
                <>
                  <Send className="w-5 h-5" />
                  <span>Generate Application</span>
                </>
              )}
            </div>
          </button>
        </form>
      </div>
    </div>
  );
};

export default PromptForm;