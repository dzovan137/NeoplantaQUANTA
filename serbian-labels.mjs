// serbian-labels.mjs
// -----------------------------------------------------------------------------
// MyST transform plugin: translate figure/table caption labels to Serbian.
//
//     "Figure 1:"  ->  "Slika 1:"
//     "Table 1:"   ->  "Tabela 1:"
//
// Why a plugin? MyST builds the caption prefix from the container's *kind*
// ("figure" -> "Figure %s:") and does NOT consult the `numbering.*.template`
// config for it. So the numbering config handles cross-references, and this
// plugin handles the caption prefixes. Together they make every label Serbian.
//
// It runs at the "project" stage, i.e. AFTER MyST injects the caption-number
// nodes during reference resolution, so the nodes exist when we rewrite them.
//
// Applies automatically to every page in the project, including new lectures.
// To translate more label kinds, add entries to LABELS below
// (e.g. code blocks: `code: { from: 'Program', to: 'Listing' }`).
// -----------------------------------------------------------------------------

const LABELS = {
  figure:    { from: 'Figure', to: 'Slika' },
  subfigure: { from: 'Figure', to: 'Slika' },
  table:     { from: 'Table',  to: 'Tabela' },
};

const translateCaptionLabels = {
  name: 'Translate caption labels to Serbian',
  doc: 'Rewrites figure/table caption prefixes, e.g. "Figure 1:" -> "Slika 1:".',
  stage: 'project',
  plugin: (_opts, utils) => (tree) => {
    utils.selectAll('captionNumber', tree).forEach((node) => {
      const map = LABELS[node.kind];
      if (!map) return;
      // 1) the template string used by exports (e.g. "Figure %s:")
      if (typeof node.template === 'string') {
        node.template = node.template.replace(map.from, map.to);
      }
      // 2) the already-resolved text the web theme renders (e.g. "Figure 1:")
      utils.selectAll('text', node).forEach((textNode) => {
        if (typeof textNode.value === 'string') {
          textNode.value = textNode.value.replace(map.from, map.to);
        }
      });
    });
  },
};

const plugin = {
  name: 'Serbian labels',
  transforms: [translateCaptionLabels],
};

export default plugin;
