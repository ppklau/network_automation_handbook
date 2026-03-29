import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import mermaid from 'astro-mermaid';

export default defineConfig({
  site: 'https://ppklau.github.io',
  base: '/network_automation_handbook',
  integrations: [
    mermaid(),
    starlight({
      title: 'Network Automation Handbook',
      description: 'A strategic guide for organisations transforming network operations through automation.',
      logo: {
        src: './src/assets/logo-dark.svg',
        replacesTitle: false,
      },
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/ppklau/network_automation_handbook' },
      ],
      favicon: '/favicon.svg',
      customCss: ['./src/styles/custom.css'],
      head: [
        {
          tag: 'script',
          attrs: { type: 'module' },
          // content: MERMAID_SCRIPT,
        },
      ],
      editLink: {
        baseUrl: 'https://github.com/ppklau/network_automation_handbook/edit/main/network_automation_handbook/',
      },
      sidebar: [
        { label: 'Executive Summary', link: '00-executive-summary/chapter' },
        { label: 'Introduction', link: '01-introduction/chapter' },
        {
          label: 'Part I — Business & Strategy',
          items: [
            { label: 'Business Alignment', link: '02-business-alignment/chapter' },
            { label: 'Maturity Model', link: '03-maturity-model/chapter' },
            { label: 'Transformation Roadmap', link: '04-transformation-roadmap/chapter' },
          ],
        },
        {
          label: 'Part II — Architecture & Tooling',
          items: [
            {
              label: 'Tooling Strategy',
              items: [
                { label: 'Overview', link: '05-tooling-strategy/chapter' },
                { label: 'Workflow Orchestration', link: '05-tooling-strategy/workflow-orchestration/chapter' },
              ],
            },
            { label: 'Architecture Patterns', link: '06-architecture-patterns/chapter' },
          ],
        },
        {
          label: 'Part III — Implementation',
          items: [
            {
              label: 'Implementation Guides',
              items: [
                { label: 'Overview', link: '07-implementation-guides/chapter' },
                { label: 'Config as Code', link: '07-implementation-guides/config-as-code/chapter' },
                { label: 'CI/CD Pipelines', link: '07-implementation-guides/ci-cd-pipelines/chapter' },
                { label: 'Testing Strategies', link: '07-implementation-guides/testing-strategies/chapter' },
                { label: 'Deployment Patterns', link: '07-implementation-guides/deployment-patterns/chapter' },
                { label: 'One-Touch Deployment', link: '07-implementation-guides/one-touch-deployment/chapter' },
              ],
            },
            { label: 'Operations Automation', link: '08-operations-automation/chapter' },
            { label: 'Greenfield Design', link: '09-greenfield-design/chapter' },
          ],
        },
        {
          label: 'Part IV — People',
          items: [
            { label: 'People and Skills', link: '10-people-and-skills/chapter' },
          ],
        },
        {
          label: 'Part V — Advanced Topics',
          items: [
            { label: 'Overview', link: '11-advanced-topics/chapter' },
            { label: 'Intent-Based Networking', link: '11-advanced-topics/intent-based-networking/chapter' },
            { label: 'AI-Driven Operations', link: '11-advanced-topics/ai-driven-operations/chapter' },
            { label: 'Auto-Healing Networks', link: '11-advanced-topics/auto-healing/chapter' },
          ],
        },
        {
          label: 'Part VI — Governance',
          items: [
            { label: 'Security & Compliance', link: '12-security-compliance/chapter' },
            { label: 'Dashboards & Metrics', link: '13-dashboards/chapter' },
          ],
        },
      ],
    }),
  ],
});
