import React from 'react';
import { HelpCircle, Lightbulb, MessageCircle, ArrowRight } from 'lucide-react';

const ClarificationBox = ({ questions }) => {
  return (
    <div className="gradient-border">
      <div className="gradient-border-inner p-6">
        <div className="flex items-start gap-4">
          <div className="flex-shrink-0">
            <div className="relative">
              <div className="w-12 h-12 rounded-full bg-primary-500/20 flex items-center justify-center">
                <HelpCircle className="w-6 h-6 text-primary-500" />
              </div>
              <div className="absolute -top-1 -right-1 w-3 h-3 bg-accent-purple rounded-full animate-pulse"></div>
            </div>
          </div>
          
          <div className="flex-1">
            <h3 className="text-lg font-semibold text-dark-text mb-2">
              Additional Information Needed
            </h3>
            <p className="text-sm text-dark-text-secondary mb-4">
              To generate a more accurate and complete backend, please provide the following details:
            </p>
            
            <div className="space-y-3 mb-6">
              {questions.map((question, idx) => (
                <div 
                  key={idx} 
                  className="flex items-start gap-3 p-3 rounded-lg bg-dark-secondary/50 border border-dark-border animate-slide-down"
                  style={{ animationDelay: `${idx * 0.1}s` }}
                >
                  <div className="flex-shrink-0 mt-0.5">
                    <div className="w-5 h-5 rounded-full bg-primary-500/20 flex items-center justify-center">
                      <span className="text-xs text-primary-400 font-mono">{idx + 1}</span>
                    </div>
                  </div>
                  <p className="text-sm text-dark-text flex-1">{question}</p>
                  <ArrowRight className="w-4 h-4 text-dark-text-secondary opacity-50" />
                </div>
              ))}
            </div>
            
            <div className="p-4 rounded-lg bg-primary-500/5 border border-primary-500/20">
              <div className="flex items-start gap-2">
                <Lightbulb className="w-4 h-4 text-primary-500 flex-shrink-0 mt-0.5" />
                <div className="text-xs text-dark-text-secondary">
                  <p className="font-medium text-primary-400 mb-1">Pro Tip</p>
                  <p>Update your prompt with the missing details above and regenerate for better results.</p>
                  <p className="mt-2 text-primary-400/60">Example: "Build a CRM with authentication (JWT), contact management, analytics dashboard, and subscription billing with Stripe"</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ClarificationBox;