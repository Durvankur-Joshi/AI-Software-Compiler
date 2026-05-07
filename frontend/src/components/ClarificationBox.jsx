import React from 'react';

const ClarificationBox = ({ questions }) => {
  return (
    <div className="bg-blue-50 border border-blue-200 rounded-lg p-6">
      <div className="flex items-start">
        <div className="flex-shrink-0">
          <svg className="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <div className="ml-3 flex-1">
          <h3 className="text-lg font-semibold text-blue-800 mb-2">
            Need More Information
          </h3>
          <p className="text-blue-700 mb-3">
            Please provide additional details to help generate a better application:
          </p>
          <ul className="list-disc list-inside space-y-1">
            {questions.map((question, idx) => (
              <li key={idx} className="text-blue-700 text-sm">
                {question}
              </li>
            ))}
          </ul>
          <div className="mt-4 p-3 bg-blue-100 rounded">
            <p className="text-sm text-blue-800">
              💡 Tip: Update your prompt with the missing information and try again
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ClarificationBox;