import React from 'react';

const MetricsPanel = ({ metrics, repairApplied }) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">System Metrics</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          label="Total Requests"
          value={metrics.total_requests || 0}
          icon="📊"
          color="blue"
        />
        <MetricCard
          label="Success Rate"
          value={`${metrics.success_rate || 0}%`}
          icon="✅"
          color="green"
        />
        <MetricCard
          label="Average Latency"
          value={`${metrics.average_latency || 0}s`}
          icon="⏱️"
          color="purple"
        />
        <MetricCard
          label="Failed Requests"
          value={metrics.failed_requests || 0}
          icon="❌"
          color="red"
        />
      </div>

      {repairApplied !== undefined && (
        <div className={`mt-4 p-3 rounded-lg ${
          repairApplied ? 'bg-orange-50 text-orange-800' : 'bg-green-50 text-green-800'
        }`}>
          <div className="flex items-center">
            <span className="text-lg mr-2">{repairApplied ? '🔧' : '✓'}</span>
            <span className="font-medium">
              {repairApplied ? 'Repair Applied: Schema was automatically fixed' : 'No Repair Needed: Schema validated successfully'}
            </span>
          </div>
        </div>
      )}
    </div>
  );
};

const MetricCard = ({ label, value, icon, color }) => {
  const colorClasses = {
    blue: 'bg-blue-50 border-blue-200',
    green: 'bg-green-50 border-green-200',
    purple: 'bg-purple-50 border-purple-200',
    red: 'bg-red-50 border-red-200',
  };

  return (
    <div className={`rounded-lg border p-4 ${colorClasses[color]}`}>
      <div className="flex items-center justify-between mb-2">
        <span className="text-2xl">{icon}</span>
        <span className="text-2xl font-bold">{value}</span>
      </div>
      <p className="text-sm text-gray-600">{label}</p>
    </div>
  );
};

export default MetricsPanel;