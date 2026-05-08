import React, { useState } from 'react';
import { Eye, Code2, Copy, Check, Database, Cpu, Shield, Brain, Layout, GitBranch, ChevronRight } from 'lucide-react';

const ResultViewer = ({ result }) => {
  const [activeTab, setActiveTab] = useState('intent');
  const [copied, setCopied] = useState(false);

  const tabs = [
    { id: 'intent', label: 'Intent', icon: Cpu, color: 'primary' },
    { id: 'architecture', label: 'Architecture', icon: GitBranch, color: 'accent-purple' },
    { id: 'database', label: 'Database', icon: Database, color: 'accent-cyan' },
    { id: 'api', label: 'API', icon: Code2, color: 'accent-pink' },
    { id: 'ui', label: 'UI', icon: Layout, color: 'primary' },
    { id: 'auth', label: 'Auth', icon: Shield, color: 'accent-purple' },
    { id: 'business_logic', label: 'Logic', icon: Brain, color: 'accent-pink' },
  ];

  const getTabContent = () => {
    const data = result[activeTab];
    if (!data) {
      return (
        <div className="text-center py-8 text-dark-text-secondary">
          <Eye className="w-12 h-12 mx-auto mb-2 opacity-50" />
          <p className="text-sm">No data available for {activeTab}</p>
        </div>
      );
    }
    return <JSONViewer data={data} />;
  };

  const handleCopyAll = () => {
    navigator.clipboard.writeText(JSON.stringify(result, null, 2));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="glass-effect rounded-xl overflow-hidden border border-dark-border animate-scale-up max-h-[85vh] flex flex-col">
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 p-4 border-b border-dark-border bg-dark-surface/50">
        <div className="flex items-center gap-2">
          <Code2 className="w-5 h-5 text-primary-500" />
          <span className="font-mono text-sm font-medium">Generated Output</span>
          <span className="text-xs text-dark-text-secondary ml-2">
            {new Date().toLocaleTimeString()}
          </span>
        </div>
        <div className="flex items-center gap-3">
          <a
            href={`http://127.0.0.1:8000/download/${result.project_id}`}
            target="_blank"
            rel="noreferrer"
            className="px-4 py-2 rounded-lg bg-primary-500 text-white hover:bg-primary-600 transition-colors whitespace-nowrap"
          >
            Download Backend
          </a>
        <button
          onClick={handleCopyAll}
          className="flex items-center gap-2 px-3 py-2 rounded-lg bg-dark-secondary hover:bg-dark-border transition-all duration-300 text-sm whitespace-nowrap"
        >
          {copied ? <Check className="w-4 h-4 text-green-500" /> : <Copy className="w-4 h-4" />}
          <span className="hidden sm:inline">{copied ? 'Copied!' : 'Copy All'}</span>
        </button>
      </div>
    </div>

      {/* Tabs */ }
  <div className="border-b border-dark-border pb-3 ">
    <div className="flex">
      {tabs.map((tab) => {
        const Icon = tab.icon;
        const isActive = activeTab === tab.id;
        return (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`group relative px-4 py-3 text-sm font-medium transition-all duration-300 whitespace-nowrap flex items-center gap-2 ${isActive
              ? 'text-primary-400 bg-dark-surface'
              : 'text-dark-text-secondary hover:text-dark-text hover:bg-dark-surface/50'
              }`}
          >
            <Icon className={`w-4 h-4 transition-colors ${isActive ? `text-${tab.color}-500` : 'opacity-50'
              }`} />
            {tab.label}
            {isActive && (
              <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-primary-500 to-accent-purple"></div>
            )}
          </button>
        );
      })}
    </div>
  </div>

  {/* Content */ }
  <div className="p-4 overflow-y-auto custom-scrollbar flex-1">
    {getTabContent()}
  </div>
    </div >
  );
};

const JSONViewer = ({ data, level = 0, path = "root" }) => {
  const [collapsed, setCollapsed] = useState({});

  const toggleCollapse = (key) => {
    setCollapsed((prev) => ({
      ...prev,
      [key]: !prev[key],
    }));
  };

  const formatValue = (value) => {
    if (typeof value === "string") {
      return <span className="text-accent-cyan">"{value}"</span>;
    }

    if (typeof value === "number") {
      return <span className="text-accent-purple">{value}</span>;
    }

    if (typeof value === "boolean") {
      return (
        <span className="text-primary-500">
          {value.toString()}
        </span>
      );
    }

    if (value === null) {
      return (
        <span className="text-dark-text-secondary">
          null
        </span>
      );
    }

    return value;
  };

  // ARRAY
  if (Array.isArray(data)) {
    if (data.length === 0) {
      return (
        <span className="text-dark-text-secondary">
          []
        </span>
      );
    }

    return (
      <div className="pl-4 border-l border-dark-border space-y-2">
        {data.map((item, idx) => (
          <div key={`${path}-${idx}`}>
            <span className="text-dark-text-secondary text-xs mr-2">
              [{idx}]
            </span>

            <JSONViewer
              data={item}
              level={level + 1}
              path={`${path}-${idx}`}
            />
          </div>
        ))}
      </div>
    );
  }

  // OBJECT
  if (typeof data === "object" && data !== null) {
    const entries = Object.entries(data);

    if (entries.length === 0) {
      return (
        <span className="text-dark-text-secondary">
          {"{}"}
        </span>
      );
    }

    return (
      <div className="space-y-1">
        {entries.map(([key, value]) => {
          const uniqueKey = `${path}-${key}`;

          const isComplex =
            typeof value === "object" &&
            value !== null;

          const isCollapsed =
            collapsed[uniqueKey];

          return (
            <div key={uniqueKey} className="ml-2">
              <div className="flex items-start gap-2 group">

                {isComplex && (
                  <button
                    onClick={() =>
                      toggleCollapse(uniqueKey)
                    }
                    className="mt-0.5 p-0.5 hover:bg-dark-secondary rounded transition"
                  >
                    <ChevronRight
                      className={`w-3 h-3 transition-transform ${isCollapsed
                        ? ""
                        : "rotate-90"
                        }`}
                    />
                  </button>
                )}

                {!isComplex && (
                  <div className="w-4" />
                )}

                <span className="text-primary-400 font-mono text-sm">
                  {key}
                </span>

                <span className="text-dark-text-secondary">
                  :
                </span>

                {!isComplex && (
                  <div className="flex-1 break-all">
                    {formatValue(value)}
                  </div>
                )}
              </div>

              {isComplex && !isCollapsed && (
                <div className="ml-4 mt-1">
                  <JSONViewer
                    data={value}
                    level={level + 1}
                    path={uniqueKey}
                  />
                </div>
              )}

              {isComplex && isCollapsed && (
                <div className="ml-6 text-xs text-dark-text-secondary">
                  {Array.isArray(value)
                    ? "[...]"
                    : "{...}"}
                </div>
              )}
            </div>
          );
        })}
      </div>
    );
  }

  return <span>{formatValue(data)}</span>;
};

export default ResultViewer;