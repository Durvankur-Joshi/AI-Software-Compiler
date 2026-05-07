import React, { useState } from 'react';

const ResultViewer = ({ result }) => {
  const [activeTab, setActiveTab] = useState('intent');

  const tabs = [
    { id: 'intent', label: 'Intent', icon: '🎯' },
    { id: 'architecture', label: 'Architecture', icon: '🏗️' },
    { id: 'database', label: 'Database', icon: '🗄️' },
    { id: 'api', label: 'API', icon: '🔌' },
    { id: 'ui', label: 'UI', icon: '🎨' },
    { id: 'auth', label: 'Auth', icon: '🔐' },
  ];

  const getTabContent = () => {
    const data = result[activeTab];
    if (!data) {
      return <p className="text-gray-500">No data available for {activeTab}</p>;
    }
    return <JSONViewer data={data} />;
  };

  return (
    <div className="bg-white rounded-lg shadow-md overflow-hidden">
      <div className="border-b border-gray-200">
        <div className="flex overflow-x-auto">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`px-4 py-3 text-sm font-medium transition whitespace-nowrap ${
                activeTab === tab.id
                  ? 'border-b-2 border-blue-500 text-blue-600 bg-blue-50'
                  : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              }`}
            >
              <span className="mr-2">{tab.icon}</span>
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      <div className="p-4">
        {getTabContent()}
      </div>
    </div>
  );
};

const JSONViewer = ({ data }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(JSON.stringify(data, null, 2));
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="relative">
      <button
        onClick={handleCopy}
        className="absolute top-2 right-2 bg-gray-700 hover:bg-gray-600 text-white text-xs px-2 py-1 rounded transition z-10"
      >
        {copied ? 'Copied!' : 'Copy'}
      </button>
      <pre className="json-viewer text-xs overflow-auto max-h-[500px]">
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
};

export default ResultViewer;