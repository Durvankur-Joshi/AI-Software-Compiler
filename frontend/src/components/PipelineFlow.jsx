import React from "react";
import {
  MessageSquare,
  Brain,
  GitBranch,
  Database,
  ShieldCheck,
  Wrench,
  RefreshCw,
  PlayCircle,
  Code2,
} from "lucide-react";

const stages = [
  {
    title: "Clarification",
    icon: MessageSquare,
    desc: "Detects vague or conflicting prompts",
  },
  {
    title: "Intent Extraction",
    icon: Brain,
    desc: "Extracts app goals, roles, and features",
  },
  {
    title: "Architecture Design",
    icon: GitBranch,
    desc: "Builds entities, modules, and flows",
  },
  {
    title: "Schema Generation",
    icon: Database,
    desc: "Generates DB, API, UI, and Auth schemas",
  },
  {
    title: "Validation",
    icon: ShieldCheck,
    desc: "Checks consistency across all layers",
  },
  {
    title: "Repair Engine",
    icon: Wrench,
    desc: "Repairs invalid or hallucinated fields",
  },
  {
    title: "Regeneration",
    icon: RefreshCw,
    desc: "Regenerates broken sections only",
  },
  {
    title: "Runtime Execution",
    icon: PlayCircle,
    desc: "Creates executable SQLite application",
  },
  {
    title: "Backend Generator",
    icon: Code2,
    desc: "Generates FastAPI backend structure",
  },
];

const PipelineFlow = () => {
  return (
    <div className="glass-effect rounded-2xl border border-dark-border p-6">
      <h2 className="text-2xl font-bold mb-6">
        Compiler Pipeline
      </h2>

      <div className="grid md:grid-cols-3 gap-4">
        {stages.map((stage, index) => {
          const Icon = stage.icon;

          return (
            <div
              key={index}
              className="rounded-xl border border-dark-border bg-dark-surface p-4 hover:border-primary-500 transition-all duration-300"
            >
              <div className="flex items-center gap-3 mb-3">
                <div className="p-2 rounded-lg bg-primary-500/10">
                  <Icon className="w-5 h-5 text-primary-400" />
                </div>

                <div>
                  <p className="text-sm text-dark-text-secondary">
                    Stage {index + 1}
                  </p>

                  <h3 className="font-semibold">
                    {stage.title}
                  </h3>
                </div>
              </div>

              <p className="text-sm text-dark-text-secondary leading-relaxed">
                {stage.desc}
              </p>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default PipelineFlow;