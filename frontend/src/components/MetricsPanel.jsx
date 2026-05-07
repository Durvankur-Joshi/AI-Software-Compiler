import React from 'react';
import { Activity, CheckCircle, XCircle, Clock, TrendingUp, Shield, Zap } from 'lucide-react';

const MetricsPanel = ({ metrics, repairApplied }) => {
  const stats = [
    {
      label: 'Total Requests',
      value: metrics.total_requests || 0,
      icon: Activity,
      color: 'primary',
      change: '+12%',
    },
    {
      label: 'Success Rate',
      value: `${metrics.success_rate || 0}%`,
      icon: CheckCircle,
      color: 'green',
      change: metrics.success_rate > 80 ? 'Excellent' : 'Good',
    },
    {
      label: 'Avg Latency',
      value: `${metrics.average_latency || 0}s`,
      icon: Clock,
      color: 'cyan',
      change: 'Real-time',
    },
    {
      label: 'Failures',
      value: metrics.failed_requests || 0,
      icon: XCircle,
      color: 'red',
      change: metrics.failed_requests === 0 ? 'Perfect' : 'Needs attention',
    },
  ];

  return (
    <div className="space-y-4 animate-slide-up">
      {/* Stats Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, idx) => {
          const Icon = stat.icon;
          const colorClasses = {
            primary: 'from-primary-600/20 to-primary-700/20 border-primary-500/30',
            green: 'from-green-600/20 to-green-700/20 border-green-500/30',
            cyan: 'from-cyan-600/20 to-cyan-700/20 border-cyan-500/30',
            red: 'from-red-600/20 to-red-700/20 border-red-500/30',
          };
          
          return (
            <div
              key={idx}
              className={`relative overflow-hidden rounded-xl border bg-gradient-to-br ${colorClasses[stat.color]} p-4 transition-all duration-300 hover:scale-[1.02]`}
            >
              <div className="flex items-center justify-between mb-2">
                <Icon className={`w-5 h-5 text-${stat.color}-500`} />
                <span className="text-xs font-mono text-dark-text-secondary">{stat.change}</span>
              </div>
              <p className="text-2xl font-bold text-dark-text">{stat.value}</p>
              <p className="text-xs text-dark-text-secondary mt-1">{stat.label}</p>
            </div>
          );
        })}
      </div>

      {/* System Status */}
      <div className="flex flex-wrap gap-3 items-center justify-between p-4 rounded-xl bg-dark-surface/50 border border-dark-border">
        <div className="flex items-center gap-3">
          <div className="relative">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse-ring"></div>
            <div className="w-2 h-2 bg-green-500 rounded-full absolute inset-0 animate-ping"></div>
          </div>
          <span className="text-sm font-mono">System Operational</span>
          <span className="text-xs text-dark-text-secondary">•</span>
          <div className="flex items-center gap-1">
            <Zap className="w-3 h-3 text-primary-500" />
            <span className="text-xs text-dark-text-secondary">Gemini AI Active</span>
          </div>
        </div>
        
        <div className={`flex items-center gap-2 px-3 py-1.5 rounded-lg transition-all duration-300 ${
          repairApplied ? 'bg-orange-500/10 border border-orange-500/30' : 'bg-green-500/10 border border-green-500/30'
        }`}>
          <Shield className={`w-4 h-4 ${repairApplied ? 'text-orange-500' : 'text-green-500'}`} />
          <span className={`text-xs font-medium ${repairApplied ? 'text-orange-400' : 'text-green-400'}`}>
            {repairApplied ? 'Auto-Repair Applied' : 'Validation Passed'}
          </span>
        </div>
      </div>

      {/* Performance Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-3 rounded-lg bg-dark-secondary/50 border border-dark-border">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-mono text-dark-text-secondary">Response Time</span>
            <TrendingUp className="w-3 h-3 text-green-500" />
          </div>
          <div className="h-1.5 bg-dark-border rounded-full overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-primary-500 to-accent-purple rounded-full transition-all duration-1000"
              style={{ width: `${Math.min(100, (metrics.average_latency || 0) * 10)}%` }}
            ></div>
          </div>
          <div className="flex justify-between mt-1">
            <span className="text-[10px] text-dark-text-secondary">0s</span>
            <span className="text-[10px] text-dark-text-secondary">5s</span>
            <span className="text-[10px] text-dark-text-secondary">10s</span>
          </div>
        </div>
        
        <div className="p-3 rounded-lg bg-dark-secondary/50 border border-dark-border">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-mono text-dark-text-secondary">Success Rate</span>
            <span className="text-xs text-green-500">{metrics.success_rate || 0}%</span>
          </div>
          <div className="h-1.5 bg-dark-border rounded-full overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-green-500 to-primary-500 rounded-full transition-all duration-1000"
              style={{ width: `${metrics.success_rate || 0}%` }}
            ></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MetricsPanel;